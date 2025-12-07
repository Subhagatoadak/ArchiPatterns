# CQRS Template (FastAPI)

Separate write and read models to simplify complex domains and read-heavy systems.

## When to use
- Read-heavy workloads needing optimized projections
- Complex write logic with validation/side effects
- Event-driven systems building read models asynchronously

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t cqrs-api . && docker run -p 8000:8000 cqrs-api`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install cqrs-api ./helm --set image.repository=your-registry/cqrs`

## Layout
- `src/commands`: write handlers
- `src/queries`: read handlers
- `src/read-models`: projections/views
- `src/event-bus`: contracts/dispatcher

## Use cases
Read-heavy APIs, auditability requirements, or domains with multiple derived views (dashboards, search indexes).
