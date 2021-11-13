import os
from functools import partial

import pandas as pd
import requests


class DataApi:
    def __init__(self, token, url, timeout=10):
        self.__url = url
        self.__token = token
        self.__timeout = timeout

    def request(self, api_name, **kwargs):
        headers = {
            "Authorization": "Token " + self.__token
        }

        req_params = {
            'api_name': api_name,
            'params': kwargs,
        }

        res = requests.post(self.__url, json=req_params, headers=headers, timeout=self.__timeout)
        result = res.json()
        if not result['success']:
            raise Exception(result['errorMessage'])

        data_type = result["data"]["type"]
        data = result["data"]["data"]

        if data_type == "pd":
            columns = data['fields']
            items = data['items']
            return pd.DataFrame(items, columns=columns)
        elif data_type == "text":
            if not isinstance(data, str):
                raise Exception('get error data')
            return data
        elif data_type == "bool":
            if not isinstance(data, bool):
                raise Exception('get error data')
            return data
        elif data_type == "list":
            if not isinstance(data, list):
                raise Exception('get error data')
            return data
        elif data_type == "json":
            return data
        elif data_type == "none":
            return None
        else:
            raise Exception("unknown data type: " + data_type)

    def __getattr__(self, name):
        return partial(self.request, name)


def api(token='', url=''):
    if url == '' or url is None:
        url = os.environ.get("LSYWYWSDK_API_URL", None)

    if url is None:
        raise Exception('url is not found')

    if token == '' or token is None:
        token = os.environ.get("LSYWYWSDK_API_TOKEN", None)

    if token is not None and token != '':
        client = DataApi(token, url=url)
        return client
    else:
        raise Exception('api token error.')
