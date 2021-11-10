import numpy as np
from punting.onedim.onescratching import scratch_win, unscratch_win


def normalize_probabilities(p,scr=-1):
    """ Naive renormalization of probabilities, ignoring non-positive """
    p_starters, ndx, n = scratch_win(p)
    sum_p = sum(p_starters)
    p_starters_normalized = [pr / sum_p for pr in p_starters]
    return unscratch_win(x=p_starters_normalized,ndx=ndx, n=n, scr=scr)


def is_prob(p):
    outside = [pi > 1.0 for pi in p]
    inside = [0.0 < pi < 1.0 for pi in p]
    return sum(inside) > sum(outside)


def to_normalized_dividends(p, scr=-1):
    if not is_prob(p):
        ps = [ 1/pi if pi>0 else scr for pi in p ]
    else:
        ps = [ pi if pi>0 else scr for pi in p ]
    p_norm = normalize_probabilities(p=ps,scr=scr)
    return [ 1/pi if pi>0 else scr for pi in p_norm ]


def to_normalized_probabilities(p, scr=-1):
    """ Convert probs or inv probs with scratching to normalize probs
    :param p:
    :param scr:
    :return:
    """
    if not is_prob(p):
        ps = [ 1/pi if pi>0 else scr for pi in p ]
    else:
        ps = [ pi if pi>0 else scr for pi in p ]
    return normalize_probabilities(p=ps,scr=scr)


def from_dividends(p,scr=-1):
    d_starters, ndx, n = scratch_win(p)
    p_starters = normalize_probabilities( [save_inversion(di) for di in d_starters] )
    return unscratch_win(x=p_starters,ndx=ndx, n=n,scr=scr)






def save_inversion(x):
    try:
        return 1/x
    except ArithmeticError:
        return np.nan




