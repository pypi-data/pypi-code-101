import warnings
from collections import namedtuple
import numpy as np
from numpy import ma
from scipy.stats import mstats_basic
from scipy.stats.stats import _contains_nan
from scipy.stats import distributions
import pyximport
pyximport.install()
from kendall_dis import kendall_dis


def _normtest_finish(z, alternative):
    """Common code between all the normality-test functions."""
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


def kendalltau(x, y, initial_lexsort=None, nan_policy='propagate',
               method='auto', variant='b', alternative='two-sided'):
    """Calculate Kendall's tau, a correlation measure for ordinal data.
    Kendall's tau is a measure of the correspondence between two rankings.
    Values close to 1 indicate strong agreement, and values close to -1
    indicate strong disagreement. This implements two variants of Kendall's
    tau: tau-b (the default) and tau-c (also known as Stuart's tau-c). These
    differ only in how they are normalized to lie within the range -1 to 1;
    the hypothesis tests (their p-values) are identical. Kendall's original
    tau-a is not implemented separately because both tau-b and tau-c reduce
    to tau-a in the absence of ties.
    Parameters
    ----------
    x, y : array_like
        Arrays of rankings, of the same shape. If arrays are not 1-D, they
        will be flattened to 1-D.
    initial_lexsort : bool, optional
        Unused (deprecated).
    nan_policy : {'propagate', 'raise', 'omit'}, optional
        Defines how to handle when input contains nan.
        The following options are available (default is 'propagate'):
          * 'propagate': returns nan
          * 'raise': throws an error
          * 'omit': performs the calculations ignoring nan values
    method : {'auto', 'asymptotic', 'exact'}, optional
        Defines which method is used to calculate the p-value [5]_.
        The following options are available (default is 'auto'):
          * 'auto': selects the appropriate method based on a trade-off
            between speed and accuracy
          * 'asymptotic': uses a normal approximation valid for large samples
          * 'exact': computes the exact p-value, but can only be used if no ties
            are present. As the sample size increases, the 'exact' computation
            time may grow and the result may lose some precision.
    variant: {'b', 'c'}, optional
        Defines which variant of Kendall's tau is returned. Default is 'b'.
    alternative : {'two-sided', 'less', 'greater'}, optional
        Defines the alternative hypothesis. Default is 'two-sided'.
        The following options are available:
        * 'two-sided': the rank correlation is nonzero
        * 'less': the rank correlation is negative (less than zero)
        * 'greater':  the rank correlation is positive (greater than zero)
    Returns
    -------
    correlation : float
       The tau statistic.
    pvalue : float
       The p-value for a hypothesis test whose null hypothesis is
       an absence of association, tau = 0.
    See Also
    --------
    spearmanr : Calculates a Spearman rank-order correlation coefficient.
    theilslopes : Computes the Theil-Sen estimator for a set of points (x, y).
    weightedtau : Computes a weighted version of Kendall's tau.
    Notes
    -----
    The definition of Kendall's tau that is used is [2]_::
      tau_b = (P - Q) / sqrt((P + Q + T) * (P + Q + U))
      tau_c = 2 (P - Q) / (n**2 * (m - 1) / m)
    where P is the number of concordant pairs, Q the number of discordant
    pairs, T the number of ties only in `x`, and U the number of ties only in
    `y`.  If a tie occurs for the same pair in both `x` and `y`, it is not
    added to either T or U. n is the total number of samples, and m is the
    number of unique values in either `x` or `y`, whichever is smaller.
    References
    ----------
    .. [1] Maurice G. Kendall, "A New Measure of Rank Correlation", Biometrika
           Vol. 30, No. 1/2, pp. 81-93, 1938.
    .. [2] Maurice G. Kendall, "The treatment of ties in ranking problems",
           Biometrika Vol. 33, No. 3, pp. 239-251. 1945.
    .. [3] Gottfried E. Noether, "Elements of Nonparametric Statistics", John
           Wiley & Sons, 1967.
    .. [4] Peter M. Fenwick, "A new data structure for cumulative frequency
           tables", Software: Practice and Experience, Vol. 24, No. 3,
           pp. 327-336, 1994.
    .. [5] Maurice G. Kendall, "Rank Correlation Methods" (4th Edition),
           Charles Griffin & Co., 1970.
    Examples
    --------
    >>> from scipy import stats
    >>> x1 = [12, 2, 1, 12, 2]
    >>> x2 = [1, 4, 7, 1, 0]
    >>> tau, p_value = stats.kendalltau(x1, x2)
    >>> tau
    -0.47140452079103173
    >>> p_value
    0.2827454599327748
    """
    x = np.asarray(x).ravel()
    y = np.asarray(y).ravel()

    if x.size != y.size:
        raise ValueError("All inputs to `kendalltau` must be of the same "
                         f"size, found x-size {x.size} and y-size {y.size}")
    elif not x.size or not y.size:
        # Return NaN if arrays are empty
        return KendalltauResult(np.nan, np.nan)

    # check both x and y
    cnx, npx = _contains_nan(x, nan_policy)
    cny, npy = _contains_nan(y, nan_policy)
    contains_nan = cnx or cny
    if npx == 'omit' or npy == 'omit':
        nan_policy = 'omit'

    if contains_nan and nan_policy == 'propagate':
        return KendalltauResult(np.nan, np.nan)

    elif contains_nan and nan_policy == 'omit':
        x = ma.masked_invalid(x)
        y = ma.masked_invalid(y)
        if variant == 'b':
            return mstats_basic.kendalltau(x, y, method=method, use_ties=True,
                                           alternative=alternative)
        else:
            message = ("nan_policy='omit' is currently compatible only with "
                       "variant='b'.")
            raise ValueError(message)

    if initial_lexsort is not None:  # deprecate to drop!
        warnings.warn('"initial_lexsort" is gone!')

    def count_rank_tie(ranks):
        cnt = np.bincount(ranks).astype('int64', copy=False)
        cnt = cnt[cnt > 1]
        return ((cnt * (cnt - 1) // 2).sum(),
                (cnt * (cnt - 1.) * (cnt - 2)).sum(),
                (cnt * (cnt - 1.) * (2*cnt + 5)).sum())

    size = x.size
    perm = np.argsort(y)  # sort on y and convert y to dense ranks
    x, y = x[perm], y[perm]
    y = np.r_[True, y[1:] != y[:-1]].cumsum(dtype=np.intp)

    # stable sort on x and convert x to dense ranks
    perm = np.argsort(x, kind='mergesort')
    x, y = x[perm], y[perm]
    x = np.r_[True, x[1:] != x[:-1]].cumsum(dtype=np.intp)

    dis = kendall_dis(x, y)  # discordant pairs

    obs = np.r_[True, (x[1:] != x[:-1]) | (y[1:] != y[:-1]), True]
    cnt = np.diff(np.nonzero(obs)[0]).astype('int64', copy=False)

    ntie = (cnt * (cnt - 1) // 2).sum()  # joint ties
    xtie, x0, x1 = count_rank_tie(x)     # ties in x, stats
    ytie, y0, y1 = count_rank_tie(y)     # ties in y, stats

    tot = (size * (size - 1)) // 2

    if xtie == tot or ytie == tot:
        return KendalltauResult(np.nan, np.nan)

    # Note that tot = con + dis + (xtie - ntie) + (ytie - ntie) + ntie
    #               = con + dis + xtie + ytie - ntie
    con_minus_dis = tot - xtie - ytie + ntie - 2 * dis
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

    if xtie == 0 and ytie == 0 and method == 'exact':
        pvalue = mstats_basic._kendall_p_exact(size, tot-dis)
    elif method == 'asymptotic':
        # con_minus_dis is approx normally distributed with this variance [3]_
        m = size * (size - 1.)
        var = ((m * (2*size + 5) - x1 - y1) / 18 +
               (2 * xtie * ytie) / m + x0 * y0 / (9 * m * (size - 2)))
        z = con_minus_dis / np.sqrt(var)
        _, pvalue = _normtest_finish(z, alternative)
    else:
        raise ValueError(f"Unknown method {method} specified.  Use 'auto', "
                         "'exact' or 'asymptotic'.")

    print(x, y, cnt, size, dis, obs, xtie, ytie, ntie, tot, con_minus_dis, tau, pvalue, m, var, z)

    return KendalltauResult(tau, pvalue)
