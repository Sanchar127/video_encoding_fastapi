from ..services.s3_event.s3_event import get_presigned_video_url, get_minio_client
from ..logging_config import setup_logger
import os
import ffmpeg
from minio.error import S3Error
from datetime import datetime
from celery_app import celery_app
from ..db.database import SessionLocal
from ..models.videojob import VideoJob
from ..models.encodeprofile import EncodeProfileDetails

logger = setup_logger()

def clamp_kbps(value_kbps: int) -> str:
    MAX_SAFE_KBPS = 2_000_000  # 2 Gbps
    return f"{min(value_kbps or 0, MAX_SAFE_KBPS)}k"


def compare_metadata_with_profile(metadata: dict, profile_details: EncodeProfileDetails):
    mismatches = []

    video_stream = next((s for s in metadata.get('streams', []) if s.get('codec_type') == 'video'), None)
    audio_stream = next((s for s in metadata.get('streams', []) if s.get('codec_type') == 'audio'), None)

    if video_stream:
        actual_video_bitrate = int(video_stream.get('bit_rate', 0))
        if profile_details.video_bitrate > actual_video_bitrate:
            warning_msg = (
                f"Encoding profile video bitrate ({profile_details.video_bitrate}) is higher "
                f"than original video bitrate ({actual_video_bitrate})."
            )
            logger.warning(warning_msg)
            mismatches.append(warning_msg)
            profile_details.video_bitrate = actual_video_bitrate

    if audio_stream:
        actual_audio_bitrate = int(audio_stream.get('bit_rate', 0))
        if profile_details.audio_bitrate > actual_audio_bitrate:
            warning_msg = (
                f"Encoding profile audio bitrate ({profile_details.audio_bitrate}) is higher "
                f"than original audio bitrate ({actual_audio_bitrate})."
            )
            logger.warning(warning_msg)
            mismatches.append(warning_msg)
            profile_details.audio_bitrate = actual_audio_bitrate

    return mismatches



