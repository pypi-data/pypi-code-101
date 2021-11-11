import torch
from .metric import SingleImageMetric

__all__ = ['MSE']


class MSE(SingleImageMetric):
    def __init__(self) -> None:
        super().__init__()

    def calc(self, image_a: torch.Tensor,
             image_b: torch.Tensor) -> torch.Tensor:
        return torch.mean((image_a - image_b)**2)
