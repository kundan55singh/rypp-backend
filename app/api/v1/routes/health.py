from fastapi import APIRouter
from app.utils.response import success_response

router = APIRouter()


@router.get("/health", tags=["Health"])
def health():
    return success_response(
        message="API is healthy",
        data={
            "version": "v1"
        }
    )