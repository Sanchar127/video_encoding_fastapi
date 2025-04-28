# from fastapi.testclient import TestClient
# from unittest import mock
# import pytest
# from io import BytesIO
# from main import app  # Assuming your FastAPI app is in the 'main' module

# @pytest.fixture
# def client():
#     with TestClient(app) as client:
#         yield client

# @pytest.fixture
# def mock_minio_client():
#     with mock.patch("your_project_path.get_minio_client") as mock_client:
#         mock_client.return_value.bucket_exists.return_value = True
#         yield mock_client

# @pytest.fixture
# def mock_process_video_encoding_task():
#     with mock.patch("your_project_path.process_video_encoding_task.delay") as mock_task:
#         yield mock_task

# def test_upload_video_and_encode(client, mock_minio_client, mock_process_video_encoding_task):
#     # Dummy video file as UploadFile
#     file_data = b"dummy video data"
#     file = BytesIO(file_data)
#     file.name = "test_video.mp4"
    
#     # Mock MinIO client behavior (e.g., successful upload)
#     mock_minio_client.put_object.return_value = None
#     mock_minio_client.bucket_exists.return_value = True

#     response = client.post(
#         "/upload-video",
#         params={"profile_id": 1, "profile_details_id": 1},
#         files={"file": ("test_video.mp4", file, "video/mp4")},
#     )

#     assert response.status_code == 202
#     assert response.json()["status"] == "queued"
#     assert "job_id" in response.json()

#     # Ensure that Celery task was triggered
#     mock_process_video_encoding_task.delay.assert_called_once()


