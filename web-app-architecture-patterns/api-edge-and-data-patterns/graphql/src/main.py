from fastapi import FastAPI

try:
    import strawberry
    from strawberry.fastapi import GraphQLRouter
except ImportError:  # pragma: no cover
    strawberry = None
    GraphQLRouter = None

from src.schema.schema import Query

app = FastAPI(title="GraphQL API")

if strawberry and GraphQLRouter:
    schema = strawberry.Schema(query=Query)
    graphql_app = GraphQLRouter(schema)
    app.include_router(graphql_app, prefix="/graphql")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "graphql": bool(strawberry)}
