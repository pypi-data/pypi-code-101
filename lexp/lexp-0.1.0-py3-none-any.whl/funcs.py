import math

import numpy


class Functions:
    custom_function = dict()

    @classmethod
    def is_defined(cls, name):
        """
        该函数名是否已预先定义
        :param name: 函数名称
        :return: bool
        """
        if not hasattr(cls, name):
            return False
        func = getattr(cls, name)
        return True if callable(func) else False

    @classmethod
    def get_defined(cls, name):
        func = getattr(cls, name, None)
        if not callable(func):
            raise Exception(f"{name} not callable")
        return func

    # 以下为lexp预先定义的函数

    @staticmethod
    def pow(x, a):
        return x ** a
        # return math.pow(x, a)

    @staticmethod
    def sin(x):
        return math.sin(x)

    @staticmethod
    def cos(x):
        return math.cos(x)

    @staticmethod
    def log(x, a):
        return math.log(x, a)

    @classmethod
    def avg(cls, *nums):
        n = len(nums)
        return cls.sum(*nums) / n

    @staticmethod
    def sum(*nums):
        total = 0
        for num in nums:
            total = total + float(num)
        return total

    @staticmethod
    def min(*vals):
        min_val = None
        for val in vals:
            val = float(val)
            if min_val is None or val < min_val:
                min_val = val
        return min_val

    @staticmethod
    def max(*vals):
        max_val = None
        for val in vals:
            val = float(val)
            if max_val is None or val > max_val:
                max_val = val
        return max_val

    @staticmethod
    def abs(val):
        return abs(val)

    @staticmethod
    def sqrt(val):
        return math.sqrt(val)

    @staticmethod
    def cbrt(val):
        return numpy.cbrt(val)

    @staticmethod
    def ifnull(val, default_val):
        """
        val为None时返回一个默认值
        :param val: 数值
        :param default_val: 默认值
        :return: 检查后的返回值
        """
        if val is None:
            return default_val
        return val

    @staticmethod
    def nullif(val, target_val):
        """
        如果val等于某个特定值，返回None
        :param val: 待检查的值
        :param target_val: 特定值
        :return: 结果
        """
        if val == target_val:
            return None
        return val

    @staticmethod
    def coalesce(*vals):
        """
        返回所有参数中第一个非空非零的值
        :param vals: 所有参数
        :return: float
        """
        for val in vals:
            if val is None:
                continue
            val = float(val)
            if val > 0:
                return val
        return vals[0]
