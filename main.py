from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import List
from schemas.speaker_schema import Speaker
from services import speaker_service
from routes import user_route
from routes import event_route
from routes import register_route

# Initialize app with 3 speakers
@asynccontextmanager
async def lifespan(app:FastAPI):
    speaker_service.initialize_speakers()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/speakers", response_model=List[Speaker])
def get_speakers():
    return speaker_service.list_speakers()

app.include_router(user_route.user_router)
app.include_router(event_route.event_router)
app.include_router(register_route.registration_router)