from src.adapters.db.repository import Repository


def get_repository() -> Repository:
    return Repository()
