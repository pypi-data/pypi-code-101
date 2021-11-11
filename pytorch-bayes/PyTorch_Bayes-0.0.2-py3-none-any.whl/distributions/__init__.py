#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .distribution import Distribution
from .variational_posterior import GaussianVariationalPosterior
from .prior import GaussianPrior, ScaleMixturePrior

__all__ = (
    'Distribution',
    'GaussianVariationalPosterior',
    'GaussianPrior',
    'ScaleMixturePrior',
)
