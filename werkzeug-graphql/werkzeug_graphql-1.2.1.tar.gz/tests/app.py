from objectql.schema import ObjectQLSchema
from werkzeug_graphql import GraphQLAdapter

api = ObjectQLSchema()


@api.root
class HelloWorld:

    @api.query
    def hello_world(self) -> str:
        return "Hello world!"


adapter = GraphQLAdapter.from_schema(
    schema=api,
    graphiql_default_query="test_query",
    graphiql_default_variables="test_variables"
)


def main(request):
    return adapter.dispatch(request=request)


if __name__ == "__main__":
    adapter.run_app(port=3501)
