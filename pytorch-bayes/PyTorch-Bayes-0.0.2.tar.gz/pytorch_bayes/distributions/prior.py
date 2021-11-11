#!/usr/bin/env python
# -*- coding: utf-8 -*-

import torch

from .distribution import Distribution


class GaussianPrior(Distribution):

    def __init__(self, mu: torch.Tensor, sigma: torch.Tensor):
        super().__init__()
        assert mu.size() == torch.Size() and sigma.size() == torch.Size()
        assert sigma > 0
        self.mu = mu
        self.sigma = sigma
        self._normal = torch.distributions.Normal(mu, sigma)

    def sample(self) -> None:
        return None

    def log_prob(self, value: torch.Tensor) -> torch.Tensor:
        _log_prob = self._normal.log_prob(value)
        return _log_prob.sum()

    def log_prior(self, value: torch.Tensor) -> torch.Tensor:
        return self.log_prob(value)


class ScaleMixturePrior(Distribution):

    def __init__(self, sigma_1: torch.Tensor, sigma_2: torch.Tensor, pi: float):
        super().__init__()
        assert sigma_1.size() == torch.Size() and sigma_2.size() == torch.Size()
        assert sigma_1 > sigma_2 and sigma_2 > 0
        self.sigma_1 = sigma_1
        self.sigma_2 = sigma_2
        self.pi = pi
        self._normal_1 = torch.distributions.Normal(0, sigma_1)
        self._normal_2 = torch.distributions.Normal(0, sigma_2)

    def sample(self) -> None:
        return None

    def log_prob(self, value: torch.Tensor) -> torch.Tensor:
        prob_1 = torch.exp(self._normal_1.log_prob(value))
        prob_2 = torch.exp(self._normal_2.log_prob(value))
        _log_prob = torch.log(self.pi * prob_1 + (1 - self.pi) * prob_2)
        return _log_prob.sum()

    def log_prior(self, value: torch.Tensor) -> torch.Tensor:
        return self.log_prob(value)
