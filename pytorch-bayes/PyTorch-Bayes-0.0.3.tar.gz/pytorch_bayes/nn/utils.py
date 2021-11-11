#!/usr/bin/env python
# -*- coding: utf-8 -*-

import typing

import torch

from .bayesian_module import BayesianModule


def variational_approximator(module: BayesianModule) -> BayesianModule:

    def kl(self) -> torch.Tensor:
        return self.log_variational_posterior - self.log_prior

    setattr(module, 'kl', kl)

    def mc_elbo(
        self,
        criterion: typing.Callable[[torch.Tensor, torch.Tensor], torch.Tensor],
        input: torch.Tensor,
        target: torch.Tensor,
        complexity_weight: float,
        num_mc_samples: int = 5,
    ) -> torch.Tensor:
        _kl = torch.zeros(num_mc_samples)
        _nll = torch.zeros(num_mc_samples)
        for idx in range(num_mc_samples):
            output = self.forward(input)
            _kl[idx] = self.kl()
            _nll[idx] = criterion(output, target)
        return _kl.mean() * complexity_weight + _nll.mean()

    setattr(module, 'mc_elbo', mc_elbo)

    def mc_pred(
        self,
        transformer: typing.Callable[[torch.Tensor], torch.Tensor],
        input: torch.Tensor,
        num_mc_samples: int = 5,
    ) -> torch.Tensor:
        pred = torch.stack([transformer(self.forward(input)) for _ in range(num_mc_samples)], dim=0)
        return pred.mean(dim=0)

    return module


def minibatch_weight(
    batch_idx: int,
    num_batches: int,
    graves: bool = False
) -> float:
    if graves:
        return 1. / num_batches
    return 2 ** (num_batches - batch_idx - 1) / (2 ** num_batches - 1)
