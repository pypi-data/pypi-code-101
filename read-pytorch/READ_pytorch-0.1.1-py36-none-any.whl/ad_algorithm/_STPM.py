""" Implementation of the SPTM algorithm for anomaly localization and detection
This method is proposed in the paper:
    'Student-Teacher Feature Pyramid Matching for Unsupervised Anomaly Detection implementation'
Following implementation is adapted form the repository:
    https://github.com/hcw-00/STPM_anomaly_detection
Original copyright below, modifications by TCL Corporate Research(HK) Co., Ltd, Copyright 2021.
"""
# Copyright [yyyy] [name of copyright owner]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import torch
from torch import nn
import torch.nn.functional as F
import sys
import os
import gc
import platform
import time
import logging
import torch.optim as optim
import numpy as np
from tqdm import tqdm
from scipy.ndimage import gaussian_filter
from READ_pytorch.optimizer import RAdam
from READ_pytorch.scheduler import CosineAnnealingScheduler
import READ_pytorch.backbones as models
from READ_pytorch.utils import set_logger, AverageMeter, EarlyStop
from READ_pytorch.utils import remove_dataparallel
from READ_pytorch.utils import estimate_thred_with_fpr


backbones = ['resnet18', 'resnet34', 'resnet50', 'resnet101', 'resnet152', 'resnext50',
            'resnext101','wide_resnet50', 'wide_resnet101', 'se_resnext50', 'se_resnext101', 'se_resnet18', 'se_resnet34', 'se_resnet50', 'se_resnet101', 'se_resnet152']


##############################################################
####################### STPM Model ###########################
##############################################################

