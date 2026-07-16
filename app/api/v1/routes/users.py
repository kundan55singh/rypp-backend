from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.database.dependency import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate, ChangePasswordRequest
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return UserService.get_me(current_user)


@router.put("/me", response_model=UserResponse)
def update_profile(
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return UserService.update_profile(
        db,
        current_user,
        data,
    )


@router.put("/change-password")
def change_password(
    data: ChangePasswordRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return UserService.change_password(
        db,
        current_user,
        data,
    )