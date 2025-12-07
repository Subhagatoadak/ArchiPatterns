from fastapi import FastAPI

from src.modules.billing.api.routes import router as billing_router
from src.modules.users.api.routes import router as users_router
from src.modules.catalog.api.routes import router as catalog_router

app = FastAPI(title="Modular Monolith")
app.include_router(billing_router, prefix="/api/billing")
app.include_router(users_router, prefix="/api/users")
app.include_router(catalog_router, prefix="/api/catalog")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "modules": ["billing", "users", "catalog"]}
