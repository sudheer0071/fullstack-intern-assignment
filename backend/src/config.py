from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    AWS_ACCESS_KEY: str = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY: str = os.getenv("AWS_SECRET_KEY")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    S3_BUCKET_NAME: str = "fullstack-intern-assignment"
    DATABSE_URL: str = os.getenv("DATABSE_URL")
    
settings = Settings()