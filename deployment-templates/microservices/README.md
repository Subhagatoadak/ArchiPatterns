# Microservices (FastAPI-first skeleton)

Multiple independently deployable services with their own storage, fronted by an API Gateway.

## When to use
- Multiple teams, heterogeneous tech, or scaling beyond a single codebase
- Need independent deploys, blast-radius reduction, and clear domain ownership
- Cross-service concerns handled via gateway and service mesh

## Layout
- `services/api-gateway`: routing, auth, rate limits
- Domain services: `user-service`, `order-service`, `payment-service`, `reporting-service`
- `shared/lib`: shared contracts/utilities
- `ops`: add scripts, observability, IaC
- Root `docker-compose.yml`: local orchestration
- Helm chart `helm/`: deploys all services from `values.yaml`

## Quickstart
- Local (single service): `cd services/user-service && docker-compose up`
- Local stack: `docker-compose up` from repository root
- Docker (per service): `docker build -t user-service ./services/user-service`
- Helm: `helm upgrade --install microservices ./helm --set services[0].image=...`

## Use cases
Large teams needing strong domain isolation, independent scaling, and room for polyglot stacks while keeping FastAPI as the default API surface.
