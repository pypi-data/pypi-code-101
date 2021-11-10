# -*- coding: utf-8 -*-
"""
@  time    : 2020/03/09
@  author  : XieYZ
"""
import requests


class BaseAPIClient(object):

    def __init__(self, base_url, header=None):
        self.header = header
        self.pure_url = base_url

    def start_requests(self, url, data=None, headers=None, files=None, methods='get'):
        if not headers:
            headers = self.header
        if methods == 'get':
            response = requests.get(url=url, params=data, headers=headers)
        elif methods == 'post':
            response = requests.post(url=url, json=data, headers=headers)
        elif methods == 'put':
            if files:
                headers['Content-Type'] = 'application/octet-stream'
                response = requests.put(url=url, files=files, headers=headers)
            else:
                response = requests.put(url=url, json=data, headers=headers)
        elif methods == 'delete':
            response = requests.delete(url=url, headers=headers)
        elif methods == 'patch':
            response = requests.patch(url=url, json=data, headers=headers)
        else:
            response = {'error': '请求methods错误'}
        return response

    @staticmethod
    def response(response, res_json=True):
        if 200 <= response.status_code < 400:
            if res_json:
                # noinspection PyBroadException
                try:
                    result = response.json()
                except Exception as _:
                    result = response.text
            else:
                result = response.text
        else:
            # noinspection PyBroadException
            try:
                result = response.json()
            except Exception as _:
                result = response.text
        return [result, response.status_code]

    def get(self, url, params=None):
        response = self.start_requests(url=url, data=params)
        return self.response(response)

    def post(self, url, data=None):
        response = self.start_requests(url=url, data=data, methods='post')
        return self.response(response)

    @staticmethod
    def result_parse(data, hostname):
        if "code" in data[0]:
            if data[0]["code"] == 0:
                if hostname in data[0]["result"]:
                    host_result = data[0]["result"][hostname]
                    if host_result["Status"] == "successful":
                        result = data[0]["result"][hostname]["Result"]
                        return result, data[1]
                    else:
                        error = f'{data[0]["result"][hostname]["Result"]} \n {data[0]["result"][hostname]["Error"]}'
                else:
                    error = "获取数据失败"
            else:
                error = data[0]["error"]
        else:
            error = "获取数据失败"
        return error, 500
