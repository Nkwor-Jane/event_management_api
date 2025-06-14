from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class CreateEvent(BaseModel):
    title: str
    location: str
    date: datetime

class Event(CreateEvent):
    id: UUID
    title: str
    location: str
    date: datetime
    is_open: bool = True



