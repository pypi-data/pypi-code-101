""" Implementation of the PaDiM algorithm for anomaly localization and detection
This method is proposed in the paper:
    'Anomaly localization by modeling perceptual features'
Following implementation is adapted form the repository:
    https://github.com/xiahaifeng1995/FAVAE-anomaly-detection-localization-master
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

import os
import platform
import torch
import torch.nn as nn
import torch.nn.functional as F
# from torch.utils.data import DataLoader
from torchvision.models import wide_resnet50_2, resnet18
# from torchvision import models
from collections import OrderedDict
# import numpy as np
# if torch.cuda.is_available():
#     print('Using Cuda Mode')
#     import cupy as np
#     cache = np.fft.config.get_plan_cache()
# else:
#     print('Using Cpu Mode')
#     import numpy as np
from tqdm import tqdm
from scipy.ndimage import gaussian_filter
import gc
import time
from random import sample
import pickle
from READ_pytorch.utils import estimate_thred_with_fpr
# from scipy.spatial.distance import mahalanobis
# from sklearn.covariance import LedoitWolf

##############################################################
####################### PaDiM Model ###########################
##############################################################

class PaDiM(object):
    # train_outputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', [])])
    # test_outputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', [])])
    train_outputs_cache = None
    train_outputs = None
    def __init__(self, backbone='wide_resnet50_2'):
        global np, cache
        if torch.cuda.is_available():
            print('Using Cuda Mode')
            import cupy as np
            cache = np.fft.config.get_plan_cache()
        else:
            print('Using Cpu Mode')
            import numpy as np
        self.backbone = backbone
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        if self.backbone == 'resnet18':
            self.model = resnet18(pretrained=True, progress=True)
            t_d = 448
            d = 100
        elif self.backbone == 'wide_resnet50_2':
            self.model = wide_resnet50_2(pretrained=True, progress=True)
            t_d = 1792
            d = 550
        else:
            raise ValueError('This backbone has not been supported yet.')
        self.model.to(self.device)
        self.model.eval()
        self.idx = torch.tensor(sample(range(0, t_d), d)) #random choice features

    def train(self, 
                train_data,
                save_path,
                expect_fpr=0.01,
                **kwargs):
        batch_size = kwargs.get("batch_size", 32)
        loader_kwargs = {'num_workers': 8, 'pin_memory': True} if (torch.cuda.is_available() and platform.system() == 'Linux') else {}
        train_dataloader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True, **loader_kwargs)
        train_outputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', [])])
        outputs = []
        def hook(module, input, output):
            outputs.append(output.cpu().detach())
        self.model.layer1[-1].register_forward_hook(hook)
        self.model.layer2[-1].register_forward_hook(hook)
        self.model.layer3[-1].register_forward_hook(hook)
        # for (x, _, _) in tqdm(train_dataloader, '| feature extraction | train |'):
        for (x) in tqdm(train_dataloader, '| feature extraction | train |'):
            if type(x) != torch.Tensor:
                if type(x) == list or type(x) == tuple:
                    x = x[0]
                    if type(x) != torch.Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
            with torch.no_grad():
                _ = self.model(x.to(self.device))
            # get intermediate layer outputs
            for k, v in zip(train_outputs.keys(), outputs):
                train_outputs[k].append(v.cpu().detach())
            # initialize hook outputs
            outputs = []
        for k, v in train_outputs.items():
            train_outputs[k] = torch.cat(v, 0)
        self.train_outputs_cache = train_outputs
        # Embedding concat
        embedding_vectors = train_outputs['layer1']
        for layer_name in ['layer2', 'layer3']:
            embedding_vectors = self._embedding_concat(embedding_vectors, train_outputs[layer_name])

        # randomly select 100(resnet18)/550(wide_resnet_2) dimension
        embedding_vectors = torch.index_select(embedding_vectors, 1, self.idx)
        # calculate multivariate Gaussian distribution
        B, C, H, W = embedding_vectors.size()
        embedding_vectors = embedding_vectors.view(B, C, H * W)
        mean = torch.mean(embedding_vectors, dim=0).numpy()
        cov = np.array(torch.zeros(C, C, H * W).numpy())
        I = np.identity(C)
        for i in tqdm(range(H * W),'| feature calculation |'):
            # cov[:, :, i] = LedoitWolf().fit(embedding_vectors[:, :, i].numpy()).covariance_
            # cov[:, :, i] = np.cov(embedding_vectors[:, :, i].numpy(), rowvar=False) + 0.01 * I
            cov[:, :, i] = np.cov(np.array(embedding_vectors[:, :, i].numpy()), rowvar=False) + 0.01 * I

        # save learned distribution
        if torch.cuda.is_available():
            cache.clear()
            cov = np.asnumpy(cov)
            # cov = np.array(cov)
        self.train_outputs = [mean, cov]
        torch.cuda.empty_cache()

        self.save_weights(os.path.join(save_path, 'model.pkl'))
        self.est_thres(val_data=train_data, expect_fpr=expect_fpr)

    def save_weights(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump([self.train_outputs_cache, self.train_outputs], f)

    def load_weights(self, filepath):
        print('load train set feature from: %s' % filepath)
        with open(filepath, 'rb') as f:
            # self.train_outputs = pickle.load(f)
            loaded_features = pickle.load(f)
        self.train_outputs_cache = loaded_features[0]
        self.train_outputs = loaded_features[1]

    def est_thres(self, val_data, expect_fpr=0.01):
        assert self.train_outputs_cache is not None, 'Should train the model or load weights at first.'
        data,_,_ = val_data[0]
        img_size = data.size(2)
        # Embedding concat
        embedding_vectors = self.train_outputs_cache['layer1']
        for layer_name in ['layer2', 'layer3']:
            embedding_vectors = self._embedding_concat(embedding_vectors, self.train_outputs_cache[layer_name])

        # randomly select 100 dimension
        embedding_vectors = torch.index_select(embedding_vectors, 1, self.idx)
        # calculate distance matrix
        B, C, H, W = embedding_vectors.size()
        embedding_vectors = np.array(embedding_vectors.view(B, C, H * W).detach().numpy())
        dist_list = []
        for i in tqdm(range(H * W),'| Estimating Threshold |'):
            mean = np.array(self.train_outputs[0][:, i])
            conv_inv = np.linalg.inv(np.array(self.train_outputs[1][:, :, i]))
            dist = [self._mahalanobis(sample[:, i], mean, conv_inv) for sample in embedding_vectors]
            dist_list.append(np.expand_dims(np.array(dist), axis=0))
        dist_list = np.vstack(dist_list).transpose(1, 0).reshape(B, H, W)
        # dist_list = np.vstack(dist_list).transpose(1, 0).reshape(B, H, W)
        if torch.cuda.is_available():
            cache.clear()
            dist_list = np.asnumpy(dist_list)
            # dist_list = np.array(dist_list)
        # upsample
        dist_list = torch.tensor(dist_list)
        score_map = F.interpolate(dist_list.unsqueeze(1), size=img_size, mode='bilinear',
                                  align_corners=False).squeeze()
        if len(score_map.shape) == 2:
            score_map = torch.unsqueeze(score_map, dim=0)

        score_map_filtered = np.zeros(score_map.shape)
        for i in range(score_map.shape[0]):
            score_map_filtered[i] = np.array(gaussian_filter(score_map[i].numpy(), 
                                                    sigma=4))

        self.val_max_as = score_map_filtered.max()
        self.val_min_as = score_map_filtered.min()
        
        val_scores = (score_map_filtered - self.val_min_as) / (self.val_max_as - self.val_min_as)
        val_img_scores = val_scores.reshape(val_scores.shape[0], -1).max(axis=1)
        self.seg_thres = estimate_thred_with_fpr(val_scores, expect_fpr=expect_fpr)
        self.cls_thres = estimate_thred_with_fpr(val_img_scores, expect_fpr=expect_fpr)
        torch.cuda.empty_cache()

    def predict(self, x):
        # model prediction
        test_outputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', [])])
        outputs = []
        def hook(module, input, output):
            outputs.append(output.cpu().detach())
        self.model.layer1[-1].register_forward_hook(hook)
        self.model.layer2[-1].register_forward_hook(hook)
        self.model.layer3[-1].register_forward_hook(hook)
        with torch.no_grad():
            _ = self.model(x.to(self.device))
        # get intermediate layer outputs
        for k, v in zip(test_outputs.keys(), outputs):
            test_outputs[k].append(v.cpu().detach())
        # initialize hook outputs
        outputs = []
        for k, v in test_outputs.items():
            test_outputs[k] = torch.cat(v, 0)
        # Embedding concat
        embedding_vectors = test_outputs['layer1']
        for layer_name in ['layer2', 'layer3']:
            embedding_vectors = self._embedding_concat(embedding_vectors, test_outputs[layer_name])

        # randomly select 100 dimension
        embedding_vectors = torch.index_select(embedding_vectors, 1, self.idx)

        # calculate distance matrix
        B, C, H, W = embedding_vectors.size()
        embedding_vectors = np.array(embedding_vectors.view(B, C, H * W).detach().numpy())
        dist_list = []
        for i in range(H * W):
            mean = np.array(self.train_outputs[0][:, i])
            conv_inv = np.linalg.inv(np.array(self.train_outputs[1][:, :, i]))
            dist = [self._mahalanobis(sample[:, i], mean, conv_inv) for sample in embedding_vectors]
            # print(dist)
            # dist = np.array(dist)
            # print(dist.shape)
            dist_list.append(np.expand_dims(np.array(dist), axis=0))
        # print(np.vstack(dist_list).shape)
        dist_list = np.vstack(dist_list).transpose(1, 0).reshape(B, H, W)
        if torch.cuda.is_available():
            cache.clear()
            dist_list = np.asnumpy(dist_list)
            # dist_list = np.array(dist_list)
        # upsample
        dist_list = torch.tensor(dist_list)
        score_map = F.interpolate(dist_list.unsqueeze(1), size=x.size(2), mode='bilinear',
                                  align_corners=False).squeeze()
        if len(score_map.shape) == 2:
            score_map = torch.unsqueeze(score_map, dim=0)

        score_map_filtered = np.zeros(score_map.shape)
        for i in range(score_map.shape[0]):
            # print(type(score_map_filtered[i]))
            # print(type(np.array(score_map[i].numpy())))
            # print(type(gaussian_filter(np.array(score_map[i].numpy()), 
            #                                         sigma=4)))
            score_map_filtered[i] = np.array(gaussian_filter(score_map[i].numpy(), 
                                                    sigma=4))
        # Normalization
        # max_score = score_map_filtered.max()
        # min_score = score_map_filtered.min()
        # scores = (score_map_filtered - min_score) / (max_score - min_score)
        scores = (score_map_filtered - self.val_min_as) / (self.val_max_as - self.val_min_as)
    
        # calculate image-level ROC AUC score
        img_scores = scores.reshape(scores.shape[0], -1).max(axis=1)

        if torch.cuda.is_available():
            img_scores = np.asnumpy(img_scores)
            scores = np.asnumpy(scores)

        # return img_scores, score_map.numpy()
        return img_scores, scores

    def _embedding_concat(self, x, y):
        B, C1, H1, W1 = x.size()
        _, C2, H2, W2 = y.size()
        s = int(H1 / H2)
        x = F.unfold(x, kernel_size=s, dilation=1, stride=s)
        x = x.view(B, C1, -1, H2, W2)
        z = torch.zeros(B, C1 + C2, x.size(2), H2, W2)
        for i in range(x.size(2)):
            z[:, :, i, :, :] = torch.cat((x[:, :, i, :, :], y), 1)
        z = z.view(B, -1, H2 * W2)
        z = F.fold(z, kernel_size=s, output_size=(H1, W1), stride=s)

        return z

    def _reset_train_features(self):
        self.train_outputs = None
        self.__init__(self.backbone)
        torch.cuda.empty_cache()


    def _validate_vector(self, u, dtype=None):
        # XXX Is order='c' really necessary?
        u = np.asarray(u, dtype=dtype, order='c').squeeze()
        # Ensure values such as u=1 and u=[1] still return 1-D arrays.
        u = np.atleast_1d(u)
        if u.ndim > 1:
            raise ValueError("Input vector should be 1-D.")
        return u

    def _mahalanobis(self, u, v, VI):
        """
        Compute the Mahalanobis distance between two 1-D arrays.

        Parameters
        ----------
        u : (N,) array_like
            Input array.
        v : (N,) array_like
            Input array.
        VI : ndarray
            The inverse of the covariance matrix.

        Returns
        -------
        mahalanobis : double
            The Mahalanobis distance between vectors `u` and `v`.
        """
        u = self._validate_vector(u)
        v = self._validate_vector(v)
        VI = np.atleast_2d(VI)
        delta = u - v
        m = np.dot(np.dot(delta, VI), delta)
        return np.sqrt(m)