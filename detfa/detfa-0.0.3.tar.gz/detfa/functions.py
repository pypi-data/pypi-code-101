"""
:authors: Alexander Goncharenko
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2021 Alexander Goncharenko
"""


import numpy as np

from typing import *
from itertools import *

def factors_product(beg: List, end: List) -> List:
    '''
    Return numpy vector of the influence of individual factors on the change effective variable
    The effective indicator is a product of factors.

    :param beg:  beginning values of factors;
    :param end: ending values of factors;
    :return:  influencing values.
    '''

    if len(beg) != len(end):
        return 'NA'

    beg = np.array(beg)
    end = np.array(end)
    sep = np.array(list(product([0, 1], repeat=len(beg))))[1:]

    return (sep.T*((sep*(end-beg)+beg*(1-sep)).prod(1)/sep.sum(1))).sum(1)

