#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

import torch


class BayesianModule(torch.nn.Module, metaclass=abc.ABCMeta):

    def __init__(self) -> None:
        super().__init__()
        self._log_prior = torch.tensor(0.0)
        self._log_variational_posterior = torch.tensor(0.0)

    @property
    def log_prior(self) -> torch.Tensor:
        return self._log_prior

    def _log_prior_reset(self) -> torch.Tensor:
        self._log_prior = torch.tensor(0.0)

    @property
    def log_variational_posterior(self) -> torch.Tensor:
        return self._log_variational_posterior

    def _log_variational_posterior_reset(self) -> torch.Tensor:
        self._log_variational_posterior = torch.tensor(0.0)
