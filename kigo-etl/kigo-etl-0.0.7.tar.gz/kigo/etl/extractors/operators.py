from operator import add
from operator import and_
from operator import contains
from operator import eq
from operator import ge
from operator import getitem
from operator import gt
from operator import inv
from operator import le
from operator import lshift
from operator import lt
from operator import mod
from operator import mul
from operator import ne
from operator import neg
from operator import or_
from operator import rshift
from operator import sub
from operator import truediv
div = truediv


class ExtractorOperator:

    def __lt__(self, other):
        """Implement the ``<`` operator."""
        return self.operate(lt, other)

    def __le__(self, other):
        """Implement the ``<=`` operator."""
        return self.operate(le, other)

    def __eq__(self, other):
        """Implement the ``==`` operator."""
        return self.operate(eq, other)

    def __ne__(self, other):
        """Implement the ``!=`` operator."""
        return self.operate(ne, other)

    def __gt__(self, other):
        """Implement the ``>`` operator."""
        return self.operate(gt, other)

    def __ge__(self, other):
        """Implement the ``>=`` operator."""
        return self.operate(ge, other)

    def __neg__(self):
        """Implement the ``-`` operator."""
        return self.operate(neg)

    def __contains__(self, other):
        return self.operate(contains, other)

    def __getitem__(self, index):
        """Implement the [] operator."""
        return self.operate(getitem, index)

    def __lshift__(self, other):
        """implement the << operator."""
        return self.operate(lshift, other)

    def __rshift__(self, other):
        """implement the >> operator."""
        return self.operate(rshift, other)

    def __radd__(self, other):
        """Implement the ``+`` operator in reverse."""
        return self.reverse_operate(add, other)

    def __rsub__(self, other):
        """Implement the ``-`` operator in reverse."""
        return self.reverse_operate(sub, other)

    def __rmul__(self, other):
        """Implement the ``*`` operator in reverse."""
        return self.reverse_operate(mul, other)

    def __rdiv__(self, other):
        """Implement the ``/`` operator in reverse."""
        return self.reverse_operate(div, other)

    def __rmod__(self, other):
        """Implement the ``%`` operator in reverse."""
        return self.reverse_operate(mod, other)

    def __add__(self, other):
        """Implement the ``+`` operator."""
        return self.operate(add, other)

    def __sub__(self, other):
        """Implement the ``-`` operator."""
        return self.operate(sub, other)

    def __mul__(self, other):
        """Implement the ``*`` operator."""
        return self.operate(mul, other)

    def __div__(self, other):
        """Implement the ``/`` operator."""
        return self.operate(div, other)

    def __mod__(self, other):
        """Implement the ``%`` operator."""
        return self.operate(mod, other)

    def __truediv__(self, other):
        """Implement the ``//`` operator."""
        return self.operate(truediv, other)

    def __rtruediv__(self, other):
        """Implement the ``//`` operator in reverse."""
        return self.reverse_operate(truediv, other)

    def operate(self, op, *other, **kwargs):
        r"""Operate on an argument."""
        print(str(op), other, kwargs)

    def reverse_operate(self, op, other, **kwargs):
        """Reverse operate on an argument."""
        print(str(op), other, kwargs)