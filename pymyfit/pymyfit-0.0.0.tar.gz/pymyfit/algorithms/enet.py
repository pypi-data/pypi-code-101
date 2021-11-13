"""Elastic Net Family Fitters"""

import numpy as np
import scipy.linalg as la
from .base import BaseFit
from ._enet import _enet

__all__ = ["LeastSquaresFit", "EnetFit"]


class LeastSquaresFit(BaseFit):
    def __new__(cls, x, y):
        obj = super().__new__(cls, "lstsq", x, y)

        return obj

    @staticmethod
    def _fit(x, y):
        fit, _, _, _ = la.lstsq(x, y)

        return fit


class EnetFit(BaseFit):
    def __new__(cls, x, y, alpha, beta, max_it=1000):
        obj = super().__new__(cls, "enet", x, y, alpha=alpha, beta=beta, max_it=max_it)

        return obj

    @staticmethod
    def _fit(x, y, alpha, beta, max_it):
        theta = np.zeros(x.shape[1], dtype=x.dtype, order="F")

        nsamp = x.shape[0]

        lam = alpha * beta * nsamp
        gam = alpha * (1.0 - beta) * nsamp

        fit = _enet(theta, x, y, lam, gam, max_it)

        return fit