@celery_app.task(name="project.tasks.video_tasks.process_video_encoding_task")
def process_video_encoding_task(job_id: int, selected_profile_id: int, selected_profile_details_id: int):
    logger.info(f"Starting encoding task for job_id={job_id}")
    db = SessionLocal()

    try:
        video_job = db.query(VideoJob).filter(VideoJob.id == job_id).first()
        if not video_job:
            msg = f"VideoJob with ID {job_id} not found."
            logger.error(msg)
            return {"status": "failed", "status_code": 404, "message": msg, "job_id": job_id}

        video_job.status = "processing"
        db.commit()

        if not video_job.video_filename.lower().endswith(".mp4"):
            msg = f"Only .mp4 files are supported. Got: {video_job.video_filename}"
            logger.error(msg)
            video_job.status = "failed"
            video_job.updated_at = datetime.utcnow()
            db.commit()
            return {"status": "failed", "status_code": 400, "message": msg, "job_id": job_id}

        profile_details = db.query(EncodeProfileDetails).filter(
            EncodeProfileDetails.profile_id == selected_profile_id,
            EncodeProfileDetails.id == selected_profile_details_id
        ).first()

        if not profile_details:
            msg = "Encoding profile details not found."
            logger.error(msg)
            video_job.status = "failed"
            video_job.updated_at = datetime.utcnow()
            db.commit()
            return {"status": "failed", "status_code": 404, "message": msg, "job_id": job_id}

        input_url = get_presigned_video_url(object_name=video_job.video_filename)
        if not input_url:
            msg = "Failed to generate presigned URL."
            logger.error(msg)
            video_job.status = "failed"
            video_job.updated_at = datetime.utcnow()
            db.commit()
            return {"status": "failed", "status_code": 500, "message": msg, "job_id": job_id}

        try:
            probe = ffmpeg.probe(input_url)
            format_name = probe.get("format", {}).get("format_name", "")
            format_aliases = [f.strip().lower() for f in format_name.split(",")]

            if "mp4" not in format_aliases:
                msg = "Unsupported container format. Only MP4 is supported."
                logger.error(msg)
                video_job.status = "failed"
                video_job.updated_at = datetime.utcnow()
                db.commit()
                return {"status": "failed", "status_code": 400, "message": msg, "job_id": job_id}

            mismatches = compare_metadata_with_profile(probe, profile_details)
            if mismatches:
                msg = "Video metadata does not match encoding profile."
                logger.warning(msg)
                video_job.status = "failed"
                video_job.updated_at = datetime.utcnow()
                db.commit()
                return {"status": "failed", "status_code": 400, "message": msg, "job_id": job_id}

        except ffmpeg.Error as e:
            error_msg = e.stderr.decode() if e.stderr else str(e)
            logger.error(f"FFmpeg probe failed: {error_msg}")
            video_job.status = "failed"
            video_job.updated_at = datetime.utcnow()
            db.commit()
            return {"status": "failed", "status_code": 500, "message": "Metadata extraction failed", "job_id": job_id}

        output_dir = "/app/project/videos_encoded"
        os.makedirs(output_dir, exist_ok=True)
        base_name = os.path.splitext(video_job.video_filename)[0]
        output_filename = f"{base_name}_{profile_details.profile}_encoded.mp4"
        output_path = os.path.join(output_dir, output_filename)

        if os.path.exists(output_path):
            os.remove(output_path)

        output_args = {
            "format": "mp4",
            "vcodec": profile_details.vcodec,
            "acodec": profile_details.acodec,
            "video_bitrate": clamp_kbps(profile_details.video_bitrate),
            "audio_bitrate": clamp_kbps(profile_details.audio_bitrate),
            "ac": profile_details.audio_channel ,
            "ar": profile_details.audio_frequency,
            "sc_threshold": profile_details.sc_threshold or 0,
            "level": profile_details.level ,
            "maxrate": clamp_kbps(profile_details.max_bitrate),
            "bufsize": clamp_kbps(profile_details.bufsize),
            "movflags": profile_details.movflags or "faststart",
            "pix_fmt": profile_details.pix_fmt or "yuv420p",
            "s": f"{profile_details.width}x{profile_details.height}" if profile_details.width and profile_details.height else None,
            "y": None
        }
        output_args = {k: v for k, v in output_args.items() if v is not None}

        try:
            ffmpeg.input(input_url, protocol_whitelist='file,http,https,tcp,tls') \
                .output(output_path, **output_args) \
                .run(capture_stdout=True, capture_stderr=True)
        except ffmpeg.Error as e:
            error_msg = e.stderr.decode() if e.stderr else str(e)
            logger.error(f"FFmpeg encoding failed: {error_msg}")
            video_job.status = "failed"
            video_job.ended_at=datetime.utcnow()
            video_job.updated_at = datetime.utcnow()
            db.commit()
            return {"status": "failed", "status_code": 500, "message": "Encoding failed", "job_id": job_id}

        try:
            minio_client = get_minio_client()
            minio_client.fput_object(
                bucket_name="fastapiencode",
                object_name=output_filename,
                file_path=output_path
            )
        except S3Error as e:
            logger.error(f"MinIO upload failed: {str(e)}")
            video_job.status = "failed"
            video_job.ended_at=datetime.utcnow()
            video_job.updated_at = datetime.utcnow()
            db.commit()
            return {"status": "failed", "status_code": 500, "message": "Upload to MinIO failed", "job_id": job_id}

        video_job.status = "completed"
        video_job.ended_at=datetime.utcnow()
        video_job.updated_at = datetime.utcnow()
        db.commit()
        logger.info(f"Encoding complete for job_id={job_id}")
        return {"status": "completed", "status_code": 200, "message": "Video encoded and uploaded successfully", "job_id": job_id}

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        if 'video_job' in locals():
            video_job.status = "failed"
            video_job.ended_at= datetime.utcnow()
            video_job.updated_at = datetime.utcnow()
            db.commit()
        return {"status": "failed", "status_code": 500, "message": "Unexpected server error", "job_id": job_id}

    finally:
        db.close()

