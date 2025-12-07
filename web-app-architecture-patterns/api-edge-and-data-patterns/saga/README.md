# Saga Pattern Template (FastAPI)

Coordinate distributed workflows via orchestration or choreography.

## When to use
- Multi-step workflows across services (orders, payments, inventory)
- Need compensating actions for partial failures
- Want visibility into long-running process state

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t saga-api . && docker run -p 8000:8000 saga-api`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install saga-api ./helm --set image.repository=your-registry/saga`

## Layout
- `src/sagas`: orchestrators
- `src/steps`: activities/commands per step
- `src/integrations`: clients + contracts

## Use cases
Checkout flows, onboarding journeys, or any multi-system workflow needing retries and compensation.
