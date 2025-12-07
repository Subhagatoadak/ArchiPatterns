# Event Sourcing Template (FastAPI)

Persist domain events as the source of truth; rebuild state from event streams.

## When to use
- Need full history/audit trail
- Complex aggregates with evolving projections
- Systems benefiting from replay/temporal queries

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t event-sourcing-api . && docker run -p 8000:8000 event-sourcing-api`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install event-sourcing-api ./helm --set image.repository=your-registry/event-sourcing`

## Layout
- `src/events`: event definitions/store
- `src/aggregates`: aggregate roots
- `src/projections`: read models
- `src/event-store`: adapters for persistence

## Use cases
Auditable domains (finance, compliance), temporal analytics, and scenarios needing robust history and replay.
