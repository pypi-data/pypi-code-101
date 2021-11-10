# Copyright (c) 2014-2020 GeoSpock Ltd.

import json
import requests_mock
import click
from click.testing import CliRunner
from geospock_cli.geospockcli import geospock_cli
from unittest.mock import patch

dummy_endpoint = 'http://local:8080'


def test_get_table_list():
    dummy_tables = ["table1", "table2"]
    mock_response_code = 200
    mock_response_text = json.dumps(dummy_tables)
    with requests_mock.Mocker() as m:
        m.register_uri('GET', dummy_endpoint + '/schemas/dummySchema/tables', text=mock_response_text,
                       status_code=mock_response_code)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "table",
                                "list", "--schema", "dummySchema"])
        assert result.exit_code == 0
        assert json.loads(result.output) == dummy_tables


def test_insert_into_table():
    mock_response_code = 202
    expected_result = '{\n  "response": "Accepted"\n}\n'
    with requests_mock.Mocker() as m:
        m.register_uri('POST', dummy_endpoint + '/schemas/dummySchema/tables/dummyTable', text="",
                       status_code=mock_response_code)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "table",
                                "insert", "--schema", "dummySchema", "--table", "dummyTable", "--instance-count", "3",
                                "--data-url", "s3://something"])
        assert result.exit_code == 0
        assert result.output == expected_result


def test_drop_table_force():
    mock_response_code = 204
    expected_result = '{\n  "response": "No Content"\n}\n'
    with requests_mock.Mocker() as m:
        m.register_uri('DELETE', dummy_endpoint + '/schemas/dummySchema/tables/dummyTable', text="",
                       status_code=mock_response_code)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "table",
                                "drop", "--schema", "dummySchema", "--table", "dummyTable", "--force"])
        assert result.exit_code == 0
        assert result.output == expected_result


@patch("click.confirm")
def test_drop_table_yes(mock_click):
    mock_click.return_value = True
    mock_response_code = 204
    expected_result = '{\n  "response": "No Content"\n}\n'
    with requests_mock.Mocker() as m:
        m.register_uri('DELETE', dummy_endpoint + '/schemas/dummySchema/tables/dummyTable', text="",
                       status_code=mock_response_code)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "table",
                                "drop", "--schema", "dummySchema", "--table", "dummyTable"])
        assert result.exit_code == 0
        assert result.output == expected_result


@patch("click.confirm")
def test_drop_table_no(click_mock):
    click_mock.side_effect = abort_side_effect
    runner = CliRunner()
    result = runner.invoke(geospock_cli,
                           ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "table",
                            "drop", "--schema", "dummySchema", "--table", "dummyTable"])
    assert result.exit_code == 1
    assert result.output == "Aborted!\n"


@patch("click.confirm")
def test_revert_insert_yes(mock_click):
    mock_click.return_value = True
    mock_response_code = 204
    expected_result = '{\n  "response": "No Content"\n}\n'
    with requests_mock.Mocker() as m:
        m.register_uri('PATCH',
                       dummy_endpoint + '/schemas/dummySchema/tables/dummyTable/operation/dummyOperation',
                       text="", status_code=mock_response_code)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "table",
                                "revert-insert", "--schema", "dummySchema", "--table", "dummyTable",
                                "--operation-id", "dummyOperation"])
        assert result.exit_code == 0
        assert result.output == expected_result


@patch("click.confirm")
def test_revert_insert_no(click_mock):
    click_mock.side_effect = abort_side_effect
    runner = CliRunner()
    result = runner.invoke(geospock_cli,
                           ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "table",
                            "revert-insert", "--schema", "dummySchema", "--table", "dummyTable",
                            "--operation-id", "dummyOperation"])
    assert result.exit_code == 1
    assert result.output == "Aborted!\n"


def abort_side_effect(*args, **kwargs):
    raise click.Abort()
