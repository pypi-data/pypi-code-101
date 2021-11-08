# coding=utf8
"""
接口封装成类，供测试用例调用
同时，提供配置和参数的文件路径为全局参数
"""
from _pyland.pre_request import PRequest
from _pyland.config import Config
from _pyland.utils.error import MissingError


# # 基础路径配置， 请勿更改
# BASE_PATH = path.dirname(path.abspath(__file__))
# DATA_PATH = path.join(BASE_PATH, 'data')
# CONFIG_PATH = path.join(BASE_PATH, 'config')
# CONFIG_FILE = path.join(CONFIG_PATH, "config.yml")
# CONFIGS = Config(CONFIG_FILE).get()
# # 若不需配置cookie，可以注释这两行
# COOKIE_FILE = path.join(DATA_PATH, "input_loads/cookies")
# COOKIES = Config(COOKIE_FILE).raw_get()
#
# # 参数路径配置，按需修改
# PARAM_DEMO_FILE = path.join(DATA_PATH, "input_loads/input_demo.yml")
# # URL和SQL信息配置，按需修改
# BASE_URL = CONFIGS["dl_admin_url_id_test"]
# SQL_SERVER = CONFIGS["discover_services_id_test"]


CASE_API_INFO = {
    'list_case': ['api/cases', 'GET'],
    'create_case': ['api/cases', 'POST'],
    'detail_case': ['api/cases/{id}', 'GET'],
    'update_case': ['api/cases/{id}', 'PUT'],
    'delete_case': ['api/cases/{id}', 'DELETE'],
    'import_case': ['api/cases/many', 'POST'],
}


class CaseManage(PRequest):
    """
    Demo APIs.
    """

    def __init__(self, host):
        self.host = host
        # can read platform host url from config file
        if not host:
            try:
                xx = Config()
                self.host = Config().get("platform_url")
                if not self.host: raise ValueError
            except:
                raise MissingError("missing required parameters for 'host'")

        super(CaseManage, self).__init__(base_url=self.host)

    def import_case(self, cases):
        res = self.send_request(*CASE_API_INFO["import_case"],  json=cases)
        return res.json()

    def list_case(self, cases):
        res = self.send_request(*CASE_API_INFO["list_case"], params=cases)
        return res.json()

    def create_case(self, cases):
        res = self.send_request(*CASE_API_INFO["create_case"], params=cases)
        return res.json()

    def detail_case(self, cases):
        res = self.send_request(*CASE_API_INFO["detail_case"], params=cases)
        return res.json()

    def update_case(self, cases):
        res = self.send_request(*CASE_API_INFO["update_case"], params=cases)
        return res.json()

    def delete_case(self, cases):
        res = self.send_request(*CASE_API_INFO["delete_case"], params=cases)
        return res.json()
