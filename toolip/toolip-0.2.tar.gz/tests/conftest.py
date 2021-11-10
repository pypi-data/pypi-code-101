from os import environ

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture

environ['API_DOC_USERNAME'] = 'USERNAME'
environ['API_DOC_PASSWORD'] = 'PASSWORD'


@fixture
def test_client():
    return TestClient(app=FastAPI(docs_url=None, redoc_url=None, openapi_url=None))


@fixture
def test_app(request):
    return FastAPI(**request.param)
