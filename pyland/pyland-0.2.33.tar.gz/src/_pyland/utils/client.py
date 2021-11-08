"""
添加用于接口测试的client，对于HTTP接口添加HTTPClient，发送http请求。
还可以封装TCPClient，用来进行tcp链接，测试socket接口等等。
"""
from requests import session
import allure
from ..log import logger
from json import dumps as json_dumps

# import socket
# import json


METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'TRACE', 'OPTIONS', 'CONNECT']


class UnSupportMethodException(Exception):
    """传入method参数不支持时，抛出异常"""
    pass


class HTTPClient(object):
    """
    http请求的client。初始化时传入url、method等，可以添加headers和cookies，但没有auth、proxy。

    >>> HTTPClient('http://www.baidu.com').send()
    <Response [200]>
    """

    def __init__(self, url, method='POST', headers=None, cookies=None, timeout=20):
        """headers/cookies均为字典类型。如headers={'Content_Type':'text/html'}"""
        if headers is None:
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0"
            }
        self.url = url
        self.method = method.upper()
        self.headers = headers
        self.session = session()
        self.cookies = cookies
        self.timeout = timeout
        if self.method not in METHODS:
            raise UnSupportMethodException('不支持的method：{0}，请检查传入参数！ '.format(self.method))
        self.set_headers(headers)
        self.set_cookies(cookies)
        self.set_logger()
        # logger.debug("Header: {}".format(self.session.headers))
        # logger.debug("Cookies:{}".format(self.session.cookies))

    def set_headers(self, headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def set_logger(self):
        if not hasattr(self, 'logger'):
            self.logger = logger

    def send(self, params=None, data=None, json=None, files=None, **kwargs):
        """
        调用request方法的常见参数
        :param params: 紧跟在url后面，组合为<请求地址>, 格式为键值对（字典）
        :param data: <请求体>，字典、字节、文件格式参数
        :param json: <请求体>，json格式参数
        :param files: <请求体>，上传文件
        :param kwargs: 比较复杂的参数，如代理、认证等，一般不需要手动赋值
        :return: 返回<响应结果>
        """
        response = self.session.request(method=self.method, url=self.url,
                                        params=params, data=data, json=json,
                                        files=files, timeout=self.timeout, **kwargs)
        # 日志呈现
        self.logger.debug(self.session.cookies)
        self.logger.info('请求开始 {0} {1}'.format(self.method, response.url))
        self.logger.debug('请求头: {}'.format(self.session.headers))
        for body in (params, data, json):
            if body and isinstance(body, dict):
                self.logger.debug('请求内容: {}'.format(body))
        self.logger.info('响应结果: {}'.format(response))
        self.logger.debug('响应文本: {}'.format(u'{}'.format(response.text)))
        self.logger.debug('响应头:{}'.format(response.headers))

        # 报告呈现
        with allure.step("接口请求"):
            allure.attach(f"{self.method}\t{self.url}", "请求地址")
            allure.attach(str(self.session.headers), "请求头")
            for body in (params, data, json, files):
                allure.attach(str(body), "请求参数") if body else ''
            allure.attach(str(response.status_code), "响应码")
            allure.attach(str(response.text), "响应内容")
            allure.attach(str(response.headers), "响应头")
        return response

    def close(self):
        """关闭连接"""
        self.session.close()
        self.logger.info('请求结束\n')


#
# class TCPClient(object):
#     """用于测试TCP协议的socket请求，对于WebSocket，socket.io需要另外的封装"""
#     def __init__(self, domain, port, timeout=30, max_receive=102400):
#         self.domain = domain
#         self.port = port
#         self.connected = 0  # 连接后置为1
#         self.max_receive = max_receive
#         self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self._sock.settimeout(timeout)
#
#     def connect(self):
#         """连接指定IP、端口"""
#         if not self.connected:
#             try:
#                 self._sock.connect((self.domain, self.port))
#             except socket.error as e:
#                 logger.error(e)
#             else:
#                 self.connected = 1
#                 logger.debug('TCPClient connect to {0}:{1} success.'.format(self.domain, self.port))
#
#     def send(self, data, dtype='str', suffix=''):
#         """向服务器端发送send_string，并返回信息，若报错，则返回None"""
#         if dtype == 'json':
#             send_string = json_dumps(data) + suffix
#         else:
#             send_string = data + suffix
#         self.connect()
#         if self.connected:
#             try:
#                 self._sock.send(send_string.encode())
#                 logger.debug('TCPClient Send {0}'.format(send_string))
#             except socket.error as e:
#                 logger.exception(e)
#
#             try:
#                 rec = self._sock.recv(self.max_receive).decode()
#                 if suffix:
#                     rec = rec[:-len(suffix)]
#                 logger.debug('TCPClient received {0}'.format(rec))
#                 return rec
#             except socket.error as e:
#                 logger.exception(e)
#
#     def close(self):
#         """关闭连接"""
#         if self.connected:
#             self._sock.close()
#             logger.debug('TCPClient closed.')


if __name__ == '__main__':
    HTTPClient('http://www.baidu.com/').send()
