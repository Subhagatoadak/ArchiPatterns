from src.core.domain.entities import ServiceStatus


def get_status() -> str:
    return ServiceStatus(name="hexagonal-service", status="ok").status
