# gRPC Template (FastAPI-adjacent)

Binary RPC with protobuf contracts. This template keeps a FastAPI health surface and proto stub for service-to-service calls.

## When to use
- High-performance service-to-service calls
- Strongly typed contracts and streaming support
- Internal meshes/gateways that translate REST ↔ gRPC

## Quickstart
- Local HTTP health: `uvicorn src.main:app --reload`
- Docker: `docker build -t grpc-api . && docker run -p 8000:8000 grpc-api`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install grpc-api ./helm --set image.repository=your-registry/grpc`
- Generate stubs: `python -m grpc_tools.protoc -I src/proto --python_out=src --grpc_python_out=src src/proto/service.proto`

## Layout
- `src/proto`: protobuf contracts
- `src/server`: gRPC service implementations
- `src/clients`: generated clients/wrappers

## Use cases
Service-to-service APIs, backend control planes, and scenarios needing streaming or strict contracts.
