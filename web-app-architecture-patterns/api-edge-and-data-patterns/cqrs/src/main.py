from fastapi import FastAPI

from src.commands.create import create_item
from src.queries.list_items import list_items

app = FastAPI(title="CQRS API")


@app.post("/commands/items")
def create() -> dict:
    return create_item()


@app.get("/queries/items")
def list_all() -> list[dict]:
    return list_items()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
