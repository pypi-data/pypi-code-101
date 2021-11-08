# coding=utf8
from .config import Config
from .utils.client import HTTPClient
from .log import logger
from .extractor import extract


class PRequest(object):
    def __init__(self, base_url='', conf='config.yml', host='host_url'):
        if base_url:
            self.base_url = base_url
        else:
            try:
                base_url = Config(conf).get(host, index=0)
                if base_url:
                    self.base_url = base_url
            except Exception as e:
                pass
        self.headers: dict = {}

    def send_request(self, api_url, method='POST', status='PASS', params=None, data=None, json=None, files=None,
                     extractor=None, timeout=10, cookies=None):
        """请求定制封装"""
        if not hasattr(self, 'logger'):
            self.logger = logger
        if not hasattr(self, 'headers'):
            self.headers: dict = {}

        # 建立http连接
        if not self.headers:
            client = HTTPClient(url=(self.base_url + api_url), method=method, timeout=timeout, cookies=cookies)
        else:
            client = HTTPClient(url=(self.base_url + api_url), method=method, headers=self.headers, timeout=timeout,
                                cookies=cookies)
        # 发送请求
        client.logger = self.logger
        response = client.send(params=params, json=json, data=data, files=files)

        try:
            # 有效用例和无效用例的最基本断言（针对status_code）
            if status == 'PASS':
                assert response.status_code in [200]
            elif status == 'FAIL':
                assert response.status_code not in [200]

            # 提取json值
            if status == 'PASS' and extractor is not None:
                response = extract(extractor, response.text)
                self.logger.info("数据处理: 提取{}的值为{} ".format(extractor, response))
        except Exception as e:
            self.logger.error(e)
        client.close()
        return response
