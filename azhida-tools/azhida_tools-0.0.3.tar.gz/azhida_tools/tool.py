# -*- coding: utf-8 -*-

import time
import logging
import inspect
import os


def datetime():
    # 时间日期格式 2000-01-01 00:00:00
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 返回 调用者的方法名
def get_function_name():
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    caller_name = calframe[1][3]
    # print('caller name:', caller_name)
    return caller_name
