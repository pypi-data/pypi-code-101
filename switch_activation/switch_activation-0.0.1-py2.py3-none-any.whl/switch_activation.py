"""A switch between several activation functions."""
__version__ = "0.0.1"

from typing import List
import torch
import math
from torch import nn

_GC1 = math.sqrt(2 / math.pi)


def _gelu(x):
    return 0.5 * x * (1 + torch.tanh(_GC1 * (x + 0.044715 * x * x * x)))


def _swish(x):
    return x * torch.sigmoid(x)


def _identity(x):
    return x


CALLABLES_BY_NAME = {
    'one': torch.ones_like,
    'relu': nn.functional.relu,
    'tanh': torch.tanh,
    'gelu': _gelu,
    'swish': _swish,
    'sigmoid': torch.sigmoid,
    'identity': _identity,
}


class SwitchActivation(nn.Module):
    _logits: nn.Parameter
    _callables: List[callable] = None

    def __init__(self, activations: List[str]):
        super().__init__()

        self._callables = []

        for name in activations:
            if name in CALLABLES_BY_NAME:
                self._callables.append(CALLABLES_BY_NAME[name])

        # Register the logits
        self._logits = nn.Parameter(torch.tensor([0.0] * len(self._callables)))

        # Distribution used.
        self.gumbel = torch.distributions.Gumbel(0, 1)

        # Register temperature.
        self.register_buffer('temperature', torch.tensor([1.0]))

    @property
    def probs(self) -> torch.Tensor:
        return torch.softmax(self._logits, dim=-1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if not self.training:
            idx = torch.argmax(self._logits, dim=-1)
            return self._callables[idx](x)

        # Compute all the options.
        y = torch.stack([f(x) for f in self._callables], dim=1)
        g = self.gumbel.sample(y.size()[:2]).to(self._logits.device)
        return torch.einsum(
            'ij...,ij->i...',
            y,
            torch.softmax((g + self._logits) / self.temperature[0], dim=-1)
        )
