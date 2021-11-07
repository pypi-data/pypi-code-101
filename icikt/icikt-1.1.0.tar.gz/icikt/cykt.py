
import warnings
from collections import namedtuple

import cython
import numpy as np
from numpy import ma
from scipy.stats import mstats_basic

from scipy.stats.stats import _contains_nan
from scipy.stats import distributions

import pyximport
pyximport.install()
from kendall_dis import kendall_dis
# from scipy.stats import _stats

def _normtest_finish(z: np.ndarray, alternative):
    """Common code between all the normality-test functions."""
    prob: cython.float
    if alternative == 'less':
        prob = distributions.norm.cdf(z)
    elif alternative == 'greater':
        prob = distributions.norm.sf(z)
    elif alternative == 'two-sided':
        prob = 2 * distributions.norm.sf(np.abs(z))
    else:
        raise ValueError("alternative must be "
                         "'less', 'greater' or 'two-sided'")

    if z.ndim == 0:
        z = z[()]

    return z, prob


KendalltauResult = namedtuple('KendalltauResult', ('correlation', 'pvalue'))


def kendalltau(x: np.ndarray,
               y: np.ndarray,
               initial_lexsort=None,
               nan_policy='propagate',
               method='auto',
               variant='b',
               alternative='two-sided'):

    x: cython.np.ndarray
    y: cython.np.ndarray

    x = np.asarray(x).ravel()
    y = np.asarray(y).ravel()

    if x.size != y.size:
        raise ValueError("All inputs to `kendalltau` must be of the same "
                         f"size, found x-size {x.size} and y-size {y.size}")
    elif not x.size or not y.size:
        # Return NaN if arrays are empty
        return KendalltauResult(np.nan, np.nan)

    contains_nan: cython.bint
    cnx: cython.bint | None
    cny: cython.bint | None

    cnx, npx = _contains_nan(x, nan_policy)
    cny, npy = _contains_nan(y, nan_policy)
    contains_nan = cnx or cny

    if 'omit' in (npx, npy):
        nan_policy = 'omit'

    if contains_nan and nan_policy == 'propogate':
        return KendalltauResult(np.nan, np.nan)
    elif contains_nan and nan_policy == 'omit':
        x = ma.masked_invalid(x)
        y = ma.masked_invalid(y)
        if variant == 'b':
            return mstats_basic.kendalltau(x, y, method=method, use_ties=True, alternative=alternative)
        else:
            message = ("nan_policy='omit' is currently compatible only with "
                       "variant='b'.")
            raise ValueError(message)

    if initial_lexsort is not None:  # deprecate to drop!
        warnings.warn('"initial_lexsort" is gone!')

    def count_rank_tie(ranks: np.ndarray):
        cnt: np.ndarray
        cnt = np.bincount(ranks).astype('int64', copy=False)
        cnt = cnt[cnt > 1]
        return ((cnt * (cnt - 1) // 2).sum(),
                (cnt * (cnt - 1.) * (cnt - 2)).sum(),
                (cnt * (cnt - 1.) * (2*cnt + 5)).sum())

    size: cython.Py_ssize_t
    perm: cython.int| np.ndarray
    size = x.size
    perm = np.argsort(y)

    print(x,y)

    x, y = x[perm], y[perm]

    print(x,y)

    y = np.r_[True, y[1:] != y[:-1]].cumsum(dtype=np.intp)

    print(x,y)


# stable sort on x and convert x to dense ranks
    perm = np.argsort(x, kind='mergesort')
    x, y = x[perm], y[perm]
    x = np.r_[True, x[1:] != x[:-1]].cumsum(dtype=np.intp)

    dis: cython.int

    dis = _kendall_dis(x, y)  # discordant pairs

    obs: cython.np.matrix
    cnt: cython.np.ndarray
    obs = np.r_[True, (x[1:] != x[:-1]) | (y[1:] != y[:-1]), True]
    cnt = np.diff(np.nonzero(obs)[0]).astype('int64', copy=False)

    ntie = (cnt * (cnt - 1) // 2).sum()  # joint ties
    xtie, x0, x1 = count_rank_tie(x)     # ties in x, stats
    ytie, y0, y1 = count_rank_tie(y)     # ties in y, stats

    tot: cython.int
    tot = (size * (size - 1)) // 2

    if xtie == tot or ytie == tot:
        return KendalltauResult

    con_minus_dis: cython.int
    con_minus_dis = tot - xtie - ytie - 2 * dis + ntie

    tau: cython.float
    minclasses: cython.int

    if variant == 'b':
        tau = con_minus_dis / np.sqrt(tot - xtie) / np.sqrt(tot - ytie)
    elif variant == 'c':
        minclasses = min(len(set(x)), len(set(y)))
        tau = 2*con_minus_dis / (size**2 * (minclasses-1)/minclasses)
    else:
        raise ValueError(f"Unknown variant of the method chosen: {variant}. "
                         "variant must be 'b' or 'c'.")

    # Limit range to fix computational errors
    tau = min(1., max(-1., tau))

    # The p-value calculation is the same for all variants since the p-value
    # depends only on con_minus_dis.
    if method == 'exact' and (xtie != 0 or ytie != 0):
        raise ValueError("Ties found, exact method cannot be used.")

    if method == 'auto':
        if (xtie == 0 and ytie == 0) and (size <= 33 or
                                          min(dis, tot-dis) <= 1):
            method = 'exact'
        else:
            method = 'asymptotic'

    pvalue: cython.float
    m: cython.float
    var: cython.np.float64
    z: cython.float

    if xtie == 0 and ytie == 0 and method == 'exact':
        pvalue = mstats_basic._kendall_p_exact(size, abs(tot-dis))
    elif method == 'asymptotic':
        # con_minus_dis is approx normally distributed with this variance [3]_
        m = size * (size - 1.)
        var = ((m * (2*size + 5) - x1 - y1) / 18 +
               (2 * xtie * ytie) / m + x0 * y0 / (9 * m * (size - 2)))
        z = con_minus_dis / np.sqrt(var)
        print(type(z))
        _, pvalue = _normtest_finish(z, alternative)
    else:
        raise ValueError(f"Unknown method {method} specified.  Use 'auto', "
                         "'exact' or 'asymptotic'.")

    return KendalltauResult(tau, pvalue)











