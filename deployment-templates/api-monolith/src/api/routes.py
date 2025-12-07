from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
def status() -> dict:
    return {"service": "api-monolith", "status": "ok"}
