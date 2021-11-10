from http.client import HTTPException
from typing import Union, Any

from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from exceptions.exception_result import exception_result
from fastapi.exceptions import RequestValidationError, HTTPException


class BaseCustomHttpException(HTTPException):

    def __init__(self, status_code: int = 400, val: str = None, *args, **kwargs):
        self.val = val
        super(BaseCustomHttpException, self).__init__(status_code, *args, **kwargs)


def get_exception_handlers():
    return Union[Exception], Union[internal_exception_handler]


def get_validation_exception_handlers():
    return BaseCustomHttpException, api_exception_handler


def get_request_validation_exception_handlers():
    return RequestValidationError, api_validation_exception_handler


def internal_exception_handler(request, exc: Exception):
    if isinstance(exc, BaseCustomHttpException):
        return api_exception_handler(request, exc)

    if isinstance(exc, ValidationError):
        return api_validation_exception_handler(request, exc)

    return JSONResponse(status_code=500,
                        content=exception_result.get_content(exc))


def api_exception_handler(request: Request, exc: BaseCustomHttpException):
    if isinstance(exc.detail, dict):
        return JSONResponse(status_code=exc.status_code,
                            content=exc.detail)
    return JSONResponse(status_code=exc.status_code,
                        content=exception_result.get_content(exc))


def api_validation_exception_handler(request: Request, exc: Any):
    result = ""
    if isinstance(exc.errors(), list):
        result = list(map(lambda error: {
            "field": error["loc"][-1],
            "detail": error["msg"]
        }, exc.errors()))

    return JSONResponse(status_code=400,
                        content={
                            "status_code": 400,
                            "message": "not ok",
                            "result": result
                        })
