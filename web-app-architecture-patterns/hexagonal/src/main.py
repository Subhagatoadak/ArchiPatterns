from fastapi import FastAPI

from src.adapters.http.routes import router as http_router

app = FastAPI(title="Hexagonal Architecture")
app.include_router(http_router, prefix="/api")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
