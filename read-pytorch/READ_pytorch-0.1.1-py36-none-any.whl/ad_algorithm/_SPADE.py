""" Implementation of the SPADE algorithm for anomaly localization and detection
This method is proposed in the paper:
    'Sub-Image Anomaly Detection with Deep Pyramid Correspondences'
Following implementation is adapted form the repository:
    https://github.com/byungjae89/SPADE-pytorch 
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
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import models
from collections import OrderedDict
import numpy as np
from tqdm import tqdm
from scipy.ndimage import gaussian_filter
import gc
import os
import time
import pickle
import platform
import READ_pytorch.backbones as models
from READ_pytorch.utils import estimate_thred_with_fpr

backbones = ['resnet18', 'resnet34', 'resnet50', 'resnet101', 'resnet152', 'resnext50',
            'resnext101','wide_resnet50', 'wide_resnet101', 'se_resnext50', 'se_resnext101', 'se_resnet18', 'se_resnet34', 'se_resnet50', 'se_resnet101', 'se_resnet152']

__all__ = ['SPADE']

class SPADE(object):

    train_outputs = None

    def __init__(self, backbone='wide_resnet50', topk=5):
        super(SPADE, self).__init__()
        # device setup
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.topk = topk
        self.backbone = backbone
        # load model
        self.model = getattr(models, self.backbone)(pretrained=True)
        self.model.to(self.device)
        self.model.eval()
        self.val_max_as = None
        self.val_min_as = None
        self.val_max_is = None
        self.val_min_is = None

    def train(self, 
                train_data,
                save_path,
                expect_fpr=0.01,
                **kwargs):
        '''
        class_name: only for information print, default None
        '''
        batch_size = kwargs.get("batch_size", 32)
        loader_kwargs = {'num_workers': 8, 'pin_memory': True} if (torch.cuda.is_available() and platform.system() == 'Linux') else {}
        train_dataloader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True, **loader_kwargs)
        train_outputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', []), ('avgpool', [])])

        # for (x, _, _) in tqdm(train_dataloader, '| feature extraction | train |' ):
        for (x) in tqdm(train_dataloader, '| feature extraction | train |' ):
            if type(x) != torch.Tensor:
                if type(x) == list or type(x) == tuple:
                    x = x[0]
                    if type(x) != torch.Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
            
            self.train_size = (x.size(-2), x.size(-1))
            # model prediction
            with torch.no_grad():
                x1, x2, x3, x4, avg, _ = self.model(x.to(self.device))
            # get intermediate layer outputs
            for k, v in zip(train_outputs.keys(), [x1.cpu().detach(), x2.cpu().detach(), x3.cpu().detach(), avg.cpu().detach()]):
                train_outputs[k].append(v)
            # initialize hook outputs
            outputs = []
        for k, v in train_outputs.items():
            train_outputs[k] = torch.cat(v, 0)
        self.train_outputs = train_outputs
        torch.cuda.empty_cache()
        self.save_weights(os.path.join(save_path, 'model.pkl'))
        self.est_thres(train_data, expect_fpr=expect_fpr)

    def save_weights(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump([self.train_outputs, self.train_size], f)

    def load_weights(self, filepath):
        print('load train set feature from: %s' % filepath)
        with open(filepath, 'rb') as f:
            self.train_outputs, self.train_size = pickle.load(f)

    def est_thres(self, val_data, expect_fpr=0.01):
        assert self.train_outputs is not None, 'Should train the model or load weights at first.'
        dist_matrix = self._calc_dist_matrix(torch.flatten(self.train_outputs['avgpool'], 1),
                                                torch.flatten(self.train_outputs['avgpool'], 1))
        topk_values, topk_indexes = torch.topk(dist_matrix, k=self.topk + 1, dim=1, largest=False)
        val_img_scores = torch.mean(topk_values[:,1:], 1).cpu().detach().numpy()
        topk_indexes = topk_indexes[:,1:]
        val_score_map_list = []
        for t_idx in tqdm(range(self.train_outputs['avgpool'].shape[0]), '| Estimating threshold |' ):
            score_maps = []
            for layer_name in ['layer1', 'layer2', 'layer3']:  # for each layer

                # construct a gallery of features at all pixel locations of the K nearest neighbors
                topk_feat_map = self.train_outputs[layer_name][topk_indexes[t_idx]]
                test_feat_map = self.train_outputs[layer_name][t_idx:t_idx + 1]
                feat_gallery = topk_feat_map.transpose(3, 1).flatten(0, 2).unsqueeze(-1).unsqueeze(-1)
                # calculate distance matrix
                dist_matrix_list = []

                for d_idx in range(feat_gallery.shape[0] // 100): # TODO: 
                    dist_matrix = torch.pairwise_distance(feat_gallery[d_idx * 100:d_idx * 100 + 100].to(self.device), 
                                                            test_feat_map.to(self.device))
                    dist_matrix_list.append(dist_matrix)

                dist_matrix = torch.cat(dist_matrix_list, 0)

                # k nearest features from the gallery (k=1)
                score_map = torch.min(dist_matrix, dim=0)[0]
                score_map = F.interpolate(score_map.unsqueeze(0).unsqueeze(0), 
                                        size=self.train_size,
                                        mode='bilinear', align_corners=False)
                score_maps.append(score_map)

            # average distance between the features
            score_map = torch.mean(torch.cat(score_maps, 0), dim=0)

            # apply gaussian smoothing on the score map
            score_map = gaussian_filter(score_map.squeeze().cpu().detach().numpy(), sigma=4)
            val_score_map_list.extend(score_map)

        torch.cuda.empty_cache()
        val_scores = np.asarray(val_score_map_list)
        self.val_max_as = val_scores.max()
        self.val_min_as = val_scores.min()
        val_scores = (val_scores - self.val_min_as) / (self.val_max_as - self.val_min_as)
        self.val_max_is = val_img_scores.max()
        self.val_min_is = val_img_scores.min()
        val_img_scores = (val_img_scores - self.val_min_is) / (self.val_max_is - self.val_min_is)
        self.seg_thres = estimate_thred_with_fpr(val_scores, expect_fpr=expect_fpr)
        self.cls_thres = estimate_thred_with_fpr(val_img_scores, expect_fpr=expect_fpr)

    def predict(self, x):
        # model prediction
        if len(x.shape) == 3:
            x = torch.unsqueeze(x, dim=0)
        n, c, h, w = x.shape
        # assert n==1, 'Only work for batch size == 1'# TODO support batch_size > 1:
        test_outputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', []), ('avgpool', [])])

        with torch.no_grad():
            x1, x2, x3, x4, avg, _ = self.model(x.to(self.device))
        # get intermediate layer outputs
        for k, v in zip(test_outputs.keys(), [x1.cpu().detach(), x2.cpu().detach(), x3.cpu().detach(), avg.cpu().detach()]):
            test_outputs[k].append(v)
        # initialize hook outputs
        outputs = []
        for k, v in test_outputs.items():
            test_outputs[k] = torch.cat(v, 0)
        # calculate distance matrix
        dist_matrix = self._calc_dist_matrix(torch.flatten(test_outputs['avgpool'], 1),
                                       torch.flatten(self.train_outputs['avgpool'], 1))
        # select K nearest neighbor and take average
        topk_values, topk_indexes = torch.topk(dist_matrix, k=self.topk, dim=1, largest=False)
        scores = torch.mean(topk_values, 1).cpu().detach().numpy()
        score_map_list = []
        for t_idx in range(test_outputs['avgpool'].shape[0]):
            score_maps = []
            for layer_name in ['layer1', 'layer2', 'layer3']:
                # construct a gallery of features at all pixel locations of the K nearest neighbors
                topk_feat_map = self.train_outputs[layer_name][topk_indexes[t_idx]]
                test_feat_map = test_outputs[layer_name][t_idx:t_idx+1]
                feat_gallery = topk_feat_map.transpose(3, 1).flatten(0, 2).unsqueeze(-1).unsqueeze(-1)
                # calculate distance matrix
                dist_matrix_list = []
                for d_idx in range(feat_gallery.shape[0] // 100):
                    dist_matrix = torch.pairwise_distance(feat_gallery[d_idx * 100:d_idx * 100 + 100].to(self.device), 
                                                            test_feat_map.to(self.device))
                    dist_matrix_list.append(dist_matrix)
                dist_matrix = torch.cat(dist_matrix_list, 0)

                # k nearest features from the gallery (k=1)
                score_map = torch.min(dist_matrix, dim=0)[0]
                score_map = F.interpolate(score_map.unsqueeze(0).unsqueeze(0), size=(h,w),
                                            mode='bilinear', align_corners=False)
                score_maps.append(score_map)

            # average distance between the features
            score_map = torch.mean(torch.cat(score_maps, 0), dim=0)
            score_map_list.append(score_map.cpu().detach().numpy())

        img_score = np.expand_dims(scores,axis=1)
        score = np.vstack(score_map_list)

        if (self.val_max_is is not None) and (self.val_min_is is not None):
            img_score = (img_score - self.val_min_is) / (self.val_max_is - self.val_min_is)
        if (self.val_max_as is not None) and (self.val_min_as is not None):
            score = (score - self.val_min_as) / (self.val_max_as - self.val_min_as)

        torch.cuda.empty_cache()

        return img_score, score

    def _calc_dist_matrix(self, x, y):
        """Calculate Euclidean distance matrix with torch.tensor"""
        n = x.size(0)
        m = y.size(0)
        d = x.size(1)
        x = x.unsqueeze(1).expand(n, m, d)
        y = y.unsqueeze(0).expand(n, m, d)
        dist_matrix = torch.sqrt(torch.pow(x - y, 2).sum(2))
        return dist_matrix

