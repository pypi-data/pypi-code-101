""" Implementation of the USTAD algorithm for anomaly localization and detection
This method is proposed in the paper:
    Uninformed Students: Student–Teacher Anomaly Detection with Discriminative Latent Embeddings
Following implementation is adapted form the repository:
    https://github.com/denguir/student-teacher-anomaly-detection 
Fast Dense Feature Extraction code gently borrowed from
    https://github.com/erezposner/Fast_Dense_Feature_Extraction/blob/master/pytorch/FDFE.py
"""
import torch
from torch import nn
import torch.optim as optim
from torchvision import models
import numpy as np
from tqdm import tqdm
from einops import rearrange, reduce
import random
import os
import time
import logging
import platform
from scipy.ndimage import gaussian_filter
from adabelief_pytorch import AdaBelief
from READ_pytorch.optimizer import RAdam
from READ_pytorch.utils import set_logger, AverageMeter, EarlyStop
from READ_pytorch.utils import remove_dataparallel
from READ_pytorch.utils import estimate_thred_with_fpr
from READ_pytorch.scheduler import CosineAnnealingScheduler
from torch.nn import functional as F
from torch.utils import model_zoo


pretrained_settings = {
    'teacher_17': {
        'imagenet': {
            'url': 'https://gitee.com/zc08174024/read/attach_files/629135/download/teacher_net_17-d678c047.pt',
            'input_space': 'RGB',
            'input_size': [3, 17, 17],
            'input_range': [0, 1],
            'mean': [0.485, 0.456, 0.406],
            'std': [0.229, 0.224, 0.225],
            'patch_size': 17
        }
    },
    'teacher_33': {
        'imagenet': {
            'url': 'https://gitee.com/zc08174024/read/attach_files/629136/download/teacher_net_33-896f39f6.pt',
            'input_space': 'RGB',
            'input_size': [3, 33, 33],
            'input_range': [0, 1],
            'mean': [0.485, 0.456, 0.406],
            'std': [0.229, 0.224, 0.225],
            'patch_size': 33
        }
    },
    'teacher_65': {
        'imagenet': {
            'url': 'https://gitee.com/zc08174024/read/attach_files/629137/download/teacher_net_65-3cb6666c.pt',
            'input_space': 'RGB',
            'input_size': [3, 65, 65],
            'input_range': [0, 1],
            'mean': [0.485, 0.456, 0.406],
            'std': [0.229, 0.224, 0.225],
            'patch_size': 65
        }
    },
}

class AnomalyResnet18(nn.Module):
    ''' Resnet18 extended for anomaly classification:
        Designed to tell wether an object presents
        anomalies or not'''
    def __init__(self):
        super(AnomalyResnet18, self).__init__()
        self.resnet18 = self._get_resnet18_backbone()
        self.linear = nn.Linear(512, 2)
        self.softmax = nn.Softmax(dim=1)
    
    def _get_resnet18_backbone(self):
        resnet18 = models.resnet18(pretrained=True)
        resnet18 = nn.Sequential(*list(resnet18.children())[:-1])
        return resnet18

    def forward(self, x):
        x = self.resnet18(x)
        x = x.view(-1, 512)
        y = self.softmax(self.linear(x))
        return y

class AnomalyNet65(nn.Module):
    '''Patch-based CNN for anomaly detection
       Designed to work with patches of size 65x65
    '''
    def __init__(self):
        super(AnomalyNet65, self).__init__()
        self.patch_size = 65
        self.conv1 = nn.Conv2d(3, 128, 5, 1)
        self.conv2 = nn.Conv2d(128, 128, 5, 1)
        self.conv3 = nn.Conv2d(128, 256, 5, 1)
        self.conv4 = nn.Conv2d(256, 256, 4, 1)
        self.conv5 = nn.Conv2d(256, 128, 1, 1)
        self.dropout_2d = nn.Dropout2d(0.2)
        self.decode = nn.Linear(128, 512)
        self.dropout = nn.Dropout(0.2)
        self.max_pool = nn.MaxPool2d(2, 2)
        self.l_relu = nn.LeakyReLU(5e-3)

    def forward(self, x):
        x = self.l_relu(self.conv1(x))
        x = self.max_pool(x)
        x = self.l_relu(self.conv2(x))
        x = self.max_pool(x)
        x = self.l_relu(self.conv3(x))
        x = self.max_pool(x)
        x = self.l_relu(self.conv4(x))
        x = self.l_relu(self.conv5(x))
        x = self.dropout_2d(x)
        x = x.view(-1, 128)
        x = self.l_relu(self.decode(x))
        x = self.dropout(x)
        return x