class STPM(object):
    def __init__(self, backbone='resnet18', layers=[1,2,3]):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.backbone = backbone
        assert (self.backbone in backbones), f"Only support backbones in {backbones}."
        # Define teacher and student model
        self.teacher = getattr(models, self.backbone)(pretrained=True)
        self.student = getattr(models, self.backbone)(pretrained=False)
        # Set to cpu or cuda device 
        self.teacher = self.teacher.to(self.device)
        # self.teacher.eval()
        self.student = self.student.to(self.device)

        for param in self.teacher.parameters():
            param.requires_grad = False

        for param in self.student.parameters():
            param.requires_grad = True
        
        self.layers = layers
        # Initialize parameters
        self.val_max_as = None
        self.val_min_as = None
        self.seg_thres = None
        self.cls_thres = None
    
    def train(self, 
                train_data,
                save_path,
                val_data=None,
                expect_fpr=0.01,
                **kwargs):
        batch_size = kwargs.get("batch_size", 32)
        lr = kwargs.get("lr", 0.0001)
        epochs = kwargs.get("epochs", 300)
        optimizer_name = kwargs.get("optimizer", 'adam')
        scheduler_name = kwargs.get("scheduler", 'step')
        validation_ratio = kwargs.get("validation_ratio", 0.2)
        logger = logging.getLogger('READ.Train')
        set_logger(os.path.join(save_path, 'train.log'), 'READ')
        loader_kwargs = {'num_workers': 8, 'pin_memory': True} if (torch.cuda.is_available() and platform.system() == 'Linux') else {}
        if val_data == None:
            img_nums = len(train_data)
            valid_num = int(img_nums * validation_ratio)
            train_num = img_nums - valid_num
            train_data, val_data = torch.utils.data.random_split(train_data, [train_num, valid_num])
        
        train_dataloader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True, **loader_kwargs)
        val_dataloader = torch.utils.data.DataLoader(val_data, batch_size=int(4*batch_size), shuffle=True, **loader_kwargs)

        if (optimizer_name == 'adam') or (optimizer_name == 'Adam'):
            optimizer = optim.Adam(self.student.parameters(), lr=lr, weight_decay=0.00001, amsgrad=True)
        elif (optimizer_name == 'sgd') or (optimizer_name == 'SGD'):
            optimizer = optim.SGD(self.student.parameters(), lr=lr, momentum=0.9, nesterov=True)
        elif (optimizer_name == 'radam') or (optimizer_name == 'RAdam'):
            optimizer = RAdam(self.student.parameters(), lr=lr, weight_decay=0.00001)
        elif (optimizer_name == 'adabelief') or (optimizer_name == 'Adabelief'):
            optimizer = AdaBelief(self.student.parameters(), lr=lr, weight_decay=0.00001, eps=1e-16, betas=(0.9,0.999), weight_decouple = True, rectify = True)
        else:
            raise ValueError('Could Only Support optimizer in [Adam, SGD].')
        
        if scheduler_name == 'step':
            scheduler = optim.lr_scheduler.StepLR(optimizer, int(0.1 * epochs), 0.5)
        elif scheduler_name == 'cosine':
            scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs, eta_min=1e-8)
        # criterion = torch.nn.MSELoss(reduction='sum')
        x_ref, _, _ = iter(train_dataloader).next()
        assert (len(x_ref.shape) == 4), 'input tensor should be 4-dim.'
        assert (x_ref.shape[2] == x_ref.shape[3]), 'Input height should be equal to width.'

        start_time = time.time()
        epoch_time = AverageMeter()
        save_lowest = os.path.join(save_path, 'model_lowest_loss.pt')
        early_stop = EarlyStop(patience=int(0.1*epochs) if int(0.1*epochs) > 20 else 20, 
                                save_name=save_lowest)

        # print('Dataset size : Train set - {}'.format(dataset_sizes['train']))
        for epoch in range(epochs):
            losses = AverageMeter()
            self.teacher.eval()
            self.student.train()
            for (data) in tqdm(train_dataloader, '| training epoch %s |' % (epoch+1)):
                if type(data) != torch.Tensor:
                    if type(data) == list or type(data) == tuple:
                        data = data[0]
                        if type(data) != torch.Tensor:
                            raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                    else:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')

                data = data.to(self.device)
                optimizer.zero_grad()
                with torch.set_grad_enabled(True):
                    
                    features_t = self.teacher(data)
                    features_s = self.student(data)

                    # get loss using features.
                    loss = self._cal_loss(features_s, features_t)
                    losses.update(loss.item(), data.size(0))
                    loss.backward()
                    optimizer.step()

            logger.info('Train Epoch: {} L2_Loss: {:.6f}'.format(
                epoch, losses.avg))
            # sys.exit()
            # scheduler.step()

            val_loss = self._val(val_dataloader)
            if (early_stop(val_loss, self.student, optimizer)):
                break

            epoch_time.update(time.time() - start_time)
            start_time = time.time()

        self.est_thres(val_data, expect_fpr=expect_fpr, batch_size=batch_size)


    def _val(self, val_loader):
        self.student.eval()
        self.teacher.eval()
        
        losses = AverageMeter()
        #Start to evaluate
        for (data) in tqdm(val_loader):
            if type(data) != torch.Tensor:
                if type(data) == list or type(data) == tuple:
                    data = data[0]
                    if type(data) != torch.Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
            data = data.to(self.device)
            # generator mask
            img_size = data.size(-1)

            with torch.no_grad():
                features_t = self.teacher(data)
                features_s = self.student(data)

            loss = self._cal_loss(features_t, features_s)
            losses.update(loss.item(), data.size(0))

        return losses.avg

    def load_weights(self, ckpt_path):
        if torch.cuda.is_available():
            params = torch.load(ckpt_path)
        else:
            params = torch.load(ckpt_path, map_location='cpu')
        try:
            params = params["state_dict"]
        except:
            params = params

        self.student.load_state_dict(remove_dataparallel(params))
        print('Pretrained weights from %s has been loaded.' %ckpt_path)

    def est_thres(self, val_data, expect_fpr=0.01, **kwargs):
        batch_size = kwargs.get("batch_size", 4)
        loader_kwargs = {'num_workers': 8, 'pin_memory': True} if (torch.cuda.is_available() and platform.system() == 'Linux') else {}
        val_dataloader = torch.utils.data.DataLoader(val_data, batch_size=int(4*batch_size), shuffle=False, **loader_kwargs)

        self.student.eval()
        self.teacher.eval()
        
        val_scores = []

        for (data) in tqdm(val_dataloader,'|Estimating Threshold|'):
            if type(data) != torch.Tensor:
                if type(data) == list or type(data) == tuple:
                    data = data[0]
                    if type(data) != torch.Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')

            data = data.to(self.device)
            # cal img_size
            img_size = data.size(-1)

            with torch.no_grad():
                features_t = self.teacher(data)
                features_s = self.student(data)

            score_map = self._cal_score(features_s, features_t, img_size)

            score_map = score_map.squeeze().cpu().numpy()
            if len(score_map.shape) < 3:
                score_map = torch.unsqueeze(score_map, dim=0)
            
            for i in range(score_map.shape[0]):
                score_map[i] = gaussian_filter(score_map[i], sigma=4)
            val_scores.extend(score_map)


        val_scores = np.asarray(val_scores)

        self.val_max_as = val_scores.max()
        self.val_min_as = val_scores.min()
        val_scores = (val_scores - self.val_min_as) / (self.val_max_as - self.val_min_as)
        val_img_scores = val_scores.reshape(val_scores.shape[0], -1).max(axis=1)
        self.seg_thres = estimate_thred_with_fpr(val_scores, expect_fpr=expect_fpr)
        self.cls_thres = estimate_thred_with_fpr(val_img_scores, expect_fpr=expect_fpr)

    def predict(self, test_data, **kwargs):

        self.student.eval()
        self.teacher.eval()

        score = 0
        with torch.no_grad():
            data = test_data.to(self.device)
            # cal img size
            img_size = data.size(-1)

            with torch.no_grad():
                features_t = self.teacher(data)
                features_s = self.student(data)

            score_map = self._cal_score(features_s, features_t, img_size)

        score = score_map.squeeze().cpu().numpy()
        if score.ndim < 3:
            score = np.expand_dims(score, axis=0)
        for i in range(score.shape[0]):
            score[i] = gaussian_filter(score[i], sigma=7)

        if (self.val_max_as is not None) and (self.val_min_as is not None):
            # print('Normalizing!')
            score = (score - self.val_min_as) / (self.val_max_as - self.val_min_as)

        img_score = score.reshape(score.shape[0], -1).max(axis=1)

        return img_score, score


    def _cal_loss(self, tout_list, sout_list):
        '''
        Args:
        tout_list: list of 3 layers' output
        sout_list: list of 3 layers' output

        '''
        criterion = torch.nn.MSELoss(reduction='sum')
        total_loss = 0
        # with torch.set_grad_enabled(True):
        for i in self.layers:
            if i == str('avgpool'):
                i = int(4)
            else:
                i = int(i) - 1
            tout = tout_list[i]
            sout = sout_list[i]
            b, c, h, w = tout.shape
            tout_norm = torch.divide(tout, torch.norm(tout, p=2, dim=1, keepdim=True))
            sout_norm = torch.divide(sout, torch.norm(sout, p=2, dim=1, keepdim=True))
            loss_cache = (0.5/(w*h)) * criterion(sout_norm, tout_norm)
            total_loss += loss_cache
        return total_loss

    def _cal_score(self, tout_list, sout_list, img_size):
        '''
        Args:
        tout_list: list of 3 layers' output
        sout_list: list of 3 layers' output

        '''

        # criterion = torch.nn.MSELoss(reduction='none')
        total_loss = []
        score_map = torch.ones([img_size, img_size])
        for idx, i in enumerate(self.layers):
            if i == str('avgpool'):
                i = int(4)
            else:
                i = int(i) - 1
        # for i in range(len(tout_list)):
            tout = tout_list[i]
            sout = sout_list[i]
            b, c, h, w = tout.shape
            tout_norm = torch.divide(tout, torch.norm(tout, p=2, dim=1, keepdim=True))
            sout_norm = torch.divide(sout, torch.norm(sout, p=2, dim=1, keepdim=True))
            # loss_cache = (0.5) * criterion(sout_norm, tout_norm)
            loss_cache = (0.5) * torch.nn.PairwiseDistance(p=2, keepdim=True)(tout_norm, sout_norm)**2
            # total_loss.append(loss_cache)
            loss_cache = F.interpolate(loss_cache, size=(img_size,img_size),
                                        mode='bilinear', align_corners=False)
            # if idx == 0:
            #     score_map = np.ones([b,c,h,w])
            score_map = score_map.to(loss_cache.device)
            score_map = torch.mul(score_map, loss_cache)

        return score_map



