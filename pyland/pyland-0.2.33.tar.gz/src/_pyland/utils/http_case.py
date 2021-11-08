# coding=utf8
import pytest
from ..config import Config
from ..pre_request import PRequest
from ..extractor import extract


def get_test_data(test_data_path):
    case = []
    http = []
    expected = []
    tests = Config(test_data_path).get('tests')
    for test in tests:
        case.append(test.get('case', ''))
        http.append(test.get('http', {}))
        expected.append(test.get('expected', {}))
    parameters = zip(case, http, expected)
    return case, parameters


cases, list_params = get_test_data("data/http_case_data/test_imgen.yml")


class TestImageGen():
    """
    Test Auto Banner Generation APIs.
    """
    @pytest.mark.skip()
    @pytest.mark.parametrize("case,http,expected", list(list_params), ids=cases)
    def test_requests(self, case, http, expected):
        response = PRequest().send_request(api_url=http['path'],
                                           method=http['method'],
                                           params=http['params'])
        assert extract("success", response) == expected['response']["success"]
