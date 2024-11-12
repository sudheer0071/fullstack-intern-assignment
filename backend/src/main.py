from fastapi import FastAPI
from src.api.routes import router
from src.models.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to the origins you want to allow, e.g., ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Specify methods if you want to restrict, e.g., ["GET", "POST"]
    allow_headers=["*"],  # Specify headers if you want to restrict
)

app.include_router(router)