class AnomalyNet33(nn.Module):
    '''Patch-based CNN for anomaly detection
       Designed to work with patches of size 65x65
    '''
    def __init__(self):
        super(AnomalyNet33, self).__init__()
        self.patch_size = 33
        self.conv1 = nn.Conv2d(3, 128, 3, 1)
        self.conv2 = nn.Conv2d(128, 256, 5, 1)
        self.conv3 = nn.Conv2d(256, 256, 3, 1)
        self.conv4 = nn.Conv2d(256, 256, 3, 1)
        self.conv5 = nn.Conv2d(256, 128, 1, 1)
        self.dropout_2d = nn.Dropout2d(0.2)
        self.decode = nn.Linear(128, 512)
        self.dropout = nn.Dropout(0.2)
        self.max_pool = nn.MaxPool2d(2, 2)
        self.l_relu = nn.LeakyReLU(5e-3)

    def forward(self, x):
        x = self.l_relu(self.conv1(x))
        x = self.max_pool(x)
        x = self.l_relu(self.conv2(x))
        x = self.max_pool(x)
        x = self.l_relu(self.conv3(x))
        x = self.l_relu(self.conv4(x))
        x = self.l_relu(self.conv5(x))
        x = self.dropout_2d(x)
        x = x.view(-1, 128)
        x = self.l_relu(self.decode(x))
        x = self.dropout(x)
        return x


class AnomalyNet17(nn.Module):
    '''Patch-based CNN for anomaly detection
       Designed to work with patches of size 65x65
    '''
    def __init__(self):
        super(AnomalyNet17, self).__init__()
        self.patch_size = 17
        self.conv1 = nn.Conv2d(3, 128, 3, 1)
        self.conv2 = nn.Conv2d(128, 256, 5, 1)
        self.conv3 = nn.Conv2d(256, 256, 3, 1)
        self.conv4 = nn.Conv2d(256, 256, 3, 1)
        self.conv5 = nn.Conv2d(256, 128, 1, 1)
        self.dropout_2d = nn.Dropout2d(0.2)
        self.decode = nn.Linear(128, 512)
        self.dropout = nn.Dropout(0.2)
        self.max_pool = nn.MaxPool2d(2, 2)
        self.l_relu = nn.LeakyReLU(5e-3)

    def forward(self, x):
        x = self.l_relu(self.conv1(x))
        # x = self.max_pool(x)
        x = self.l_relu(self.conv2(x))
        x = self.max_pool(x)
        x = self.l_relu(self.conv3(x))
        x = self.l_relu(self.conv4(x))
        x = self.l_relu(self.conv5(x))
        x = self.dropout_2d(x)
        x = x.view(-1, 128)
        x = self.l_relu(self.decode(x))
        x = self.dropout(x)
        return x


class multiPoolPrepare(nn.Module):
    def __init__(self, patchY, patchX):
        super(multiPoolPrepare, self).__init__()
        pady = patchY - 1
        padx = patchX - 1

        self.pad_top = np.ceil(pady / 2).astype(int)
        self.pad_bottom = np.floor(pady / 2).astype(int)
        self.pad_left = np.ceil(padx / 2).astype(int)
        self.pad_right = np.floor(padx / 2).astype(int)

    def forward(self, x):
        y = F.pad(x, [self.pad_left, self.pad_right, self.pad_top, self.pad_bottom], value=0)
        return y


class unwrapPrepare(nn.Module):
    def __init__(self):
        super(unwrapPrepare, self).__init__()

    def forward(self, x):
        x_ = F.pad(x, [0, -1, 0, -1], value=0)
        y = x_.contiguous().view(x_.shape[0], -1)
        y = y.transpose(0, 1)
        return y.contiguous()

class unwrapPool(nn.Module):
    def __init__(self, outChans, curImgW, curImgH, dW, dH):
        super(unwrapPool, self).__init__()
        self.outChans = int(outChans)
        self.curImgW = int(curImgW)
        self.curImgH = int(curImgH)
        self.dW = int(dW)
        self.dH = int(dH)

    def forward(self, x, ):
        y = x.view((self.outChans, self.curImgW, self.curImgH, self.dH, self.dW, -1))
        y = y.transpose(2, 3)

        return y.contiguous()


