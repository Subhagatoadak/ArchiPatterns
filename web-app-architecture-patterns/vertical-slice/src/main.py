from fastapi import FastAPI

from src.features.orders.handlers import router as orders_router
from src.features.users.handlers import router as users_router

app = FastAPI(title="Vertical Slice API")
app.include_router(orders_router, prefix="/api/orders")
app.include_router(users_router, prefix="/api/users")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
