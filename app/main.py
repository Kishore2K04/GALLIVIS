from fastapi import FastAPI

from app.models.schemas import HealthResponse
from app.services.health_service import get_health_status


app = FastAPI(
    title="GALLIVIS API",
    description=(
        "Intelligent Multimodal Clinical Decision Support System "
        "for Pre-operative Gallstone Classification"
    ),
    version="0.1.0",
)


@app.get("/", tags=["General"])
def root():
    return {
        "project": "GALLIVIS",
        "message": "GALLIVIS API is running",
    }


@app.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check():
    return get_health_status()