class multiMaxPooling(nn.Module):
    def __init__(self, kW, kH, dW, dH):
        super(multiMaxPooling, self).__init__()
        layers = []
        self.padd = []
        for i in range(0, dH):
            for j in range(0, dW):
                self.padd.append((-j, -i))
                layers.append(nn.MaxPool2d(kernel_size=(kW, kH), stride=(dW, dH)))
        self.max_layers = nn.ModuleList(layers)
        self.s = dH

    def forward(self, x):

        hh = []
        ww = []
        res = []

        for i in range(0, len(self.max_layers)):
            pad_left, pad_top = self.padd[i]
            _x = F.pad(x, [pad_left, pad_left, pad_top, pad_top], value=0)
            _x = self.max_layers[i](_x)
            h, w = _x.size()[2], _x.size()[3]
            hh.append(h)
            ww.append(w)
            res.append(_x)
        max_h, max_w = np.max(hh), np.max(ww)
        for i in range(0, len(self.max_layers)):
            _x = res[i]
            h, w = _x.size()[2], _x.size()[3]
            pad_top = np.floor((max_h - h) / 2).astype(int)
            pad_bottom = np.ceil((max_h - h) / 2).astype(int)
            pad_left = np.floor((max_w - w) / 2).astype(int)
            pad_right = np.ceil((max_w - w) / 2).astype(int)
            _x = F.pad(_x, [pad_left, pad_right, pad_top, pad_bottom], value=0)
            res[i] = _x
        return torch.cat(res, 0)

class multiConv(nn.Module):
    def __init__(self, nInputPlane, nOutputPlane, kW, kH, dW, dH):
        super(multiConv, self).__init__()
        layers = []
        self.padd = []
        for i in range(0, dH):
            for j in range(0, dW):
                self.padd.append((-j, -i))
                torch.manual_seed(10)
                torch.cuda.manual_seed(10)
                a = nn.Conv2d(nInputPlane, nOutputPlane, kernel_size=(kW, kH), stride=(dW, dH), padding=0)
                layers.append(a)
        self.max_layers = nn.ModuleList(layers)
        self.s = dW

    def forward(self, x):
        hh = []
        ww = []
        res = []

        for i in range(0, len(self.max_layers)):
            pad_left, pad_top = self.padd[i]
            _x = F.pad(x, [pad_left, pad_left, pad_top, pad_top], value=0)
            _x = self.max_layers[i](_x)
            h, w = _x.size()[2], _x.size()[3]
            hh.append(h)
            ww.append(w)
            res.append(_x)
        max_h, max_w = np.max(hh), np.max(ww)
        for i in range(0, len(self.max_layers)):
            _x = res[i]
            h, w = _x.size()[2], _x.size()[3]
            pad_top = np.ceil((max_h - h) / 2).astype(int)
            pad_bottom = np.floor((max_h - h) / 2).astype(int)
            pad_left = np.ceil((max_w - w) / 2).astype(int)
            pad_right = np.floor((max_w - w) / 2).astype(int)
            _x = F.pad(_x, [pad_left, pad_right, pad_top, pad_bottom], value=0)
            res[i] = _x
        return torch.cat(res, 0)

class FDFEAnomalyNet65(nn.Module):
    '''CNN that uses Fast Dense Feature Extraction to
       efficiently apply a patch-based CNN <base_net> on a whole image
    '''
    def __init__(self, base_net, pH, pW, imH, imW, sLs=[2,2,2]):
        super(FDFEAnomalyNet65, self).__init__()
        assert (base_net.patch_size == 65)
        self.imH = imH
        self.imW = imW
        sL1, sL2, sL3 = sLs
        self.multiPoolPrepare = multiPoolPrepare(pH, pW)
        self.conv1 = base_net.conv1
        self.multiMaxPooling1 = multiMaxPooling(sL1, sL1, sL1, sL1)
        self.conv2 = base_net.conv2
        self.multiMaxPooling2 = multiMaxPooling(sL2, sL2, sL2, sL2)
        self.conv3 = base_net.conv3
        self.multiMaxPooling3 = multiMaxPooling(sL3, sL3, sL3, sL3)
        self.conv4 = base_net.conv4
        self.conv5 = base_net.conv5

        self.outChans = self.conv5.out_channels
        self.unwrapPrepare = unwrapPrepare()
        self.unwrapPool3 = unwrapPool(self.outChans, imH / (sL1 * sL2 * sL3), imW / (sL1 * sL2 * sL3), sL3, sL3)
        self.unwrapPool2 = unwrapPool(self.outChans, imH / (sL1 * sL2), imW / (sL1 * sL2), sL2, sL2)
        self.unwrapPool1 = unwrapPool(self.outChans, imH / sL1, imW / sL1, sL1, sL1)

        self.decode = base_net.decode
        self.decodeChans = self.decode.out_features
        self.l_relu = base_net.l_relu

    def forward(self, x):
        x = self.multiPoolPrepare(x)

        x = self.l_relu(self.conv1(x))
        x = self.multiMaxPooling1(x)

        x = self.l_relu(self.conv2(x))
        x = self.multiMaxPooling2(x)

        x = self.l_relu(self.conv3(x))
        x = self.multiMaxPooling3(x)

        x = self.l_relu(self.conv4(x))
        x = self.l_relu(self.conv5(x))

        x = self.unwrapPrepare(x)
        x = self.unwrapPool3(x)
        x = self.unwrapPool2(x)
        x = self.unwrapPool1(x)

        y = x.view(self.outChans, self.imH, self.imW, -1)
        y = y.permute(3, 1, 2, 0)
        y = self.l_relu(self.decode(y))
        return y


