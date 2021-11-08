# coding=utf8
"""
接口封装成类，供测试用例调用
同时，提供配置和参数的文件路径为全局参数
"""
from _pyland.pre_request import PRequest
from _pyland.config import Config

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


RESULT_API_INFO = {
    'list_result': ['api/results', 'GET'],
    'create_result': ['api/results', 'POST'],
    'detail_result': ['api/results/{id}', 'GET'],
    'update_result': ['api/results/{id}', 'PUT'],
    'delete_result': ['api/results/{id}', 'DELETE']
}


class ResultManage(PRequest):
    """
    Demo APIs.
    """

    def __init__(self):
        BASE_URL = Config().get("platform_url")
        super(ResultManage, self).__init__(base_url=BASE_URL)

    def list_result(self, results):
        res = self.send_request(*RESULT_API_INFO["list_result"],  params=results)
        return res

    def create_result(self, results):
        res = self.send_request(*RESULT_API_INFO["create_result"],  json=results)
        return res

    def detail_result(self, results):
        res = self.send_request(*RESULT_API_INFO["detail_result"],  json=results)
        return res

    def update_result(self, results):
        res = self.send_request(*RESULT_API_INFO["update_result"],  json=results)
        return res

    def delete_result(self, results):
        res = self.send_request(*RESULT_API_INFO["delete_result"],  json=results)
        return res