from fastapi import FastAPI
from app.api import router as api_router

# from app.db.models.base import Base
# from app.db.session import engine
#
# # Create Tables
# Base.metadata.create_all(bind=engine)

# Init App
app = FastAPI()

app.include_router(api_router)
