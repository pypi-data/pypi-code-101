import timm.models as timmmodels
import torch.nn as nn
from torch import Tensor
import torch
import torch.nn.functional as F

__all__ = ['se_resnext50', 'se_resnext101', 'se_resnet18', 'se_resnet34', 'se_resnet50', 'se_resnet101', 'se_resnet152']

class se_resnet18(nn.Module):
    def __init__(self, pretrained=True):
        super(se_resnet18, self).__init__()
        model = timmmodels.senet.legacy_seresnet18(pretrained=pretrained)
        self.layer0 = model.layer0
        self.pool0 = model.pool0
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        # self.avgpool = model.avgpool
        # self.fc = model.fc
        self.global_pool = model.global_pool
        self.last_linear = model.last_linear
        self.drop_rate = model.drop_rate

    def forward(self, x: Tensor) -> Tensor:
        x = self.layer0(x)
        x = self.pool0(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.global_pool(x)
        avg = x.clone()
        if self.drop_rate > 0.:
            x = F.dropout(x, p=self.drop_rate, training=self.training)
        x = self.last_linear(x)

        return x1, x2, x3, x4, avg, x

class se_resnet34(nn.Module):
    def __init__(self, pretrained=True):
        super(se_resnet34, self).__init__()
        model = timmmodels.senet.legacy_seresnet34(pretrained=pretrained)
        self.layer0 = model.layer0
        self.pool0 = model.pool0
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        # self.avgpool = model.avgpool
        # self.fc = model.fc
        self.global_pool = model.global_pool
        self.last_linear = model.last_linear
        self.drop_rate = model.drop_rate

    def forward(self, x: Tensor) -> Tensor:
        x = self.layer0(x)
        x = self.pool0(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.global_pool(x)
        avg = x.clone()
        if self.drop_rate > 0.:
            x = F.dropout(x, p=self.drop_rate, training=self.training)
        x = self.last_linear(x)

        return x1, x2, x3, x4, avg, x

class se_resnet50(nn.Module):
    def __init__(self, pretrained=True):
        super(se_resnet50, self).__init__()
        model = timmmodels.senet.legacy_seresnet50(pretrained=pretrained)
        self.layer0 = model.layer0
        self.pool0 = model.pool0
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        # self.avgpool = model.avgpool
        # self.fc = model.fc
        self.global_pool = model.global_pool
        self.last_linear = model.last_linear
        self.drop_rate = model.drop_rate

    def forward(self, x: Tensor) -> Tensor:
        x = self.layer0(x)
        x = self.pool0(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.global_pool(x)
        avg = x.clone()
        if self.drop_rate > 0.:
            x = F.dropout(x, p=self.drop_rate, training=self.training)
        x = self.last_linear(x)

        return x1, x2, x3, x4, avg, x

class se_resnet101(nn.Module):
    def __init__(self, pretrained=True):
        super(se_resnet101, self).__init__()
        model = timmmodels.senet.legacy_seresnet101(pretrained=pretrained)
        self.layer0 = model.layer0
        self.pool0 = model.pool0
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        # self.avgpool = model.avgpool
        # self.fc = model.fc
        self.global_pool = model.global_pool
        self.last_linear = model.last_linear
        self.drop_rate = model.drop_rate

    def forward(self, x: Tensor) -> Tensor:
        x = self.layer0(x)
        x = self.pool0(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.global_pool(x)
        avg = x.clone()
        if self.drop_rate > 0.:
            x = F.dropout(x, p=self.drop_rate, training=self.training)
        x = self.last_linear(x)

        return x1, x2, x3, x4, avg, x

class se_resnet152(nn.Module):
    def __init__(self, pretrained=True):
        super(se_resnet152, self).__init__()
        model = timmmodels.senet.legacy_seresnet152(pretrained=pretrained)
        self.layer0 = model.layer0
        self.pool0 = model.pool0
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        # self.avgpool = model.avgpool
        # self.fc = model.fc
        self.global_pool = model.global_pool
        self.last_linear = model.last_linear
        self.drop_rate = model.drop_rate

    def forward(self, x: Tensor) -> Tensor:
        x = self.layer0(x)
        x = self.pool0(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.global_pool(x)
        avg = x.clone()
        if self.drop_rate > 0.:
            x = F.dropout(x, p=self.drop_rate, training=self.training)
        x = self.last_linear(x)

        return x1, x2, x3, x4, avg, x

class se_resnext50(nn.Module):
    def __init__(self, pretrained=True):
        super(se_resnext50, self).__init__()
        model = timmmodels.senet.legacy_seresnext50_32x4d(pretrained=pretrained)
        self.layer0 = model.layer0
        self.pool0 = model.pool0
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        # self.avgpool = model.avgpool
        # self.fc = model.fc
        self.global_pool = model.global_pool
        self.last_linear = model.last_linear
        self.drop_rate = model.drop_rate

    def forward(self, x: Tensor) -> Tensor:
        x = self.layer0(x)
        x = self.pool0(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.global_pool(x)
        avg = x.clone()
        if self.drop_rate > 0.:
            x = F.dropout(x, p=self.drop_rate, training=self.training)
        x = self.last_linear(x)

        return x1, x2, x3, x4, avg, x

class se_resnext101(nn.Module):
    def __init__(self, pretrained=True):
        super(se_resnext101, self).__init__()
        model = timmmodels.senet.legacy_seresnext101_32x4d(pretrained=pretrained)
        self.layer0 = model.layer0
        self.pool0 = model.pool0
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        # self.avgpool = model.avgpool
        # self.fc = model.fc
        self.global_pool = model.global_pool
        self.last_linear = model.last_linear
        self.drop_rate = model.drop_rate

    def forward(self, x: Tensor) -> Tensor:
        x = self.layer0(x)
        x = self.pool0(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.global_pool(x)
        avg = x.clone()
        if self.drop_rate > 0.:
            x = F.dropout(x, p=self.drop_rate, training=self.training)
        x = self.last_linear(x)

        return x1, x2, x3, x4, avg, x

