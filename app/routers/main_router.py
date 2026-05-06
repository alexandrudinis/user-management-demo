from fastapi import APIRouter, HTTPException
from typing import List
from app.models import User
from app.schemas import UserCreate, UserUpdate

router = APIRouter()

@router.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    db_user = User(**user.dict())
    db_user.save()  # Assuming User has a save method
    return db_user

@router.get("/users/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 10):
    return User.query.offset(skip).limit(limit).all()  # Adjust based on your ORM

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    user = User.query.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate):
    db_user = User.query.get(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db_user.save()  # Save the updated user
    return db_user

@router.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    db_user = User.query.get(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.delete()  # Assuming a delete method exists
    return {"detail": "User deleted"}