from fastapi import APIRouter, UploadFile, HTTPException, Depends,File
from ..models.database import get_db
from sqlalchemy.orm import Session
from ..models.models import Upload
from ..services.s3_service import S3Service
from ..services.pdf_service import PDFService
from ..services.qa_service import QAService
from ..schemas.responses import ChatResponse
from .dependencies import get_s3_service, get_pdf_service
import os

router = APIRouter()
qa_service = QAService()

@router.post("/upload/" )
async def upload_file(
    file: UploadFile = File(...) ,
    s3_service: S3Service = Depends(get_s3_service),
    pdf_service: PDFService = Depends(get_pdf_service),
    db: Session = Depends(get_db)
):
  if file.content_type != "application/pdf":
    raise HTTPException(status_code=400, detail="Please upload a PDF file!")

  try:
    # Extract text from PDF
    text_output = await pdf_service.extract_text(file)
    
    # Save extracted text temporarily 
    extract_file = 'extract.txt'
    
    with open(extract_file, "wb") as output_file:
        output_file.write(text_output)

    # Upload to S3
    s3_object_key = f"{file.filename.split('.')[0]}/{extract_file}"
    await s3_service.upload_file(extract_file, s3_object_key)
    
    # Clean up temporary file
    os.remove(extract_file)
    
    # Get content from S3 and initialize QA chain
    content = s3_service.get_file_content(s3_object_key)
    qa_service.initialize_qa_chain(content)
    
    db_upload = Upload(
       file_name=file.filename,
       file_size=12,
    )

    db.add(db_upload)
    db.commit()
    db.refresh(db_upload)

    return {"message":"Pdf uploaded successfully !"}

  except Exception as e:
    if os.path.exists(extract_file):
            os.remove(extract_file)
    raise HTTPException(status_code=500, detail=str(e))
    
 

@router.get("/chat/", response_model=ChatResponse)
async def chat_bot(query: str):
    try:
        answer = qa_service.get_answer(query)
        return ChatResponse(question=query, answer=answer)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/test/", response_model=ChatResponse)
async def chat_bot(query: str):
    try:
        
        return ChatResponse(question=query, answer="This is the resume of Sudheer Chaurasia, a Full Stack Developer currently working at Global Electronics Solutions in Gurugram, Haryana. He has a Bachelor's degree in Computer Science and Engineering from Dronacharya College of Engineering and has technical skills in several languages such as C/C++, Python, SQL, JavaScript, HTML/CSS, and R. \n\nIn his current role at Global Electronics Solutions, Sudheer Chaurasia has led a digital transformation initiative, developed an e-commerce platform, and has implemented efficient caching strategies and lazy loading techniques. He has also used Docker for containerization and AWS for cloud deployment.\n\nPreviously, Sudheer worked as a Frontend Developer at Edunet Foundation in Delhi, India. Here, he deployed and configured web applications using React, diagnosed and resolved technical issues, and managed the upkeep and optimization of React-based web interfaces.\n\nSudheer has also worked on a couple of projects such as Swasthlekh where he improved appointment management and implemented automated scheduling, and MLHybridX-Module where he simplified machine learning tasks and implemented machine learning algorithms.\n\nYou can contact Sudheer through his phone number (828-744-9499) or his email (sudheer1614@gmail.com). His portfolio, LinkedIn, and Github links are also provided.")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))