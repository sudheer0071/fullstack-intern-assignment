from ..services.s3_service import S3Service
from ..services.pdf_service import PDFService
from ..services.qa_service import QAService

def get_s3_service() -> S3Service:
    return S3Service()

def get_pdf_service() -> PDFService:
    return PDFService()

def get_qa_service() -> QAService:
    return QAService()