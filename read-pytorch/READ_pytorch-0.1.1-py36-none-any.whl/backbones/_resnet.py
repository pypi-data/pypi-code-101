import torchvision.models as torchmodel
import torch.nn as nn
from torch import Tensor
import torch

__all__ = ['resnet18', 'resnet34', 'resnet50', 'resnet101',
           'resnet152', 'resnext50', 'resnext101',
           'wide_resnet50', 'wide_resnet101']

class resnet18(nn.Module):
    def __init__(self, pretrained=True):
        super(resnet18, self).__init__()
        model = torchmodel.resnet18(pretrained=pretrained)
        modules = list(model.children())[:4] 
        self.stem = nn.Sequential(*modules)
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        self.avgpool = model.avgpool
        self.fc = model.fc
    
    def forward(self, x: Tensor) -> Tensor:
        x = self.stem(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.avgpool(x)
        avg = x.clone()
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x1, x2, x3, x4, avg, x

class resnet34(nn.Module):
    def __init__(self, pretrained=True):
        super(resnet34, self).__init__()
        model = torchmodel.resnet34(pretrained=pretrained)
        modules = list(model.children())[:4] 
        self.stem = nn.Sequential(*modules)
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        self.avgpool = model.avgpool
        self.fc = model.fc

    def forward(self, x: Tensor) -> Tensor:
        x = self.stem(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.avgpool(x)
        avg = x.clone()
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x1, x2, x3, x4, avg, x

class resnet50(nn.Module):
    def __init__(self, pretrained=True):
        super(resnet50, self).__init__()
        model = torchmodel.resnet50(pretrained=pretrained)
        modules = list(model.children())[:4] 
        self.stem = nn.Sequential(*modules)
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        self.avgpool = model.avgpool
        self.fc = model.fc
    
    def forward(self, x: Tensor) -> Tensor:
        x = self.stem(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.avgpool(x)
        avg = x.clone()
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x1, x2, x3, x4, avg, x

class resnet101(nn.Module):
    def __init__(self, pretrained=True):
        super(resnet101, self).__init__()
        model = torchmodel.resnet101(pretrained=pretrained)
        modules = list(model.children())[:4] 
        self.stem = nn.Sequential(*modules)
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        self.avgpool = model.avgpool
        self.fc = model.fc
    
    def forward(self, x: Tensor) -> Tensor:
        x = self.stem(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.avgpool(x)
        avg = x.clone()
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x1, x2, x3, x4, avg, x

class resnet152(nn.Module):
    def __init__(self, pretrained=True):
        super(resnet152, self).__init__()
        model = torchmodel.resnet152(pretrained=pretrained)
        modules = list(model.children())[:4] 
        self.stem = nn.Sequential(*modules)
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        self.avgpool = model.avgpool
        self.fc = model.fc
    
    def forward(self, x: Tensor) -> Tensor:
        x = self.stem(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.avgpool(x)
        avg = x.clone()
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x1, x2, x3, x4, avg, x

class resnext50(nn.Module):
    def __init__(self, pretrained=True):
        super(resnext50, self).__init__()
        model = torchmodel.resnext50_32x4d(pretrained=pretrained)
        modules = list(model.children())[:4] 
        self.stem = nn.Sequential(*modules)
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        self.avgpool = model.avgpool
        self.fc = model.fc
    
    def forward(self, x: Tensor) -> Tensor:
        x = self.stem(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.avgpool(x)
        avg = x.clone()
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x1, x2, x3, x4, avg, x

class resnext101(nn.Module):
    def __init__(self, pretrained=True):
        super(resnext101, self).__init__()
        model = torchmodel.resnext101_32x8d(pretrained=pretrained)
        modules = list(model.children())[:4] 
        self.stem = nn.Sequential(*modules)
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        self.avgpool = model.avgpool
        self.fc = model.fc
    
    def forward(self, x: Tensor) -> Tensor:
        x = self.stem(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.avgpool(x)
        avg = x.clone()
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x1, x2, x3, x4, avg, x

class wide_resnet50(nn.Module):
    def __init__(self, pretrained=True):
        super(wide_resnet50, self).__init__()
        model = torchmodel.wide_resnet50_2(pretrained=pretrained)
        modules = list(model.children())[:4] 
        self.stem = nn.Sequential(*modules)
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        self.avgpool = model.avgpool
        self.fc = model.fc
    
    def forward(self, x: Tensor) -> Tensor:
        x = self.stem(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.avgpool(x)
        avg = x.clone()
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x1, x2, x3, x4, avg, x

class wide_resnet101(nn.Module):
    def __init__(self, pretrained=True):
        super(wide_resnet101, self).__init__()
        model = torchmodel.wide_resnet101_2(pretrained=pretrained)
        modules = list(model.children())[:4] 
        self.stem = nn.Sequential(*modules)
        self.layer1 = model.layer1
        self.layer2 = model.layer2
        self.layer3 = model.layer3
        self.layer4 = model.layer4
        self.avgpool = model.avgpool
        self.fc = model.fc
    
    def forward(self, x: Tensor) -> Tensor:
        x = self.stem(x)
        x = self.layer1(x)
        x1 = x.clone()
        x = self.layer2(x)
        x2 = x.clone()
        x = self.layer3(x)
        x3 = x.clone()
        x = self.layer4(x)
        x4 = x.clone()
        x = self.avgpool(x)
        avg = x.clone()
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x1, x2, x3, x4, avg, x

