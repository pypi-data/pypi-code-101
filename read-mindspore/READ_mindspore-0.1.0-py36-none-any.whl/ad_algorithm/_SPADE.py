from mindspore import train
from tqdm import tqdm
import sys
import time
from collections import OrderedDict
from READ_mindspore.backbones import resnet_model_zoo
import mindspore
import cv2
# from mindspore import Tensor
import os
import gc
import mindspore.nn as nn
import mindspore.numpy as msnp
import numpy as np
from mindspore import context
import pickle
import cupy as cp
import scipy
from scipy.ndimage import gaussian_filter
from READ_mindspore.utils import estimate_thred_with_fpr

backbones = ['resnet18', 'resnet34', 'resnet50', 'resnet101', 'resnet152', 'resnext50',
            'resnext101','wide_resnet50', 'wide_resnet101', 'se_resnext50', 'se_resnext101', 'se_resnet18', 'se_resnet34', 'se_resnet50', 'se_resnet101', 'se_resnet152']

__all__ = ['SPADE']


class SPADE(object):

    train_outputs = None

    def __init__(self, backbone='resnet50', topk=5, device='GPU'):
        super(SPADE, self).__init__()
        # device setup
        self.device = device
        context.set_context(mode=context.GRAPH_MODE, device_target=self.device, save_graphs=False)
        self.topk = topk
        self.backbone = backbone
        # load model
        model_zoo = resnet_model_zoo()
        self.model = getattr(model_zoo, self.backbone)(pretrain=True)
        for param in self.model.get_parameters():
            param.requires_grad = False
        
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
        self.model.set_train(False)
        self.model.set_grad(False)
        batch_size = kwargs.get("batch_size", 32)
        train_data = train_data.batch(batch_size)
        train_dataloader = train_data.create_dict_iterator()
        train_outputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', []), ('avgpool', [])])
        for (itr, data) in tqdm(enumerate(train_dataloader), '| feature extraction | train |' ):
            if type(data['data']) != mindspore.Tensor:
                if type(data['data']) == list or type(data['data']) == tuple:
                    data = data[0]
                    if type(data['data']) != mindspore.Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
            data = data['data']
            self.train_size = (data.shape[-2], data.shape[-1])
            x1, x2, x3, x4, avg, _ = self.model(data)
        #     for k, v in zip(train_outputs.keys(), [x1, x2, x3, avg]):
        #         train_outputs[k].append(v)

        # for k, v in train_outputs.items():
        #     train_outputs[k] = (msnp.concatenate(v, 0)).asnumpy()
            if itr == 0:
                train_outputs['layer1'] = np.zeros((1, x1.shape[1],x1.shape[2],x1.shape[3]))
                train_outputs['layer2'] = np.zeros((1, x2.shape[1],x2.shape[2],x2.shape[3]))
                train_outputs['layer3'] = np.zeros((1, x3.shape[1],x3.shape[2],x3.shape[3]))
                train_outputs['avgpool'] = np.zeros((1, avg.shape[1],avg.shape[2],avg.shape[3]))
            for k, v in zip(train_outputs.keys(), [x1, x2, x3, avg]):
                train_outputs[k] = np.vstack((train_outputs[k], v.asnumpy()))

        for k, v in train_outputs.items():
            train_outputs[k] = train_outputs[k][1:]
        
        self.train_outputs = train_outputs
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
        dist_matrix = self._calc_dist_matrix(self.train_outputs['avgpool'].reshape(self.train_outputs['avgpool'].shape[0], -1), self.train_outputs['avgpool'].reshape(self.train_outputs['avgpool'].shape[0], -1))
        topk_values, topk_indexes = topk_np(dist_matrix, K=self.topk + 1, axis=1, largest=False)
        val_img_scores = np.mean(topk_values[:,1:], 1)
        topk_indexes = topk_indexes[:,1:]
        val_score_map_list = []
        for t_idx in tqdm(range(self.train_outputs['avgpool'].shape[0]), '| Estimating threshold |' ):
            score_maps = []
            for layer_name in ['layer1', 'layer2', 'layer3']:  # for each
                topk_feat_map = self.train_outputs[layer_name][topk_indexes[t_idx]]
                test_feat_map = self.train_outputs[layer_name][t_idx:t_idx + 1]
                feat_gallery = topk_feat_map.transpose(0,3,2,1)
                feat_gallery = np.expand_dims(np.expand_dims(feat_gallery.reshape(feat_gallery.shape[0]*feat_gallery.shape[1]*feat_gallery.shape[2],feat_gallery.shape[-1]), axis=-1),axis=-1)

                dist_matrix_list = []

                for d_idx in range(feat_gallery.shape[0] // 100):
                    dist_matrix = cp.linalg.norm(cp.asarray(feat_gallery[d_idx * 100:d_idx * 100 + 100])-cp.asarray(test_feat_map), axis=1)
                    dist_matrix_list.append(dist_matrix)

                dist_matrix = cp.concatenate(dist_matrix_list, 0)
                # k nearest features from the gallery (k=1)
                score_map = cp.asnumpy(cp.min(dist_matrix, axis=0))
                # score_map = np.resize(score_map, self.train_size)
                score_map = cv2.resize(score_map, self.train_size, interpolation=cv2.INTER_LINEAR)
                score_maps.append(score_map)

            # average distance between the features
            score_map = np.mean(np.concatenate(score_maps, 0), axis=0)

            # apply gaussian smoothing on the score map
            score_map = gaussian_filter(score_map, sigma=4)
            val_score_map_list.extend(score_map)

        gc.collect()
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
        # context.set_context(mode=context.GRAPH_MODE, device_target=self.device, save_graphs=False)
        # model prediction
        if len(x.shape) == 3:
            x = msnp.expand_dims(x, axis=0)
        n, c, h, w = x.shape
        # assert n==1, 'Only work for batch size == 1'# TODO support batch_size > 1:
        test_outputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', []), ('avgpool', [])])
        x1, x2, x3, x4, avg, _ = self.model(x)
        test_outputs['layer1'] = np.zeros((1, x1.shape[1],x1.shape[2],x1.shape[3]))
        test_outputs['layer2'] = np.zeros((1, x2.shape[1],x2.shape[2],x2.shape[3]))
        test_outputs['layer3'] = np.zeros((1, x3.shape[1],x3.shape[2],x3.shape[3]))
        test_outputs['avgpool'] = np.zeros((1, avg.shape[1],avg.shape[2],avg.shape[3]))
        for k, v in zip(test_outputs.keys(), [x1, x2, x3, avg]):
            # test_outputs[k].append(v)
            test_outputs[k] = np.vstack((test_outputs[k], v.asnumpy()))

        for k, v in test_outputs.items():
            # test_outputs[k] = (msnp.concatenate(v, 0)).asnumpy()
            test_outputs[k] = test_outputs[k][1:]
        
        # calculate distance matrix
        dist_matrix = self._calc_dist_matrix(test_outputs['avgpool'].reshape(test_outputs['avgpool'].shape[0], -1), self.train_outputs['avgpool'].reshape(self.train_outputs['avgpool'].shape[0], -1))
        topk_values, topk_indexes = topk_np(dist_matrix, K=self.topk, axis=1, largest=False)
        scores = np.mean(topk_values, 1)

        score_map_list = []
        for t_idx in range(test_outputs['avgpool'].shape[0]):
            score_maps = []
            for layer_name in ['layer1', 'layer2', 'layer3']:
                # construct a gallery of features at all pixel locations of the K nearest neighbors
                topk_feat_map = self.train_outputs[layer_name][topk_indexes[t_idx]]
                test_feat_map = test_outputs[layer_name][t_idx:t_idx+1]
                feat_gallery = topk_feat_map.transpose(0,3,2,1)
                feat_gallery = np.expand_dims(np.expand_dims(feat_gallery.reshape(feat_gallery.shape[0]*feat_gallery.shape[1]*feat_gallery.shape[2],feat_gallery.shape[-1]), axis=-1),axis=-1)
                # calculate distance matrix
                dist_matrix_list = []
                for d_idx in range(feat_gallery.shape[0] // 100):
                    dist_matrix = cp.linalg.norm(cp.asarray(feat_gallery[d_idx * 100:d_idx * 100 + 100])-cp.asarray(test_feat_map), axis=1)
                    dist_matrix_list.append(dist_matrix)

                dist_matrix = cp.concatenate(dist_matrix_list, 0)
                # k nearest features from the gallery (k=1)
                score_map = cp.asnumpy(cp.min(dist_matrix, axis=0))
                # score_map = np.resize(score_map, self.train_size)
                score_map = cv2.resize(score_map, self.train_size, interpolation=cv2.INTER_LINEAR)
                score_map = np.expand_dims(np.expand_dims(score_map,axis=0), axis=0)
                score_maps.append(score_map)

            # average distance between the features
            score_map = np.mean(np.concatenate(score_maps, 0), axis=0)
            # apply gaussian smoothing on the score map
            score_map = gaussian_filter(score_map, sigma=4)
            score_map_list.append(score_map)

        img_score = np.expand_dims(scores,axis=1)
        score = np.vstack(score_map_list)

        if (self.val_max_is is not None) and (self.val_min_is is not None):
            img_score = (img_score - self.val_min_is) / (self.val_max_is - self.val_min_is)
        if (self.val_max_as is not None) and (self.val_min_as is not None):
            score = (score - self.val_min_as) / (self.val_max_as - self.val_min_as)
        gc.collect()
        return img_score, score

    def _calc_dist_matrix(self, x, y):
        """Calculate Euclidean distance matrix"""
        # x = mindspore.Tensor(x)
        # y = mindspore.Tensor(y)
        n = x.shape[0]
        m = y.shape[0]
        d = x.shape[1]
        x = np.expand_dims(x,axis=1).repeat(m, axis=1)
        y = np.expand_dims(y,axis=0).repeat(n, axis=0)
        # x = x.unsqueeze(1).expand(n, m, d)
        # y = y.unsqueeze(0).expand(n, m, d)
        # x = mindspore.Tensor(x)
        # y = mindspore.Tensor(y)
        # dist_matrix = msnp.sqrt(msnp.power(x - y, 2).sum(2))
        # return dist_matrix.asnumpy()
        return np.sqrt(np.power(x-y, 2).sum(2))
    
def topk_np(matrix, K, axis=1, largest=True):
    if largest:
        if axis == 0:
            row_index = np.arange(matrix.shape[1 - axis])
            topk_index = np.argpartition(-matrix, K, axis=axis)[0:K, :]
            topk_data = matrix[topk_index, row_index]
            topk_index_sort = np.argsort(-topk_data,axis=axis)
            topk_data_sort = topk_data[topk_index_sort,row_index]
            topk_index_sort = topk_index[0:K,:][topk_index_sort,row_index]
        else:
            column_index = np.arange(matrix.shape[1 - axis])[:, None]
            topk_index = np.argpartition(-matrix, K, axis=axis)[:, 0:K]
            topk_data = matrix[column_index, topk_index]
            topk_index_sort = np.argsort(-topk_data, axis=axis)
            topk_data_sort = topk_data[column_index, topk_index_sort]
            topk_index_sort = topk_index[:,0:K][column_index,topk_index_sort]
    else:
        if axis == 0:
            row_index = np.arange(matrix.shape[1 - axis])
            topk_index = np.argpartition(matrix, K, axis=axis)[0:K, :]
            topk_data = matrix[topk_index, row_index]
            topk_index_sort = np.argsort(topk_data,axis=axis)
            topk_data_sort = topk_data[topk_index_sort,row_index]
            topk_index_sort = topk_index[0:K,:][topk_index_sort,row_index]
        else:
            column_index = np.arange(matrix.shape[1 - axis])[:, None]
            topk_index = np.argpartition(matrix, K, axis=axis)[:, 0:K]
            topk_data = matrix[column_index, topk_index]
            topk_index_sort = np.argsort(topk_data, axis=axis)
            topk_data_sort = topk_data[column_index, topk_index_sort]
            topk_index_sort = topk_index[:,0:K][column_index,topk_index_sort]

    return topk_data_sort, topk_index_sort