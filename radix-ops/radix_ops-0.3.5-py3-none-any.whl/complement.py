'''This module finds the r and (r-1) complements of a number in base
r.
'''

from radix.radix import Num, DIGITS


def prepare_value(n):

    value = n.value.lstrip('+-')

    adjusted_len = len(value)
    radix_pos = value.find('.')
    value = value.replace('.', '')

    return value, radix_pos, adjusted_len


def insert_radix_point(val, pos, length):

    if pos > -1:
        lst = list(val)
        lst.insert(pos, '.')
        r = ''.join(lst)
    else:
        r = val

    if len(r) < length:
        result = r.zfill(length)
    else:
        result = r

    return result


def dim_radix_compl(n):
    '''(r-1) or the diminished radix complement.'''

    value, radix_pos, adjusted_len = prepare_value(n)
    minuend = DIGITS[n.base - 1] * len(value)
    subtrahend = Num(value, n.base)
    r = Num(minuend, n.base) - subtrahend

    result = insert_radix_point(r.value, radix_pos, adjusted_len)

    return result


def radix_compl(n):
    '''r or the radix complement.'''

    if n == Num(0, n.base):
        return '0'

    r_minus_1_compl = dim_radix_compl(n)
    adjusted_len = len(r_minus_1_compl)
    radix_pos = r_minus_1_compl.find('.')
    value = r_minus_1_compl.replace('.', '')

    r = Num(value, n.base) + Num(1, n.base)
    result = insert_radix_point(r.value, radix_pos, adjusted_len)

    return result
