#app/project/services/s3_event/s3_event
from minio import Minio
import os
from datetime import timedelta
# import requests
# import io
# from project.utils.virus_scanner import scan_file_stream
def get_minio_client():
    return Minio(
        endpoint=os.getenv("S3_ENDPOINT", "localhost:9000").replace("http://", ""),
        access_key='ZBEPTqKcHk36Cqp6Qxv0',
        secret_key='iCY4vGDHBDG7b0J8itnx7boL3mM2ot2AFIBvhSIc',
        secure=False  # set to True if you use HTTPS
    )



def get_presigned_video_url(object_name: str, expires_in_seconds: int = 3600) -> str:
    bucket = "fastapiencode"
    client = get_minio_client()

    try:
        if not client.bucket_exists(bucket):
            raise Exception(f"Bucket {bucket} does not exist.")

        url = client.presigned_get_object(bucket, object_name, expires=timedelta(seconds=expires_in_seconds))

        # # Fetch the file using the presigned URL
        # response = requests.get(url)
        # if response.status_code != 200:
        #     raise Exception("Failed to download file for virus scan")

        # # Scan the file using a stream
        # scan_result = scan_file_stream(io.BytesIO(response.content))

        # if scan_result["status"] == "infected":
        #     raise Exception(f"Virus found: {scan_result['virus']}")

        # if scan_result["status"] != "clean" and scan_result["status"] != "OK":
        #     raise Exception(f"Virus scanning failed: {scan_result}")

        return url

    except Exception as e:
        print(f"Error: {e}")
        return None


