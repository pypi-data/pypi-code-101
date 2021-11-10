'''This module converts numbers - both integer and floating-point -
from one base to another. It also enables arithmetic operations in a
given base.
'''
from string import digits, ascii_uppercase
import math
from copy import copy

# 10 digits + 26 letters = 36 - upto base 36 is supported
DIGITS = digits + ascii_uppercase


class Num:
    '''Instantiate this class to represent a value in a certain base.
    Parameters -
    value - Can be a string or int or float in the given base.
    base - The base of the given value (should be between 2 and 36).
    '''

    def __init__(self, value, base=10):
        self.value = str(value).upper()
        self.base = int(base)
        if not (2 <= base <= 36):
            raise ValueError('Base must be an int between 2 and 36.')
        self.validate()
        if self.base == 10:
            self.base10_value = self._get_numeric_value(value)
        else:
            self.base10_value = self._to_base10()

    def _get_numeric_value(self, value):
        '''Convert possible string representation to number.'''

        if isinstance(value, str):
            try:
                return int(value)
            except ValueError:
                return float(value)

        return value

    def __repr__(self):
        return self.value

    def clone(self):
        return copy(self)

    def validate(self):
        '''Check if the user input is a valid number in the specified
        base.'''
        valid_digits = DIGITS[:self.base]
        for digit in self.value:
            if (digit not in ('.', '+', '-') and
                    not (self.base == 10 and digit in ('e', 'E'))):
                if digit not in valid_digits:
                    raise ValueError(f'{self.value} is an invalid base'
                                     f' {self.base} number.')

    def to(self, base, prec=10):
        '''Convert a number in a certain base to a new base, and return
        the instance. The stored base 10 value is used in the process.
        This is an inplace conversion.

        Parameters -
        base - The target base
        prec - The number of decimal places in the result if a float is
               being converted.
        '''
        if base == self.base:
            return self

        if base == 10:
            self.value = str(self.base10_value)
            self.base = 10
            return self

        frac_part, int_part = math.modf(self.base10_value)

        sign = '-' if int_part < 0 else ''
        int_part = abs(int(int_part))
        int_val = ''
        while int_part:
            int_part, rem = divmod(int_part, base)
            int_val = DIGITS[rem] + int_val
        if not int_val:
            int_val = '0'

        frac_part = abs(frac_part)
        frac_val = ''
        while frac_part and len(frac_val) < prec:
            val = frac_part * base
            frac_val += DIGITS[int(val)]
            frac_part = val - int(val)

        if frac_val or isinstance(self.base10_value, float):
            result = sign + int_val + '.' + (frac_val or '0')
        else:
            result = sign + int_val

        self.value = result
        self.base = base
        return self

    def conv(self, to_base, prec=10):
        '''Convert number to given base and return a new instance.'''

        return self.clone().to(to_base, prec)

    def _to_base10(self):
        '''Calculate the base 10 value of the stored number.'''

        int_part, *rest = self.value.split('.')
        frac_part = rest[0] if rest else ''

        int_value = 0
        sign = 1
        if int_part:
            c = int_part[0]
            if c in ('+', '-'):
                sign = -1 if c == '-' else 1
                int_part = int_part[1:]

        for index, digit in enumerate(int_part[::-1]):
            int_value += DIGITS.index(digit) * self.base ** index
        int_value *= sign

        frac_value = 0
        for index, digit in enumerate(frac_part, 1):
            frac_value += DIGITS.index(digit) * self.base ** -index
        frac_value *= sign

        if frac_value:
            result = int_value + frac_value
        else:
            result = int_value

        return result

    def __eq__(self, other):

        a, b = self._get_base10_values(other)
        if a == b:
            return True
        return False

    def __add__(self, other):

        self._check_bases(other)
        a, b = self._get_base10_values(other)
        result = a + b
        return self.__class__(result, 10).to(self.base)

    def __sub__(self, other):

        self._check_bases(other)
        a, b = self._get_base10_values(other)
        result = a - b
        return self.__class__(result, 10).to(self.base)

    def __mul__(self, other):

        self._check_bases(other)
        a, b = self._get_base10_values(other)
        result = a * b
        return self.__class__(result, 10).to(self.base)

    def __truediv__(self, other):

        self._check_bases(other)
        a, b = self._get_base10_values(other)
        result = a / b
        return self.__class__(result, 10).to(self.base)

    def __floordiv__(self, other):

        self._check_bases(other)
        a, b = self._get_base10_values(other)
        result = a // b
        return self.__class__(result, 10).to(self.base)

    def __mod__(self, other):

        self._check_bases(other)
        a, b = self._get_base10_values(other)
        result = a % b
        return self.__class__(result, 10).to(self.base)

    def __divmod__(self, other):

        self._check_bases(other)
        a, b = self._get_base10_values(other)
        q, r = divmod(a, b)
        return (self.__class__(q, 10).to(self.base),
                self.__class__(r, 10).to(self.base))

    def __pow__(self, other):

        self._check_bases(other)
        a, b = self._get_base10_values(other)
        result = a ** b
        return self.__class__(result, 10).to(self.base)

    def __neg__(self):

        a, _ = self._get_base10_values(self.__class__(-1))
        result = -1 * a
        return self.__class__(result, 10).to(self.base)

    def __pos__(self):

        return self

    def _get_base10_values(self, other):
        '''Return the base10 values.'''

        return self.base10_value, other.base10_value

    def _check_bases(self, other):
        '''Computations are possible when the operands have the same
        base.
        '''
        if self.base != other.base:
            raise TypeError(f'{self} and {other} don\'t have the same base.')
