# coding=utf8
from pyland import run_by

# *按需更改*
RUN_PARAM = {
    "collect": ['test_suits', '--collect-only'],
    "by_dir": ['test_suits'],
    "by_mod": ['test_suits/test_01.py'],
    "by_class": ['test_suits/test_01.py::TestDemo'],
    "by_func": ['test_suits/test_01.py::TestDemo::test_demo_valid'],
    "by_search": ['-k', 'test_demo_valid'],
    "by_severity": ['--allure-severities', 'blocker'],
    "by_feature": ['--allure-features', 'Demo'],
    "by_story": ['--allure-stories', 'List Demo'],
}

if __name__ == "__main__":
    # *按需调用*
    run_param = RUN_PARAM["by_dir"]
    # 执行用例
    run_by(run_param)
