from abc import abstractmethod

from lexp.exception import CalcError


class Operation:
    # operations
    # 以下为定义的各种运算方法
    # 各类算数、逻辑运算符，以及自定义函数，都被定义为operation

    # 运算名称
    name = ''
    # 所需最少参数个数
    argc = 0

    def __init__(self):
        pass

    def check(self, argv):
        """
        在每个operation计算之前检查参数个数
        :param argv: 参数列表
        :return: None
        """
        if len(argv) < self.argc:
            raise CalcError('function %s: %d arguments need' % (self.name, self.argc), self, argv)

    @abstractmethod
    def operate(self, argv):
        """
        带入所需参数，使用该operation得到结果
        :param argv: 参数列表
        :return: value(float)
        """
        raise NotImplementedError
