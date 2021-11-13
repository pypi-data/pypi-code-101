from lexp.operation import Operation

# 一元运算符


class Not(Operation):
    # 非运算
    name = '!'
    argc = 1

    def operate(self, argv):
        super().check(argv)
        return 1 if float(argv[0]) == 0 else 0


class Negative(Operation):
    # 负号运算
    name = '-'
    argc = 1

    def operate(self, argv):
        super().check(argv)
        return 0 - float(argv[0])
