# Microservices Template

Multiple independent services with their own storage, fronted by an API Gateway. Fit for larger teams, heterogeneous stacks, or high scale.

## Layout
- services/api-gateway: routing, auth, rate limiting, logging
- services/user-service: identity/profile APIs + DB
- services/order-service: orders + persistence
- services/payment-service: payment orchestration + PCI concerns
- services/reporting-service: async projections, BI endpoints
- shared/lib: contracts, tracing/logging middleware, codegen outputs
- ops: service mesh config, deployment charts/manifests, scripts

## Notes
- Prefer async messaging for cross-service workflows; use the Outbox pattern per service.
- Apply mTLS/timeouts/retries at gateway/mesh level.
- Keep service boundaries aligned to teams and business domains.
