from fastapi import FastAPI
from app.api import router as api_router
from app.database import create_database

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    create_database()  # Create database tables


app.include_router(api_router)
