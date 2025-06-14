from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class Registration(BaseModel):
    id: UUID
    user_id: str
    event_id: str
    registration_date: datetime
    attended: bool = False
