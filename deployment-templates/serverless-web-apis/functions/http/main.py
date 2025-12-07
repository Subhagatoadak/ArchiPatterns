from fastapi import FastAPI
try:
    from mangum import Mangum
except ImportError:  # pragma: no cover - optional for containers
    Mangum = None

app = FastAPI(title="Serverless HTTP Functions")


@app.get("/health")
def health() -> dict:
    return {"service": "serverless-http", "status": "ok"}


handler = Mangum(app) if Mangum else None
