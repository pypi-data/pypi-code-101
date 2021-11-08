import os.path
import re
import sys
from .log import logger


def dfs_showdir(path, depth=0):
    """ tree the path """
    if depth == 0:
        print(f"./{path}")

    for item in os.listdir(path):
        if '.git' not in item:
            print("| " * depth + "+--" + item)

            newitem = path + '/' + item
            if os.path.isdir(newitem):
                dfs_showdir(newitem, depth + 1)


def create_scaffold(project_name, simple=False, sub=False, topo=False):
    """ create scaffold with specified project name.
    """

    def show_tree(prj_name):
        try:
            print(f"\n$ tree {prj_name} -a")
            dfs_showdir(prj_name)
            print("")
        except Exception as e:
            logger.warning(e.__str__())

    def str2hump(text):
        arr = filter(None, text.lower().split('_'))
        res = ''
        for i in arr:
            res = res + i[0].upper() + i[1:]
        return res

    if not project_name or type(project_name) is not str:
        logger.error(f"Project name missing or not string type")
        return 1
    if not re.match("^[A-Za-z0-9_-]*$", project_name):
        logger.error(
            f"Project name format error: can only include [A-Z] or [a-z] or [0-9] or [_] "
        )
        return 1
    if os.path.isdir(project_name):
        logger.warning(
            f"Project folder {project_name} exists, please specify a new project name."
        )
        show_tree(project_name)
        return 1
    elif os.path.isfile(project_name):
        logger.warning(
            f"Project name {project_name} conflicts with existed file, please specify a new one."
        )
        return 1

    logger.info(f"Create new project: {project_name}")
    print(f"Project Root Dir: {os.path.join(os.getcwd(), project_name)}\n")

    def create_folder(path):
        os.makedirs(path)
        msg = f"created folder: {path}"
        print(msg)

    def create_file(path, file_content=""):
        with open(path, "w", encoding="utf-8") as f:
            f.write(file_content)
        msg = f"created file: {path}"
        print(msg)

    create_folder(project_name)
    create_folder(os.path.join(project_name, "common"))
    create_folder(os.path.join(project_name, "config"))
    create_folder(os.path.join(project_name, "data"))
    create_folder(os.path.join(project_name, "log"))
    create_folder(os.path.join(project_name, "report"))
    create_folder(os.path.join(project_name, "data/input_loads"))
    create_folder(os.path.join(project_name, "test_suits"))

    create_file(os.path.join(project_name, "common", "__init__.py"))
    create_file(os.path.join(project_name, "test_suits", "__init__.py"))
    create_file(os.path.join(project_name, "__init__.py"))

    demo_common_argv_content = """\"\"\"
Content of common/common_argv.py
Any function here can be directly called by yaml file in the data/input_loads
Example of yaml content:
url: ${url_http(127.0.0.1, 5000)}
\"\"\"
import re


def url_http(ip, port):
    return 'http://{}:{}'.format(ip, port)


def ip_port(http_url):
    ip, port = re.split('[/ :]', http_url.strip('http://'))
    return ip, port
"""

    demo_config_yml_content = f"""# Content of config/config.yml
# Required: API Base URL Config
test_{project_name}_url: 'https://{project_name}.com'

# Required: Log Config 
log:
  file_name: test.log
  backup: 5
  console_level: INFO
  file_level: INFO
  pattern: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Optional: SQL Server/DB Config
test_{project_name}_server: &test_{project_name}_server
  'sql_server': 127.0.0.1
  'sql_port': 3306
  'sql_user': root
  'sql_password':  123456

test_{project_name}_db1:
  <<: *test_{project_name}_server
  'db_name': 'db1'
"""

    demo_param_yml_content = """# Content of data/input_loads/parameterize.yml
# basic value (NOT start with `param_`,  just called in this yaml file, but ignored by pyland parameterize) 
name: &name
  valid:
    - '#test'
  invalid:
    - false
    - ${url_http(127.0.0.1, 5000)}  # dynamic data （func located in common.common_argv）

offset_limit: &offset_limit
  offset:
    valid: [0, 1, 1000, 0]
    invalid: [~, -1, true]  # ~ means None
  limit:
    valid: [10, 1000, 20]
    invalid: [~, 'x', true]  # 'x' means missing key

# Combination Params
param_0:  # Combination: combine all params to 2 lists, called with `param_0_valid` or `param_0_invalid`
    name:
        valid:
            - '#test'
        invalid:
            - false
            - ${url_http(127.0.0.1, 5000)}
    offset:
        valid: [0, 1, 1000, 0]
        invalid: [~, -1, true]
    limit:
        valid: [10, 1000, 20]
        invalid: [~, 'x', true]

param_0_duplicate:  # same with param_0
  name: *name
  <<: *offset_limit

# No Combination Params (means user combine and write params manually)
param_1: 'ONE VALUE'  # One Directly Constant, called with `param_1`

param_2:  # One Directly List: called with `param_2`
  - name: 'test1'
    offset: 0
    limit: 1
  - name: 'test2'
    offset: -1
    limit: 0

param_3:  # Two Directly Lists: called with `param_3_valid` AND `param_3_invalid` 
  valid:
    - name: 'test1'
      offset: 0
      limit: 1
  invalid:
    - name: 'test2'
      offset: -1
      limit: 0
    - name: 'test3'
      offset: 0
      limit: -1
"""

    demo_const_content = f"""\"\"\"
Content of const.py
Global Constants Definitions.
\"\"\"
import os
from pyland import (
    Config,
    Logger
)

__all__ = [
    'Const',
    'cfg',
    'logger',
    'ParamSets'
]


class Const:
    \"\"\"Global Constants\"\"\"

    # relative to the dir `config`
    DEFAULT_CONF_PATH: str = 'config.yml'

    # relative to the dir `data`
    DEFAULT_PARAM_PATH: str = 'input_loads/parameterize.yml'
    DEFAULT_COOKIE_PATH: str = 'input_loads/cookies'

    # key name of DEFAULT_CONF_PATH
    DEFAULT_URL: str = 'test_{project_name}_url'
    DEFAULT_LOG: str = 'log'
    DEFAULT_MYSQL: str = ''

    # email or name
    AUTHOR: str = ''


# global base path is based on this file
_file_path = os.path.dirname(os.path.abspath(__file__))

# cfg.config: config content
# cfg.DATA_PATH: locate `data` path
cfg = Config(path=_file_path, config=Const.DEFAULT_CONF_PATH)

# logger.info()
logger = Logger(config=cfg.config[Const.DEFAULT_LOG], log_path=cfg.LOG_PATH)


# cookie content
# cookies = Config(path=cfg.DATA_PATH, config=Const.DEFAULT_COOKIE_PATH).raw_get()

# mysql config, usage as following:
# > from pyland import Sql
# > Sql(mysql_server).query()
# mysql_server = cfg.config[Const.DEFAULT_MYSQL]


class ParamSets:
    \"\"\"params defined here\"\"\"
    param_0_valid: list
    param_0_invalid: list

"""

    demo_services_topo_content = f"""\"\"\"
Content of services.py
API Services Definitions.
\"\"\"
import szqa_framework
import allure
from .const import *
from pyland import PRequest


class {str2hump(project_name)}(szqa_framework.TopoHttp, PRequest):
    \"\"\"
    {str2hump(project_name)} APIs.
    \"\"\"

    def __init__(self):
        super().__init__()                              # required
        self.base_url = cfg.config[Const.DEFAULT_URL]   # required
        self.config = cfg.config                        # optional
        self.base_path = cfg.BASE_PATH                  # optional
        self.data_path = cfg.DATA_PATH                  # optional

    @allure.step('api - 0')  # optional: request step name
    def get_{project_name}(self, json, status='PASS'):
        api_url = ''  
        method = 'GET'  
        res = self.send_request(api_url, method, params=json, status=status)  # GET method: params
        return res 
"""

    demo_services_content = f"""\"\"\"
Content of services.py
API Services Definitions.
\"\"\"
import os
import allure
from .const import *
from pyland import (
    PRequest,
    extract
)


class {str2hump(project_name)}(PRequest):
    \"\"\"
    {str2hump(project_name)} APIs.
    \"\"\"

    def __init__(self):
        super().__init__()  # required
        self.base_url = cfg.config[Const.DEFAULT_URL]  # required
        self.logger = logger
        self.config = cfg.config
        self.base_path = cfg.BASE_PATH
        self.data_path = cfg.DATA_PATH

    @allure.step('api - 0')  # request step name
    def get_{project_name}(self, json, status='PASS'):
        api_url = ''  
        method = 'GET'  
        res = self.send_request(api_url, method, params=json, status=status)  # GET method: params
        return res 

    @allure.step('api - 1')
    def post_{project_name}(self, json, status='PASS'):
        api_url = ''  
        method = 'POST'
        res = self.send_request(api_url, method, json=json, status=status)  # POST method: json
        self.id = extract('result.id', res)  # extract from API 1, use in API 2
        return res  

    @allure.step('api - 2')
    def put_{project_name}(self, json, status='PASS'):
        api_url = ''
        method = 'PUT'
        if json.get('path') and isinstance(json['path'], str):
            json['path'] = os.path.join(self.data_path, json['path'])
        with open(json['path'], 'rb') as f:
            res = self.send_request(api_url, method, json=json, files={{'name': f}}, status=status)  # File Type Request
        return res

    @allure.step('api - 3')
    def delete_{project_name}(self, json, status='PASS'):
        api_url = f'{{self.id}}'  # extract from API 1, use in API 2
        method = 'DELETE'
        res = self.send_request(api_url, method, status=status)  
        return res
"""

    demo_conftest_01_content = f"""\"\"\"
Content of test_suits/conftest.py
pytest conftest, setup or teardown hooks
\"\"\"
import pytest
from ..services import logger
from ..services import {str2hump(project_name)}


@pytest.fixture(scope='function')
def env_api():
    logger.info('准备测试，执行前置接口')
    {project_name} = {str2hump(project_name)}()
    yield {project_name}
    logger.info('结束测试，执行后置接口')

"""

    demo_test_topo_01_content = f"""\"\"\"
Content of test_suits/test_01.py 
\"\"\"
import os
import szqa_framework
from pyland import extract
from pyland import com_params_obj
from ..services import {str2hump(project_name)}
from ..const import *

__author__ = Const.AUTHOR

# Transfer params to Object attributes
MyParam = ParamSets()
com_params_obj(path=cfg.DATA_PATH, yaml_files_list=Const.DEFAULT_PARAM_PATH, obj=MyParam)


class Test{str2hump(project_name)}1({str2hump(project_name)}):
    INPUT = {{'param1': MyParam.param_0_valid}}  # 声明当前case接受一个key为param1的传惨

    @szqa_framework.case_setting(paramesize=['param1'])
    def test_case(self):
        self.logger.info('Step1: demo step')
        self.logger.debug(f'This is the input [{{self.input[\"param1\"]}}]') 
        res = self.get_demo_api(self.input['param1'])
        if res is not None:
            self.result.add_result(self.result.PASS, item='step1', comment='demo test')  


class Test{str2hump(project_name)}2({str2hump(project_name)}):
    @szqa_framework.case_setting(input={{'param2': MyParam.param_0_invalid}}, paramesize=['param2'])
    def test_case(self):
        self.logger.info('Step1: demo step')
        self.logger.debug(f'This is the input [{{self.input}}]')  # input属性是外部传入的参数
        res = self.get_demo_api(self.input['param2'])
        assert res is not None


if __name__ == '__main__':
    import os

    szqa_framework.set_env_name('api_env')
    root_path = cfg.BASE_PATH
    case_path = os.path.join(root_path, 'test_suits/test_01.py')
    case_name_1 = 'TopoHttp-Test{str2hump(project_name)}1.test_case'
    case_name_2 = 'TopoHttp-Test{str2hump(project_name)}2.test_case'

    print(szqa_framework.get_case_tree(root_path))
    print(szqa_framework.run_one_case(case_path, case_name_1, root_path))
    print(szqa_framework.run_one_case(case_path, case_name_2, root_path))
    # case_executor = szqa_framework.Executor(case_path, case_name, root_path)
    # case_executor.run_case(case_name)
    # print(case_executor.get_case_result())
    # print(case_executor.get_case_output())


"""

    demo_test_01_content = f"""\"\"\"
Content of test_suits/test_01.py 
\"\"\"
import allure
import pytest
from pyland import extract
from pyland import com_params_obj
from ..services import {str2hump(project_name)}
from ..const import *

__author__ = Const.AUTHOR

# Transfer params to Object attributes
MyParam = ParamSets()
com_params_obj(path=cfg.DATA_PATH, yaml_files_list=Const.DEFAULT_PARAM_PATH, obj=MyParam)


@allure.epic('epic {str2hump(project_name)}')  
@allure.feature('feature {str2hump(project_name)} ') 
class Test{str2hump(project_name)}(object):
    \"\"\"test cases\"\"\"

    @allure.title('Get {str2hump(project_name)} Valid')   
    @allure.severity('normal')  
    @pytest.mark.parametrize("INPUT", MyParam.param_0_valid)
    def test_get_{project_name}_valid(self, INPUT):
        {project_name} = {str2hump(project_name)}()
        res = {project_name}.get_{project_name}(INPUT)
        success = extract('success', res)
        assert success

    @allure.title('Get {str2hump(project_name)} Invalid')  
    @pytest.mark.parametrize("INPUT", MyParam.param_0_invalid)
    def test_get_{project_name}_invalid(self, INPUT):
        {project_name} = {str2hump(project_name)}()
        res = {project_name}.get_{project_name}(INPUT)
        success = extract('success', res)
        assert not success
"""

    demo_simple_test_01_content = f"""\"\"\"
Content of simple test_suits/test_01.py 
\"\"\"


def test_get_{project_name}_valid():
    \"\"\"test cases content\"\"\"
    assert True

"""

    demo_run_py_content = f"""\"\"\"Content of run.py\"\"\"
from pyland import run_by

# *按需更改*
RUN_PARAM = {{
    "collect": ['test_suits', '--collect-only'],
    "by_dir": ['test_suits'],
    "by_mod": ['test_suits/test_01.py'],
    "by_class": ['test_suits/test_01.py::Test{str2hump(project_name)}'],
    "by_func": ['test_suits/test_01.py::Test{str2hump(project_name)}::test_get_{project_name}_valid'],
    "by_search": ['-k', 'test_get_{project_name}_valid'],
    "by_severity": ['--allure-severities', 'blocker'],
    "by_feature": ['--allure-features', 'feature {str2hump(project_name)}'],
    "by_story": ['--allure-stories', 'story {str2hump(project_name)}'],
}}

if __name__ == "__main__":
    # *按需调用*
    run_param = RUN_PARAM["by_dir"]
    # 执行用例
    run_by(run_param)
"""

    demo_main_py_content = """\"\"\"
Content of main.py
Entry point for third party to call. Afford 2 calling choices
\"\"\"

# \"\"\"
# choice 1
# same as executing command `pyland` at term, example following:
# ❯ python main.py
# usage: pyland [-h] [--version] [--no-color] {init,server,platform}
# pyland: error: the following arguments are required: command, args
# \"\"\"
#
# if __name__ == "__main__":
#     import pyland
#     sys.exit(pyland.main())


\"\"\"
choice 2
same as executing command `pyland platform` at term
❯ python main.py
usage: Process some integrated operations with Auto platform.
       [-h] (--import IMPORT | --list LIST | --run RUN)
Process some integrated operations with Auto platform.: error: one of the arguments --import --list --run is required
\"\"\"

if __name__ == '__main__':
    import pyland
    import sys

    sys.exit(pyland.main(['platform', *sys.argv[1:]]))

"""

    demo_conftest_py_content = """\"\"\"
[Important!!!  DO NOT TOUCH!!!]
\"\"\"
import os
from pyland import Config


pytest_plugins = 'pytester'


def pytest_addoption(parser):
    parser.addoption('--case-manage', required=False, help='analysis cases to manage by platform')


def pytest_generate_tests(metafunc):
    res = {}
    res['extra'] = {}
    res['extra']['params'] = {}

    for param in metafunc.fixturenames:
        if param.startswith('param'):
            if not param.endswith('valid'):
                param = param + '_valid'
            if hasattr(metafunc.module, 'combined'):
                param_pool = metafunc.module.combined[param]
                metafunc.parametrize(param, param_pool)
                # res['extra']['params'][param] = param_pool
            else:
                raise ValueError(f"param {param} set, but not found `combined`")

    project_path = metafunc.config.getoption('--case-manage')

    if project_path:
        for mark in metafunc.definition.iter_markers():
            if mark.name == 'allure_display_name':
                res['name'] = mark.args[0]
            elif mark.name == 'allure_label':
                label_type = mark.kwargs['label_type']
                label_value = mark.args[0]
                res['extra'][label_type] = label_value

        res['extra']['nodeID'] = metafunc.definition.nodeid
        res['extra']['path'] = metafunc.definition.location[0]
        res['extra']['module'] = metafunc.module.__name__
        if hasattr(metafunc.module, '__author__'):
            res['author'] = metafunc.module.__author__
        else:
            res['author'] = 'has no author yet'
        res['extra']['class'] = metafunc.cls.__name__ if metafunc.cls else None
        res['extra']['function'] = metafunc.function.__name__
        res['description'] = 'has no description yet' if not metafunc.function.__doc__ else metafunc.function.__doc__
        res['primary_key'] = 'extra.nodeID'
        res['category'] = 'pyland'
        res['priority'] = res['extra'].get('severity') if res['extra'].get('severity') else ''

        cfg = Config(path=project_path)
        case_manage_yml = os.path.join(cfg.DATA_PATH, '.tmp_case_manage.yml')
        cfg.update([res], case_manage_yml)

"""

    demo_input_project_content = """{
    "project_id": 0,
    "project_path": "",
    "host": ""
}
"""

    demo_input_case_content = f"""{{
    "project_path": "",
    "cases": [
        {{
            "case_id": 1,
            "extra": {{
                "class": "Test{str2hump(project_name)}",
                "feature": "{project_name} feature 01",
                "function": "test_get_{project_name}_valid",
                "module": "test_suits.test_01",
                "nodeID": "test_suits/test_01.py::Test{str2hump(project_name)}::test_get_{project_name}_valid",
                "params": {{}},
                "path": "test_suits/test_01.py",
                "severity": "blocker",
                "story": "{project_name} story 01"
            }}
        }}
    ],
    "project_name": "{project_name}",
    "category": "pyland",
    "output_path": "output.json",
    "runtime_args": {{
        "-n": "auto"
    }}
}}
"""

    create_file(os.path.join(project_name, "common", "common_argv.py"), demo_common_argv_content)
    create_file(os.path.join(project_name, "config", "config.yml"), demo_config_yml_content)
    create_file(os.path.join(project_name, "data/input_loads", "parameterize.yml"), demo_param_yml_content)
    create_file(os.path.join(project_name, "const.py"), demo_const_content)

    if not sub and not topo:
        create_file(os.path.join(project_name, "main.py"), demo_main_py_content)
        create_file(os.path.join(project_name, "conftest.py"), demo_conftest_py_content)

    if simple:
        create_file(os.path.join(project_name, "test_suits", "test_01.py"), demo_simple_test_01_content)
    else:
        create_file(os.path.join(project_name, "test_suits", "test_01.py"), demo_test_01_content)

    if topo:
        create_file(os.path.join(project_name, "services.py"), demo_services_topo_content)
        create_file(os.path.join(project_name, "test_suits", "test_01.py"), demo_test_topo_01_content)
    else:
        create_file(os.path.join(project_name, "services.py"), demo_services_content)
        create_file(os.path.join(project_name, "test_suits", "conftest.py"), demo_conftest_01_content)
        create_file(os.path.join(project_name, "run.py"), demo_run_py_content)
        create_file(os.path.join(project_name, "data/input_loads", "input_project.json"), demo_input_project_content)
        create_file(os.path.join(project_name, "data/input_loads", "input_case.json"), demo_input_case_content)

    show_tree(project_name)
    return 0


def main_scaffold(project, simple, sub, topo):
    sys.exit(create_scaffold(project, simple, sub, topo))
