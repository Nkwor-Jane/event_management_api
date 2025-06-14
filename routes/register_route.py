from fastapi import APIRouter
from typing import List
from schemas.register_schema import Registration
import services.register_service as register_service

registration_router = APIRouter(prefix="/registrations", tags=["Registrations"])

# Register a user for an event
@registration_router.post("/{user_id}/{event_id}")
def register_user(user_id: str, event_id: str):
    return register_service.register_user(user_id, event_id)

# List all registrations
@registration_router.get("/", response_model=List[Registration])
def list_all_registrations():
    return register_service.list_all_registrations()

# Get all registrations for a specific user
@registration_router.get("/user/{user_id}", response_model=List[Registration])
def get_user_registration(user_id: str):
    return register_service.get_user_registration(user_id)

# Mark attendance for an event
@registration_router.post("/{rid}/attend")
def mark_attendance(rid: str):
    return register_service.mark_attended(rid)