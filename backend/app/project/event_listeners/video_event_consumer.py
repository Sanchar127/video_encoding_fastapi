from kombu import Connection, Exchange, Queue
import json
from datetime import datetime
from ..tasks.video_tasks import process_video_encoding_task
from ..db.database import SessionLocal
from ..models.videojob import VideoJob
from ..models.encodeprofile import EncodeProfileDetails
from ..logging_config import setup_logger

logger = setup_logger()

# Define the queue and exchange (must match MinIO config)
exchange = Exchange('amq.direct', type='direct')
queue = Queue('minio', exchange=exchange, routing_key='minio')

def handle_minio_event(body):
    try:
        logger.info(f"Received message: {body}")
        records = body.get("Records", [])
        db = SessionLocal()
        
        for record in records:
            object_key = record.get("s3", {}).get("object", {}).get("key")
            if not object_key:
                continue

            # Check if already processed
            if db.query(VideoJob).filter_by(video_filename=object_key).first():
                logger.info(f"Skipping duplicate video: {object_key}")
                continue

            profile = db.query(EncodeProfileDetails).first()
            if not profile:
                logger.error("Encoding profile missing!")
                continue

            # Create job
            video_job = VideoJob(
                video_filename=object_key,
                encoding_profile=profile.profile_id,
                status="queued",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            db.add(video_job)
            db.commit()
            db.refresh(video_job)
            logger.info(f"Created job {video_job.id} for {object_key}")

            # Trigger task
            process_video_encoding_task.delay(video_job.id)

        db.close()

    except Exception as e:
        logger.error(f"Error handling event: {e}", exc_info=True)

def run_event_listener():
    with Connection('amqp://guest:guest@rabbitmq:5672//') as conn:
        with conn.Consumer(queue, callbacks=[handle_minio_event], accept=['json']):
            while True:
                try:
                    conn.drain_events(timeout=10)
                except Exception as e:
                    logger.debug("Waiting for new messages...")
