from fastapi import FastAPI

app = FastAPI()
speakers = {}

# List all speakers
@app.get("/speakers")
def list_speakers():
    return speakers