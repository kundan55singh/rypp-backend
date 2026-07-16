from typing import Optional

from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):
    name: str
    phone: str
    email: EmailStr
    password: str
    confirm_password: str
    referral_code: Optional[str] = None


class RegisterResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"