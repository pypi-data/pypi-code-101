import json
import sys
import uuid
from pprint import pprint

import pytest
import requests
from requests import Response

from project_root import PROJECT_ROOT
from superwise import Client
from superwise import Superwise
from superwise.controller.exceptions import *
from superwise.models.task import Task
from tests import config
from tests import get_sw
from tests import print_results


@pytest.fixture(scope="function")
def mock_get_token(monkeypatch):
    monkeypatch.setattr(Client, "get_token", lambda *args, **kwargs: "token")


@pytest.fixture(scope="function")
def sw():
    return Superwise(client_name="test", client_id="test", secret="test")


@pytest.fixture(scope="function")
def mock_transaction_requests(monkeypatch):
    the_response = Response()
    the_response._content = b'{ "transaction_id" : "123" }'
    the_response.status_code = 201
    monkeypatch.setattr(requests, "post", lambda *args, **kwargs: the_response)


@pytest.fixture(scope="function")
def get_transaction_records_payload():
    with open(f"{PROJECT_ROOT}/tests/resources/transaction/records_payload.json") as f:
        return json.loads(f.read())


def test_transaction_records(mock_transaction_requests, mock_get_token, sw, get_transaction_records_payload):
    status = sw.transaction.log_batch(task_id=1, records=get_transaction_records_payload)
    assert isinstance(status, dict) and "transaction_id" in status.keys()
    status = sw.transaction.log_batch(task_id="test", version_id="test", records=get_transaction_records_payload)
    assert isinstance(status, dict) and "transaction_id" in status.keys()


def test_transaction_file(mock_transaction_requests, mock_get_token, sw):
    status = sw.transaction.log_file("gs://fvsdfvfdv")
    assert isinstance(status, dict) and "transaction_id" in status.keys()


def test_transaction_with_wrong_file_path(mock_transaction_requests, mock_get_token, sw):
    ok = False
    try:
        status = sw.transaction.log_file("wrong path")
    except Exception as e:
        assert str(e) == "transaction file failed because of wrong file path. file path should be gcs or s3 path."
        ok = True
    assert ok is True
