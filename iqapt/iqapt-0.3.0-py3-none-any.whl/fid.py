import torch
from . import model
from .metric import MultiImageMetric, Union, List
from . import utils
import torch.nn.functional as F
import numpy as np

__all__ = ['FID']


class FID(MultiImageMetric):
    def __init__(self, input_type, eps=1e-6) -> None:
        super().__init__()
        if input_type not in ['image', 'feature']:
            msg = 'input_type should be image or feature, but got {}'.format(
                input_type)
            raise ValueError(msg)

        self.input_type = input_type
        self.eps = eps

        if input_type == 'image':
            self.inception = model.fid.InceptionV3()
            self.inception.eval()

    def calc(
            self, images_a: Union[torch.Tensor, List[torch.Tensor]],
            images_b: Union[torch.Tensor, List[torch.Tensor]]) -> torch.Tensor:
        if self.input_type == 'feature':
            features_a = images_a
            features_b = images_b
        else:
            features_a = self.calc_feature(images_a)
            features_b = self.calc_feature(images_b)

        mu_a = torch.mean(features_a, dim=0)
        mu_b = torch.mean(features_b, dim=0)
        sigma_a = torch.cov(features_a.t())
        sigma_b = torch.cov(features_b.t())
        diff_mu = mu_a - mu_b
        covmean, error = utils.sqrtm_newton_schulz(sigma_a.mm(sigma_b),
                                                   num_iters=100)

        if not torch.isfinite(covmean).all():
            offset = utils.to_device(
                torch.eye(sigma_a.size(0), dtype=sigma_a.dtype) * self.eps,
                utils.get_device(sigma_a))
            covmean, error = utils.sqrtm_newton_schulz(
                (sigma_a + offset).mm(sigma_b + offset), num_iters=100)

        fid = diff_mu.dot(diff_mu) + torch.trace(sigma_a + sigma_b -
                                                 2 * covmean)
        return fid

    def calc_feature(self, images: Union[torch.Tensor, List[torch.Tensor]]):
        if not hasattr(self, 'inception'):
            self.inception = model.fid.InceptionV3()
            self.inception.eval()

        images = [
            F.interpolate(image.unsqueeze(0),
                          size=(299, 299),
                          mode='bilinear',
                          align_corners=False) for image in images
        ]
        images = torch.cat(images, dim=0)
        images = 2 * images - 1
        features = self.inception(images)[0].squeeze(2).squeeze(2)
        return features
