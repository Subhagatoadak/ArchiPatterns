# GraphQL API Template (FastAPI + Strawberry-ready)

Schema-driven single endpoint where clients ask for exactly what they need.

## When to use
- Multiple frontends with diverse data needs
- Complex graphs aggregated from multiple services
- You want strong schema/contracts and fewer round-trips

## Quickstart
- Local: `uvicorn src.main:app --reload` (installs strawberry if present)
- Docker: `docker build -t graphql-api . && docker run -p 8000:8000 graphql-api`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install graphql-api ./helm --set image.repository=your-registry/graphql`

## Layout
- `src/schema`: schema definition (sample `Query` provided)
- `src/resolvers`: place resolvers
- `src/loaders`: data loaders/batching

## Use cases
Highly interactive UIs (dashboards, forms) and multi-client APIs where payload shaping and over-fetch prevention matter.
