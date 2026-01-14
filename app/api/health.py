from fastapi import APIRouter
from app.models.health import HealthResponse

router = APIRouter()

@router.get("/", response_model=HealthResponse)
def health_check():
    return {
        "message": "Backend is healthy 🚀",
        "status": "OK"
    }