class FDFEAnomalyNet33(nn.Module):
    '''CNN that uses Fast Dense Feature Extraction to
       efficiently apply a patch-based CNN <base_net> on a whole image
    '''
    def __init__(self, base_net, pH, pW, imH, imW, sLs=[2,2]):
        super(FDFEAnomalyNet33, self).__init__()
        assert (base_net.patch_size == 33)
        self.imH = imH
        self.imW = imW
        sL1, sL2 = sLs
        self.multiPoolPrepare = multiPoolPrepare(pH, pW)
        self.conv1 = base_net.conv1
        self.multiMaxPooling1 = multiMaxPooling(sL1, sL1, sL1, sL1)
        self.conv2 = base_net.conv2
        self.multiMaxPooling2 = multiMaxPooling(sL2, sL2, sL2, sL2)
        self.conv3 = base_net.conv3
        self.conv4 = base_net.conv4
        self.conv5 = base_net.conv5

        self.outChans = self.conv5.out_channels
        self.unwrapPrepare = unwrapPrepare()
        self.unwrapPool2 = unwrapPool(self.outChans, imH / (sL1 * sL2), imW / (sL1 * sL2), sL2, sL2)
        self.unwrapPool1 = unwrapPool(self.outChans, imH / sL1, imW / sL1, sL1, sL1)

        self.decode = base_net.decode
        self.decodeChans = self.decode.out_features
        self.l_relu = base_net.l_relu

    def forward(self, x):
        x = self.multiPoolPrepare(x)

        x = self.l_relu(self.conv1(x))
        x = self.multiMaxPooling1(x)

        x = self.l_relu(self.conv2(x))
        x = self.multiMaxPooling2(x)

        x = self.l_relu(self.conv3(x))
        x = self.l_relu(self.conv4(x))
        x = self.l_relu(self.conv5(x))

        x = self.unwrapPrepare(x)
        x = self.unwrapPool2(x)
        x = self.unwrapPool1(x)

        y = x.view(self.outChans, self.imH, self.imW, -1)
        y = y.permute(3, 1, 2, 0)
        y = self.l_relu(self.decode(y))
        return y


class FDFEAnomalyNet17(nn.Module):
    '''CNN that uses Fast Dense Feature Extraction to
       efficiently apply a patch-based CNN <base_net> on a whole image
    '''
    def __init__(self, base_net, pH, pW, imH, imW, sLs=2):
        super(FDFEAnomalyNet17, self).__init__()
        assert (base_net.patch_size == 17)
        self.imH = imH
        self.imW = imW
        sL1 = sLs
        self.multiPoolPrepare = multiPoolPrepare(pH, pW)
        self.conv1 = base_net.conv1
        self.multiMaxPooling1 = multiMaxPooling(sL1, sL1, sL1, sL1)
        self.conv2 = base_net.conv2
        self.conv3 = base_net.conv3
        self.conv4 = base_net.conv4
        self.conv5 = base_net.conv5

        self.outChans = self.conv5.out_channels
        self.unwrapPrepare = unwrapPrepare()
        self.unwrapPool1 = unwrapPool(self.outChans, imH / sL1, imW / sL1, sL1, sL1)

        self.decode = base_net.decode
        self.decodeChans = self.decode.out_features
        self.l_relu = base_net.l_relu

    def forward(self, x):
        x = self.multiPoolPrepare(x)

        x = self.l_relu(self.conv1(x))
        x = self.l_relu(self.conv2(x))
        x = self.multiMaxPooling1(x)
        x = self.l_relu(self.conv3(x))
        x = self.l_relu(self.conv4(x))
        x = self.l_relu(self.conv5(x))

        # x = self._unwrapPrepare(x)

        x = self.unwrapPrepare(x)
        x = self.unwrapPool1(x)

        y = x.view(self.outChans, self.imH, self.imW, -1)
        y = y.permute(3, 1, 2, 0)
        y = self.l_relu(self.decode(y))
        return y


##############################################################
####################### USTAD Model ###########################
##############################################################

