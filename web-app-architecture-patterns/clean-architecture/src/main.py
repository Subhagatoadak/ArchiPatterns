from fastapi import FastAPI

from src.interface_adapters.controllers.http import router as http_router

app = FastAPI(title="Clean Architecture API")
app.include_router(http_router, prefix="/api")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
