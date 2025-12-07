# Simple Product / Internal App

Start with a modular monolith and classic layered or clean architecture. Ship REST APIs and optionally an SPA served from the same deployable.

## Suggested stack
- Deploy: modular monolith (single repo/deploy)
- Internals: layered or clean architecture
- Edge: REST + basic auth/session
- Extras: background jobs, minimal message bus if needed

## Layout hint
- Follow `../../modular-monolith` structure; colocate web UI in the same repo for simplicity.
