from typing import Any

from pydantic import ValidationError
from pydantic.main import ModelMetaclass
from starlette.requests import Request

from ..exceptions.util_exception import QueryParamException

def get_filters(request: Request,
                filter_schema_class: ModelMetaclass,
                model_mapper: dict
                ) -> Any:
    try:
        validate = filter_schema_class(**request.query_params)
    except ValidationError:
        raise QueryParamException()
    result = [
        model_mapper.get(key) <= request.query_params.get(key) if key.endswith("__lt") else
        model_mapper.get(key) >= request.query_params.get(key) if key.endswith("__gt") else
        model_mapper.get(key).in_(request.query_params.get(key).split(",")) if key.endswith("__in") else
        model_mapper.get(key).contains(request.query_params.get(key)) if key.endswith("__contain") else
        model_mapper.get(key) == request.query_params.get(key)
        for key in request.query_params
        if hasattr(validate, key)
        if getattr(validate, key) is not None
    ]
    return result
