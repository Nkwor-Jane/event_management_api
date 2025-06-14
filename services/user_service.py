from uuid import uuid4
from fastapi import FastAPI, HTTPException
from schemas.user_schema import User, CreateUser

users = {}


def create_user(user:CreateUser):
    user_id = str(uuid4())
    new_user = User(id=user_id, is_active=True, **user.model_dump())
    users[user_id] = new_user.model_dump()
    return new_user

def list_users():
    return list(users.values())

def get_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]
    
def update_user(user_id: str, update: CreateUser):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id].update(update.model_dump())
    return users[user_id]

def delete_user(user_id: str):
    if users.pop(user_id, None) is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}

def deactivate_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id]["is_active"] = False
    return {"detail": "User deactivated"}
