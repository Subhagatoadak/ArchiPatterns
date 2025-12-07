# Service-Based (Mini-Services) Template

A handful of coarse-grained services to reduce coupling without full microservice complexity.

## Layout
- services/web-api: main HTTP surface combining several domains
- services/payments: isolated payment/risk logic
- services/reporting: analytics and scheduled reports
- shared: common contracts, telemetry, shared modules
- ops: deployment manifests, CI/CD pipelines

## Notes
- Start with 3–10 services; split further only when teams/throughput demand it.
- Prefer shared DB schemas within a service, separate DBs between services.
