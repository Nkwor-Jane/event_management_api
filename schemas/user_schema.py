from pydantic import BaseModel
from uuid import UUID

class User(BaseModel):
    id: UUID
    name: str
    email: str
    is_active: bool

class CreateUser(BaseModel):
    name: str
    email: str