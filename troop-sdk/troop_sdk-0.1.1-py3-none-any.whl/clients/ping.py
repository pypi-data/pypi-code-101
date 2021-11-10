# -*- coding: utf-8 -*-
"""
@  time    : 2020/03/09
@  author  : XieYZ
"""
from troop.api import APIClient


class PingClient(APIClient):

    def ping(self, data):
        """测试主机连通性"""
        url = f"{self.ping_url}"
        common_params = self.common_params()
        common_params.update(data)
        res = self.post(url=url, data=common_params)
        return res
