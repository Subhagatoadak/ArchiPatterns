# Modular Monolith Architecture (FastAPI)

Single deployable structured into bounded-context modules with strict interfaces.

## When to use
- Domain boundaries matter but distributed systems overhead is undesirable
- Teams want clear ownership per module inside one repo/runtime
- You plan gradual extraction of services later

## Layout
- `src/modules/<domain>/api`: module HTTP surface
- Extend modules with app/domain/infra folders as needed
- `src/shared`: cross-cutting utilities
- Deployment: Dockerfile, docker-compose, Helm chart

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t modular-monolith-arch . && docker run -p 8000:8000 modular-monolith-arch`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install modular-monolith-arch ./helm --set image.repository=your-registry/modular-monolith-arch`

## Use cases
Growing products with multiple bounded contexts (billing, users, catalog) where synchronous in-process calls suffice and refactors are expected.
