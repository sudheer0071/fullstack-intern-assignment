import pymupdf
from fastapi import UploadFile

class PDFService:
    @staticmethod
    async def extract_text(file: UploadFile) -> bytes:
        # Read the uploaded file and pass it to pymupdf.Document
        with pymupdf.Document(stream=await file.read()) as doc:
            text_output = bytes()
            for page in doc:
                text = page.get_text().encode("utf8")
                text_output += text
                text_output += bytes((12,))  # Adding a newline character
            return text_output
