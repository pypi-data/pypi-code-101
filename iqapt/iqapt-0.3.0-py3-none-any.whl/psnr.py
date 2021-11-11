import torch
from . import utils
from .metric import SingleImageMetric
from .mse import MSE

__all__ = ['PSNR']


class PSNR(SingleImageMetric):
    def __init__(self, peak=1.0, convert_to_gray=False) -> None:
        super().__init__()
        self.peak = peak
        self.convert_to_gray = convert_to_gray
        self.mse = MSE()

    def calc(self, image_a: torch.Tensor,
             image_b: torch.Tensor) -> torch.Tensor:
        C, H, W = image_a.size()
        soft_factor = 0.1**32

        if self.convert_to_gray == True:
            if C == 1:
                mse = self.mse(image_a, image_b)[0]
            elif C == 3:
                image_a_y = utils.image_colorspace.rgb_to_gray(image_a)
                image_b_y = utils.image_colorspace.rgb_to_gray(image_b)
                mse = self.mse(image_a_y, image_b_y)[0]
            else:
                msg = 'the channel of img({}) should be 1(Gray) or 3(RGB).'.format(
                    C)
                raise ValueError(msg)
        else:
            mse = self.mse(image_a, image_b)[0]

        return 10 * torch.log10(self.peak**2 / (mse + soft_factor))
