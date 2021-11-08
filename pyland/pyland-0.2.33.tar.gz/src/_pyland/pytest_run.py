# coding=utf8
import pytest
import os
import sys
from .utils.allure_opt import copy_history
from .log import logger


# *按需更改*
RUN_PARAM = {
    "collect": ['test_suits', '--collect-only'],
    "by_dir": ['test_suits'],
    "by_mod": ['test_suits/test_01_demo.py'],
    "by_class": ['test_suits/test_01_demo.py::TestDemo'],
    "by_func": ['test_suits/test_01_demo.py::TestDemo::test_demo_valid'],
    "by_search": ['-k', 'test_demo_valid'],
    "by_severity": ['--allure-severities', 'blocker'],
    "by_feature": ['--allure-features', 'Demo'],
    "by_story": ['--allure-stories', 'List Demo'],
}

# 不需更改
ALLURE_PARAM = [
    '-v',
    '--alluredir',
    'allure-result',
    "--clean-alluredir"
]


def run_by(run_param=None):
    # 切换工作空间
    BASE_PATH = os.path.abspath(sys.path[0])
    os.chdir(f'{BASE_PATH}')
    logger.info(f"current workspace: {BASE_PATH}")

    # *按需调用*
    if run_param and type(run_param) is list:
        pytest_param = run_param + ALLURE_PARAM
    else:
        logger.warning(f"not read valid run param, collect from current workspace {BASE_PATH}")
        pytest_param = ALLURE_PARAM

    # 执行测试用例
    pytest.main(pytest_param)

    # 复制历史结果，并生成报告
    # copy_history("report", "allure-result")
    os.system(f"allure generate allure-result -o report --clean")

    # 打开报告， 生成url
    os.system(f"allure open report")