from fastapi import APIRouter

router = APIRouter()


@router.get("")
def list_users() -> list[dict]:
    return [{"id": "usr_1", "email": "user@example.com"}]
