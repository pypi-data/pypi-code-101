from typing import Any, List

from starlette.requests import Request
from sqlalchemy import desc, asc

ORDER_KEY = 'order'


def get_order_params(request: Request, order_keys: List[str]) -> list:
    result = []
    if ORDER_KEY in request.query_params:
        orders = request.query_params.get(ORDER_KEY, [])
        if isinstance(orders, str):
            result = request.query_params.get('order').split(',')
        elif isinstance(orders, list):
            result = orders
    orders = [desc(o_param.replace("-", '')) if o_param.startswith('-') else asc(o_param) for o_param in result
              if isinstance(o_param, str)
              if (o_param in order_keys or o_param.replace("-", '') in order_keys)
              ]
    return orders
