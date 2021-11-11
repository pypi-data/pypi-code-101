#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

import torch

from .distribution import Distribution


class GaussianVariationalPosterior(Distribution):

    def __init__(self, mu: torch.Tensor, rho: torch.Tensor):
        super().__init__()
        assert mu.size() == rho.size()
        self.mu = mu
        self.rho = rho
        self.sigma = torch.log(1 + torch.exp(rho))
        self._normal = torch.distributions.Normal(0, 1)

    def sample(self) -> torch.Tensor:
        epsilon = self._normal.sample(sample_shape=self.sigma.size())
        return self.mu + self.sigma * epsilon

    def log_prob(self, value: torch.Tensor) -> torch.Tensor:
        _log_prob = -torch.log(math.sqrt(2 * math.pi) * self.sigma) - (value - self.mu) ** 2 / (2 * self.sigma ** 2)
        return _log_prob.sum()

    def log_variational_posterior(self, value: torch.Tensor) -> torch.Tensor:
        return self.log_prob(value)
