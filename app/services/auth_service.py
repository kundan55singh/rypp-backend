from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token


class AuthService:

    @staticmethod
    def register(
        db: Session,
        name: str,
        phone: str,
        email: str,
        password: str,
        confirm_password: str,
        referral_code: str | None = None,
    ):

        # Check if passwords match
        if password != confirm_password:
            raise HTTPException(
                status_code=400,
                detail="Passwords do not match"
            )

        # Check email already exists
        existing_user = UserRepository.get_by_email(db, email)

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        # Check phone already exists
        existing_phone = UserRepository.get_by_phone(db, phone)

        if existing_phone:
            raise HTTPException(
                status_code=400,
                detail="Phone number already registered"
            )

        # Create new user
        user = User(
            name=name,
            phone=phone,
            email=email,
            hashed_password=hash_password(password),
            referral_code=referral_code,
        )

        return UserRepository.create(db, user)

    @staticmethod
    def login(
        db: Session,
        email: str,
        password: str,
    ):

        user = UserRepository.get_by_email(db, email)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        if not verify_password(
            password,
            user.hashed_password
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        access_token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user.id,
                "name": user.name,
                "phone": user.phone,
                "email": user.email,
                "role": user.role,
                "is_verified": user.is_verified,
            },
        }