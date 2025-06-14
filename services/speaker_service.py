from uuid import uuid4

speakers = {}

def initialize_speakers():
    for i in range(1, 4):
        sid = str(uuid4())
        speakers[sid] = {
            "id": sid,
            "name": f"Speaker: {i}",
            "topic": f"Topic: {i}"
        }

def list_speakers():
    return list(speakers.values())