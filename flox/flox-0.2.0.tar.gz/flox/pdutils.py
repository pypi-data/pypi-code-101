import numpy as np
from .xrutils import is_scalar


# copied from pandas.cur
def choose_bins(x, bins, right=True):
    assert not np.iterable(bins)
    if is_scalar(bins) and bins < 1:
        raise ValueError("`bins` should be a positive integer.")

    try:  # for array-like
        sz = x.size
    except AttributeError:
        x = np.asarray(x)
        sz = x.size

    if sz == 0:
        raise ValueError("Cannot cut empty array")

    rng = (np.nanmin(x), np.nanmax(x))
    mn, mx = (mi + 0.0 for mi in rng)

    if np.isinf(mn) or np.isinf(mx):
        # GH 24314
        raise ValueError("cannot specify integer `bins` when input data contains infinity")
    elif mn == mx:  # adjust end points before binning
        mn -= 0.001 * abs(mn) if mn != 0 else 0.001
        mx += 0.001 * abs(mx) if mx != 0 else 0.001
        bins = np.linspace(mn, mx, bins + 1, endpoint=True)
    else:  # adjust end points after binning
        bins = np.linspace(mn, mx, bins + 1, endpoint=True)
        adj = (mx - mn) * 0.001  # 0.1% of the range
        if right:
            bins[0] -= adj
        else:
            bins[-1] += adj
    return bins
