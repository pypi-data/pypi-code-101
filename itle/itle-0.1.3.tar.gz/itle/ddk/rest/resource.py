# -*- coding: UTF-8 -*-
import aiohttp as aiohttp

from itle.base import RestApi
from itle.ddk.ddk_resource_type import DDKResourceType


class DDKResourceUrlRequest(RestApi):
    def __init__(self, aio_http: aiohttp, domain: str, port: int):
        super(DDKResourceUrlRequest, self).__init__(aio_http, domain, port)

        self.ddk_pid = None
        self.custom_params = None
        self.url = None
        self.resource_type = DDKResourceType.BILLIONS_SUBSIDE.value

    def get_api_uri(self):
        return '/api/1.0/ddk/resource_url'

    def get_method(self):
        return 'GET'
