""" Implementation of the RIAD algorithm for anomaly localization and detection
This method is proposed in the paper:
    'Student-Teacher Feature Pyramid Matching for Unsupervised Anomaly Detection'
Following implementation is adapted form the repository:
    https://github.com/plutoyuxie/Reconstruction-by-inpainting-for-visual-anomaly-detection
"""
import torch
from torch import nn
import torch.optim as optim
import numpy as np
from tqdm import tqdm
import random
import os
import time
import logging
import platform
from READ_pytorch.losses import MSGMS_Loss, SSIM_Loss, MSGMS_Score
from scipy.ndimage import gaussian_filter
from adabelief_pytorch import AdaBelief
from READ_pytorch.optimizer import RAdam
from READ_pytorch.utils import set_logger, AverageMeter, EarlyStop
from READ_pytorch.utils import remove_dataparallel
from READ_pytorch.utils import estimate_thred_with_fpr

def gen_mask(k_list, n, im_size):
    while True:
        Ms = []
        for k in k_list:
            N = im_size // k
            rdn = np.random.permutation(N**2)
            additive = N**2 % n
            if additive > 0:
                rdn = np.concatenate((rdn, np.asarray([-1] * (n - additive))))
            n_index = rdn.reshape(n, -1)
            for index in n_index:
                tmp = [0 if i in index else 1 for i in range(N**2)]
                tmp = np.asarray(tmp).reshape(N, N)
                tmp = tmp.repeat(k, 0).repeat(k, 1)
                Ms.append(tmp)
        yield Ms


def conv(in_channels, out_channels, kernel_size=3, stride=1, padding=1):
    return nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size, stride=stride, padding=padding)


def upconv2x2(in_channels, out_channels, mode='transpose'):
    if mode == 'transpose':
        return nn.ConvTranspose2d(in_channels, out_channels, kernel_size=4, stride=2, padding=1)
    else:
        return nn.Sequential(nn.Upsample(mode='bilinear', scale_factor=2),
                             conv(in_channels, out_channels, kernel_size=1, stride=1, padding=0))


class UNetDownBlock(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding):
        super(UNetDownBlock, self).__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding

        self.conv1 = conv(self.in_channels, self.out_channels, kernel_size=self.kernel_size, stride=self.stride)
        self.bn1 = nn.BatchNorm2d(self.out_channels)
        self.relu1 = nn.ReLU()

        self.conv2 = conv(self.out_channels, self.out_channels)
        self.bn2 = nn.BatchNorm2d(self.out_channels)
        self.relu2 = nn.ReLU()

    def forward(self, x):
        x = self.relu1(self.bn1(self.conv1(x)))
        x = self.relu2(self.bn2(self.conv2(x)))

        return x


class UNetUpBlock(nn.Module):
    def __init__(self, in_channels, out_channels, merge_mode='concat', up_mode='transpose'):
        super(UNetUpBlock, self).__init__()

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.merge_mode = merge_mode
        self.up_mode = up_mode

        self.upconv = upconv2x2(self.in_channels, self.out_channels, mode=self.up_mode)

        if self.merge_mode == 'concat':
            self.conv1 = conv(2 * self.out_channels, self.out_channels)
        else:
            self.conv1 = conv(self.out_channels, self.out_channels)
        self.bn1 = nn.BatchNorm2d(self.out_channels)
        self.relu1 = nn.ReLU()
        self.conv2 = conv(self.out_channels, self.out_channels)
        self.bn2 = nn.BatchNorm2d(self.out_channels)
        self.relu2 = nn.ReLU()

    def forward(self, from_up, from_down):
        from_up = self.upconv(from_up)

        if self.merge_mode == 'concat':
            x = torch.cat((from_up, from_down), 1)
        else:
            x = from_up + from_down
        x = self.relu1(self.bn1(self.conv1(x)))
        x = self.relu2(self.bn2(self.conv2(x)))

        return x


class UNet(nn.Module):
    def __init__(self, n_channels=3, merge_mode='concat', up_mode='transpose'):
        super(UNet, self).__init__()
        self.n_chnnels = n_channels
        self.merge_mode = merge_mode
        self.up_mode = up_mode

        self.down1 = UNetDownBlock(self.n_chnnels, 64, 3, 1, 1)
        self.down2 = UNetDownBlock(64, 128, 4, 2, 1)
        self.down3 = UNetDownBlock(128, 256, 4, 2, 1)
        self.down4 = UNetDownBlock(256, 512, 4, 2, 1)
        self.down5 = UNetDownBlock(512, 512, 4, 2, 1)

        self.up1 = UNetUpBlock(512, 512, merge_mode=self.merge_mode, up_mode=self.up_mode)
        self.up2 = UNetUpBlock(512, 256, merge_mode=self.merge_mode, up_mode=self.up_mode)
        self.up3 = UNetUpBlock(256, 128, merge_mode=self.merge_mode, up_mode=self.up_mode)
        self.up4 = UNetUpBlock(128, 64, merge_mode=self.merge_mode, up_mode=self.up_mode)

        self.conv_final = nn.Sequential(conv(64, 3, 3, 1, 1), nn.Tanh())

    def forward(self, x):
        x1 = self.down1(x)
        x2 = self.down2(x1)
        x3 = self.down3(x2)
        x4 = self.down4(x3)
        x5 = self.down5(x4)

        x = self.up1(x5, x4)
        x = self.up2(x, x3)
        x = self.up3(x, x2)
        x = self.up4(x, x1)
        x = self.conv_final(x)

        return x

