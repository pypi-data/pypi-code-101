# -*- coding: utf-8 -*-
# @Time : 2021/11/16 4:29 下午
# @Author : Kane.Yan
# @File : main.py

from typing import List

# hook函数，在用例收集完毕之后会被调用
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    """
    1、用例收集完毕后，遍历用例对象，修改name、nodeid编码格式
    2、将python的默认编码格式unicode装换为utf-8，再装换为unicode_escape
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode_escape")