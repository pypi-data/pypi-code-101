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


PROJECT_API_INFO = {
    'list_project': ['api/projects', 'GET'],
    'create_project': ['api/projects', 'POST'],
    'detail_project': ['api/projects/{id}', 'GET'],
    'update_project': ['api/projects/{id}', 'PUT'],
    'delete_project': ['api/projects/{id}', 'DELETE']
}


class ProjectManage(PRequest):
    """
    Demo APIs.
    """

    def __init__(self):
        BASE_URL = Config().get("platform_url")
        super(ProjectManage, self).__init__(base_url=BASE_URL)

    def list_project(self, projects):
        res = self.send_request(*PROJECT_API_INFO["list_project"],  params=projects)
        return res

    def create_project(self, projects):
        res = self.send_request(*PROJECT_API_INFO["create_project"],  params=projects)
        return res

    def detail_project(self, projects):
        res = self.send_request(*PROJECT_API_INFO["detail_project"],  params=projects)
        return res

    def update_project(self, projects):
        res = self.send_request(*PROJECT_API_INFO["update_project"],  params=projects)
        return res

    def delete_project(self, projects):
        res = self.send_request(*PROJECT_API_INFO["delete_project"],  params=projects)
        return res
