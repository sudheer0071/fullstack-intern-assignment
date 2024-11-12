from pydantic import BaseModel
from datetime import datetime

class UploadResponse(BaseModel):
    id: int
    file_name: str 
    file_size: str
    created_at: datetime

    class Config:
        orm_mode = True