import numpy as np


def meanrel(x1, x2, axis=0):
    """mean relative error

    Parameters
    ----------
    x1, x2 : array_like
       The performance measure depends on the difference between these two
       arrays.
    axis : int
       axis along which the summary statistic is calculated
    Returns
    -------
    mse : ndarray or float
       mean relative error along given axis.
    Notes
    -----
    If ``x1`` and ``x2`` have different shapes, then they need to broadcast.
    This uses ``numpy.asanyarray`` to convert the input. Whether this is the
    desired result or not depends on the array subclass, for example
    numpy matrices will silently produce an incorrect result.
    """
    x1 = np.asanyarray(x1)
    x2 = np.asanyarray(x2)
    return np.mean(np.abs(x1 - x2) / x2, axis=axis)


__all__ = [
    meanrel
]
