# -*- coding: utf-8 -*-
"""
@  time    : 2020/03/09
@  author  : XieYZ
"""
from troop.api import APIClient


class ResultClient(APIClient):

    def result(self, task_id, wait=False):
        """获取任务结果"""
        url = f"{self.result_url}"
        data = {
            "task_id": task_id,
            "wait": wait
        }
        res = self.get(url=url, params=data)
        return res
