# -*- coding: utf-8 -*-
"""
@  time    : 2020/03/09
@  author  : XieYZ
"""
from troop.api import APIClient


class FileSendClient(APIClient):

    def file_send(self, data):
        """文件推送"""
        url = f"{self.file_send_url}"
        res = self.post(url=url, data=data)
        return res
