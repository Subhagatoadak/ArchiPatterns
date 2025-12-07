# Hexagonal Architecture (Ports & Adapters) with FastAPI

Domain-centric core with adapters for I/O, enabling framework/database swaps.

## When to use
- Long-lived systems where infrastructure may change
- Need to reuse core logic across transports (HTTP, CLI, workers)
- Teams wanting clear inbound/outbound ports and testability

## Layout
- `src/core/domain`: entities/value objects
- `src/core/application`: use cases + ports
- `src/adapters/http`: FastAPI controllers
- `src/adapters/db`, `src/adapters/messaging`: outbound adapters
- `src/config`: wiring/DI
- Deployment assets: Dockerfile, docker-compose, Helm chart

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t hexagonal . && docker run -p 8000:8000 hexagonal`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install hexagonal ./helm --set image.repository=your-registry/hexagonal`

## Use cases
Systems needing strong testability and swappable infrastructure—multi-transport APIs, vendor migrations, or code shared across HTTP/CLI/batch.
