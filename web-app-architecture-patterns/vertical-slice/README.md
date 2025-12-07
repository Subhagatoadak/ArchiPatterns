# Vertical Slice Architecture (FastAPI)

Organize by feature slice instead of technical layer. Each slice owns handlers, validation, and data access.

## When to use
- Feature teams shipping independently
- CQRS-friendly flows with commands/queries per slice
- Desire to minimize cross-feature coupling

## Layout
- `src/features/orders`: handlers for order flows
- `src/features/users`: handlers for user flows
- `src/shared`: cross-cutting pieces
- Deployment assets: Dockerfile, docker-compose, Helm chart

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t vertical-slice . && docker run -p 8000:8000 vertical-slice`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install vertical-slice ./helm --set image.repository=your-registry/vertical-slice`

## Use cases
Product teams working on verticals (orders, users, catalog) with minimal coordination; greenfield APIs needing fast iteration.
