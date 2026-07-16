from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.database.dependency import get_db
from app.models.user import User
from app.schemas.auth import RegisterRequest, LoginRequest
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(
    user: RegisterRequest,
    db: Session = Depends(get_db),
):
    return AuthService.register(
        db=db,
        name=user.name,
        phone=user.phone,
        email=user.email,
        password=user.password,
        confirm_password=user.confirm_password,
        referral_code=user.referral_code,
    )


@router.post("/login")
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db),
):
    return AuthService.login(
        db=db,
        email=credentials.email,
        password=credentials.password,
    )


@router.get("/me")
def me(
    current_user: User = Depends(get_current_user),
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "phone": current_user.phone,
        "email": current_user.email,
        "role": current_user.role,
        "is_active": current_user.is_active,
        "is_verified": current_user.is_verified,
        "profile_image": current_user.profile_image,
        "referral_code": current_user.referral_code,
    }