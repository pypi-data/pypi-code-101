# -*- coding: utf-8 -*-
import sys
import requests
import os

from . import response

class Client(object):
    scheme = "https"

    def __init__(self, protocol = None, endpoint = None, method = None, timeout = 60, proxy = None, domain = None):
        """HTTP profile.
        :param protocol: http or https, default is https.
        :type protocol: str
        :param endpoint: The domain to access, like: cvm.tencentcloudapi.com
        :type endpoint: str
        """
        self.protocol = protocol or "https"
        self.endpoint = endpoint or "cloud.sealan.tech"
        self.method = method or "post"
        self.timeout = timeout
        self.proxy = proxy
        self.domain = domain
        self.token = None

    def request(self, params = None):

        if params == None:
            return None

        if self.token == None:
            self.get_token()

        if self.token == None:
            return {"error": "get token error"}

        if params.method == params.GET:
            return self.get(params)

        elif params.method == params.POST:
            return self.post(params)

    def get(self, params):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "user-agent": "sealan-cloud-sdk-python-v1"
        }

        url = f"{self.protocol}://{self.endpoint}/{params.path}?token={self.token}"
        r = requests.get(url, params = params.payload, headers = headers)
        if r.status_code == requests.codes.ok:
            return r.json()

    def post(self, params):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "user-agent": "sealan-cloud-sdk-python-v1",
            'Content-Type': 'application/json;charset=UTF-8'
        }

        url = f"{self.protocol}://{self.endpoint}/{params.path}?token={self.token}"
        r = requests.post(url, json = params.payload)
        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            return response.http_status_error(r)

    def get_token(self):
        payload = {
            'grant_type': "client_credential",
            'appid': self.appid,
            'secret': self.secret
        }
        r = requests.get(f"{self.protocol}://{self.endpoint}/user/token", params = payload)
        if r.status_code != requests.codes.ok:
            return response.AUTH_ERROR

        self.token = r.json()["token"]

class RequestParam(object):
    def __init__(self, method = None, path = None, payload = None):
        self.method = method or "get"
        self.path = path
        self.payload = payload
        self.GET = "get"
        self.POST = "post"