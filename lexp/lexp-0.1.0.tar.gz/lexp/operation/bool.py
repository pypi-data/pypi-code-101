from lexp.operation import Operation

# 二元运算符，只返回1/0


class Bool(Operation):
    argc = 2

    def __init__(self, func):
        # func为成立条件，返回True/False
        super().__init__()
        self.func = func

    def operate(self, argv):
        super().check(argv)
        val0 = None if argv[0] is None else float(argv[0])
        val1 = None if argv[1] is None else float(argv[1])
        return 1 if self.func(val0, val1) else 0


class And(Bool):
    name = '&&'

    def __init__(self):
        super().__init__(lambda x, y: x != 0 and y != 0)


class Or(Bool):
    name = '||'

    def __init__(self):
        super().__init__(lambda x, y: x != 0 or y != 0)


class Eq(Bool):
    name = '=='

    def __init__(self):
        super().__init__(lambda x, y: x == y)


class Neq(Bool):
    name = '!='

    def __init__(self):
        super().__init__(lambda x, y: x != y)


class Gt(Bool):
    name = '>'

    def __init__(self):
        super().__init__(lambda x, y: x > y)


class Lt(Bool):
    name = '<'

    def __init__(self):
        super().__init__(lambda x, y: x < y)


class Ge(Bool):
    name = '>='

    def __init__(self):
        super().__init__(lambda x, y: x >= y)


class Le(Bool):
    name = '<='

    def __init__(self):
        super().__init__(lambda x, y: x <= y)
