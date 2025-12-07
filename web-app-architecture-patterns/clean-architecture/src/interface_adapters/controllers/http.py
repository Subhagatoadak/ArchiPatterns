from fastapi import APIRouter

from src.use_cases.health import get_status

router = APIRouter()


@router.get("/status")
def status() -> dict:
    return {"status": get_status()}
