# Classic Layered Architecture (FastAPI)

N-layered service separating API, application, domain, and infrastructure concerns.

## When to use
- Conventional CRUD/business apps where layering is clear
- Teams familiar with MVC/N-tier wanting straightforward structure
- Early to mid-stage products that may later modularize

## Layout
- `src/api`: controllers/routers
- `src/application`: use cases / orchestrators
- `src/domain`: entities and domain services
- `src/infrastructure`: DB/messaging/external adapters
- Dockerfile, docker-compose, Helm chart for deploys

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t classic-layered . && docker run -p 8000:8000 classic-layered`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install classic-layered ./helm --set image.repository=your-registry/classic-layered`

## Use cases
Straightforward business APIs, admin consoles, and internal tools where simplicity and familiarity matter more than strict domain isolation.
