# src/api/routes/authors.py
from flask import Blueprint
from flask import request
from ..utils.responses import response_with
from ..utils import responses as resp
from ..cases_execute import run_case
from ..utils.error import MissingError

test_routes = Blueprint("test_routes", __name__)


@test_routes.route('/run', methods=['POST'])
def test_cases():
    try:
        data = request.get_json()
        result = run_case(data)
        return response_with(resp.SUCCESS_201, value={"result":
                                                          result})
    except MissingError as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422, message=e.__str__())
    except FileNotFoundError as e:
        print(e)
        return response_with(resp.INVALID_INPUT_423, message=e.__str__())
