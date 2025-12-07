# Serverless Web APIs Template

Function-per-endpoint/API pattern using HTTP gateway + event triggers. Ideal for spiky traffic, POCs, or internal tools.

## Layout
- functions/http: HTTP handlers (one folder per route)
- functions/events: async/event-driven functions (queues, cron, webhooks)
- infra: IaC templates (SAM/CDK/Terraform), gateway config, env vars
- tests: integration tests and local emulation scripts

## Notes
- Keep cold start impact low: slim dependencies, shared layers for SDKs.
- Centralize auth/observability via gateway config rather than per function.
