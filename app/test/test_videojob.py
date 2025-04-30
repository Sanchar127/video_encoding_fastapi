import pytest
from datetime import datetime, timedelta
from uuid import uuid4
import io
from unittest.mock import MagicMock, AsyncMock
from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session
from project.routes.s3_video import upload_video_and_encode, get_all_jobs, retry_failed_job
from project.models.videojob import VideoJob
from project.models.encodeprofile import EncodeProfileDetails
from project.models.user import User
from project.schemas.videojob import VideoJobRead

# Mock dependencies
@pytest.fixture
def mock_db():
    return MagicMock(spec=Session)

@pytest.fixture
def mock_minio_client():
    client = MagicMock()
    client.bucket_exists.return_value = True
    client.put_object.return_value = None
    return client

@pytest.fixture
def mock_user():
    user = MagicMock(spec=User)
    user.unique_id = str(uuid4())
    return user

@pytest.fixture
def mock_upload_file():
    file = AsyncMock(spec=UploadFile)
    file.filename = "test.mp4"
    file.content_type = "video/mp4"
    file.read = AsyncMock(return_value=b"dummy video data")
    return file

@pytest.fixture
def mock_video_job():
    job = MagicMock(spec=VideoJob)
    job.id = 1
    job.video_filename = "test.mp4"
    job.job_by = str(uuid4())
    job.retry_count = 0
    job.started_at = datetime.utcnow()
    job.encoding_profile = 1
    job.encoding_profileDetails = 1
    job.status = "queued"
    job.created_at = datetime.utcnow()
    job.updated_at = datetime.utcnow()
    return job

@pytest.fixture
def mock_encode_profile():
    profile = MagicMock(spec=EncodeProfileDetails)
    profile.profile_id = 1
    profile.id = 1
    profile.parent_profile = MagicMock()  # Simulate parent profile
    return profile

# Mock external services
@pytest.fixture(autouse=True)
def setup_mocks(mocker):
    mocker.patch("project.routes.s3_video.get_minio_client", return_value=MagicMock())
    mocker.patch("project.routes.s3_video.get_presigned_video_url", return_value="http://minio/presigned/test.mp4")
    mocker.patch("project.routes.s3_video.process_video_encoding_task.delay", return_value=None)

# Tests for upload_video_and_encode
@pytest.mark.asyncio
async def test_upload_video_and_encode_success(mock_db, mock_minio_client, mock_user, mock_upload_file, mock_encode_profile, mocker):
    # Arrange
    mocker.patch("project.routes.s3_video.get_minio_client", return_value=mock_minio_client)
    mock_db.query.return_value.filter.return_value.first.return_value = mock_encode_profile
    mock_db.add = MagicMock()
    mock_db.commit = MagicMock()
    mock_db.refresh = MagicMock()

    # Act
    response = await upload_video_and_encode(
        profile_id=1,
        profile_details_id=1,
        file=mock_upload_file,
        db=mock_db,
        current_user=mock_user
    )

    # Assert
    assert response["status"] == "queued"
    assert response["status_code"] == 202
    assert response["message"] == "Video encoding task has been submitted successfully."
    assert "job_id" in response
    mock_minio_client.put_object.assert_called()
    mock_db.add.assert_called()
    mock_db.commit.assert_called()
    mock_db.refresh.assert_called()
    assert mock_upload_file.read.called

@pytest.mark.asyncio
async def test_upload_video_and_encode_profile_not_found(mock_db, mock_minio_client, mock_user, mock_upload_file, mocker):
    # Arrange
    mocker.patch("project.services.s3_event.s3_event.get_minio_client", return_value=mock_minio_client)
    mock_minio_client.bucket_exists.return_value = True  # Mock bucket check
    mock_minio_client.put_object = AsyncMock()  # Mock put_object as async
    mock_db.query.return_value.filter.return_value.first.return_value = None
    mock_upload_file.read = AsyncMock(return_value=b"fake_video_data")  # Mock file read
    mocker.patch("project.services.s3_event.s3_event.get_presigned_video_url", return_value="http://fake-url")  # Mock presigned URL

    # Act & Assert
    with pytest.raises(HTTPException) as exc:
        await upload_video_and_encode(
            profile_id=1,
            profile_details_id=1,
            file=mock_upload_file,
            db=mock_db,
            current_user=mock_user
        )
    assert exc.value.status_code == 404
    assert exc.value.detail == "Encoding profile details not found"

@pytest.mark.asyncio
async def test_upload_video_and_encode_no_parent_profile(mock_db, mock_minio_client, mock_user, mock_upload_file, mocker):
    # Arrange
    mocker.patch("project.routes.s3_video.get_minio_client", return_value=mock_minio_client)
    profile = MagicMock(spec=EncodeProfileDetails)
    profile.profile_id = 1
    profile.id = 1
    profile.parent_profile = None
    mock_db.query.return_value.filter.return_value.first.return_value = profile

    # Act & Assert
    with pytest.raises(HTTPException) as exc:
        await upload_video_and_encode(
            profile_id=1,
            profile_details_id=1,
            file=mock_upload_file,
            db=mock_db,
            current_user=mock_user
        )
    assert exc.value.status_code == 400
    assert exc.value.detail == "Encoding profile missing parent"

