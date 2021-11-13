# -*- coding: utf-8 -*-
import typing
from copy import deepcopy

from lexp.exception import CalcError
from lexp.expnode import _Node
from lexp.funcs import Functions


class Lexp:
    """
    实例化后可解析表达式，进行计算，如
    exp = Lexp()
    exp.load('expression string')
    result = exp.calc({'x': x value, 'y': y value})
    """
    def __init__(self, string=None):
        self.string = None
        self._expression = None
        if isinstance(string, str):
            self.load(string)

    def load(self, string):
        """
        解析表达式
        :param string: 表达式字符串
        :return: 成功与否
        """
        if not string:
            self._expression = None
            return False
        self.string = string
        self._expression = _Node(string)
        self._expression.parse()
        # self._print_expresstion(self._expression)
        return False if self._expression is None else True

    def calc(self, callback=None, params=None, **kwargs):
        """
        用已经解析的表达式，带入变量值或可获得值的函数，得到计算结果
        :param callback: callable, 带入变量名，返回变量值
        :param params: dict, 带入变量名，获得变量值
        :param kwargs: 变量值
        :return: float, 计算结果
        """
        if self._expression is None:
            raise CalcError("no expression be loaded")

        if callback is not None:
            return self._expression.get_value(callback)

        if params is None:
            p = dict()
        else:
            p = deepcopy(params)
        p.update(kwargs)
        return self._expression.get_value(p)

    def get_functions(self, only_undefined=False):
        """
        获得当前表达式所调用的函数
        :return: list
        """
        if self._expression is None:
            # raise CalcError("no expression be loaded")
            return list()
        functions = self._expression.get_functions()
        if only_undefined:
            functions = list(filter(lambda x: x.get("type") == "undefined", functions))
        return functions

    def get_variable_list(self):
        """
        获得当前表达式中出现的所有变量
        :return: list
        """
        if self._expression is None:
            # raise CalcError("no expression be loaded")
            return list()
        return self._expression.getVariables()

    def is_available(self):
        """
        当前是否已成功读取表达式，可进行计算
        :return: True/False
        """
        if self._expression is None:
            return False
        return True

    def __str__(self):
        return "" if self.string is None else self.string

    @classmethod
    def register(cls, name, func):
        """
        添加自定义函数，为静态方法
        :param name: 表达式中的函数名
        :param func: 函数
        :return: None
        """
        if callable(func) is False:
            raise Exception(f"{name} not callable")
        Functions.custom_function[name] = func

    # @classmethod
    # def _print_expresstion(cls, node, deep=0):
    #     """
    #     print解析后的层级关系，调试使用
    #     :param node: 需print的节点
    #     :param deep: 当前node的缩进数
    #     :return: None
    #     """
    #     if node is None:
    #         return
    #     d = deep + 1
    #     s = ''
    #     for i in range(0, deep):
    #         s = s + '\t'
    #     if node.value is not None:
    #         v = node.value
    #     else:
    #         t = str(type(node.operation))
    #         find = 'Lexp.Node.'
    #         p0 = t.find(find)
    #         if p0 != -1:
    #             t = t[p0 + len(find):-2]
    #         v = "%s %s" % (node.string, t)
    #     s = s + v
    #     print(s)
    #     for i in range(0, len(node.children)):
    #         cls._print_expresstion(node.children[i], d)
