# -*- coding: utf-8 -*-
"""
@  time    : 2020/03/09
@  author  : XieYZ
"""
from troop.api import APIClient


class PluginClient(APIClient):

    def plugin(self, data, plugin_name, action, args=None, no_check=False, config_byte=None, config_name=None):
        """执行命令"""
        url = f"{self.plugin_task_url}"
        data.update({
            "plugin": plugin_name,
            "action": action,
            "args": args,
            "config_byte": config_byte,
            "config_name": config_name,
            "no_check": no_check
        })
        common_params = self.common_params()
        common_params.update(data)
        res = self.post(url=url, data=common_params)
        return res
