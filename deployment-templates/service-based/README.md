# Service-Based / Mini-Services (FastAPI)

A handful of coarse-grained services to reduce coupling without full microservice overhead.

## When to use
- 3–10 services are enough for team/domain splits
- You want independent deploys for critical areas (payments/reporting) but shared stack elsewhere
- Reduced distributed complexity compared to dozens of microservices

## Layout
- Services: `web-api`, `payments`, `reporting`
- `shared`: shared contracts/telemetry
- `ops`: CI/CD scripts and manifests
- Root `docker-compose.yml`: spins up all services
- Helm chart `helm/`: templated deployments from `values.yaml`

## Quickstart
- Local service: `cd services/web-api && docker-compose up`
- Local stack: `docker-compose up` from repository root
- Docker: `docker build -t payments ./services/payments`
- Helm: `helm upgrade --install service-based ./helm --set services[0].image=...`

## Use cases
Products that outgrow a monolith but don’t need dozens of services—split along business capabilities while keeping operational simplicity.
