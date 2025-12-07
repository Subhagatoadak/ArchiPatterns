events: list[dict] = []


def append_event(event: dict) -> None:
    events.append(event)


def list_events() -> list[dict]:
    return events
