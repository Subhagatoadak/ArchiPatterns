from fastapi import FastAPI

from src.api.routes import router as api_router

app = FastAPI(title="API Monolith")
app.include_router(api_router, prefix="/api")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
