from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
from app.core.cors import setup_cors

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

setup_cors(app)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def home():
    return {
        "message": f"{settings.APP_NAME} 🚀"
    }