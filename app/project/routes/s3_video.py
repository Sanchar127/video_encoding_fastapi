from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from uuid import uuid4
from typing import List, Optional
from pydantic import BaseModel
from minio import Minio
import os
from ..schemas.videojob import VideoJobRead
from ..services.s3_event.s3_event import get_minio_client, get_presigned_video_url
from ..db.database import SessionLocal
from ..models.videojob import VideoJob
from ..models.encodeprofile import EncodeProfileDetails
from ..models.s3credentials import S3Credentials
from project.tasks.video_tasks import process_video_encoding_task
from ..logging_config import setup_logger
from ..auth.auth import get_current_user
from ..models.user import User
import os
logger = setup_logger()
router = APIRouter()
DEFAULT_BUCKET_NAME = 'fastapiencode'



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ExternalUploadRequest(BaseModel):
    bucket_name: str
    access_key: str
    secret_key: str
    endpoint: str
    profile_id: int
    profile_details_id: int
    region: str
    video_filename: str
    credential_name:str = "external-upload"


@router.post("/upload-video-external")
async def upload_video_from_external_source(
    request: ExternalUploadRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Accept video path from external MinIO source, copy it to our bucket, create a job, store credentials, and trigger encoding.
    """
    try:
        logger.info(f"Received request to encode video '{request.video_filename}' from external endpoint '{request.endpoint}' by user {current_user.unique_id}")
        logger.info(f"Request Body {request}")

        
        external_client = Minio(
            endpoint=request.endpoint.replace("http://", "").replace("https://", ""),
            access_key=request.access_key,
            secret_key=request.secret_key,
            secure=False
        )

        
        try:
            stat = external_client.stat_object(request.bucket_name, request.video_filename)
        except Exception as e:
            logger.error(f"Video '{request.video_filename}' not found in external bucket '{request.bucket_name}': {e}")
            raise HTTPException(status_code=404, detail="Video not found in external bucket")


        existing_cred = db.query(S3Credentials).filter_by(
            user_id=current_user.id,
            endpoint=request.endpoint,
            bucket=request.bucket_name,
            access_key=request.access_key,
            secret_key=request.secret_key
        ).first()

        if not existing_cred:
            new_cred = S3Credentials(
                user_id=current_user.id,
                name=request.credential_name,
                access_key=request.access_key,
                secret_key=request.secret_key,
                region=request.region,
                endpoint=request.endpoint,
                bucket=request.bucket_name
            )
            db.add(new_cred)
            db.commit()
            db.refresh(new_cred)
            logger.info(f"S3 credentials saved with ID {new_cred.id}")
        else:
            logger.info(f"S3 credentials already exist with ID {existing_cred.id}")

        
        target_client = get_minio_client()
        target_bucket = DEFAULT_BUCKET_NAME

        # Ensure target bucket exists
        if not target_client.bucket_exists(target_bucket):
            target_client.make_bucket(target_bucket)
            logger.info(f"Created target bucket '{target_bucket}'")


        file_ext = request.video_filename.split('.')[-1]
        target_filename = f"{uuid4()}.{file_ext}"

        external_data = external_client.get_object(request.bucket_name, request.video_filename)
        try:
            target_client.put_object(
                bucket_name=target_bucket,
                object_name=target_filename,
                data=external_data,
                length=stat.size,
                content_type=getattr(external_data, "content_type", "video/mp4")
            )
            logger.info(f"Copied video '{request.video_filename}' to '{target_bucket}/{target_filename}'")
        finally:
            external_data.close()
            external_data.release_conn()

        # Generate presigned URL
        url = get_presigned_video_url(object_name=target_filename)
        if not url:
            logger.error("Failed to generate presigned URL")
            raise HTTPException(status_code=500, detail="Could not generate presigned URL")

        # Fetch encoding profile
        profile = db.query(EncodeProfileDetails).filter(
            EncodeProfileDetails.profile_id == request.profile_id,
            EncodeProfileDetails.id == request.profile_details_id
        ).first()

        if not profile:
            logger.error(f"Encoding profile not found: profile_id={request.profile_id}, details_id={request.profile_details_id}")
            raise HTTPException(status_code=404, detail="Encoding profile details not found")

        if not profile.parent_profile:
            logger.error("Profile missing parent")
            raise HTTPException(status_code=400, detail="Encoding profile missing parent")

        # Create video job
        video_job = VideoJob(
            video_filename=target_filename,
            job_by=current_user.unique_id,
            retry_count=0,
            started_at=datetime.utcnow(),
            encoding_profile=request.profile_id,
            encoding_profileDetails=request.profile_details_id,
            status="queued",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.add(video_job)
        db.commit()
        db.refresh(video_job)

        logger.info(f"Video job created: ID {video_job.id}")

        process_video_encoding_task.delay(video_job.id, request.profile_id, request.profile_details_id)

        return {
            "status": "queued",
            "status_code": 202,
            "message": "Video encoding task has been submitted successfully.",
            "job_id": video_job.id,
            "target_filename": target_filename,
            "presigned_url": url,
        }

    except HTTPException as http_exc:
        logger.error(f"HTTPException: {http_exc.detail}", exc_info=True)
        raise http_exc
    except Exception as e:
        logger.error(f"Failed to process external video upload: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/job", response_model=List[VideoJobRead])
def get_all_jobs(db: Session = Depends(get_db)):
    """
    Fetch all video encoding jobs.
    """
    try:
        logger.info("Fetching all video encoding jobs")
        jobs = db.query(VideoJob).all()
        return jobs
    except Exception as e:
        logger.error(f"Error fetching video jobs: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Could not retrieve video jobs")


@router.put("/retry-job/{job_id}")
def retry_failed_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Retry a failed video encoding job.
    Only jobs with status 'failed' and retry_count < 10 are allowed.
    Minimum 5 minutes wait between retries.
    """
    try:
        job = db.query(VideoJob).filter(VideoJob.id == job_id).first()

        if not job:
            raise HTTPException(status_code=404, detail="Job not found")

        if job.status != "failed":
            raise HTTPException(status_code=400, detail="Only failed jobs can be retried")

        if job.retry_count >= 10:
            raise HTTPException(status_code=429, detail="Retry limit exceeded")

        if job.updated_at and datetime.utcnow() < job.updated_at + timedelta(minutes=5):
            wait_time = (job.updated_at + timedelta(minutes=5)) - datetime.utcnow()
            minutes = wait_time.seconds // 60
            seconds = wait_time.seconds % 60
            raise HTTPException(
                status_code=429,
                detail=f"Retry not allowed yet. Please wait {minutes} minutes and {seconds} seconds."
            )

        # Update job for retry
        job.retry_count += 1
        job.status = "queued"
        job.updated_at = datetime.utcnow()
        db.commit()

        logger.info(f"Retrying video job {job_id}, attempt {job.retry_count}")

        # Trigger encoding task again
        process_video_encoding_task.delay(job.id, job.encoding_profile, job.encoding_profileDetails)

        return {
            "status": "queued",
            "status_code": 202,
            "message": "Retry initiated for video encoding task.",
            "retry_count": job.retry_count
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Retry failed for job {job_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Retry failed unexpectedly")
