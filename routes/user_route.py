from fastapi import APIRouter
from schemas.user_schema import User, CreateUser
from typing import List
import services.user_service as user_service

user_router = APIRouter(prefix="/users", tags=["Users"])

# Create a user
@user_router.post("/", response_model=User)
def create_user(user: CreateUser):
    return user_service.create_user(user)

# List all users
@user_router.get("/", response_model=List[User])
def list_users():
    return user_service.list_users()

# Get one user
@user_router.get("/{user_id}", response_model=User)
def get_user(user_id:str):
        return user_service.get_user(user_id)

# Update a user's details
@user_router.put("/{user_id}", response_model=User)
def update_user(user_id: str, update: CreateUser):
    return user_service.update_user(user_id, update)

# Delete user
@user_router.delete("/{user_id}")
def delete_user(user_id: str):
     return user_service.delete_user(user_id)

# Deactivate a user
@user_router.post("/{user_id}/deactivate")
def deactivate_user(user_id: str):
    return user_service.deactivate_user(user_id)