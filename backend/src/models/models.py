from ..models.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP 
from sqlalchemy import func


class Upload(Base):
    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, nullable=False)
    file_name = Column(String, nullable=False)
    file_size = Column(Integer, nullable=False)  
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())