from fastapi import APIRouter, HTTPException
from schemas.event_schema import CreateEvent, Event
from typing import List
import services.event_service as event_service

event_router = APIRouter(prefix="/events", tags=["Events"])

# Create an event
@event_router.post("/", response_model=Event)
def create_event(event: CreateEvent):
    return event_service.create_event(event)

# List all events
@event_router.get("/", response_model=List[Event])
def list_events():
    return event_service.list_events()

# Get one event
@event_router.get("/{event_id}", response_model=Event)
def get_one_event(event_id:str):
    return event_service.get_event(event_id)

# Close an event
@event_router.put("/{event_id}/close")
def close_event(event_id: str):
    return event_service.close_event(event_id)

# Update event details
@event_router.put("/{event_id}", response_model=Event)
def update_event(event_id: str, update:CreateEvent):
    return event_service.update_event(event_id, update)

# Delete an event
@event_router.delete("/{event_id}")
def delete_event(event_id:str):
    return event_service.delete_event(event_id)
