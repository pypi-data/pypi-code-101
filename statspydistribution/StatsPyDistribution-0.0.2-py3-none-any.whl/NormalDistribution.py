
from src.Distributions import Distributions
import math
from matplotlib import pyplot as plt


class NormalDistribution(Distributions):

    def frequency_density_formula(self):
        return "\u0192(x)=e^(-((x-μ)/σ)\u00B2/2)/(\u03C3\u221A(2\u03C0))"

    def name(self):
        return "Normal Distribution"

    def notation(self):
        return '\u039D(\u03BC,\u03C3\u00B2)'

    def parameters(self):
        return "mean can be any real number and variance can be any positive real number"

    def __init__(self, mean, var, size=None):
        """
        :param mean:
        :float mean:
        :param var:
        :float var:
        :param size:
        :int size:
        """
        if isinstance(var, str):
            raise Exception("var must be non string type")

        if isinstance(mean, str):
            raise Exception("mean must be non string type")
        if size is None:
            size = 10
        if var <= 0 or var is None:
            raise Exception('A variance(' + var + ') cannot be negative or zero')
        if not isinstance(size, int):
            raise Exception('Size must be int type')
        if size < 2:
            raise Exception('Size (' + size + ') is not valid. it must be more than one')

        self.__mn = mean
        self.__var = var
        self.__size = size
        self.__x = [float(i / 10) for i in range(10 * (0 - int(size / 2)), 10 * (1 + int(size / 2)))]
        self.__y = [self.__fx(self.__mn, var, i) for i in self.__x]
        self.__mgf = [self.__mgfunction(self.__mn, var, i) for i in self.__x]
        self.__skw = 0
        self.__krt = 0
        self.__mod = mean
        self.__med = mean

        Distributions.__init__(self, x=self.__x, y=self.__y, m=self.__mn, v=self.__var, mo=self.__mod, me=self.__med,
                               sk=self.__skw, kr=self.__krt,mgf=self.__mgf)

    def __str__(self):
        d = {'mean': self.__mn, 'var': self.__var, 'size': self.__size}
        n = self.name() + str(d)
        return n

    def __fx(self, u, o, i):
        return math.exp(-1 * math.pow(i - u, 2) / (2 * math.pow(o, 2))) / (o * math.sqrt(2 * math.pi))

    def __mgfunction(self, u, o, i):
        return math.exp(u*i - math.pow(o, 2)*math.pow(i, 2)/2)

    def get_data(self):
        return {'x': self.__x, 'y': self.__y}

    def plot(self, y=None):
        if y is None:
            y = self.__y
        plt.scatter(self.__x, y)
        plt.plot(self.__x, y)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title(self.__str__())
        plt.show()
