""" Implementation of the FAVAE algorithm for anomaly localization and detection
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
import torch
from torch import nn
import torch.optim as optim
from torchvision import models
import numpy as np
from tqdm import tqdm
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
from READ_pytorch.utils import get_patch, patch2img
from READ_pytorch.utils import estimate_thred_with_fpr
from READ_pytorch.scheduler import CosineAnnealingScheduler
from torch.nn import functional as F

class VAE(nn.Module):
    def __init__(self, input_channel=3, output_size=128, z_dim=100):
        super(VAE, self).__init__()
        assert (output_size in [128, 256, 512]) # only design for these sizes
        scale_factor  = int(output_size // 128)
        # encode
        self.encode = nn.Sequential(
            nn.Conv2d(input_channel, 128, kernel_size=4, stride=2, padding=1),  # 128 => 64
            nn.BatchNorm2d(128),
            nn.LeakyReLU(negative_slope=0.2),
            nn.Conv2d(128, 128, kernel_size=4, stride=2, padding=1),  # 64 => 32
            nn.BatchNorm2d(128),
            nn.LeakyReLU(negative_slope=0.2),
            nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(negative_slope=0.2),
            nn.Conv2d(256, 256, kernel_size=4, stride=2, padding=1),  # 32 => 16
            nn.BatchNorm2d(256),
            nn.LeakyReLU(negative_slope=0.2),
            nn.Conv2d(256, 512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(512),
            nn.LeakyReLU(negative_slope=0.2),
            nn.Conv2d(512, 512, kernel_size=4, stride=2, padding=1),  # 16 => 8
            nn.BatchNorm2d(512),
            nn.LeakyReLU(negative_slope=0.2),
            nn.Conv2d(512, 512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(512),
            nn.LeakyReLU(negative_slope=0.2),
            nn.Conv2d(512, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.LeakyReLU(negative_slope=0.2),
            nn.Conv2d(32, 200, kernel_size=8, stride=1),  # 8 => 1
            # nn.Flatten(),
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            Split())

        # decode
        self.decode = nn.Sequential(
            DeFlatten(z_dim),
            nn.ConvTranspose2d(100, 32, kernel_size=8, stride=1),  # 1 => 8
            nn.BatchNorm2d(32),
            nn.LeakyReLU(negative_slope=0.2),
            Scale(scale_factor), #scale the feature size for the final output
            nn.ConvTranspose2d(32, 512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(512),
            nn.LeakyReLU(negative_slope=0.2),
            nn.ConvTranspose2d(512, 512, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(512),
            nn.LeakyReLU(negative_slope=0.2),
            nn.ConvTranspose2d(512, 512, kernel_size=4, stride=2, padding=1),  # double the feature size 
            nn.BatchNorm2d(512),
            nn.LeakyReLU(negative_slope=0.2),
            nn.ConvTranspose2d(512, 256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(negative_slope=0.2),
            nn.ConvTranspose2d(256, 256, kernel_size=4, stride=2, padding=1),  # double the feature size
            nn.BatchNorm2d(256),
            nn.LeakyReLU(negative_slope=0.2),
            nn.ConvTranspose2d(256, 128, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(negative_slope=0.2),
            nn.ConvTranspose2d(128, 128, kernel_size=4, stride=2, padding=1),  # double the feature size
            nn.BatchNorm2d(128),
            nn.LeakyReLU(negative_slope=0.2),
            nn.ConvTranspose2d(128, input_channel, kernel_size=4, stride=2, padding=1),  # double the feature size      
            nn.Identity(),
            nn.Sigmoid()
            # nn.Tanh()
        )


        self.adapter = nn.ModuleList([Adapter_model(128), Adapter_model(256), Adapter_model(512)])


    def reparameterize(self, mu, log_var):
        if self.training:
            std = log_var.mul(0.5).exp_()
            eps = std.new(std.size()).normal_()
            return eps.mul(std).add_(mu)
        else:
            return mu

    def forward(self, x):
        n, c, h, w = x.shape
        assert (h == w) # only works for h==w
        assert (h in [128, 256, 512]) # only desire for size 128 or 256
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)

        return z, self.decode(z), mu, logvar


class DeFlatten(nn.Module):
    def __init__(self, z_dim):
        super(DeFlatten, self).__init__()
        self.z_dim = z_dim
    def forward(self, x):
        x = x.view(x.shape[0], self.z_dim, 1, 1)
        return x

class Scale(nn.Module):
    def __init__(self, scale_factor):
        super(Scale, self).__init__()
        self.scale_factor = scale_factor
    def forward(self, x):
        x = x.repeat(1,1,self.scale_factor,self.scale_factor)
        return x


class Split(nn.Module):
    def forward(self, x):
        mu, logvar = x.chunk(2, dim=1)
        return mu, logvar


class Adapter_model(nn.Module):
    def __init__(self, channel=128):
        super(Adapter_model, self).__init__()

        self.conv = nn.Sequential(nn.Conv2d(channel, channel, kernel_size=1, stride=1), nn.ReLU(),
                                  nn.Conv2d(channel, channel, kernel_size=1, stride=1))

    def forward(self, x):
        return self.conv(x)

##############################################################
####################### FAVAE Model ###########################
##############################################################
class FAVAE(object):
    def __init__(self, **kwargs):
        n_channels = kwargs.get("n_channels", 3)
        crop_size = kwargs.get("crop_size", 128)
        self.crop_size = crop_size
        z_dim = kwargs.get("z_dim", 100)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = VAE(input_channel=n_channels, output_size=crop_size, z_dim=z_dim).to(self.device)
        self.teacher = models.vgg16(pretrained=True).to(self.device)
        for param in self.teacher.parameters():
            param.requires_grad = False
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
        lr = kwargs.get("lr", 1e-3)
        epochs = kwargs.get("epochs", 300)
        optimizer_name = kwargs.get("optimizer", 'adam')
        scheduler_name = kwargs.get("scheduler", 'step')
        kld_weight = kwargs.get("kld_weight", 1.0)
        self.kld_weight = kld_weight
        batch_size = kwargs.get("batch_size", 4)
        validation_ratio = kwargs.get("validation_ratio", 0.2)

        self.logger = logging.getLogger('READ.Train')
        set_logger(os.path.join(save_path, 'train.log'), 'READ')
        self.save_path = save_path
        loader_kwargs = {'num_workers': 8, 'pin_memory': True} if (torch.cuda.is_available() and platform.system() == 'Linux') else {}
        if val_data == None:
            img_nums = len(train_data)
            valid_num = int(img_nums * validation_ratio)
            train_num = img_nums - valid_num
            train_data, val_data = torch.utils.data.random_split(train_data, [train_num, valid_num])

        train_data_cat = train_data
        while len(train_data_cat) < 10000: # train on 10000 images
            train_data_cat = torch.utils.data.ConcatDataset([train_data_cat, train_data])

        train_dataloader = torch.utils.data.DataLoader(train_data_cat, batch_size=batch_size, shuffle=True, **loader_kwargs)
        val_dataloader = torch.utils.data.DataLoader(val_data, batch_size=int(4*batch_size), shuffle=True, **loader_kwargs)

        if (optimizer_name == 'adam') or (optimizer_name == 'Adam'):
            optimizer = optim.Adam(filter(lambda p: p.requires_grad, self.model.parameters()), lr=lr, weight_decay=1e-6)
        elif (optimizer_name == 'sgd') or (optimizer_name == 'SGD'):
            optimizer = optim.SGD(filter(lambda p: p.requires_grad, self.model.parameters()), lr=lr, momentum=0.9, nesterov=True)
        elif (optimizer_name == 'radam') or (optimizer_name == 'RAdam'):
            optimizer = RAdam(filter(lambda p: p.requires_grad, self.model.parameters()), lr=lr, weight_decay=1e-6)
        elif (optimizer_name == 'adabelief') or (optimizer_name == 'Adabelief'):
            optimizer = AdaBelief(filter(lambda p: p.requires_grad, self.model.parameters()), lr=lr, weight_decay=1e-6, eps=1e-16, betas=(0.9,0.999), weight_decouple = True, rectify = True)
        else:
            raise ValueError('Could Only Support optimizer in [Adam, SGD, RAdam, Adabelief].')
        
        if scheduler_name == 'step':
            scheduler = optim.lr_scheduler.StepLR(optimizer, int(0.1 * epochs), 0.5)
        elif scheduler_name == 'cosine':
            scheduler = CosineAnnealingScheduler(optimizer, start_anneal=30, n_epochs=epochs)
            # scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs, eta_min=1e-8)
        else:
            raise ValueError('Could Only Support scheduler in [Step, Cosine].')
        
        x_ref, _, _ = iter(train_dataloader).next()
        assert (len(x_ref.shape) == 4), 'input tensor should be 4-dim.'
        assert (x_ref.shape[2] == x_ref.shape[3]), 'Input height should be equal to width.'
        img_size = x_ref.shape[2]
        assert (img_size >= self.crop_size), 'Input size should not be smaller than the crop size.'
        
        # MSE_loss = nn.MSELoss(reduction='sum')
        epoch_time = AverageMeter()
        save_lowest = os.path.join(save_path, 'model_lowest_loss.pt')
        early_stop = EarlyStop(patience=int(0.1*epochs) if int(0.1*epochs) > 20 else 20, 
                                save_name=save_lowest)
        start_time = time.time()
        for epoch in range(0, epochs):

            self._train(epoch, train_dataloader, optimizer)

            val_loss = self._val(val_dataloader)
            if (early_stop(val_loss, self.model, optimizer)):
                break
                
            epoch_time.update(time.time() - start_time)
            start_time = time.time()
            scheduler.step()

        torch.cuda.empty_cache()
    
        self.est_thres(val_data, expect_fpr=expect_fpr)

    def _train(self, epoch, train_loader, optimizer):
        self.model.train()
        self.teacher.eval()
        losses = AverageMeter()
        MSE_loss = nn.MSELoss(reduction='sum')
        # for (data, _, _) in tqdm(train_loader):
        for (data) in tqdm(train_loader):
            if type(data) != torch.Tensor:
                if type(data) == list or type(data) == tuple:
                    data = data[0]
                    if type(data) != torch.Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
            # if torch.cuda.is_available():
            #     data = data.cuda()
            img_size = data.size(-1)
            data = data.to(self.device)
            if img_size > self.crop_size:
                data = self._random_crop(data, self.crop_size)
            z, output, mu, log_var = self.model(data)
            # get model's intermediate outputs
            s_activations, _ = self._feature_extractor(z, self.model.decode, target_layers=['11', '17', '23'])
            t_activations, _ = self._feature_extractor(data, self.teacher.features, target_layers=['7', '14', '21'])

            optimizer.zero_grad()
            mse_loss = MSE_loss(output, data)
            kld_loss = 0.5 * torch.sum(-1 - log_var + torch.exp(log_var) + mu**2)
            for i in range(len(s_activations)):
                s_act = self.model.adapter[i](s_activations[-(i + 1)])
                mse_loss += MSE_loss(s_act, t_activations[i])
            loss = mse_loss + self.kld_weight * kld_loss
            losses.update(loss.sum().item(), data.size(0))
    
            loss.backward()
            optimizer.step()

        self.logger.info('Train Epoch: {} Loss: {:.6f}'.format(epoch, losses.avg))

    def _val(self, val_loader):
        self.model.eval()
        self.teacher.eval()
        losses = AverageMeter()
        MSE_loss = nn.MSELoss(reduction='sum')
        # for (data, _, _) in tqdm(val_loader):
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
            if img_size > self.crop_size:
                data = self._random_crop(data, self.crop_size)
            with torch.no_grad():
                z, output, mu, log_var = self.model(data)
                # get model's intermediate outputs
                s_activations, _ = self._feature_extractor(z, self.model.decode, target_layers=['13', '19', '25'])
                t_activations, _ = self._feature_extractor(data, self.teacher.features, target_layers=['8', '15', '22'])

                mse_loss = MSE_loss(output, data)
                kld_loss = 0.5 * torch.sum(-1 - log_var + torch.exp(log_var) + mu**2)
                for i in range(len(s_activations)):
                    s_act = self.model.adapter[i](s_activations[-(i + 1)])
                    mse_loss += MSE_loss(s_act, t_activations[i])
                loss = mse_loss + self.kld_weight * kld_loss
                losses.update(loss.item(), data.size(0))

        return losses.avg

    def est_thres(self, val_data, expect_fpr=0.01, **kwargs):
        batch_size = kwargs.get("batch_size", 64)
        loader_kwargs = {'num_workers': 8, 'pin_memory': True} if (torch.cuda.is_available() and platform.system() == 'Linux') else {}
        val_dataloader = torch.utils.data.DataLoader(val_data, batch_size=batch_size, shuffle=False, **loader_kwargs)
        x_ref, _, _ = iter(val_dataloader).next()
        assert (x_ref.shape[2] == x_ref.shape[3]), 'Input height should be equal to width.'
        img_size = x_ref.shape[2]
        assert (img_size >= self.crop_size), 'Input size should not be smaller than the crop size.'

        if img_size > self.crop_size:
            val_dataloader = torch.utils.data.DataLoader(val_data, batch_size=1, shuffle=False, **loader_kwargs)
            val_scores = self._test_patches(val_dataloader)
        else:
            val_dataloader = torch.utils.data.DataLoader(val_data, batch_size=batch_size, shuffle=False, **loader_kwargs)
            val_scores = self._test(val_dataloader)

        val_scores = np.asarray(val_scores)
        self.val_max_as = val_scores.max()
        self.val_min_as = val_scores.min()

        val_scores = (val_scores - self.val_min_as) / (self.val_max_as - self.val_min_as)
        val_img_scores = val_scores.reshape(val_scores.shape[0], -1).max(axis=1)
        self.seg_thres = estimate_thred_with_fpr(val_scores, expect_fpr=expect_fpr)
        self.cls_thres = estimate_thred_with_fpr(val_img_scores, expect_fpr=expect_fpr)

    def _test(self, test_loader):
        self.model.eval()
        self.teacher.eval()
        MSE_loss = nn.MSELoss(reduction='none')
        scores = []

        # for (data, _, _) in tqdm(test_loader):
        for (data) in tqdm(test_loader):
            if type(data) != torch.Tensor:
                if type(data) == list or type(data) == tuple:
                    data = data[0]
                    if type(data) != torch.Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
            with torch.no_grad():
                data = data.to(self.device)
                z, output, _, _ = self.model(data)
                # get model's intermediate outputs
                s_activations, _ = self._feature_extractor(z, self.model.decode, target_layers=['11', '17', '23'])
                t_activations, _ = self._feature_extractor(data, self.teacher.features, target_layers=['7', '14', '21'])

                score = MSE_loss(output, data).sum(1, keepdim=True)
                for i in range(len(s_activations)):
                    s_act = self.model.adapter[i](s_activations[-(i + 1)])
                    mse_loss = MSE_loss(s_act, t_activations[i]).sum(1, keepdim=True)
                    score += F.interpolate(mse_loss, size=data.size(2), mode='bilinear', align_corners=False)

            score = score.squeeze().cpu().numpy()
            if score.ndim < 3:
                score = np.expand_dims(score, axis=0)
            for i in range(score.shape[0]):
                score[i] = gaussian_filter(score[i], sigma=4)

            scores.extend(score)

        return scores

    def _test_patches(self, test_loader):
        self.model.eval()
        self.teacher.eval()
        MSE_loss = nn.MSELoss(reduction='none')
        scores = []

        # for (data, _, _) in tqdm(test_loader):
        for (data) in tqdm(test_loader):
            if type(data) != torch.Tensor:
                if type(data) == list or type(data) == tuple:
                    data = data[0]
                    if type(data) != torch.Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
            with torch.no_grad():
                # print(data.shape)
                img_size = data.size(-1)
                data = get_patch(data, self.crop_size)
                data = data.to(self.device)
                # print(data.shape)
                z, output, _, _ = self.model(data)
                # print(output.shape)
                # get model's intermediate outputs
                s_activations, _ = self._feature_extractor(z, self.model.decode, target_layers=['11', '17', '23'])
                t_activations, _ = self._feature_extractor(data, self.teacher.features, target_layers=['7', '14', '21'])
                score = MSE_loss(output, data).sum(1, keepdim=True)
                for i in range(len(s_activations)):
                    s_act = self.model.adapter[i](s_activations[-(i + 1)])
                    mse_loss = MSE_loss(s_act, t_activations[i]).sum(1, keepdim=True)
                    score += F.interpolate(mse_loss, size=data.size(2), mode='bilinear', align_corners=False)
                # print(score.shape)
                output = patch2img(output.cpu(), img_size, self.crop_size)
                # print(output.shape)
                score = patch2img(score.cpu(), img_size, self.crop_size)
                # print(score.shape)
            # sys.exit()
            score = score.squeeze().cpu().numpy()
            if score.ndim < 3:
                score = np.expand_dims(score, axis=0)
            for i in range(score.shape[0]):
                score[i] = gaussian_filter(score[i], sigma=4)

            scores.extend(score)

        return scores

    def predict(self, test_data, **kwargs):
        self.model.eval()
        self.teacher.eval()
        MSE_loss = nn.MSELoss(reduction='none')
        score = 0
        with torch.no_grad():
            data = test_data.to(self.device)
            img_size = data.size(-1)
            assert (img_size >= self.crop_size), 'Input size should not be smaller than the crop size.'
            if img_size > self.crop_size:
                data = get_patch(data, self.crop_size)
                # print(data.shape)
                z, output, _, _ = self.model(data)
                # print(output.shape)
                # get model's intermediate outputs
                s_activations, _ = self._feature_extractor(z, self.model.decode, target_layers=['11', '17', '23'])
                t_activations, _ = self._feature_extractor(data, self.teacher.features, target_layers=['7', '14', '21'])
                score = MSE_loss(output, data).sum(1, keepdim=True)
                for i in range(len(s_activations)):
                    s_act = self.model.adapter[i](s_activations[-(i + 1)])
                    mse_loss = MSE_loss(s_act, t_activations[i]).sum(1, keepdim=True)
                    score += F.interpolate(mse_loss, size=data.size(2), mode='bilinear', align_corners=False)
                # print(score.shape)
                output = patch2img(output.cpu(), img_size, self.crop_size)
                # print(output.shape)
                score = patch2img(score.cpu(), img_size, self.crop_size)

            else:
                z, output, _, _ = self.model(data)
                # get model's intermediate outputs
                s_activations, _ = self._feature_extractor(z, self.model.decode, target_layers=['11', '17', '23'])
                t_activations, _ = self._feature_extractor(data, self.teacher.features, target_layers=['7', '14', '21'])

                score = MSE_loss(output, data).sum(1, keepdim=True)
                for i in range(len(s_activations)):
                    s_act = self.model.adapter[i](s_activations[-(i + 1)])
                    mse_loss = MSE_loss(s_act, t_activations[i]).sum(1, keepdim=True)
                    score += F.interpolate(mse_loss, size=data.size(2), mode='bilinear', align_corners=False)

        score = score.squeeze().cpu().numpy()
        if score.ndim < 3:
            score = np.expand_dims(score, axis=0)
        for i in range(score.shape[0]):
            score[i] = gaussian_filter(score[i], sigma=7)

        if (self.val_max_as is not None) and (self.val_min_as is not None):
            # print('Normalizing!')
            score = (score - self.val_min_as) / (self.val_max_as - self.val_min_as)

        img_score = score.reshape(score.shape[0], -1).max(axis=1)

        return img_score, score


    def _random_crop(self, tensor, size):
        h, w = tensor.shape[-2], tensor.shape[-1]
        x = random.randint(0, w-size) #random number
        y = random.randint(0, h-size)
        tensor_crop = tensor[:,:,y:y+size, x:x+size].clone()
        return tensor_crop

    def load_weights(self, ckpt_path):
        if torch.cuda.is_available():
            params = torch.load(ckpt_path)
        else:
            params = torch.load(ckpt_path, map_location='cpu')
        try:
            params = params["state_dict"]
        except:
            params = params

        self.model.load_state_dict(remove_dataparallel(params))
        print('Pretrained weights from %s has been loaded.' %ckpt_path)
    
    def _feature_extractor(self, x, model, target_layers):
        target_activations = list()
        for name, module in model._modules.items():
            x = module(x)
            if name in target_layers:
                target_activations += [x]
        return target_activations, x