class USTAD(object):
    def __init__(self, **kwargs):
        self.n_students = kwargs.get("n_students", 3)
        self.patch_size = kwargs.get("patch_size", [65, 33, 17])
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.val_max_as = None
        self.val_min_as = None
        self.seg_thres = None
        self.cls_thres = None
        if (type(self.patch_size) != list) and (type(self.patch_size) != tuple):
            raise ValueError('patch_size should be a list or tuple.')
        self.teachers = [eval('AnomalyNet%s'%i)() for i in self.patch_size]
        self.s_weights = {}
        for idx, psize in enumerate(self.patch_size):
            teacher = self.teachers[idx]
            teacher.load_state_dict(remove_dataparallel(model_zoo.load_url(pretrained_settings[f'teacher_{psize}']['imagenet']['url'])))
            teacher.eval().to(self.device)
            self.teachers[idx] = teacher
            print(f'Loading of teacher_{psize} succesful.')
            for jdx in range(self.n_students):
                self.s_weights['student_%s_%s_weights'%(psize, jdx)] = None
            self.s_weights['cali_parameters_%s'%(psize)] = None
        self.s_weights['img_height'] = None
        self.s_weights['img_width'] = None

    def train(self, 
            train_data, 
            save_path, 
            val_data=None, 
            expect_fpr=0.01,
            **kwargs):
        lr = kwargs.get("lr", 1e-4)
        epochs = kwargs.get("epochs", 100)
        optimizer_name = kwargs.get("optimizer", 'adam')
        # scheduler_name = kwargs.get("scheduler", 'step')
        batch_size = kwargs.get("batch_size", 1)
        validation_ratio = kwargs.get("validation_ratio", 0.2)
        cali_data = kwargs.get("cali_data", None)
        logger = logging.getLogger('READ.Train')
        set_logger(os.path.join(save_path, 'train.log'), 'READ')
        save_lowest = os.path.join(save_path, 'model_lowest_loss.pt')
        loader_kwargs = {'num_workers': 8, 'pin_memory': True} if (torch.cuda.is_available() and platform.system() == 'Linux') else {}
        if val_data == None:
            img_nums = len(train_data)
            valid_num = int(img_nums * validation_ratio)
            train_num = img_nums - valid_num
            train_data, val_data = torch.utils.data.random_split(train_data, [train_num, valid_num])
        if cali_data == None:
            cali_data = train_data
        
        train_dataloader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True, **loader_kwargs)
        val_dataloader = torch.utils.data.DataLoader(val_data, batch_size=batch_size, shuffle=True, **loader_kwargs)
        cali_dataloader = torch.utils.data.DataLoader(cali_data, batch_size=batch_size, shuffle=False, **loader_kwargs)

        # get the h,w of the input images 
        x_ref = iter(train_dataloader).next()
        if type(x_ref) != torch.Tensor:
            if type(x_ref) == list or type(x_ref) == tuple:
                x_ref = x_ref[0]
                if type(x_ref) != torch.Tensor:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
            else:
                raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
        n_ref, c_ref, h_ref, w_ref = x_ref.shape
        self.img_height = h_ref
        self.s_weights['img_height'] = h_ref
        self.img_width = w_ref
        self.s_weights['img_width'] = w_ref
        
        # if scheduler_name == 'step':
        #     scheduler = optim.lr_scheduler.StepLR(optimizer, int(0.1 * epochs), 0.5)
        # elif scheduler_name == 'cosine':
        #     scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs, eta_min=1e-8)
        # else:
        #     raise ValueError('Could Only Support scheduler in [step, cosine].')

        # Train student networks for each patch size
        for idx, psize in enumerate(self.patch_size):
            logger.info(f'Start to train students of patch size {psize}.')
            teacher = self.teachers[idx]
            teacher = eval('FDFEAnomalyNet%s'%psize)(base_net=teacher, 
                                                    pH=psize, 
                                                    pW=psize, 
                                                    imH=self.img_height, 
                                                    imW=self.img_width)
            teacher.eval().to(self.device)
            logger.info(f'teacher_{psize} has been converted to FDFE mode.')

            # Compute incremental mean and var over traininig set
            # because the whole training set takes too much memory space 
            with torch.no_grad():
                t_mu, t_var, N = 0, 0, 0
                for i, data in tqdm(enumerate(train_dataloader)):
                    if type(data) != torch.Tensor:
                        if type(data) == list or type(data) == tuple:
                            data = data[0]
                            if type(data) != torch.Tensor:
                                raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                        else:
                            raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                    inputs = data.to(self.device)
                    t_out = teacher(inputs)
                    t_mu, t_var, N = self._increment_mean_and_var(t_mu, t_var, N, t_out)
            

            #Define Students networks
            locals()['students_%s_hat'%psize] = [eval('AnomalyNet%s'%psize)() for i in range(self.n_students)]
            locals()['students_%s'%psize] = [eval('FDFEAnomalyNet%s'%psize)(base_net=student, 
                                                        pH=psize, 
                                                        pW=psize, 
                                                        imH=self.img_height, 
                                                        imW=self.img_width)
                        for student in locals()['students_%s_hat'%psize]]
            locals()['students_%s'%psize] = [student.to(self.device) for student in locals()['students_%s'%psize]]

            # Define optimizer and scheduler
            if (optimizer_name == 'adam') or (optimizer_name == 'Adam'):
                optimizers = [optim.Adam(student.parameters(), lr=lr, weight_decay=1e-5) for student in locals()['students_%s'%psize]]
            elif (optimizer_name == 'sgd') or (optimizer_name == 'SGD'):
                optimizers = [optim.SGD(student.parameters(), lr=lr, momentum=0.9, nesterov=True) for student in locals()['students_%s'%psize]]
            elif (optimizer_name == 'radam') or (optimizer_name == 'RAdam'):
                optimizers = [RAdam(student.parameters(), lr=lr, weight_decay=0.00001) for student in locals()['students_%s'%psize]]
            elif (optimizer_name == 'adabelief') or (optimizer_name == 'Adabelief'):
                optimizers = [AdaBelief(student.parameters(), lr=lr, weight_decay=0.00001, eps=1e-16, betas=(0.9,0.999), weight_decouple = True, rectify = True) for student in locals()['students_%s'%psize]]
            else:
                raise ValueError('Could Only Support optimizer in [Adam, SGD].')

            for jdx, student in enumerate(locals()['students_%s'%psize]):
                logger.info(f'Training Student {jdx} on anomaly-free dataset ...')
                min_running_loss = np.inf
                student_loss = nn.MSELoss()
                for epoch in range(epochs):
                    running_loss = 0.0

                    for idx, data in tqdm(enumerate(train_dataloader)):
                        if type(data) != torch.Tensor:
                            if type(data) == list or type(data) == tuple:
                                data = data[0]
                                if type(data) != torch.Tensor:
                                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                            else:
                                raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                        # zero the parameters gradient
                        optimizers[jdx].zero_grad() 

                        # forward pass
                        inputs = data.to(self.device)
                        with torch.no_grad():
                            targets = (teacher(inputs) - t_mu) / torch.sqrt(t_var)

                        outputs = student(inputs)
                        loss = student_loss(targets, outputs)

                        # backward pass
                        loss.backward()
                        optimizers[jdx].step()
                        running_loss += loss.item()

                        # print stats
                        if idx % 10 == 9:
                            logger.info(f"Epoch {epoch+1}, iter {idx+1} \t loss: {running_loss}")
                            
                            if running_loss < min_running_loss:
                                logger.info(f"Loss decreased: {min_running_loss} -> {running_loss}.")
                                logger.info(f"Storing weights of student_{psize}_{jdx}.")
                                # torch.save(student.state_dict(), model_name)
                                self.s_weights['student_%s_%s_weights'%(psize, jdx)] = student.state_dict()

                            min_running_loss = min(min_running_loss, running_loss)
                            running_loss = 0.0
                torch.cuda.empty_cache()

            # After training n students for a patch size, do a calibration
            self.s_weights['cali_parameters_%s'%(psize)] = self._calibrate(teacher, locals()['students_%s'%psize], cali_dataloader, psize, logger)

        # Save weights and cali parameters
        torch.save(self.s_weights, save_lowest)
        self.est_thres(val_data, expect_fpr=expect_fpr)

    def _calibrate(self, teacher, students, cali_dataloader, patch_size, logger):
        with torch.no_grad():
            logger.info(f'Callibrating teacher on defect free dataset at patch size {patch_size}.')
            t_mu, t_var, t_N = 0, 0, 0
            for i, data in tqdm(enumerate(cali_dataloader)):
                if type(data) != torch.Tensor:
                    if type(data) == list or type(data) == tuple:
                        data = data[0]
                        if type(data) != torch.Tensor:
                            raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                    else:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                inputs = data.to(self.device)
                t_out = teacher(inputs)
                t_mu, t_var, t_N = self._increment_mean_and_var(t_mu, t_var, t_N, t_out)

            logger.info(f'Callibrating scoring parameters on defect free dataset at patch size {patch_size}.')
            max_err, max_var = 0, 0
            mu_err, var_err, N_err = 0, 0, 0
            mu_var, var_var, N_var = 0, 0, 0
            for i, batch in tqdm(enumerate(cali_dataloader)):
                if type(data) != torch.Tensor:
                    if type(data) == list or type(data) == tuple:
                        data = data[0]
                        if type(data) != torch.Tensor:
                            raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                    else:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                inputs = data.to(self.device)
                t_out = (teacher(inputs) - t_mu) / torch.sqrt(t_var)
                s_out = torch.stack([student(inputs) for student in students], dim=1)
                # s_out = predict_student(students, inputs) # MC dropout
                s_err = self._get_error_map(s_out, t_out)
                s_var = self._get_variance_map(s_out)
                mu_err, var_err, N_err = self._increment_mean_and_var(mu_err, var_err, N_err, s_err)
                mu_var, var_var, N_var = self._increment_mean_and_var(mu_var, var_var, N_var, s_var)

                max_err = max(max_err, torch.max(s_err))
                max_var = max(max_var, torch.max(s_var))
        return [t_mu, t_var, t_N, mu_err, var_err, N_err, mu_var, var_var, N_var, max_err, max_var]

    def est_thres(self, val_data, expect_fpr=0.01, **kwargs):
        batch_size = kwargs.get("batch_size", 1)

        loader_kwargs = {'num_workers': 8, 'pin_memory': True} if (torch.cuda.is_available() and platform.system() == 'Linux') else {}
        val_dataloader = torch.utils.data.DataLoader(val_data, batch_size=batch_size, shuffle=False, **loader_kwargs)

        try:
            img_height = self.img_height
            img_width = self.img_width
        except AttributeError:
            img_height = self.s_weights['img_height']
            img_width = self.s_weights['img_width']

        multi_score_map = []
        for idx, psize in enumerate(self.patch_size):
            print(f'Start to inference at patch size {psize}.')
            teacher = self.teachers[idx]
            teacher = eval('FDFEAnomalyNet%s'%psize)(base_net=teacher, 
                                                    pH=psize, 
                                                    pW=psize, 
                                                    imH=img_height, 
                                                    imW=img_width)
            teacher.eval().to(self.device)
            print(f'teacher_{psize} has been converted to FDFE mode.')

            #Define Students networks and Load weights
            locals()['students_%s_hat'%psize] = [eval('AnomalyNet%s'%psize)() for i in range(self.n_students)]
            for sdx in range(self.n_students):
                locals()['students_%s_hat'%psize][sdx].load_state_dict(self.s_weights['student_%s_%s_weights'%(psize, sdx)])
            locals()['students_%s'%psize] = [eval('FDFEAnomalyNet%s'%psize)(base_net=student, 
                                                        pH=psize, 
                                                        pW=psize, 
                                                        imH=img_height, 
                                                        imW=img_width)
                        for student in locals()['students_%s_hat'%psize]]
            locals()['students_%s'%psize] = [student.eval().to(self.device) for student in locals()['students_%s'%psize]]

            t_mu, t_var, t_N, mu_err, var_err, N_err, mu_var, var_var, N_var, max_err, max_var = self.s_weights['cali_parameters_%s'%(psize)]
            score_map_list = []
            for (data) in tqdm(val_dataloader,'|Estimating Threshold|'):
                if type(data) != torch.Tensor:
                    if type(data) == list or type(data) == tuple:
                        data = data[0]
                        if type(data) != torch.Tensor:
                            raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                    else:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                
                with torch.no_grad():
                    inputs = data.to(self.device)
                    t_out = (teacher(inputs) - t_mu) / torch.sqrt(t_var)
                    s_out = torch.stack([student(inputs) for student in locals()['students_%s'%psize]], dim=1)

                    s_err = self._get_error_map(s_out, t_out)
                    s_var = self._get_variance_map(s_out)
                    score_map = (s_err - mu_err) / torch.sqrt(var_err) + (s_var - mu_var) / torch.sqrt(var_var)
                    score_map = rearrange(score_map, 'b h w -> h (b w)').cpu()
                    score_map_list.append(score_map)
            
            multi_score_map.append(np.stack(score_map_list, axis=0))
        multi_score_map = np.stack(multi_score_map, axis=0)
        val_scores = reduce(multi_score_map, 'id b h w -> b h w', 'mean')
        print(val_scores.shape)
        self.val_max_as = val_scores.max()
        self.val_min_as = val_scores.min()

        val_scores = (val_scores - self.val_min_as) / (self.val_max_as - self.val_min_as)
        val_img_scores = val_scores.reshape(val_scores.shape[0], -1).max(axis=1)
        self.seg_thres = estimate_thred_with_fpr(val_scores, expect_fpr=expect_fpr)
        self.cls_thres = estimate_thred_with_fpr(val_img_scores, expect_fpr=expect_fpr)

    def load_weights(self, ckpt_path):
        if torch.cuda.is_available():
            params = torch.load(ckpt_path)
        else:
            params = torch.load(ckpt_path, map_location='cpu')
        self.s_weights = params
        print('Pretrained weights from %s has been loaded.' %ckpt_path)

    def predict(self, test_data, **kwargs):
        try:
            img_height = self.img_height
            img_width = self.img_width
        except AttributeError:
            img_height = self.s_weights['img_height']
            img_width = self.s_weights['img_width']
        
        multi_score_map = []
        for idx, psize in enumerate(self.patch_size):
            # print(f'Start to inference at patch size {psize}.')
            teacher = self.teachers[idx]
            teacher = eval('FDFEAnomalyNet%s'%psize)(base_net=teacher, 
                                                    pH=psize, 
                                                    pW=psize, 
                                                    imH=img_height, 
                                                    imW=img_width)
            teacher.eval().to(self.device)
            # print(f'teacher_{psize} has been converted to FDFE mode.')

            #Define Students networks and Load weights
            locals()['students_%s_hat'%psize] = [eval('AnomalyNet%s'%psize)() for i in range(self.n_students)]
            for sdx in range(self.n_students):
                locals()['students_%s_hat'%psize][sdx].load_state_dict(self.s_weights['student_%s_%s_weights'%(psize, sdx)])
            locals()['students_%s'%psize] = [eval('FDFEAnomalyNet%s'%psize)(base_net=student, 
                                                        pH=psize, 
                                                        pW=psize, 
                                                        imH=img_height, 
                                                        imW=img_width)
                        for student in locals()['students_%s_hat'%psize]]
            locals()['students_%s'%psize] = [student.eval().to(self.device) for student in locals()['students_%s'%psize]]

            t_mu, t_var, t_N, mu_err, var_err, N_err, mu_var, var_var, N_var, max_err, max_var = self.s_weights['cali_parameters_%s'%(psize)]
            with torch.no_grad():
                inputs = test_data.to(self.device)
                t_out = (teacher(inputs) - t_mu) / torch.sqrt(t_var)
                s_out = torch.stack([student(inputs) for student in locals()['students_%s'%psize]], dim=1)

                s_err = self._get_error_map(s_out, t_out)
                s_var = self._get_variance_map(s_out)
                score_map = (s_err - mu_err) / torch.sqrt(var_err) + (s_var - mu_var) / torch.sqrt(var_var)
                # score_map = rearrange(score_map, 'b h w -> h (b w)').cpu()
                score_map = score_map.cpu()

            multi_score_map.append(score_map)
        
        multi_score_map = np.stack(multi_score_map, axis=0)
        mean_score_map = reduce(multi_score_map, 'id b h w -> b h w', 'mean')
        score = np.zeros(mean_score_map.shape)
        for i in range(mean_score_map.shape[0]):
            score[i] = np.array(gaussian_filter(mean_score_map[i], sigma=7))

        if (self.val_max_as is not None) and (self.val_min_as is not None):
            # print('Normalizing!')
            score = (score - self.val_min_as) / (self.val_max_as - self.val_min_as)

        img_score = score.reshape(score.shape[0], -1).max(axis=1)

        return img_score, score

    def _increment_mean_and_var(self, mu_N, var_N, N, batch):
        '''Increment value of mean and variance based on
        current mean, var and new batch
        '''
        # batch: (batch, h, w, vector)
        B = batch.size()[0] # batch size
        # we want a descriptor vector -> mean over batch and pixels
        mu_B = torch.mean(batch, dim=[0,1,2])
        S_B = B * torch.var(batch, dim=[0,1,2], unbiased=False) 
        S_N = N * var_N
        mu_NB = N/(N + B) * mu_N + B/(N + B) * mu_B
        S_NB = S_N + S_B + B * mu_B**2 + N * mu_N**2 - (N + B) * mu_NB**2
        var_NB = S_NB / (N+B)
        return mu_NB, var_NB, N + B

    def _get_error_map(self, students_pred, teacher_pred):
        mu_students = reduce(students_pred, 'b id h w vec -> b h w vec', 'mean')
        err = reduce((mu_students - teacher_pred)**2, 'b h w vec -> b h w', 'sum')
        return err

    def _get_variance_map(self, students_pred):
        sse = reduce(students_pred**2, 'b id h w vec -> b id h w', 'sum')
        msse = reduce(sse, 'b id h w -> b h w', 'mean')
        mu_students = reduce(students_pred, 'b id h w vec -> b h w vec', 'mean')
        var = msse - reduce(mu_students**2, 'b h w vec -> b h w', 'sum')
        return var