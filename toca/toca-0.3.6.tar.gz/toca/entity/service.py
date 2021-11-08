from typing import List
from winney import Winney

from toca.entity.api import Api


class Service(object):
    def __init__(self, name, host, port, headers=None, scheme="http"):
        self.name = name
        self.host = host
        self.port = port
        self.scheme = scheme
        self.headers = headers
        self.api_list: List[Api] = []
        self.winney = Winney(host=self.host,
                             port=self.port,
                             headers=self.headers,
                             protocol=scheme)

    def is_json(self):
        if not self.headers:
            return False
        for key, value in self.headers.items():
            if key.lower() == "content-type" and value.lower(
            ) == "application/json":
                return True
        return False

    def add_api(self, api: Api):
        if not isinstance(api, Api):
            raise TypeError(
                "Invalid type, Api is expected, but {} found".format(
                    type(api)))
        self.api_list.append(api)

    def get_dynamic_value(self, dynamic_name):
        group_name, dynamic_name = dynamic_name.split(".", 1)
        for group in self.group_list:
            if not group.name == group_name:
                continue
            return group.get_dynamic_value(dynamic_name)
