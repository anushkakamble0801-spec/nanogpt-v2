
from fastapi import FastAPI

app = FastAPI(
    title="NanoGPT API",
    description="Backend API for NanoGPT text generation",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to NanoGPT API"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "project": "NanoGPT-v2"
    }
