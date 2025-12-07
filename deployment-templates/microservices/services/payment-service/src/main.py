from fastapi import FastAPI

app = FastAPI(title="payment-service service")


@app.get("/health")
def health() -> dict:
    return {"service": "payment-service", "status": "ok"}
