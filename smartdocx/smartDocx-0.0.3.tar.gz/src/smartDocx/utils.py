"""
@File  : utils.py
@IDE   : PyCharm
@Author: Sanbom
@Date  : 2021/7/14
@Desc  : 
"""

# -*- coding: utf-8 -*-
import functools
import inspect
import time
from typing import Any

from smartDocx import SmartReportBase


def get_function_name():
    """获取正在运行函数(或方法)名称"""
    return inspect.stack()[1][3]


def put_paragraph_data(message):
    """将段落数据归类"""

    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            """嵌套函数"""
            frame = inspect.currentframe().f_back
            # 获取被装饰方法的实例对象
            self_obj = frame.f_locals['self']  # SmartReportDataBase类型
            # 获取被装饰方法的函数名称
            function_name = func.__name__
            # 返回章节数据
            chapter_data = func(*args, **kwargs)
            # 获取章节层级
            chapter_level = self_obj.get_chapter_level(function_name)
            # 绑定该章节层级数据
            self_obj._data[chapter_level] = chapter_data

        return inner

    if callable(message):
        func = message
        return decorator(func)
    else:
        return decorator


def handle_paragraph(message):
    """处理段落"""

    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            """嵌套函数"""
            frame = inspect.currentframe().f_back
            # 1.获取被装饰方法的实例对象
            self_obj = frame.f_locals['self']  # type:SmartReportBase
            # 2.获取被装饰方法的函数名称
            function_name = func.__name__
            # 3.执行函数前操作
            pass
            # 4.执行章节处理函数
            func(*args, **kwargs)
            # 5.函数执行后执行
            time.sleep(0.1)
            # 6.处理段落
            self_obj._handle_paragraphs(chapter=function_name)

        return inner

    if callable(message):
        func = message
        return decorator(func)
    else:
        return decorator


def config_dict_to_obj(data: dict):
    """字典转对象属性"""

    def handle_dict(obj: object, dict_data: dict):
        """处理字典数据"""
        for k, v in dict_data.items():
            obj_ = get_obj(v)
            setattr(obj, k, obj_)

    def get_obj(value: Any):
        """设置属性"""
        if isinstance(value, dict):
            obj_ = type('', (object,), dict())
            for k, v in value.items():
                setattr(obj_, k, get_obj(v))
            return obj_
        else:
            return value

    config_obj = type('', (object,), dict())
    try:
        handle_dict(obj=config_obj, dict_data=data)
    except Exception as e:
        pass
    finally:
        return config_obj


def print_func_params(output: bool = False):
    """打印函数的参数"""

    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            """嵌套函数"""
            # 获取被装饰方法的函数名称
            function_name = func.__name__
            if output:
                print("=" * 10 + "  output_func_params  " + "=" * 10)
                print("func_name: {}".format(function_name))
                print("args: {}".format(args))
                print("kwargs: {}".format(kwargs))
                print("=" * 10 + "  output_func_params  " + "=" * 10)
            # 执行
            func(*args, **kwargs)

        return inner

    if callable(output):
        func = output
        return decorator(func)
    else:
        return decorator