##############################################################
####################### RIAD Model ###########################
##############################################################
class RIAD(object):
    def __init__(self, **kwargs):
        n_channels = kwargs.get("n_channels", 3)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = UNet(n_channels=n_channels).to(self.device)
        self.k_value = kwargs.get("k_value", [2, 4, 8, 16])
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
        lr = kwargs.get("lr", 0.0001)
        epochs = kwargs.get("epochs", 300)
        optimizer_name = kwargs.get("optimizer", 'adam')
        scheduler_name = kwargs.get("scheduler", 'step')
        # k_value_ori = kwargs.get("k_value", [2, 4, 8, 16])
        alpha = kwargs.get("alpha", 1.0)
        belta = kwargs.get("belta", 1.0)
        gamma = kwargs.get("gamma", 1.0)
        batch_size = kwargs.get("batch_size", 4)
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
            optimizer = optim.Adam(filter(lambda p: p.requires_grad, self.model.parameters()), lr=lr, weight_decay=0.00001, amsgrad=True)
        elif (optimizer_name == 'sgd') or (optimizer_name == 'SGD'):
            optimizer = optim.SGD(filter(lambda p: p.requires_grad, self.model.parameters()), lr=lr, momentum=0.9, nesterov=True)
        elif (optimizer_name == 'radam') or (optimizer_name == 'RAdam'):
            optimizer = RAdam(filter(lambda p: p.requires_grad, self.model.parameters()), lr=lr, weight_decay=0.00001)
        elif (optimizer_name == 'adabelief') or (optimizer_name == 'Adabelief'):
            optimizer = AdaBelief(filter(lambda p: p.requires_grad, self.model.parameters()), lr=lr, weight_decay=0.00001, eps=1e-16, betas=(0.9,0.999), weight_decouple = True, rectify = True)
        else:
            raise ValueError('Could Only Support optimizer in [Adam, SGD].')
        
        if scheduler_name == 'step':
            scheduler = optim.lr_scheduler.StepLR(optimizer, int(0.1 * epochs), 0.5)
        elif scheduler_name == 'cosine':
            scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs, eta_min=1e-8)
        
        x_ref, _, _ = iter(train_dataloader).next()
        assert (len(x_ref.shape) == 4), 'input tensor should be 4-dim.'
        assert (x_ref.shape[2] == x_ref.shape[3]), 'Input height should be equal to width.'

        # img_size = x_ref.shape[2]
        ssim = SSIM_Loss()
        mse = nn.MSELoss(reduction='mean')
        msgms = MSGMS_Loss()
        
        epoch_time = AverageMeter()
        save_lowest = os.path.join(save_path, 'model_lowest_loss.pt')
        early_stop = EarlyStop(patience=int(0.1*epochs) if int(0.1*epochs) > 20 else 20, 
                                save_name=save_lowest)
        start_time = time.time()
        for epoch in range(0, epochs):
            self.model.train()
            l2_losses = AverageMeter()
            gms_losses = AverageMeter()
            ssim_losses = AverageMeter()
            # for (data, _, _) in tqdm(train_dataloader, '| training epoch %s |' % (epoch+1)):
            for (data) in tqdm(train_dataloader, '| training epoch %s |' % (epoch+1)):
                if type(data) != torch.Tensor:
                    if type(data) == list or type(data) == tuple:
                        data = data[0]
                        if type(data) != torch.Tensor:
                            raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                    else:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                optimizer.zero_grad()

                data = data.to(self.device)
                # generator mask
                img_size = data.size(-1)
                k_value = random.sample(self.k_value, 1)
                Ms_generator = gen_mask(k_value, 3, img_size)
                Ms = next(Ms_generator)

                inputs = [data * (torch.tensor(mask, requires_grad=False).to(self.device)) for mask in Ms]
                outputs = [self.model(x) for x in inputs]
                output = sum(map(lambda x, y: x * (torch.tensor(1 - y, requires_grad=False).to(self.device)), outputs, Ms))

                l2_loss = mse(data, output)
                gms_loss = msgms(data, output)
                ssim_loss = ssim(data, output)

                loss = gamma * l2_loss + alpha * gms_loss + belta * ssim_loss

                l2_losses.update(l2_loss.item(), data.size(0))
                gms_losses.update(gms_loss.item(), data.size(0))
                ssim_losses.update(ssim_loss.item(), data.size(0))
                loss.backward()
                optimizer.step()

            logger.info('Train Epoch: {} L2_Loss: {:.6f} GMS_Loss: {:.6f} SSIM_Loss: {:.6f}'.format(
                epoch, l2_losses.avg, gms_losses.avg, ssim_losses.avg))
            scheduler.step()

            val_loss = self._val(val_dataloader)
            if (early_stop(val_loss, self.model, optimizer)):
                break
                
            epoch_time.update(time.time() - start_time)
            start_time = time.time()

        self.est_thres(val_data, expect_fpr=expect_fpr)
    
    def _val(self, val_loader):
        self.model.eval()
        losses = AverageMeter()
        ssim = SSIM_Loss()
        mse = nn.MSELoss(reduction='mean')
        msgms = MSGMS_Loss()
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
            k_value = random.sample(self.k_value, 1)
            Ms_generator = gen_mask(k_value, 3, img_size)
            Ms = next(Ms_generator)
            inputs = [data * (torch.tensor(mask, requires_grad=False).to(self.device)) for mask in Ms]
            with torch.no_grad():
                outputs = [self.model(x) for x in inputs]
                output = sum(map(lambda x, y: x * (torch.tensor(1 - y, requires_grad=False).to(self.device)), outputs, Ms))

                l2_loss = mse(data, output)
                gms_loss = msgms(data, output)
                ssim_loss = ssim(data, output)

                loss = 1.0 * l2_loss + 1.0 * gms_loss + 1.0 * ssim_loss
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

        self.model.load_state_dict(remove_dataparallel(params))
        print('Pretrained weights from %s has been loaded.' %ckpt_path)
    
    def est_thres(self, val_data, expect_fpr=0.01, **kwargs):
        batch_size = kwargs.get("batch_size", 4)
        
        loader_kwargs = {'num_workers': 8, 'pin_memory': True} if (torch.cuda.is_available() and platform.system() == 'Linux') else {}
        val_dataloader = torch.utils.data.DataLoader(val_data, batch_size=int(4*batch_size), shuffle=False, **loader_kwargs)

        msgms_score = MSGMS_Score()
        self.model.eval()
        val_scores = []
        # for (data, _, _) in tqdm(val_dataloader,'|Estimating Threshold|'):
        for (data) in tqdm(val_dataloader,'|Estimating Threshold|'):
            if type(data) != torch.Tensor:
                if type(data) == list or type(data) == tuple:
                    data = data[0]
                    if type(data) != torch.Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
            score = 0
            with torch.no_grad():
                data = data.to(self.device)
                for k in self.k_value:
                    img_size = data.size(-1)
                    N = img_size // k
                    Ms_generator = gen_mask([k], 3, img_size)
                    Ms = next(Ms_generator)
                    inputs = [data * (torch.tensor(mask, requires_grad=False).to(self.device)) for mask in Ms]
                    outputs = [self.model(x) for x in inputs]
                    output = sum(map(lambda x, y: x * (torch.tensor(1 - y, requires_grad=False).to(self.device)), outputs, Ms))
                    score += msgms_score(data, output) / (N**2)

            score = score.squeeze().cpu().numpy()
            if score.ndim < 3:
                score = np.expand_dims(score, axis=0)
            for i in range(score.shape[0]):
                score[i] = gaussian_filter(score[i], sigma=7)

            val_scores.extend(score)

        val_scores = np.asarray(val_scores)
        self.val_max_as = val_scores.max()
        self.val_min_as = val_scores.min()

        val_scores = (val_scores - self.val_min_as) / (self.val_max_as - self.val_min_as)
        val_img_scores = val_scores.reshape(val_scores.shape[0], -1).max(axis=1)
        self.seg_thres = estimate_thred_with_fpr(val_scores, expect_fpr=expect_fpr)
        self.cls_thres = estimate_thred_with_fpr(val_img_scores, expect_fpr=expect_fpr)

    def predict(self, test_data, **kwargs):
        self.model.eval()
        msgms_score = MSGMS_Score()
        score = 0
        with torch.no_grad():
            data = test_data.to(self.device)
            for k in self.k_value:
                img_size = data.size(-1)
                N = img_size // k
                Ms_generator = gen_mask([k], 3, img_size)
                Ms = next(Ms_generator)
                inputs = [data * (torch.tensor(mask, requires_grad=False).to(self.device)) for mask in Ms]
                outputs = [self.model(x) for x in inputs]
                output = sum(map(lambda x, y: x * (torch.tensor(1 - y, requires_grad=False).to(self.device)), outputs, Ms))
                score += msgms_score(data, output) / (N**2)

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
