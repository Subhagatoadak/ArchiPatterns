from fastapi import FastAPI

from src.api.routes import router as api_router

app = FastAPI(title="Classic Layered API")
app.include_router(api_router, prefix="/api")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}
