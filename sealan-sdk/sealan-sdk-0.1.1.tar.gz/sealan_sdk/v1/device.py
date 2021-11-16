# -*- coding: utf-8 -*-
from . import response
from . import client

class DeviceRequest(object):

    def __init__(self):
        return

    def get_device_list(self, sorter = None, page = 1, size = 20):
        params = client.RequestParam()
        params.path = f"server/device/list"
        params.method = params.POST
        params.payload = {
            "pageindex": page,
            "pagesize": size,
            "sorter": sorter,
        }
        return params
