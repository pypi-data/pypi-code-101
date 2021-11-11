# -*- coding: utf-8 -*-
"""
@  time    : 2020/03/09
@  author  : XieYZ
"""
from troop.api import APIClient


class HostClient(APIClient):

    def list(self, params=None):
        """获取HOST详细信息列表"""
        url = f"{self.host_base_url}s"
        res = self.get(url=url, params=params)
        return res

    def all(self, params=None):
        """获取所有HOST（包括未接受和已拒绝的主机）"""
        url = f"{self.host_base_url}s/all"
        res = self.get(url=url, params=params)
        return res

    def keys(self):
        """获取HOST主机名列表"""
        url = f"{self.host_base_url}/keys"
        res = self.get(url=url)
        return res

    def accept(self, host):
        """接受指定HOST"""
        url = f"{self.host_base_url}/accept"
        res = self.post(url=url, data={"hostname": host})
        return res

    def accept_all(self):
        """接受所有HOST"""
        url = f"{self.host_base_url}/accept/all"
        res = self.post(url=url)
        return res

    def reject(self, host):
        """拒绝HOST"""
        url = f"{self.host_base_url}/reject"
        res = self.post(url=url, data={"hostname": host})
        return res

    def reject_all(self):
        """拒绝所有HOST"""
        url = f"{self.host_base_url}/reject/all"
        res = self.post(url=url)
        return res

    def delete(self, host):
        """删除指定HOST"""
        url = f"{self.host_base_url}/delete"
        res = self.post(url=url, data={"hostname": host})
        return res

    def delete_all(self):
        """删除所有HOST"""
        url = f"{self.host_base_url}/delete/all"
        res = self.post(url=url)
        return res
