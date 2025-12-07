from fastapi import FastAPI

app = FastAPI(title="order-service service")


@app.get("/health")
def health() -> dict:
    return {"service": "order-service", "status": "ok"}
