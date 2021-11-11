# -*- coding: utf-8 -*-
"""
@  time    : 2020/03/09
@  author  : XieYZ
"""
from troop.api import APIClient


class FileManageClient(APIClient):

    def files(self, data, prefix):
        """文件列表"""
        url = f"{self.file_manage_base_url}"
        data.update({
            "prefix": prefix
        })
        common_params = self.common_params()
        common_params.update(data)
        res = self.get(url=url, params=common_params)
        return res

    def file_manage(self, data, prefix, action):
        """文件管理"""
        url = f"{self.file_manage_base_url}"
        data.update({
            "action": action,
            "prefix": prefix
        })
        common_params = self.common_params()
        common_params.update(data)
        res = self.post(url=url, data=common_params)
        return res
