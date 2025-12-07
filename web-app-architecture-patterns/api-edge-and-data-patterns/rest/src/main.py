from fastapi import FastAPI

from src.routes.api import router as api_router

app = FastAPI(title="REST API")
app.include_router(api_router, prefix="/api")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
