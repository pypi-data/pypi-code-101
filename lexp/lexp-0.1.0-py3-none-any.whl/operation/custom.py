from lexp.exception import CalcError
from lexp.operation import Operation


class Bracket(Operation):
    # 括号
    def __init__(self):
        super().__init__()
        self.argc = 1

    def operate(self, argv):
        return float(argv[0])


class Variable(Operation):
    # 变量
    def __init__(self, variable):
        super().__init__()
        self.variable = variable

    def operate(self, val):
        return float(val)


class CustomOperation(Operation):
    # 自定义函数
    def __init__(self, name, func):
        super().__init__()
        self.name = name
        self.func = func
        if self.func:
            self.argc = func.__code__.co_argcount
        else:
            self.argc = None

    def operate(self, argv):
        if self.argc is not None:
            super().check(argv)
        if callable(self.func) is False:
            raise CalcError('%s not callable' % self.name)
        result = self.func(*argv)
        if isinstance(result, str):
            result = float(result)
        return result
