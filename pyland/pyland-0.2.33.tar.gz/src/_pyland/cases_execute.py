# coding=utf8
"""
execute cases and extract results
input:
{
    # "env": {},
    "project_name": "DEMO",
    "project_path": "DEMO",
    "output_path": "",
    "cases": [{
        "case_id": 1,
        # "case_name": "",
        # "case_category": "",
        # "project_name": "",
        # "output_path": "",
        "extra": {}
    }]
}
output:
{
    "report_file": "",
    "log_file": "",
    "cases": [
        {
            "case_id": None,
            "case_status": "string",
            "variables": {
                "in_puts": {},  # 数据输入
                "out_puts": {}  # 数据输出（供后面用例使用）
            },
            "attachment": {
                "log_file": "string",  # 详细执行过程文件路径
                "html_file": "string"  # html报告文件路径
            },
            "steps": [{
                "name": "string",  # 测试步骤名字
                "status": "string",  # 测试步骤状态（pass/fail/error）
                "request": {},  # 请求
                "response": {},  # 响应
                "validators": [{  # 校验项
                    "comparator": "equal",
                    "check": "status_code",
                    "check_value": None,
                    "expect_value": None,
                    "message": None,
                    "check_result": None
                }],
                "erroes": "error msg"
            }]
        }
    ]
}
"""
CASE_LIST_JSON = {
    "env": {},
    "project_name": "DEMO",
    "project_path": "DEMO",
    "output_path": "/Users/jiukunzhang/PycharmProjects/dl_cms/tmp/output.json",
    "cases": [
        {
            "case_id": 1,
            "case_name": "ListDemoInValid",
            "case_category": "PY",
            "project_name": "DEMO",
            "output_path": "/Users/jiukunzhang/PycharmProjects/dl_cms/tmp/1",
            "extra": {
                'class': "TestDemo",
                'function': 'test_demo_invalid',
                'module': 'tests.DEMO.test_suits.test_01_demo',
                'nodeID': 'DEMO/test_suits/test_01_demo.py: : TestDemo: : test_demo_invalid',
                'path': 'DEMO/test_suits/test_01_demo.py',
                'severity': 'blocker',
                'story': 'ListDemo'
            }
        },
        {
            "case_id": 2,
            "case_name": "ListDemoValid",
            "case_category": "PY",
            "project_name": "DEMO",
            "output_path": "/Users/jiukunzhang/PycharmProjects/dl_cms/tmp/1",
            "extra": {
                'class': "TestDemo",
                'function': 'test_demo_valid',
                'module': 'tests.DEMO.test_suits.test_01_demo',
                'nodeID': 'DEMO/test_suits/test_01_demo.py: : TestDemo: : test_demo_valid1',
                'path': 'DEMO/test_suits/test_01_demo.py',
                'severity': 'blocker',
                'story': 'ListDemo'
            }
        }]
}

CASE_RESULTS_JSON = {
    "report_file": "",
    "log_file": "",
    "cases": [
        {
            "case_id": None,
            "case_status": "passed",
            "variables": {
                "in_puts": {},  # 数据输入
                "out_puts": {}  # 数据输出（供后面用例使用）
            },
            "attachment": {
                "log_file": "",  # 详细执行过程文件路径
                "html_file": ""  # html报告文件路径
            },
            "steps": [{
                "name": "step 1",  # 测试步骤名字
                "status": "passed",  # 测试步骤状态（pass/fail/error）
                "request": {},  # 请求
                "response": {},  # 响应
                "validators": [{  # 校验项
                    "comparator": "equal",
                    "check": "status_code",
                    "check_value": None,
                    "expect_value": None,
                    "message": None,
                    "check_result": None
                }],
                "erroes": "error msg"
            }]
        }
    ]
}

import os
import sys
import re
from subprocess import Popen, PIPE
from copy import deepcopy
import shutil
from .config import Config, BASE_PATH
from .log import Logger
from .extractor import extract
from .cases_collect import UpdateCase
from .utils.allure_opt import copy_history
from .utils.support import rec_merge
from .utils.error import MissingError

__all__ = [
    "ExecTests",
    "run_case"
]


