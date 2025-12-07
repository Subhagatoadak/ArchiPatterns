from fastapi import APIRouter

from src.core.application.use_cases import get_status

router = APIRouter()


@router.get("/status")
def status() -> dict:
    return {"status": get_status()}
