from fastapi import FastAPI

from src.outbox.store import enqueue, dequeue

app = FastAPI(title="Outbox API")


@app.post("/commands/enqueue")
def enqueue_message() -> dict:
    enqueue({"type": "example", "payload": {"id": 1}})
    return {"status": "queued"}


@app.post("/commands/publish-next")
def publish_next() -> dict:
    message = dequeue()
    return {"published": message}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
