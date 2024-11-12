from fastapi import FastAPI, UploadFile, HTTPException, File
import boto3
from botocore.exceptions import ClientError
import logging
import pymupdf
from dotenv import load_dotenv
from io import  StringIO
import os
from langchain.document_loaders import TextLoader
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

load_dotenv()  
 
AWS_S3_CREDS = {
    "aws_access_key_id": os.getenv("AWS_ACCESS_KEY"),
    "aws_secret_access_key": os.getenv("AWS_SECRET_KEY")
}

llm =  ChatOpenAI(model="gpt-4", openai_api_key=os.getenv("OPENAI_API_KEY"))
embeddings = OpenAIEmbeddings()

s3_client = boto3.client('s3',**AWS_S3_CREDS)

print(AWS_S3_CREDS)

app = FastAPI()

qa_chain = None

async def upload_to_bucket(file, bucket, object_name:None):
  print("uploading...")
  if object_name is None:
    return "no file selected."
  
  try:
    response = s3_client.upload_file(file,bucket, object_name)
    print("res...")
    print(response)
  except ClientError as e:
    logging.error(e)
    return false
  return True

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
  global qa_chain

  if file.content_type != "application/pdf":
    raise HTTPException(status_code=400, detail="Please upload a PDF file!")
   
  with pymupdf.Document(stream=await file.read()) as doc:
      print("doc........")
      print(doc) 

      text_output = bytes()
      for page in doc: 
        text = page.get_text().encode("utf8") 
        text_output += text
        text_output += bytes((12,)) 

# -------------------------------- Todo ------------------------------------
# Upload the extract the contents fo pdf direclty and upload extracted content to aws no need to upload the pdf to S3

  # with open(file.filename, 'wb') as f:
  #   f.write(await file.read())
  extractedFile = 'extract.txt'
  with open(extractedFile,"wb") as output_file:
    output_file.write(text_output)
 
  fileName = file.filename.split('.')[0]
  
  # Uploading extracted content to s3 
  await upload_to_bucket(extractedFile,"fullstack-intern-assignment", f"{fileName}/{extractedFile}")
  # os.remove('extract.txt')
  print(f'key = {file.filename}/{extractedFile}')
  response = s3_client.get_object(Bucket='fullstack-intern-assignment',Key=f'{fileName}/{extractedFile}' )

  object_content = response["Body"].read().decode("utf-8")
  print("file content from aws")
  print(object_content)

  extractedtxt = StringIO(object_content)
  print("extraaacted........")
  print(extractedtxt)

  
  doccumets = [Document(page_content=object_content)]

  vector_store = FAISS.from_documents(doccumets,embeddings)

  qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever()  # Ensure `retriever` is correctly passed here
    )

# ----------------------------- Todo ----------------------------
# Have to store these in database
  return {
    "pdf_name": file.filename,
    "content-Type":file.content_type, 
    # "font_size":f"{file.size / 1_049_576:2f} MB",
  }   

@app.get("/chat/")
async def chat_bot(query:str):
  global qa_chain

  if qa_chain is None:
    return {"error":"No pdf found"}

  response = qa_chain({"query":query})
  answer = response.get("result","no answer found")

  return {"question": query, "answer":answer}