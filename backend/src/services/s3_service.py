import boto3
from botocore.exceptions import ClientError
import logging
from ..config import settings

class S3Service:
    def __init__(self):
        self.client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY
        )
        self.bucket_name = settings.S3_BUCKET_NAME

    async def upload_file(self, file_path: str, object_name: str) -> bool:
        try:
            self.client.upload_file(file_path, self.bucket_name, object_name)
            return True
        except ClientError as e:
            logging.error(e)
            return False
    
    def get_file_content(self, key: str) -> str:
        response = self.client.get_object(Bucket=self.bucket_name, Key=key)
        return response["Body"].read().decode("utf-8")
