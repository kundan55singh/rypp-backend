from typing import Optional

from pydantic import BaseModel, EmailStr


# -------------------------
# Create User
# -------------------------

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


# -------------------------
# User Response
# -------------------------

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: Optional[str] = None
    profile_image: Optional[str] = None
    role: str
    is_active: bool
    is_verified: bool

    model_config = {
        "from_attributes": True
    }


# -------------------------
# Update User
# -------------------------

class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    profile_image: Optional[str] = None


# -------------------------
# Change Password
# -------------------------

class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str