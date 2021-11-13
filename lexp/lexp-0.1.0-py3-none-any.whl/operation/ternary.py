from lexp.operation import Operation

# 三元运算符


class EitherOr(Operation):
    # a ? b : c
    name = '?:'
    argc = 3

    def operate(self, argv):
        super().check(argv)
        if float(argv[0]) == 0:
            return float(argv[2])
        else:
            return float(argv[1])
