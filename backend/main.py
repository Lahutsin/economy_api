import os
from fastapi import FastAPI
from routes import data
from database import engine, SessionLocal
from models import Base

# Get ENVs
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_HOST = os.getenv("REDIS_HOST")

# Create object FastAPI
app = FastAPI()

# Init DB
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(data.router)

# Any
