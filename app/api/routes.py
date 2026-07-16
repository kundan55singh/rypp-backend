from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "success",
        "message": "API is healthy"
    }