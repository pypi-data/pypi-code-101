#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import warnings

import torch


class Distribution(torch.nn.Module, metaclass=abc.ABCMeta):

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def sample(self, sample_shape: torch.Size = torch.Size()) -> torch.Tensor:
        raise NotImplementedError

    @abc.abstractmethod
    def log_prob(self, value: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError

    def forward(self, value: torch.Tensor) -> torch.Tensor:
        # DO NOT USE THIS METHOD
        warnings.warn('Distribution should not be called! Use its explicit methods!')
        return self.log_prob(value)
