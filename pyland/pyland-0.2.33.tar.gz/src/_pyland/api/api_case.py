# src/api/routes/authors.py
from flask import Blueprint
from flask import request
from ..utils.responses import response_with
from ..utils import responses as resp
from ..cases_collect import list_case, update_case
from ..utils.error import MissingError


case_routes = Blueprint("case_routes", __name__)


@case_routes.route('/update', methods=['POST'])
def update_cases():
    try:
        data = request.get_json()
        result = update_case(data)
        return response_with(resp.SUCCESS_201, value={"result":
                                                          result})
    except MissingError as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422, message=e.__str__())
    except FileNotFoundError as e:
        print(e)
        return response_with(resp.INVALID_INPUT_423, message=e.__str__())


@case_routes.route('/list', methods=['GET'])
def list_cases():
    try:
        data = request.get_json()
        result = list_case(data)
        return response_with(resp.SUCCESS_201, value={"result":
                                                          result})
    except MissingError as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422, message=e.__str__())
    except FileNotFoundError as e:
        print(e)
        return response_with(resp.INVALID_INPUT_423, message=e.__str__())
