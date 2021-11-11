#!/usr/bin/env python
# -*- coding: utf-8 -*-

import torch

from pytorch_bayes import distributions
from ..bayesian_module import BayesianModule


class BayesianLinear(BayesianModule):

    def __init__(
        self,
        in_features: int,
        out_features: int,
        bias: bool = True,
        scale_mixture: bool = True,
        sigma_1: float = 1.0,
        sigma_2: float = 0.0025,
        pi: float = 0.5,
        mu: float = 0.0,
        sigma: float = 1.0,
    ) -> None:
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.use_bias = bias
        # prior
        if scale_mixture:
            self.prior = distributions.ScaleMixturePrior(
                torch.tensor(sigma_1),
                torch.tensor(sigma_2),
                pi
            )
        else:
            self.prior = distributions.GaussianPrior(
                torch.tensor(mu),
                torch.tensor(sigma)
            )
        # variational posterior
        self.weight_variational_posterior = distributions.GaussianVariationalPosterior(
            torch.nn.Parameter(torch.empty((out_features, in_features)).uniform_(-0.2, 0.2)),
            torch.nn.Parameter(torch.empty((out_features, in_features)).uniform_(-5.0, -4.0))
        )
        if self.use_bias:
            self.bias_variational_posterior = distributions.GaussianVariationalPosterior(
                torch.nn.Parameter(torch.empty((out_features,)).uniform_(-0.2, 0.2)),
                torch.nn.Parameter(torch.empty((out_features,)).uniform_(-5.0, -4.0))
            )
        else:
            self.bias_variational_posterior = None

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        self._log_prior_reset()
        self._log_variational_posterior_reset()
        weight = self.weight_variational_posterior.sample()
        self._log_prior = self.prior.log_prior(weight)
        self._log_variational_posterior = self.weight_variational_posterior.log_variational_posterior(weight)
        if self.use_bias:
            bias = self.bias_variational_posterior.sample()
            self._log_prior += self.prior.log_prior(bias)
            self._log_variational_posterior += self.bias_variational_posterior.log_variational_posterior(bias)
        else:
            bias = None
        return torch.nn.functional.linear(input, weight, bias)