class ExecTests(object):
    """批量执行测试用例，生成指定格式json，保存在指定位置"""

    def __init__(self, case_list_json):
        """
        0 获取基础路径，准备执行环境
        """
        try:
            # 项目基本信息
            project_path = extract("project_path", case_list_json)
            self.output_path = extract("output_path", case_list_json)
            self.project_path = os.path.abspath(os.path.join(BASE_PATH, project_path))
            self.runtime_args = extract("runtime_args", case_list_json)
            if os.path.exists(self.project_path):
                sys.path.extend([BASE_PATH, self.project_path])
                # os.chdir(self.project_path)
            else:
                raise FileNotFoundError(f"path not exists: {self.project_path} ")
        except KeyError:
            raise MissingError("missing required parameters for 'project_path'")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"path not exists: {self.project_path} ")

        # 数据路径
        cfg = Config(path=self.project_path)
        self.data_path = cfg.DATA_PATH
        self.log_path = cfg.LOG_PATH
        self.report_path = cfg.REPORT_PATH
        self.result_path = cfg.RESULT_PATH

        self.log_config = cfg.config.get('log') if cfg.config else None
        self.logger = Logger(log_path=self.log_path, config=self.log_config)

    def get_case_nodes(self, case_list_json):
        """
        1 提取nodeID信息，供批量执行
        return:
        {
            "DEMO/test_suits/test_01_demo.py::TestDemo::test_demo_valid":
                {"case_id": 123}
        }
        """
        case_nodes = {}
        case_list = extract("cases", case_list_json)

        # real_node_list = UpdateCase(case_list_json).get_case_node_list()
        # self.logger.debug(f"real_node_list: {real_node_list} \n\n")
        # for case in case_list:
        #     case_id = extract("case_id", case)
        #     nodeID = extract("extra.nodeID", case).strip().replace(": ", ":")
        #     if nodeID in real_node_list:
        #         case_nodes.update({nodeID: {"case_id": case_id}})
        #     else:
        #         case_nodes.update({nodeID: {"case_id": case_id, "case_status": "NotFound"}})
        #
        # self.logger.info(f"case_nodes_id: {case_nodes} \n\n")
        # return case_nodes

        for case in case_list:
            case_id = extract("case_id", case)
            nodeID = extract("extra.nodeID", case).strip().replace(": ", ":")
            case_nodes.update({nodeID: {"case_id": case_id}})

        self.logger.info(f"case_nodes_id: {case_nodes} \n\n")
        return case_nodes

    def run_test(self, case_nodes):
        """2 运行测试用例"""
        try:
            # 1. backup pytets.ini
            if os.path.exists("pytest.ini"):
                shutil.copy("pytest.ini", "pytest.ini.bak")
            # 2. update pytest.ini by case_nodes
            self._pytest_config(case_nodes)
            # 3. execute testcases by pytets.ini
            self._run_pytest_cases()
        except Exception as e:
            self.logger.error(e)
        finally:
            # 4. recovery pytest.ini
            if os.path.exists("pytest.ini.bak") and os.path.exists("pytest.ini"):
                shutil.move("pytest.ini.bak", "pytest.ini")

        # 5. get execution results
        case_results = self._get_case_results(case_nodes)
        # rec_merge(case_results, case_nodes)

        # 6. generate reports history
        # self._history_allure_report()

        return case_results

    def _pytest_config(self, case_nodes):
        """2.1 把nodeid写到pytest.ini，批量执行(*跳过NotFound的用例*）"""
        # os.chdir(self.project_path)
        with open("pytest.ini", "w") as f:
            f.write('[pytest]\ntestpaths =\n')
            for node, node_info in case_nodes.items():
                # node = re.sub(r'.*/test_suits/', 'test_suits/', node)
                # if node_info.get("case_status") != 'NotFound':
                f.write("\n\t" + node)

    def _run_pytest_cases(self):
        """2.2 批量执行测试用例, 生成allure报告"""
        PYTEST_PARAM = ['python', '-m', 'pytest']
        ALLURE_PARAM = ['--alluredir', self.result_path, "--clean-alluredir"]

        if self.runtime_args and isinstance(self.runtime_args, dict):
            for k, v in self.runtime_args.items():
                PYTEST_PARAM.extend([k, v])
        else:
            PYTEST_PARAM.extend(['--tb=short', '-n', 'auto'])

        RUNCMD = PYTEST_PARAM + ALLURE_PARAM
        self.logger.info(RUNCMD)

        result_bak_path = self.result_path + '.bak'
        if os.path.exists(result_bak_path):
            shutil.rmtree(result_bak_path)

        if os.path.exists(self.result_path):
            shutil.move(self.result_path, result_bak_path)

        if not os.path.exists(self.report_path):
            os.makedirs(self.report_path)

        with Popen(RUNCMD,
                   stdout=PIPE,
                   bufsize=1,
                   universal_newlines=True,
                   stderr=PIPE
                   ) as p:
            for line in p.stderr:
                print(line)

        os.system(f"allure generate {self.result_path} -o {self.report_path} --clean")

        if os.path.exists(self.result_path):
            shutil.rmtree(self.result_path)

        if os.path.exists(result_bak_path):
            shutil.move(result_bak_path, self.result_path)

    def _get_case_results(self, case_nodes):
        """
        2.3 获取用例执行结果
        return:
        {
            "DEMO/test_suits/test_01_demo.py::TestDemo::test_demo_valid":
                {
                    "case_status": 'passed',
                    "steps": [
                        {"name": "", "case_status": "passed"},
                        ]
                }
        }
        """
        REPORT_CASE_PATH = os.path.join(self.report_path, "data/test-cases")

        if not os.path.exists(REPORT_CASE_PATH):
            return f"Error: test case excuted block, no report file generated"

        case_result = {}
        case_result_simple = {}

        for c in os.listdir(REPORT_CASE_PATH):
            res = Config(os.path.join(REPORT_CASE_PATH, c)).json_get()
            name = extract("name", res)
            case_path = res["fullName"]
            # self.logger.debug(f"{case_path}\n\n")
            nodeID = self._convert_allure_to_pytest_nodeid(case_path)

            if not nodeID:
                continue
            if case_nodes.get(nodeID):
                _node = case_nodes.get(nodeID)
                case_id = extract("case_id", _node)
            case_status = extract("testStage.status", res)

            step_result = deepcopy(extract("cases[0].steps[0]", CASE_RESULTS_JSON))
            step_result.update({"name": name, "status": case_status})

            if not case_result.get(nodeID):
                node_result = deepcopy(extract("cases[0]", CASE_RESULTS_JSON))
                node_result.update({"case_status": case_status, "case_id": case_id, "steps": [step_result]})
                case_result[nodeID] = node_result
            else:
                case_result[nodeID]['steps'].append(step_result)
                if case_status != 'passed': case_result[nodeID]['case_status'] = 'failed'

        for node in case_result:
            self._translate_status(case_result[node])
        # self.logger.debug(f"case_nodes_status: {case_result} \n\n")

        for key, value in case_result.items():
            node = {}
            node['steps'] = []
            node['case_id'] = value.get('case_id')
            node['case_status'] = value.get('case_status')
            for i in value.get('steps'):
                if type(i) is dict:
                    node['steps'].append(i.get('status'))
            case_result_simple[key] = node

        self.logger.info(f"case status: {case_result_simple} \n\n")
        return case_result

    def _translate_status(self, case):
        """
        change status passed to pass, failed to fail
        case:
        {
            "DEMO/test_suits/test_01_demo.py::TestDemo::test_demo_valid":
                {
                    "case_status": 'passed',
                    "steps": [
                        {"name": "", "status": "passed"},
                        ]
                }
        }
        """
        if case['case_status'] == 'passed':
            case['case_status'] = 'pass'
        elif case['case_status'] == 'failed':
            case['case_status'] = 'fail'
        else:
            pass
        if 'steps' in case.keys():
            for step in case['steps']:
                if step['status'] == 'passed':
                    step['status'] = 'pass'
                elif step['status'] == 'failed':
                    step['status'] = 'fail'
                else:
                    pass

    def _convert_allure_to_pytest_nodeid(self, case_path):
        """ 2.3.1
        case_path: 'DEMO.test_suits.test_01_demo.TestDemo#test_demo_valid'
        to
        case_nodeid: 'DEMO/test_suits/test_01_demo.py::TestDemo::test_demo_valid'
        """
        _info = case_path.split("#")
        if len(_info) != 2:
            self.logger.error("can not parse case node")
            return None

        _module, func = _info
        _path = _module.split(".")

        if _path[-1].startswith("Test"):
            cls = _path[-1]
            module = _path[-2]
            path = _path[:-2]
            case_nodeid = '/'.join(path) + '/' + module + '.py' + "::" + cls + "::" + func
        else:
            case_nodeid = _module.replace('.', '/') + '.py' + "::" + func
        # self.logger.debug(f"case_nodeid: {case_nodeid}")
        return case_nodeid

    # def _history_allure_report(self):
    #     copy_history(self.report_path, self.result_path)
    #     os.system(f"allure generate {self.result_path} -o {self.report_path} --clean")

    def export_json(self, case_result, log_file_name):
        """
        3. 返回指定格式json输出到指定路径
        """
        output_json = deepcopy(CASE_RESULTS_JSON)

        output_json["report_file"] = self.report_path
        output_json["log_file"] = log_file_name
        output_json["cases"] = list(case_result.values())

        # self.logger.debug(f"output_json: {output_json}")
        Config(self.output_path).json_put(output_json)
        return output_json

    def backup_log(self):
        self.logger.info("备份日志")
        log_file_name = self.logger.log_file_name
        log_file_name_bak = f"{self.logger.log_file_name}.bak"
        os.system(
            f"touch {log_file_name} {log_file_name_bak}; "
            f"cat {log_file_name} >> {log_file_name_bak}; "
            f"cat /dev/null > {log_file_name}"
        )
        return log_file_name


def run_case(case_list_json=CASE_LIST_JSON):
    et = ExecTests(case_list_json)
    log_file_name = et.backup_log()
    case_nodes = et.get_case_nodes(case_list_json)
    case_results = et.run_test(case_nodes)
    res = et.export_json(case_results, log_file_name)
    return res


if __name__ == "__main__":
    """只需要读取一个输入参数，定义名称为 CASE_LIST_JSON，就可以了"""
    run_case(CASE_LIST_JSON)
