from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from ..config import settings

class QAService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4", 
            openai_api_key=settings.OPENAI_API_KEY
        )
        self.embeddings = OpenAIEmbeddings()
        self.qa_chain = None

    def initialize_qa_chain(self, content: str):
        documents = [Document(page_content=content)]
        vector_store = FAISS.from_documents(documents, self.embeddings)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever()
        )

    def get_answer(self, query: str) -> str:
        if not self.qa_chain:
            raise ValueError("QA chain not initialized")
        response = self.qa_chain({"query": query})
        return response.get("result", "No answer found")
