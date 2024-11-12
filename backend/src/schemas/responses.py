from pydantic import BaseModel
  
class ChatResponse(BaseModel):
    question: str
    answer: str