from celery import Celery
from dotenv import load_dotenv
import os
load_dotenv()


CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

celery_app = Celery(
    "video_encoding",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
    include=["project.tasks.video_tasks"],
)

celery_app.conf.update(
    task_routes={
        "project.tasks.video_tasks.process_video_encoding_task": {"queue": "video-encoding"},
        
    },
    broker_heartbeat=10,       # Send heartbeats every 10s to keep RabbitMQ happy
    broker_connection_timeout=30,
    broker_pool_limit=5,       # Limit concurrent broker connections
    task_acks_late=True,       # Ensure task acknowledgment is reliable
    worker_prefetch_multiplier=1,  # Don't overload workers with tasks
    worker_concurrency=2,      # Adjust based on your machine
)
