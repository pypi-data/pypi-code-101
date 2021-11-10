'''This module represents signed binary numbers in 2's complement
form. It also enables 2's complement addition and subtraction.'''

from radix.radix import Num
from radix.complement import dim_radix_compl, radix_compl


class Bin(Num):
    '''Signed binary numbers.

    Find representations of a number in binary 2's complement,
    1's complement and sign magnitude forms. Perform 2's complement
    addition and subtraction.
    '''

    def __init__(self, *args, twos_compl=None, **kwargs):
        '''Initialize binary number.

        If `twos_compl` parameter is passed, then only that is set on
        the instance. All other initialization is skipped. This is
        useful while adding and subtracting multiple binary numbers.
        '''
        if twos_compl is None:
            super().__init__(*args, **kwargs)

        self._2_compl = twos_compl or self.twos_compl()

    def __repr__(self):
        return self._2_compl

    def _process_base2(self):
        '''Create a base 2 number whose value has no sign and starts
        with 0.
        '''

        value = self.clone().to(2).value.lstrip('+-')
        if value[0] in ('1', '.'):
            value = '0' + value
        n = Num(value, 2)
        return n

    def twos_compl(self):
        '''Find the 2's complement.'''

        n = self._process_base2()
        if self.sign() == -1:
            res = radix_compl(n)
            twos_compl_str = res[1:] if res.startswith('11') else res
        else:
            twos_compl_str = n.value

        return twos_compl_str

    def ones_compl(self):
        '''Find the 1's complement.'''

        n = self._process_base2()
        if self.sign() == -1:
            res = dim_radix_compl(n)
            ones_compl_str = res[1:] if res.startswith('11') else res
        else:
            ones_compl_str = n.value

        return ones_compl_str

    def sign_mag(self):
        '''Find the sign magnitude representation.'''

        value = self.clone().to(2).value.lstrip('+-')
        if self.sign() == -1:
            return '1' + value
        elif value[0] in ('1', '.'):
            return '0' + value
        else:
            return value

    def format(self, size=8, blanks_every=None):
        '''Format the 2's complement string to be of a given size, with
        blanks inserted at intervals.
        '''

        value = self._2_compl
        fillchar = value[0]
        value = value.rjust(size, fillchar)

        if blanks_every:
            segments = []
            for i in range(0, len(value), blanks_every):
                segments.append(value[i:i + blanks_every])
                segments.append(' ')
            segments = segments[:-1]
            value = ''.join(segments)

        return value

    def sign(self):
        '''Sign of the binary number input to `Bin` class.'''

        if self.value.startswith('-'):
            return -1
        return 1

    def __add__(self, other):
        '''2's complement addition.'''

        a = self._2_compl
        b = other._2_compl
        twos_compl = self._add(a, b)
        return self.__class__(twos_compl=twos_compl)

    def _add(self, a, b):
        '''Perform addition of 2 binary numbers.'''

        # Make numbers equal in length
        if len(a) < len(b):
            a = a.rjust(len(b), a[0])
        else:
            b = b.rjust(len(a), b[0])

        # To track overflow
        if a[0] == b[0] == '0':
            flag = 0
        elif a[0] == b[0] == '1':
            flag = 1
        else:
            flag = -1

        a = a[::-1]
        b = b[::-1]
        carry = '0'
        r = ''  # intermediate result

        # Binary addition
        for i, j in zip(a, b):
            if i == '0' and j == '0':
                r += carry
                carry = '0'
            elif (i == '0' and j == '1') or (i == '1' and j == '0'):
                if carry == '1':
                    r += '0'
                else:
                    r += '1'
            else:
                if carry == '1':
                    r += '1'
                else:
                    r += '0'
                    carry = '1'
        r = r[::-1]
        # overflow
        if r[0] == '1' and flag == 0:
            result = '0' + r
        elif r[0] == '0' and flag == 1:
            result = '1' + r
        else:
            result = r

        return result

    def __sub__(self, other):
        '''2's complement subtraction.

        Add minuend to 2's complement of the subtrahend.
        '''

        a = self._2_compl
        b = (-other)._2_compl
        twos_compl = self._add(a, b)

        return self.__class__(twos_compl=twos_compl)

    @classmethod
    def from_Num(cls, instance: Num):

        # Prevent recalculation of base 10 value when Bin instance is
        # created.
        inst = cls(instance.base10_value, 10)
        inst.value = instance.value
        inst.base = instance.base

        return inst

    def __getattr__(self, name):

        if name in ('value', 'base', 'base10_value'):
            raise NotImplementedError('Use `Num` class and convert the result '
                                      'to the `Bin` class with the `from_Num` '
                                      'classmethod.')

        raise AttributeError(f"'Bin' object has no attribute {name!r}")
