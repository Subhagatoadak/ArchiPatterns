from fastapi import FastAPI

from src.sagas.order_saga import execute_order_saga

app = FastAPI(title="Saga API")


@app.post("/commands/place-order")
def place_order() -> dict:
    return execute_order_saga()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
