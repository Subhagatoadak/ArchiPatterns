from fastapi import APIRouter

router = APIRouter()


@router.get("")
def list_orders() -> list[dict]:
    return [{"id": "ord_1", "status": "draft"}]


@router.post("")
def create_order() -> dict:
    return {"id": "ord_new", "status": "created"}
