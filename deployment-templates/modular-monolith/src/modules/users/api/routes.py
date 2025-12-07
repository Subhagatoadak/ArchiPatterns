from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
def status() -> dict:
    return {"module": "users", "status": "ok"}
