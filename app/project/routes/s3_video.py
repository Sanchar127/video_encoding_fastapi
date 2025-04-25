from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
from uuid import uuid4
from typing import List
from ..services.s3_event.s3_event import get_minio_client, get_presigned_video_url
from ..db.database import SessionLocal
from ..models.videojob import VideoJob
from ..models.encodeprofile import EncodeProfileDetails
from project.tasks.video_tasks import process_video_encoding_task
from ..logging_config import setup_logger
from .user import get_current_user,get_admin_user
from ..models.user import User
from ..schemas.videojob import VideoJobRead
import io



logger = setup_logger()
router = APIRouter()
bucket_name = "fastapiencode"

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload-video")
async def upload_video_and_encode(
    profile_id: int,
    profile_details_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
Upload the video 
	"""
    try:
        logger.info(f"Uploading video to MinIO and starting encoding process")

        # 1. Upload video to MinIO
        client = get_minio_client()

        # Ensure bucket exists
        found = client.bucket_exists(bucket_name)
        if not found:
            client.make_bucket(bucket_name)
            logger.info(f"Created bucket: {bucket_name}")

        # Generate a unique filename
        file_extension = file.filename.split('.')[-1]
        filename = f"{uuid4()}.{file_extension}"

        file_data = await file.read()
        file_stream = io.BytesIO(file_data)

        client.put_object(
            bucket_name,
            filename,
            data=file_stream,  
            length=len(file_data),
            content_type=file.content_type
)

        logger.info(f"Uploaded video: {filename}")

        # 2. Generate presigned URL
        url = get_presigned_video_url(object_name=filename)
        if not url:
            logger.error("Failed to generate presigned URL")
            raise HTTPException(status_code=500, detail="Could not generate presigned URL")
        
        # 3. Fetch the encoding profile
        profile = db.query(EncodeProfileDetails).filter(
            EncodeProfileDetails.profile_id == profile_id,
            EncodeProfileDetails.id == profile_details_id
        ).first()

        if not profile:
            logger.error("Encoding profile details not found")
            raise HTTPException(status_code=404, detail="Encoding profile details not found")

        if not profile.parent_profile:
            logger.error("Encoding profile does not have a parent")
            raise HTTPException(status_code=400, detail="Encoding profile missing parent")

        # 4. Create a video job
        video_job = VideoJob(
            video_filename=filename,
            job_by=current_user.unique_id,
            retry_count= 0,
            started_at= datetime.utcnow(),
            encoding_profile=profile_id,
            encoding_profileDetails=profile_details_id,
            status="queued",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.add(video_job)
        db.commit()
        db.refresh(video_job)

        logger.info(f"Video job created: {video_job.id}")
        # 5. Trigger Celery task
        process_video_encoding_task.delay(video_job.id, profile_id, profile_details_id)
        return {
        "status": "queued",
        "status_code": 202,
        "message": "Video encoding task has been submitted successfully.",
        "job_id": video_job.id
    }
       

    except Exception as e:
        logger.error(f"Upload or encoding failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
     
@router.get("/job", response_model=List[VideoJobRead])
def get_all_jobs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    """
	Use to  get all job Store in Database.
	"""
    try:
        logger.info("Fetching all video jobs")

        jobs = db.query(VideoJob).all()

        return jobs

    except Exception as e:
        logger.error(f"Failed to fetch video jobs: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Could not retrieve video jobs")
    




@router.put("/retry-job/{job_id}")
def retry_failed_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    """
	Use to  retry the job in case of Job failure 
	"""
    try:
        job = db.query(VideoJob).filter(VideoJob.id == job_id).first()
    
    
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")

        if job.status != "failed":
            raise HTTPException(status_code=400, detail="Only failed jobs can be retried")

        if job.retry_count >= 10: #I'm setting max retry as 10 it is configurable and leter replace by orginal value (max_retry)
            raise HTTPException(status_code=429, detail="Retry limit exceeded")
        if job.updated_at and datetime.utcnow() < job.updated_at + timedelta(minutes=5):
            time_remaining = (job.updated_at + timedelta(minutes=5)) - datetime.utcnow()
            raise HTTPException(
                status_code=429,
                detail=f"Retry not allowed yet. Please wait {time_remaining.seconds // 60} minutes and {time_remaining.seconds % 60} seconds."
            )
        job.retry_count += 1
        job.status = "queued"
        job.updated_at = datetime.utcnow()
        db.commit()

        logger.info(f"Retrying job {job.id}, new retry count: {job.retry_count}")

        # Trigger Celery task again
        process_video_encoding_task.delay(job.id, job.encoding_profile, 5)  

        return {
            "status": "queued",
            "status_code": 202,
            "message": "Retry initiated for video encoding task.",
            "retry_count": job.retry_count
        }

    except HTTPException:
        raise  # Let FastAPI handle expected errors

    except Exception as e:
        logger.error(f"Retry failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Retry failed unexpectedly")
    