@pytest.mark.asyncio
async def test_upload_video_and_encode_presigned_url_failure(mock_db, mock_minio_client, mock_user, mock_upload_file, mock_encode_profile, mocker):
    # Arrange
    mocker.patch("project.routes.s3_video.get_minio_client", return_value=mock_minio_client)  
    mocker.patch("project.routes.s3_video.get_presigned_video_url", return_value=None)  # Mock URL generation failure
    mock_db.query.return_value.filter.return_value.first.return_value = mock_encode_profile

    # Act & Assert
    with pytest.raises(HTTPException) as exc:
        await upload_video_and_encode(
            profile_id=1,
            profile_details_id=1,
            file=mock_upload_file,
            db=mock_db,
            current_user=mock_user
        )
    
    
    assert exc.value.status_code == 404



def test_get_all_jobs_success(mock_db, mock_user, mock_video_job):
    # Arrange
    mock_db.query.return_value.all.return_value = [mock_video_job]

    
    response = get_all_jobs(db=mock_db, current_user=mock_user)

    # Assert
    assert isinstance(response, list)
    assert len(response) == 1
    assert response[0] == mock_video_job
    mock_db.query.assert_called_once()

def test_get_all_jobs_empty(mock_db, mock_user):
    # Arrange
    mock_db.query.return_value.all.return_value = []

    # Act
    response = get_all_jobs(db=mock_db, current_user=mock_user)

    # Assert
    assert isinstance(response, list)
    assert len(response) == 0
    mock_db.query.assert_called_once()

def test_get_all_jobs_exception(mock_db, mock_user):
    # Arrange
    mock_db.query.side_effect = Exception("Database error")

    # Act & Assert
    with pytest.raises(HTTPException) as exc:
        get_all_jobs(db=mock_db, current_user=mock_user)
    assert exc.value.status_code == 500
    assert exc.value.detail == "Could not retrieve video jobs"

# Tests for retry_failed_job
def test_retry_failed_job_success(mock_db, mock_user, mock_video_job):
    # Arrange
    mock_video_job.status = "failed"
    mock_video_job.retry_count = 1
    mock_video_job.updated_at = datetime.utcnow() - timedelta(minutes=10)  # Enough time has passed
    mock_db.query.return_value.filter.return_value.first.return_value = mock_video_job
    mock_db.commit = MagicMock()

    # Act
    response = retry_failed_job(job_id=1, db=mock_db, current_user=mock_user)

    # Assert
    assert response["status"] == "queued"
    assert response["status_code"] == 202
    assert response["message"] == "Retry initiated for video encoding task."
    assert response["retry_count"] == 2
    assert mock_video_job.status == "queued"
    assert mock_video_job.retry_count == 2
    mock_db.commit.assert_called_once()

def test_retry_failed_job_not_found(mock_db, mock_user):
    # Arrange
    mock_db.query.return_value.filter.return_value.first.return_value = None

    # Act & Assert
    with pytest.raises(HTTPException) as exc:
        retry_failed_job(job_id=1, db=mock_db, current_user=mock_user)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Job not found"

def test_retry_failed_job_not_failed(mock_db, mock_user, mock_video_job):
    # Arrange
    mock_video_job.status = "queued"
    mock_db.query.return_value.filter.return_value.first.return_value = mock_video_job

    # Act & Assert
    with pytest.raises(HTTPException) as exc:
        retry_failed_job(job_id=1, db=mock_db, current_user=mock_user)
    assert exc.value.status_code == 400
    assert exc.value.detail == "Only failed jobs can be retried"

def test_retry_failed_job_retry_limit_exceeded(mock_db, mock_user, mock_video_job):
    # Arrange
    mock_video_job.status = "failed"
    mock_video_job.retry_count = 10
    mock_db.query.return_value.filter.return_value.first.return_value = mock_video_job

    # Act & Assert
    with pytest.raises(HTTPException) as exc:
        retry_failed_job(job_id=1, db=mock_db, current_user=mock_user)
    assert exc.value.status_code == 429
    assert exc.value.detail == "Retry limit exceeded"

def test_retry_failed_job_retry_too_soon(mock_db, mock_user, mock_video_job):
    # Arrange
    mock_video_job.status = "failed"
    mock_video_job.retry_count = 1
    mock_video_job.updated_at = datetime.utcnow() - timedelta(minutes=2)  # Too soon
    mock_db.query.return_value.filter.return_value.first.return_value = mock_video_job

    # Act & Assert
    with pytest.raises(HTTPException) as exc:
        retry_failed_job(job_id=1, db=mock_db, current_user=mock_user)
    assert exc.value.status_code == 429
    assert "Retry not allowed yet" in exc.value.detail

def test_retry_failed_job_unexpected_error(mock_db, mock_user, mock_video_job):
    # Arrange
    mock_video_job.status = "failed"
    mock_video_job.retry_count = 1
    mock_video_job.updated_at = datetime.utcnow() - timedelta(minutes=10)
    mock_db.query.return_value.filter.return_value.first.return_value = mock_video_job
    mock_db.commit.side_effect = Exception("Unexpected error")

    # Act & Assert
    with pytest.raises(HTTPException) as exc:
        retry_failed_job(job_id=1, db=mock_db, current_user=mock_user)
    assert exc.value.status_code == 500
    assert exc.value.detail == "Retry failed unexpectedly"