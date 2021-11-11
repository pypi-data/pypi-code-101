# -*- coding: utf-8 -*-
"""
@  time    : 2020/03/09
@  author  : XieYZ
"""
from troop.base import BaseAPIClient


class APIClient(BaseAPIClient):

    def __init__(self, base_url, header=None):
        super(APIClient, self).__init__(base_url, header)
        self.base_url = '{base_url}'.format(base_url=base_url)
        self.host_base_url = '{base_url}/host'.format(base_url=self.base_url)
        self.ping_url = '{base_url}/ping'.format(base_url=self.base_url)
        self.file_send_url = '{base_url}/file'.format(base_url=self.base_url)
        self.command_task_url = '{base_url}/tasks'.format(base_url=self.base_url)
        self.plugin_url = '{base_url}/plugin'.format(base_url=self.base_url)
        self.result_url = '{base_url}/task'.format(base_url=self.base_url)
        self.file_manage_base_url = '{base_url}/file_manage'.format(base_url=self.base_url)

    @staticmethod
    def common_params():
        return {
            "target": "",
            "target_type": "server",
            "tag": "",
            "os": "",
            "detach": False,
            "timeout": 0
        }
