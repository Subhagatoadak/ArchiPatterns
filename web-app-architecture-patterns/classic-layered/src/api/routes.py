from fastapi import APIRouter

from src.application.services import get_status

router = APIRouter()


@router.get("/status")
def status() -> dict:
    return {"status": get_status()}
