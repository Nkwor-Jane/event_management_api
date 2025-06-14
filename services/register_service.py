from uuid import uuid4
from datetime import datetime
from fastapi import HTTPException
from schemas.register_schema import Registration
from services.event_service import events
from services.user_service import users

registrations = {}

def get_user_registration(user_id: str):
    return [reg for reg in registrations.values() if reg.user_id == user_id]

def list_all_registrations():
    return list(registrations.values())

def register_user(user_id: str, event_id:str):
    if user_id not in users or event_id not in events:
         raise HTTPException(status_code=404, detail="User or event not found")
    if not users[user_id]["is_active"]: 
        raise HTTPException(status_code=400, detail="User is inactive")
    if not events[event_id].is_open:
        raise HTTPException(status_code=400, detail="Event registration is closed")
    for regs in registrations.values():
        if regs.user_id == user_id and regs["event_id"] == event_id:
            raise HTTPException(status_code=400, detail="User already registered")
    
    rid = str(uuid4())
    regs = Registration(id=rid, user_id=user_id, event_id=event_id, registration_date=datetime.utcnow())
    registrations[rid] = regs
    return {"detail": "User registered"}

def mark_attended(rid: str):
    if rid not in registrations:
        raise HTTPException(status_code=404, detail="Registration not found")
    registrations[rid].attended = True
    return {"detail": "Attendance marked"}