from fastapi import APIRouter

router = APIRouter()


@router.get("")
def list_examples() -> list[dict]:
    return [{"id": 1, "name": "example"}]
