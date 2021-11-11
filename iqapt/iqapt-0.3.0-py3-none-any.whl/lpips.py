from numpy import uint
import torch
import torch.nn as nn
import os
from . import utils
from .metric import SingleImageMetric
from .model import lpips

__all__ = ['LPIPS']


class LPIPS(SingleImageMetric):
    def __init__(self,
                 input_type,
                 net='vgg16',
                 linear_calibration=True,
                 spatial=False) -> None:
        super().__init__()

        if input_type not in ['image', 'feature']:
            msg = 'input_type should be image or feature, but got {}.'.format(
                input_type)
            raise ValueError(msg)
        else:
            self.input_type = input_type

        self.image_dim = ['C', 'H', 'W']
        self.feature_dim = ['N', 'C', 'H', 'W']
        self.pretrained_net = lpips.models[net]()
        self.channels = lpips.channels[net]
        self.num_layers = len(self.channels)
        self.linear_calibration = linear_calibration
        self.spatial = spatial
        self.model = nn.Module()
        self.scaling_layer = ScalingLayer()

        if linear_calibration == True:
            self.model.lins = []

            for i in range(self.num_layers):
                lin = LinearLayer(self.channels[i])
                self.model.add_module('lin{}'.format(i), lin)
                self.model.lins.append(lin)

            self.model.lins = nn.ModuleList(self.model.lins)

            model_path = os.path.join(os.path.dirname(__file__),
                                      'weight/lpips', '{}.pth'.format(net))
            self.model.load_state_dict(torch.load(model_path,
                                                  map_location='cpu'),
                                       strict=False)

    def calc(self, img_a: torch.Tensor, img_b: torch.Tensor):
        if self.input_type == 'image':
            feat_a = self.calc_feature(img_a)
            feat_b = self.calc_feature(img_b)
        else:
            feat_a = img_a
            feat_b = img_b

        diff = [(feat_a[i] - feat_b[i])**2 for i in range(self.num_layers)]

        if self.linear_calibration == True:
            res = [self.model.lins[l](diff[l]) for l in range(self.num_layers)]
        else:
            res = [
                diff[l].sum(dim=1, keepdim=True)
                for l in range(self.num_layers)
            ]

        if self.spatial == True:
            res = [
                utils.upsample(res[l], out_size=img_a.shape[2:])
                for l in range(self.num_layers)
            ]
        else:
            res = [
                utils.spatial_average(res[l], keepdim=True)
                for l in range(self.num_layers)
            ]

        val = res[0]

        for l in range(1, self.num_layers):
            val += res[l]

        val = val.squeeze()

        return val

    def calc_feature(self, image: torch.Tensor):
        image = image.unsqueeze(0)
        image = 2 * image - 1
        image = self.scaling_layer(image)
        features = self.pretrained_net(image)
        features = [utils.normalize_tensor(feature) for feature in features]
        return features


class ScalingLayer(nn.Module):
    def __init__(self):
        super().__init__()
        self.shift = nn.Parameter(
            torch.tensor([-.030, -.088, -.188]).reshape(1, 3, 1, 1))
        self.scale = nn.Parameter(
            torch.tensor([.458, .448, .450]).reshape(1, 3, 1, 1))

    def forward(self, input_tensor):
        return (input_tensor - self.shift) / self.scale


class LinearLayer(nn.Module):
    def __init__(self, in_channels, out_channels=1):
        super().__init__()
        layers = [nn.Identity()]
        layers += [
            nn.Conv2d(in_channels,
                      out_channels,
                      kernel_size=1,
                      stride=1,
                      padding=0,
                      bias=False)
        ]
        self.model = nn.Sequential(*layers)

    def forward(self, input_tensor):
        return self.model(input_tensor)


# based on https://github.com/richzhang/PerceptualSimilarity
# Copyright (c) 2018, Richard Zhang, Phillip Isola, Alexei A. Efros, Eli Shechtman, Oliver Wang
# All rights reserved.
