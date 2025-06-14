from uuid import uuid4
from fastapi import  HTTPException
from schemas.event_schema import Event, CreateEvent

events = {}

def create_event(event: CreateEvent):
    eid = str(uuid4())
    new_event = Event(id=eid, **event.model_dump())
    events[eid] = new_event
    return new_event

def list_events():
    return list(events.values())

def get_event(event_id:str):
    if event_id not in events:
        raise HTTPException(status_code=404, detail="Event not found")
    return events[event_id]


def close_event(event_id: str):
    if event_id not in events:
        raise HTTPException(status_code=404, detail="Event not found")
    event = events[event_id] 
    event.is_open = False
    return {"detail": "Event registration closed"}

def update_event(event_id:str, update:CreateEvent):
    if event_id not in events:
        raise HTTPException(status_code=404, detail="Event not found")
    updated_event = events[event_id].copy(update=update.model_dump())
    events[event_id] = updated_event
    return events[event_id]

def delete_event(event_id:str):
    if events.pop(event_id, None) is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"detail": "Event deleted"}
    
