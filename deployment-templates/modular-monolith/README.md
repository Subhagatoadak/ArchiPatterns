# Modular Monolith (FastAPI)

One deployable with clear domain modules for bounded contexts without distributed systems complexity.

## When to use
- You want microservice-like boundaries but a single deploy
- A few teams collaborating on shared code with strict module rules
- Feature set still fits in one database/runtime

## Layout
- `src/modules/<domain>/api`: module-specific HTTP surface
- `src/modules/<domain>/...`: add app/domain/infra layers per module
- `src/shared`: cross-cutting concerns (auth, logging, telemetry)
- `infra`: DB/bootstrap scripts, local containers

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t modular-monolith . && docker run -p 8000:8000 modular-monolith`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install modular-monolith ./helm --set image.repository=your-registry/modular-monolith`

## Use cases
Growing products that need domain boundaries and enforceable interfaces, but where synchronous intra-process calls are still acceptable.
