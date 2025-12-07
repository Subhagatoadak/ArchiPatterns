# Outbox Pattern Template (FastAPI)

Guarantee message delivery by writing business data and an outbox record in the same transaction.

## When to use
- Reliable integration events alongside database writes
- Need idempotent, retriable publishing to brokers
- Service-to-service messaging where loss/duplication is unacceptable

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t outbox-api . && docker run -p 8000:8000 outbox-api`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install outbox-api ./helm --set image.repository=your-registry/outbox`

## Layout
- `src/outbox`: store/repo
- `src/publishers`: publish to brokers
- `src/processors`: workers polling/outbox streaming

## Use cases
Transactional messaging, integrating with Kafka/Rabbit/SQS while keeping source-of-truth in your database.
