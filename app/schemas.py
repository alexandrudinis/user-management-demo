from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: str  # Assuming ISO format string representation

    class Config:
        from_attributes = True

class ItemCreate(BaseModel):
    title: str

class ItemUpdate(BaseModel):
    title: Optional[str] = None

class ItemResponse(BaseModel):
    id: int
    title: str
    owner_id: int
    created_at: str  # Assuming ISO format string representation

    class Config:
        from_attributes = True