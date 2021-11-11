#!/usr/bin/env python
# -*- coding: utf-8 -*-

import typing

import torch

from ..bayesian_module import BayesianModule
from .bayesian_linear import BayesianLinear


class BayesianMLP(BayesianModule):

    def __init__(
        self,
        in_features: int,
        hidden_features: typing.Tuple[int, ...],
        out_features: int,
        scale_mixture: bool = True,
        sigma_1: float = 1.0,
        sigma_2: float = 0.0025,
        pi: float = 0.5,
        mu: float = 0.0,
        sigma: float = 1.0,
    ) -> None:
        super().__init__()
        features = (in_features,) + hidden_features + (out_features,)
        self.num_affine_maps = len(features) - 1
        self.layers = torch.nn.ModuleList([
            BayesianLinear(
                features[idx],
                features[idx + 1],
                bias=True,
                scale_mixture=scale_mixture,
                sigma_1=sigma_1,
                sigma_2=sigma_2,
                pi=pi,
                mu=mu,
                sigma=sigma,
            ) for idx in range(self.num_affine_maps)
        ])
        self.activation = torch.nn.ReLU(inplace=True)

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        self._log_prior_reset()
        self._log_variational_posterior_reset()
        output = input
        for idx, layer in enumerate(self.layers):
            output = layer(output)
            self._log_prior += layer.log_prior
            self._log_variational_posterior += layer.log_variational_posterior
            if idx < self.num_affine_maps - 1:
                output = self.activation(output)
        return output
