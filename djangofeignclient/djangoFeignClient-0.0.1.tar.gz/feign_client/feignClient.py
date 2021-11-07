#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------
    Author:     JiChao_Song
    Date  :     2021/11/7 下午9:14
    Desc  :
--------------------------------------
"""
from py_eureka_client import eureka_client


class FeignClient():

    def __init__(self, method, path, **kwargs):
        self.eureka_server = f"{kwargs.get('host')}/eureka"
        self.method = method
        self.path = path
        self.data = kwargs.get('data')
        self.headers = kwargs.get('headers') if kwargs.get('headers') else {
            'Content-Type': 'application/json;charset=UTF-8'}
        self.app_name = kwargs.get('app_name')

        eureka_client.init(eureka_server = self.eureka_server, app_name = self.app_name)

        self.result = eureka_client.do_service(self.app_name, self.path,
                                               # 返回类型，默认为 `string`，可以传入 `json`，如果传入值是 `json`，那么该方法会返回一个 `dict` 对象
                                               method = self.method,
                                               data = self.data,
                                               headers = self.headers,
                                               return_type = "json")
