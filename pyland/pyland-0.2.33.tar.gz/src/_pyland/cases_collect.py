# coding=utf8
"""
generate cases mapping relationship
upstream param:
{
    "project_id": "",
    "project_path": ""
}
call case/many api param:
[
  {
    "primary_key": "anyitem or extra.xxxx",
    "author": "string",
    "name": "string",
    "category": "string",
    "priority": "string",
    "description": "string",
    "project_id": 0,
    "group_id": 0,
    "extra": {}
  }
]
"""
PROJECT_JSON = {
    "project_id": 35,
    "project_path": "DEMO"
}

import os
import sys
import shutil
from subprocess import Popen, PIPE
from .config import Config, BASE_PATH
from .log import Logger
from .extractor import extract
from _pyland.thirdparty import CaseManage
from .utils.error import MissingError

__all__ = [
    "UpdateCase",
    "list_case",
    "update_case"
]


PYTESTCONFIG = 'pytest.ini'
PYTESTCONFIG1 = 'pytest.ini.bak'


class UpdateCase(object):
    """批量更新用例到平台"""

    def __init__(self, project_json):
        """
        0 获取基础路径，准备执行环境
        """
        try:
            # 项目基本信息
            self.project_id = project_json.get("project_id")
            self.platform_url = project_json.get("host")
            project_path = project_json["project_path"]
            self.project_path = os.path.abspath(os.path.join(BASE_PATH, project_path))
            if os.path.exists(self.project_path):
                sys.path.extend([BASE_PATH, self.project_path])
                # os.chdir(self.project_path)")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"path not exists: {self.project_path} ")

        # 数据路径
        cfg = Config(path=self.project_path)
        self.data_path = cfg.DATA_PATH
        self.log_path = cfg.LOG_PATH
        self.logger = Logger(log_path=self.log_path)

    def get_case_base_info(self, project_path=None):
        """
        1. 获取用例映射关系等基本信息， 以nodeID为判断基准
        """
        project_path = project_path if project_path else self.project_path
        case_base_info = []
        self.logger.info(f"{os.getcwd()}")

        if os.path.exists(PYTESTCONFIG):
            shutil.copy(PYTESTCONFIG, PYTESTCONFIG1)

        with open(PYTESTCONFIG, "w") as f:
            f.write('[pytest]\ntestpaths =\n\t' + project_path)

        with Popen(['python', '-m', 'pytest',
                    '--collect-only',
                    '--tb=short',  # shorter traceback format
                    '--case-manage='+project_path,
                    ], stdout=PIPE, bufsize=1,
                   universal_newlines=True) as p:
            for line in p.stdout:
                print(line, end='')

        if os.path.exists(PYTESTCONFIG1) and os.path.exists(PYTESTCONFIG):
            shutil.move(PYTESTCONFIG1, PYTESTCONFIG)

        case_manage_yml = os.path.join(self.data_path, ".tmp_case_manage.yml")
        if os.path.exists(case_manage_yml):
            case_base_info = Config(case_manage_yml).get()
            os.remove(case_manage_yml)
        self.logger.debug(f"case_base_info: {case_base_info}")
        return case_base_info

    def get_case_info(self, case_base_info=None):
        """
        2. 补全case信息（根据case的三级模块，判断并创建三级分组;暂时不用）
        """
        # for case in case_base_info:
        #     epic = case["extra"].get("epic")
        #     feature = case["extra"].get("feature")
        #     story = case["extra"].get("story")
        #
        #     mum_id = 1
        #     for group in [epic, feature, story]:
        #         project_name =
        if not case_base_info:
            case_base_info = self.get_case_base_info()
        for case in case_base_info:
            case.update({"project_id": self.project_id})
        case_info = case_base_info
        self.logger.info(f"本次发现{len(case_info)}条测试用例")
        return case_info

    def update_case_to_platform(self, case_info, platform_url=''):
        """
        3 更新用例到平台
        """
        if not platform_url:
            platform_url = self.platform_url
        cm = CaseManage(platform_url)
        res = cm.import_case(cases=case_info)
        return res

    def get_case_node_list(self, project_path=None):
        """
        4 获取用例的nodeid列表, 仅供用例执行的查询
        """
        project_path = project_path if project_path else self.project_path

        case_base_info = self.get_case_base_info(project_path)
        case_node_list = []
        for case in case_base_info:
            nodeID = extract("extra.nodeID", case).strip().replace(": ", ":")
            case_node_list.append(nodeID)
        return case_node_list


def update_case(project_json=PROJECT_JSON):
    uc = UpdateCase(project_json)
    uc.logger.info(project_json)
    case_info = uc.get_case_info()
    res = uc.update_case_to_platform(case_info)
    return res


def list_case(project_json=PROJECT_JSON):
    uc = UpdateCase(project_json)
    uc.logger.info(project_json)
    case_info = uc.get_case_info()
    return case_info


if __name__ == "__main__":
    """传入PR_LIST_JSON = {project_path、project_id、group_id}就可以了"""
    # update_case(PROJECT_JSON)
    list_case(PROJECT_JSON)
