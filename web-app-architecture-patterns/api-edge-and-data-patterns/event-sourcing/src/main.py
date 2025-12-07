from fastapi import FastAPI

from src.events.store import append_event, list_events

app = FastAPI(title="Event Sourcing API")


@app.post("/commands/record")
def record_event() -> dict:
    append_event({"type": "example-recorded"})
    return {"status": "recorded"}


@app.get("/events")
def events() -> list[dict]:
    return list_events()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
