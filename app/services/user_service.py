from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserUpdate, ChangePasswordRequest
from app.core.security import verify_password, hash_password
from app.repositories.user_repository import UserRepository


class UserService:

    @staticmethod
    def get_me(current_user: User):
        return current_user

    @staticmethod
    def update_profile(
        db: Session,
        current_user: User,
        data: UserUpdate,
    ):

        if data.name is not None:
            current_user.name = data.name

        if data.phone is not None:
            current_user.phone = data.phone

        if data.profile_image is not None:
            current_user.profile_image = data.profile_image

        return UserRepository.update(db, current_user)

    @staticmethod
    def change_password(
        db: Session,
        current_user: User,
        data: ChangePasswordRequest,
    ):

        if not verify_password(
            data.old_password,
            current_user.hashed_password,
        ):
            raise HTTPException(
                status_code=400,
                detail="Old password is incorrect",
            )

        current_user.hashed_password = hash_password(
            data.new_password
        )

        UserRepository.update(db, current_user)

        return {
            "success": True,
            "message": "Password changed successfully"
        }