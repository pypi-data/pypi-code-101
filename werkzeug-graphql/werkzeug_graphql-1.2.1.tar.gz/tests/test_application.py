import threading
import time
import urllib

import pytest
from werkzeug.test import Client, EnvironBuilder
from werkzeug.wrappers import BaseResponse, Request

from werkzeug_graphql import GraphQLAdapter


def is_objectql_installed():
    try:
        import objectql
    except ImportError:
        return False

    return True


class TestApplication:

    def test_dispatch(self, schema):
        adapter = GraphQLAdapter(schema=schema)

        builder = EnvironBuilder(method='GET', query_string="query={hello}")

        request = Request(builder.get_environ())
        response = adapter.dispatch(request=request)

        assert response.status_code == 200
        assert response.data == b'{"data":{"hello":"world"}}'

    def test_app(self, schema):
        adapter = GraphQLAdapter(schema=schema)

        c = Client(adapter.application(), BaseResponse)
        response = c.get('/?query={hello}')

        assert response.status_code == 200
        assert response.data == b'{"data":{"hello":"world"}}'

    def test_graphiql(self, schema):
        adapter = GraphQLAdapter(schema=schema)

        c = Client(adapter.application(), BaseResponse)
        response = c.get('/', headers={"Accept": "text/html"})

        assert response.status_code == 200
        assert b'GraphiQL' in response.data

    def test_no_graphiql(self, schema):
        adapter = GraphQLAdapter(schema=schema, serve_graphiql=False)

        c = Client(adapter.application(), BaseResponse)
        response = c.get('/', headers={"Accept": "text/html"})

        assert response.status_code == 400

    def test_run_app_graphiql(self, schema):
        adapter = GraphQLAdapter(schema=schema)

        thread = threading.Thread(target=adapter.run_app, daemon=True)
        thread.start()

        time.sleep(0.5)

        req = urllib.request.Request(
            "http://localhost:5000",
            headers={"Accept": "text/html"}
        )
        response = urllib.request.urlopen(req).read()

        assert b'GraphiQL' in response

    @pytest.mark.skipif(
            not is_objectql_installed(),
            reason="ObjectQL is not installed"
        )
    def test_objectql(self):

        from objectql import ObjectQLSchema

        schema = ObjectQLSchema()

        @schema.root
        class RootQueryType:

            @schema.query
            def hello(self) -> str:
                return "world"

        adapter = GraphQLAdapter.from_schema(schema=schema)

        c = Client(adapter.application(), BaseResponse)
        response = c.get('/?query={hello}')

        assert response.status_code == 200
        assert response.data == b'{"data":{"hello":"world"}}'
