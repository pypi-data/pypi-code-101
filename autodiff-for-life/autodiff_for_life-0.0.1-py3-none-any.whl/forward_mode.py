import numpy as np

class Dual:
    """Basic dual number class"""

    __numpy_ufunc__ = None # Numpy up to 13.0
    __array_ufunc__ = None # Numpy 13.0 and above

    def __init__(self, value, grad=None):
        self.value = value
        if grad is None:
            self.grad = np.ones_like(self.value)
        else:
            self.grad = grad

    def __eq__(self, other):
        try:
            return (self.value == other.value) and (self.grad == other.grad)
        except AttributeError:
            return False

    def __neg__(self):
        return Dual(-self.value, -self.grad)

    def __pos__(self):
        return Dual(self.value, self.grad)

    def __add__(self, other):
        try:
            return Dual(self.value + other.value, self.grad + other.grad)
        except AttributeError:
            return Dual(self.value + other, self.grad)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        try:
            return Dual(self.value*other.value, other.value*self.grad + self.value*other.grad)
        except AttributeError:
            return Dual(self.value*other, other*self.grad)

    def __rmul__(self, other):
        return self*other

    def __truediv__(self, other):
        try:
            return Dual(self.value/other.value, self.grad/other.value - self.value*other.grad/other.value**2)
        except AttributeError:
            return Dual(self.value/other, self.grad/other)

    def __rtruediv__(self, other):
        ## todo: support vector
        try:
            return Dual(other.value/self.value, other.grad/self.value - other.value*self.grad/self.value**2)
        except AttributeError:
            return Dual(other/self.value, -other*self.grad/self.value**2)

    def __pow__(self, other):
        try:
            return Dual(self.value**other.value, other.value*self.value**(other.value - 1)*self.grad + np.log(self.value)*self.value**other.value*other.grad)
        except AttributeError:
            return Dual(self.value**other, other*self.value**(other - 1)*self.grad)

    def __rpow__(self, other):
        ## todo: support vector
        try:
            return Dual(other.value**self.value, self.value*other.value**(self.value - 1)*other.grad + np.log(other.value)*other.value**self.value*self.grad)
        except AttributeError:
            return Dual(other**self.value, np.log(self.value)*other**self.value*self.grad)

    @staticmethod
    def sin(dual):
        try:
            return Dual(np.sin(dual.value), np.cos(dual.value)*dual.grad)
        except AttributeError:
            return Dual(np.sin(dual), 0)

    @staticmethod
    def cos(dual):
        try:
            return Dual(np.cos(dual.value), -np.sin(dual.value)*dual.grad)
        except AttributeError:
            return Dual(np.cos(dual), 0)

    @staticmethod
    def exp(dual):
        try:
            return Dual(np.exp(dual.value), np.exp(dual.value)*dual.grad)
        except AttributeError:
            return Dual(np.exp(dual), 0)

    @staticmethod
    def log(dual):
        try:
            return Dual(np.log(dual.value), dual.grad/dual.value)
        except AttributeError:
            return Dual(np.log(dual), 0)

    def __call__(self, seed):
        if self.grad.shape != seed.shape:
            raise ValueError("Shape of the seed does not match that of the independent vector")
        return self.value, np.sum(self.grad*seed)
