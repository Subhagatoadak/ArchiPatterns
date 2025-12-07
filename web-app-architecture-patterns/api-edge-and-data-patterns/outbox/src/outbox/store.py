from collections import deque

_queue: deque[dict] = deque()


def enqueue(message: dict) -> None:
    _queue.append(message)


def dequeue() -> dict | None:
    return _queue.popleft() if _queue else None
