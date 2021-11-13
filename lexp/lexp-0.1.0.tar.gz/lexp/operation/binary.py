import math

from lexp.operation import Operation

# 二元运算符


class Plus(Operation):
    # 加法运算
    name = '+'
    argc = 2

    def operate(self, argv):
        super().check(argv)
        return float(argv[0]) + float(argv[1])


class Minus(Operation):
    # 减法运算
    name = '-'
    argc = 2

    def operate(self, argv):
        super().check(argv)
        return float(argv[0]) - float(argv[1])


class Multi(Operation):
    # 乘法运算
    name = '*'
    argc = 2

    def operate(self, argv):
        super().check(argv)
        return float(argv[0]) * float(argv[1])


class Divide(Operation):
    # 除法运算
    name = '/'
    argc = 2

    def operate(self, argv):
        super().check(argv)
        f1 = float(argv[1])
        if f1 == 0:
            return None
        return float(argv[0]) / float(argv[1])


class Power(Operation):
    # 幂运算
    name = '^'
    argc = 2

    def operate(self, argv):
        super().check(argv)
        return math.pow(float(argv[0]), float(argv[1]))
