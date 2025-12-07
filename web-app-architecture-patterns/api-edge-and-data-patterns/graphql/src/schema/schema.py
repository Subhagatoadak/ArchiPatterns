try:
    import strawberry
except ImportError:  # pragma: no cover
    strawberry = None

if strawberry:

    @strawberry.type
    class Query:
        @strawberry.field
        def hello(self) -> str:  # pragma: no cover - illustrative
            return "hello from graphql"
else:
    class Query:  # type: ignore
        pass
