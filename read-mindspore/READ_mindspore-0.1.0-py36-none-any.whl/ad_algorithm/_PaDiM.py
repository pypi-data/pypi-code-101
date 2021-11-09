import os
import platform
import mindspore
import mindspore.nn as nn
import numpy as np
import cupy as cp
import mindspore.numpy as msnp
from mindspore import Tensor
from mindspore import context
from random import sample
from collections import OrderedDict
from tqdm import tqdm
from scipy.ndimage import gaussian_filter
import scipy.ndimage as ndi
import pickle
import gc
import time
import cv2
from READ_mindspore.utils import estimate_thred_with_fpr
from READ_mindspore.backbones import resnet_model_zoo

class PaDiM(object):
    # train_outputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', [])])
    # test_outputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', [])])
    train_outputs_cache = None
    train_outputs = None
    def __init__(self, backbone='resnet50', device='GPU'):
        self.device = device
        context.set_context(mode=context.GRAPH_MODE, device_target=self.device, save_graphs=False)
        self.backbone = backbone
        if self.backbone == 'resnet18':
            self.model = resnet_model_zoo().resnet18()
            t_d = 448
            d = 100
        elif self.backbone == 'resnet50':
            self.model = resnet_model_zoo().resnet50()
            # t_d = 448
            # d = 100
            t_d = 1792
            d = 550
        else:
            raise ValueError('This backbone has not been supported yet.')
        self.model.set_train(False)
        self.model.set_grad(False)
        self.idx = Tensor(sample(range(0, t_d), d)) #random choice features

    def train(self, 
                train_data,
                save_path,
                expect_fpr=0.01,
                **kwargs):
        batch_size = kwargs.get("batch_size", 32)
        step_by_each_epoch = train_data.get_dataset_size()
        train_data_batch = train_data.batch(batch_size)
        train_dataloader = train_data_batch.create_dict_iterator()
        train_outputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', [])])
        for (itr, x) in tqdm(enumerate(train_dataloader), '| feature extraction | train |'):
            x = x['data']
            if type(x) != mindspore.Tensor:
                if type(x) == list or type(x) == tuple:
                    x = x[0]
                    if type(x) != mindspore.Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
            x1, x2, x3, x4, avg, _ = self.model(x)
            if itr == 0:
                train_outputs['layer1'] = np.zeros((1, x1.shape[1],x1.shape[2],x1.shape[3]))
                train_outputs['layer2'] = np.zeros((1, x2.shape[1],x2.shape[2],x2.shape[3]))
                train_outputs['layer3'] = np.zeros((1, x3.shape[1],x3.shape[2],x3.shape[3]))
            for k, v in zip(train_outputs.keys(), [x1, x2, x3]):
                train_outputs[k] = np.vstack((train_outputs[k], v.asnumpy()))

        for k, v in train_outputs.items():
            train_outputs[k] = train_outputs[k][1:]
        self.train_outputs_cache = train_outputs
        # Embedding concat
        embedding_vectors = train_outputs['layer1']
        for layer_name in ['layer2', 'layer3']:
            embedding_vectors = self._embedding_concat(embedding_vectors, train_outputs[layer_name])
        embedding_vectors = embedding_vectors[:,self.idx.asnumpy()]
        B, C, H, W = embedding_vectors.shape
        embedding_vectors = embedding_vectors.reshape(B, C, H * W)
        mean = embedding_vectors.mean(axis=0)
        cov = np.zeros((C, C, H * W))
        I = np.identity(C)
        for i in tqdm(range(H * W),'| feature calculation |'):
            cov[:, :, i] = cp.asnumpy(cp.cov(cp.asarray(embedding_vectors[:, :, i]), rowvar=False)) + 0.01 * I

        self.train_outputs = [mean, cov]
        #torch.cuda.empty_cache()
        self.save_weights(os.path.join(save_path, 'model.pkl'))
        self.est_thres(val_data=train_dataloader, expect_fpr=expect_fpr)

    def save_weights(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump([self.train_outputs_cache, self.train_outputs], f, protocol = 4)

    def load_weights(self, filepath):
        print('load train set feature from: %s' % filepath)
        with open(filepath, 'rb') as f:
            # self.train_outputs = pickle.load(f)
            loaded_features = pickle.load(f)
        self.train_outputs_cache = loaded_features[0]
        self.train_outputs = loaded_features[1]
    
    def est_thres(self, val_data, expect_fpr=0.01):
        assert self.train_outputs_cache is not None, 'Should train the model or load weights at first.'
        dict_data = next(val_data)
        data = dict_data["data"]
        img_size = data.shape[2]
        embedding_vectors = self.train_outputs_cache['layer1']
        for layer_name in ['layer2', 'layer3']:
            embedding_vectors = self._embedding_concat(embedding_vectors, self.train_outputs_cache[layer_name])
        embedding_vectors = embedding_vectors[:,self.idx.asnumpy()]
        B, C, H, W = embedding_vectors.shape
        embedding_vectors = embedding_vectors.reshape(B, C, H * W)
        dist_list = []
        for i in tqdm(range(H * W),'| Estimating Threshold |'):
            mean = cp.asarray(self.train_outputs[0][:, i])
            conv_inv = cp.linalg.inv(cp.asarray(self.train_outputs[1][:, :, i]))
            dist = [self._mahalanobis(sample[:, i], mean, conv_inv) for sample in embedding_vectors]
            dist_list.append(cp.expand_dims(cp.array(dist), axis=0))
        dist_list = cp.asnumpy(cp.vstack(dist_list).transpose(1, 0).reshape(B, H, W))
        # dist_list = dist_list.transpose(0,-1)
        # dist_list = bilinear_interpolate_numpy(np.moveaxis(dist_list, 0, -1), img_size, img_size)
        score_map = ndi.zoom(dist_list, (1, img_size/H, img_size/W), order=2)
        if len(score_map.shape) == 2:
            score_map = np.expand_dims(score_map, axis=0)

        score_map_filtered = np.zeros(score_map.shape)
        for i in range(score_map.shape[0]):
            score_map_filtered[i] = np.array(gaussian_filter(score_map[i], 
                                                    sigma=4))

        self.val_max_as = score_map_filtered.max()
        self.val_min_as = score_map_filtered.min()
        
        val_scores = (score_map_filtered - self.val_min_as) / (self.val_max_as - self.val_min_as)
        val_img_scores = val_scores.reshape(val_scores.shape[0], -1).max(axis=1)
        self.seg_thres = estimate_thred_with_fpr(val_scores, expect_fpr=expect_fpr)
        self.cls_thres = estimate_thred_with_fpr(val_img_scores, expect_fpr=expect_fpr)

    def predict(self, x):
        # context.set_context(mode=context.GRAPH_MODE, device_target=self.device, save_graphs=False)
        # model prediction
        if len(x.shape) == 3:
            x = msnp.expand_dims(x, axis=0)
        n, c, h, w = x.shape
        test_outputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', [])])
        x1, x2, x3, x4, avg, _ = self.model(x)
        test_outputs['layer1'] = np.zeros((1, x1.shape[1],x1.shape[2],x1.shape[3]))
        test_outputs['layer2'] = np.zeros((1, x2.shape[1],x2.shape[2],x2.shape[3]))
        test_outputs['layer3'] = np.zeros((1, x3.shape[1],x3.shape[2],x3.shape[3]))
        for k, v in zip(test_outputs.keys(), [x1, x2, x3]):
            # test_outputs[k].append(v)
            test_outputs[k] = np.vstack((test_outputs[k], v.asnumpy()))

        for k, v in test_outputs.items():
            # test_outputs[k] = (msnp.concatenate(v, 0)).asnumpy()
            test_outputs[k] = test_outputs[k][1:]
        # Embedding concat
        embedding_vectors = test_outputs['layer1']
        for layer_name in ['layer2', 'layer3']:
            embedding_vectors = self._embedding_concat(embedding_vectors, test_outputs[layer_name])
    
        embedding_vectors = embedding_vectors[:,self.idx.asnumpy()]
        B, C, H, W = embedding_vectors.shape
        embedding_vectors = embedding_vectors.reshape(B, C, H * W)
        dist_list = []
        for i in range(H * W):
            mean = cp.asarray(self.train_outputs[0][:, i])
            conv_inv = cp.linalg.inv(cp.asarray(self.train_outputs[1][:, :, i]))
            dist = [self._mahalanobis(sample[:, i], mean, conv_inv) for sample in embedding_vectors]
            dist_list.append(cp.expand_dims(cp.array(dist), axis=0))
        dist_list = cp.asnumpy(cp.vstack(dist_list).transpose(1, 0).reshape(B, H, W))
        score_map = ndi.zoom(dist_list, (1, h/H, w/W), order=2)
        if len(score_map.shape) == 2:
            score_map = np.expand_dims(score_map, axis=0)

        score_map_filtered = np.zeros(score_map.shape)
        for i in range(score_map.shape[0]):
            score_map_filtered[i] = np.array(gaussian_filter(score_map[i], 
                                                    sigma=4))

        scores = (score_map_filtered - self.val_min_as) / (self.val_max_as - self.val_min_as)
    
        # calculate image-level ROC AUC score
        img_scores = scores.reshape(scores.shape[0], -1).max(axis=1)

        return img_scores, scores

        
    def _reset_train_features(self):
        self.train_outputs = None
        self.__init__(self.backbone)

    
    def _validate_vector(self, u, dtype=None):
        # XXX Is order='c' really necessary?
        u = cp.asarray(u, dtype=dtype, order='c').squeeze()
        # Ensure values such as u=1 and u=[1] still return 1-D arrays.
        u = cp.atleast_1d(u)
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
        VI = cp.atleast_2d(VI)
        delta = u - v
        m = cp.dot(cp.dot(delta, VI), delta)
        return cp.sqrt(m)

        


    def _embedding_concat(self, x, y):
        B, C1, H1, W1 = x.shape
        _, C2, H2, W2 = y.shape
        s1 = int(H1 / H2)
        s2 = int(W1 / W2)
        assert s1 == s2, 'Size not correct.'
        # y = np.resize(y, (y.shape[0], y.shape[1], y.shape[2]*s1, y.shape[3]*s1))
        y = ndi.zoom(y, (1,1,s1,s1),order=1)
        return np.concatenate((x,y), axis=1)