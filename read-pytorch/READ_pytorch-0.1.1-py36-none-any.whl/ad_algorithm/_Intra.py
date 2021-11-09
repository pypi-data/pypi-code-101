""" Implementation of the Semi-Orth algorithm for anomaly localization and detection
This method is proposed in the paper:
    'Inpainting Transformer for Anomaly Detection'
The code about creating training sequence is adpated from:
    https://github.com/jhy12/inpainting-transformer
"""
from re import L
import torch 
from torch import nn
import torch.nn.functional as F
from tqdm import tqdm
from functools import partial
import random
import os
import cv2
import time
import logging
import platform
import numpy as np
import kornia.filters as filters
import torch.optim as optim
from torchvision.utils import save_image
from scipy.ndimage import gaussian_filter
from READ_pytorch.utils import set_logger, remove_dataparallel, AverageMeter, EarlyStop
from READ_pytorch.losses import SSIMLoss, MSGMSLoss
from adabelief_pytorch import AdaBelief
from READ_pytorch.optimizer import RAdam
from READ_pytorch.utils import estimate_thred_with_fpr
from itertools import repeat as itrepeat
import collections.abc
from einops import rearrange, repeat
from einops.layers.torch import Rearrange
import copy

##################################
# Comments Notification 
# B: batch size
# C: channels
# S: image size
# L: side length of windows  
# D: dimensions of patch embedings
# K: patch size
# n: numbers of head
###################################

# From PyTorch internals
def _ntuple(n):
    def parse(x):
        if isinstance(x, collections.abc.Iterable):
            return x
        return tuple(itrepeat(x, n))
    return parse


to_1tuple = _ntuple(1)
to_2tuple = _ntuple(2)
to_3tuple = _ntuple(3)
to_4tuple = _ntuple(4)
to_ntuple = _ntuple

def transpose_view(x, n):
    return x.view(x.size(0),x.size(1),n,-1).transpose(1,2).contiguous()

def drop_path(x, drop_prob: float = 0., training: bool = False):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).
    This is the same as the DropConnect impl I created for EfficientNet, etc networks, however,
    the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for
    changing the layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use
    'survival rate' as the argument.
    """
    if drop_prob == 0. or not training:
        return x
    keep_prob = 1 - drop_prob
    shape = (x.shape[0],) + (1,) * (x.ndim - 1)  # work with diff dim tensors, not just 2D ConvNets
    random_tensor = keep_prob + torch.rand(shape, dtype=x.dtype, device=x.device)
    random_tensor.floor_()  # binarize
    output = x.div(keep_prob) * random_tensor
    return output


class DropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample  (when applied in main path of residual blocks).
    """
    def __init__(self, drop_prob=None):
        super(DropPath, self).__init__()
        self.drop_prob = drop_prob

    def forward(self, x):
        return drop_path(x, self.drop_prob, self.training)

class Mlp(nn.Module):
    """ MLP as used in Vision Transformer, MLP-Mixer and related networks
    """
    def __init__(self, in_features, hidden_features=None, out_features=None, act_layer=nn.GELU, drop=0.):
        super().__init__()
        out_features = out_features or in_features
        hidden_features = hidden_features or in_features
        self.fc1 = nn.Linear(in_features, hidden_features)
        self.act = act_layer()
        self.fc2 = nn.Linear(hidden_features, out_features)
        self.drop = nn.Dropout(drop)

    def forward(self, x):
        x = self.fc1(x)
        x = self.act(x)
        x = self.drop(x)
        x = self.fc2(x)
        x = self.drop(x)
        return x

class PatchEmbed(nn.Module):
    """ 2D Image to Patch Embedding
    """
    def __init__(self, img_size=224, patch_size=16, in_chans=3, embed_dim=768, norm_layer=None, flatten=True):
        super().__init__()
        img_size = to_2tuple(img_size)
        patch_size = to_2tuple(patch_size)
        self.img_size = img_size
        self.patch_size = patch_size
        self.grid_size = (img_size[0] // patch_size[0], img_size[1] // patch_size[1])
        self.num_patches = self.grid_size[0] * self.grid_size[1]
        self.flatten = flatten

        self.proj = nn.Conv2d(in_chans, embed_dim, kernel_size=patch_size, stride=patch_size)
        self.norm = norm_layer(embed_dim) if norm_layer else nn.Identity()

    def forward(self, x):
        B, C, H, W = x.shape
        assert H == self.img_size[0] and W == self.img_size[1], \
            f"Input image size ({H}*{W}) doesn't match model ({self.img_size[0]}*{self.img_size[1]})."
        x = self.proj(x)
        if self.flatten:
            x = x.flatten(2).transpose(1, 2)  # BCHW -> BNC
        x = self.norm(x)
        return x

class Attention(nn.Module):
    def __init__(self, dim, num_heads=8, qkv_bias=False, attn_drop=0., proj_drop=0.):
        super().__init__()
        self.num_heads = num_heads
        head_dim = dim // num_heads
        self.scale = head_dim ** -0.5

        self.qkv = nn.Linear(dim, dim * 3, bias=qkv_bias)
        self.attn_drop = nn.Dropout(attn_drop)
        self.proj = nn.Linear(dim, dim)
        self.proj_drop = nn.Dropout(proj_drop)

    def forward(self, x):
        B, N, C = x.shape
        qkv = self.qkv(x).reshape(B, N, 3, self.num_heads, C // self.num_heads).permute(2, 0, 3, 1, 4)
        q, k, v = qkv[0], qkv[1], qkv[2]   # make torchscript happy (cannot use tensor as tuple)
        attn = (q @ k.transpose(-2, -1)) * self.scale
        attn = attn.softmax(dim=-1)
        attn = self.attn_drop(attn)

        x = (attn @ v).transpose(1, 2).reshape(B, N, C)
        x = self.proj(x)
        x = self.proj_drop(x)
        return x

class MFSA(nn.Module):
    def __init__(self, dim=512, num_heads=8, attn_drop=0., proj_drop=0.):
        super().__init__()
        self.n = num_heads
        self.w_q = Mlp(dim, dim*2, dim//2)
        self.w_k = Mlp(dim, dim*2, dim//2)
        self.w_v = nn.Linear(dim, num_heads*dim//num_heads, bias=False)
        self.attn_drop = nn.Dropout(attn_drop)
        self.proj = nn.Linear(dim, dim)
        self.proj_drop = nn.Dropout(proj_drop)
        # self.scale = (dim//2) ** -0.5

    def forward(self, x):
        B, N, C = x.shape
        q = transpose_view(self.w_q(x), self.n)                             # (B, n, L^2, D'/n)  D'=D/2
        k = transpose_view(self.w_k(x), self.n)                             # (B, n, L^2, D'/n)  D'=D/2
        v = transpose_view(self.w_v(x), self.n)                             # (B, n, L^2, D/n)   
        # attn = torch.matmul(q/q.size()[-1]**0.5, k.transpose(2, 3))         # (B, n, L^2, L^2)
        # attn = F.softmax(attn, dim=-1)                                      
        # o = torch.matmul(attn, v)                                           # (B, n, L^2, D/n)
        attn = (q @ k.transpose(-2, -1)) * (q.size()[-1]**-0.5)
        attn = attn.softmax(dim=-1)
        attn = self.attn_drop(attn)

        x = (attn @ v).transpose(1, 2).reshape(B, N, C)
        x = self.proj(x)
        x = self.proj_drop(x)

        return x

class TrfBlock(nn.Module):

    def __init__(self, dim, num_heads=8, mlp_ratio=4., 
                drop=0., drop_path=0., act_layer=nn.GELU, 
                norm_layer=nn.LayerNorm):
        super(TrfBlock, self).__init__()
        self.norm1 = norm_layer(dim)
        self.attn = MFSA(dim, num_heads=num_heads)
        # NOTE: drop path for stochastic depth, we shall see if this is better than dropout here
        self.drop_path = DropPath(drop_path) if drop_path > 0. else nn.Identity()
        self.norm2 = norm_layer(dim)
        mlp_hidden_dim = int(dim * mlp_ratio)
        self.mlp = Mlp(in_features=dim, hidden_features=mlp_hidden_dim, act_layer=act_layer, drop=drop)
        self.size = dim

    def forward(self, x):
        x = x + self.drop_path(self.attn(self.norm1(x)))
        x = x + self.drop_path(self.mlp(self.norm2(x)))
        return x

# class FixedPositionalEncoding(nn.Module):
#     def __init__(self, embedding_dim, max_length):
#         super().__init__()

#         pe = torch.zeros(max_length, embedding_dim)
#         position = torch.arange(0, max_length, dtype=torch.float).unsqueeze(1)
#         div_term = torch.exp(
#             torch.arange(0, embedding_dim, 2).float()
#             * (-torch.log(torch.tensor(10000.0)) / embedding_dim)
#         )
#         pe[:, 0::2] = torch.sin(position * div_term)
#         pe[:, 1::2] = torch.cos(position * div_term)
#         pe = pe.unsqueeze(0).transpose(0, 1)
#         self.pe = pe

#     def forward(self, x):
#         x = x + self.pe[: x.size(0), :].to(x.device)
#         return x

def FixedPositionalEncoding(embedding_dim, max_length):
    pe = torch.zeros(max_length, embedding_dim)
    position = torch.arange(0, max_length, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(
        torch.arange(0, embedding_dim, 2).float()
        * (-torch.log(torch.tensor(10000.0)) / embedding_dim)
    )
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    pe = pe.unsqueeze(0)
    return pe

class path_emb(nn.Module):
    def __init__(self, patch_size=16, in_chans=3, embed_dim=512, img_size=256, flatten=True):
        super().__init__()
        img_size = to_2tuple(img_size)
        patch_size = to_2tuple(patch_size)
        self.img_size = img_size
        self.patch_size = patch_size
        self.grid_size = (img_size[0] // patch_size[0], img_size[1] // patch_size[1])
        self.num_patches = self.grid_size[0] * self.grid_size[1]
        self.flatten = flatten
        patch_dim = in_chans * patch_size[0] * patch_size[1]
        self.rearrange = Rearrange('b n c p1 p2 -> b n (c p1 p2)', p1 = patch_size[0], p2 = patch_size[1])
        self.linear = nn.Linear(patch_dim, embed_dim)
        self.patch_range=[]
        self._get_patches()

    def _get_patches(self):
        for j in range(self.grid_size[0]):
            for i in range(self.grid_size[1]):
                self.patch_range.append([[j*self.patch_size[0], j*self.patch_size[0]+self.patch_size[0]],[i*self.patch_size[1], i*self.patch_size[1]+self.patch_size[1]]])

    def forward(self, x):

        B, C, H, W = x.shape
        assert H == self.img_size[0] and W == self.img_size[1], \
            f"Input image size ({H}*{W}) doesn't match model ({self.img_size[0]}*{self.img_size[1]})."

        patch_list = []
        for y_range, x_range in self.patch_range:
            # patch_cache = torch.unsqueeze(x[:,:,y_range[0]:y_range[1], x_range[0]:x_range[1]], dim=1)
            patch_cache = x[:,:,y_range[0]:y_range[1], x_range[0]:x_range[1]]
            patch_list.append(patch_cache)
        x = torch.stack(patch_list, dim=1)
        x = self.rearrange(x)
        x = self.linear(x)
        return x


def tensor2nparr(tensor):
    np_arr = tensor.detach().cpu().numpy()
    np_arr = (np.moveaxis(np_arr, 1, 3)*255).astype(np.uint8)
    return np_arr

class TrfNet(nn.Module):
    def __init__(self, embed_dim=512, channels=3, patch_size=16, window_length=7, stack_num=13, grid_size_max=16, pos_mode='local', pool='mean'):

        super(TrfNet, self).__init__()

        self.patchem = path_emb(patch_size=patch_size, in_chans=channels, embed_dim=embed_dim, img_size=patch_size*window_length)
        self.K = patch_size
        self.L = window_length
        self.pool = pool
        self.C = channels
        self.embed_dim = embed_dim
        self.x_inpaint = nn.Parameter(torch.randn(1, 1, embed_dim))
        self.pos_embedding_loc = nn.Parameter(torch.randn(1, self.L*self.L, embed_dim))
        self.pos_embedding_glb = nn.Parameter(torch.randn(1, grid_size_max*grid_size_max, embed_dim)) # every loc in the image has a 512 position embedding
        self.lin_proj = nn.Linear(self.K*self.K*self.C, embed_dim)
        layer = TrfBlock(dim=embed_dim)
        self.layers = self._clones(layer, stack_num)
        self.norm = nn.LayerNorm(layer.size)
        self.Proj = nn.Linear(embed_dim, channels*patch_size*patch_size)

        self.mse = nn.MSELoss(reduction='mean')
        self.msgms = MSGMSLoss(num_scales=3, in_channels=3)
        self.ssim = SSIMLoss(kernel_size=11, sigma=1.5)


    def forward(self, x):
        assert x.shape[-1] == self.embed_dim, 'Embed dim should be the same.'

        # residual = []
        # for block in self.DownBlockList:
        #     x = block(x)
        #     residual.append(x)
        # x = self.Neck(x)
        # for j in range(len(self.UpBlockList)):
        #     x = self.UpBlockList[j](x+residual[-j-1])
        layers = []
        for i, layer in enumerate(self.layers):
            if i > len(self.layers)/2:
                x = x + layers[len(self.layers)-i]
            x = layer(x)
            layers.append(x)
        x = self.norm(x)
        x = x.mean(dim = 1) if self.pool == 'mean' else x[:, 0]
        x = self.Proj(x)
        return x

    def _clones(self, module, N):
        return nn.ModuleList([copy.deepcopy(module) for _ in range(N)])

    def _train_one_batch(self, batch_img):
        x, gt = self._prepare_train_batch(batch_img, self.x_inpaint, self.pos_embedding_glb, self.lin_proj)

        recon = self.forward(x)
        gt = gt.reshape(gt.size(0), self.C, self.K, self.K)
        recon = recon.reshape(recon.size(0), self.C, self.K, self.K)

        loss, _, _ = self._compute_loss(recon, gt)
        return loss
    
    def _prepare_train_batch(self, batch_img, x_inpaint, pos_embedding_glb, lin_proj):
        # get img size
        B, C, H, W = batch_img.size()

        # confusing notations.. we use M x N not N x M for original papers.
        M = int(H / self.K)
        N = int(W / self.K)

        # We start from 1~M*N and -1 at the pos_embedding_glb_idx -= 1 to make the range 0~M*N-1
        pos_embedding_glb_grid = torch.arange(1, N*M+1, dtype=torch.long).reshape(M, N)
        
        # sampled_rs_idx : [B, 2] / sampled_rs_idx[b] = [r, s] (0 <= r <= M-L / 0 <= s <= N-L)
        sampled_rs_idx = torch.cat([torch.randint(0, M-self.L+1, (B,1)), torch.randint(0, N-self.L+1, (B,1))], dim=1)

        # pos_embedding_glb_idx : [B, L*L] (size : L*L, but 0 <= value < M*N)
        # sampled subgrid's positional embedding index : i, j(sampled_rs_idx) -> i*N + j(pos_embedding_glb_grid)
        pos_embedding_glb_idx = torch.vstack([pos_embedding_glb_grid[r:r+self.L, s:s+self.L].unsqueeze(0) for r, s in sampled_rs_idx]).unsqueeze(dim=1)

        pos_embedding_glb_idx = pos_embedding_glb_idx.reshape(pos_embedding_glb_idx.size(0), -1)
        pos_embedding_glb_idx -= 1

        # sampled subgrid's values...
        batch_subgrid = torch.vstack([batch_img[l,:,self.K*r:self.K*(r+self.L),self.K*s:self.K*(s+self.L)].unsqueeze(0) for l, (r, s) in enumerate(sampled_rs_idx)])

        # batch subgrid : [B, C, L*K, L*K] / corresponding positional embedding index(pos_embedding_glb_idx) : [B, L, L] (value range : 1~L**2)
        # now... convert to transformer input formats..
        # pos_embedding_glb_idx : [B, L*L]
        # pos_embedding_glb : [1, M*N, d_model]
        # pos_embedding : [B, L*L, d_model]

        pos_embedding = torch.zeros((B, self.L*self.L, pos_embedding_glb.size(2))).to(pos_embedding_glb.device)

        for b in range(B):
            for n in range(pos_embedding_glb_idx.size(1)):
                pos_embedding[b,n,:] = pos_embedding_glb[:,pos_embedding_glb_idx[b, n],:]
                
        #pos_embedding = pos_embedding_glb[pos_embedding_glb_idx]
        # h, w : L
        batch_subgrid_flatten = rearrange(batch_subgrid, 'b c (h p1) (w p2) -> b (h w) (p1 p2 c)', p1=self.K, p2=self.K)

        # inpaint index
        # sampled_tu_idx : [B]
        # it extracts from the flattened array with hidden dimension 
        sampled_tu_idx = torch.randint(0, self.L*self.L, (B,))
        sampled_tu_idx_one_hot = F.one_hot(sampled_tu_idx, self.L*self.L)

        sampled_tu_idx_T = sampled_tu_idx_one_hot.bool()
        sampled_tu_idx_F = torch.logical_not(sampled_tu_idx_T)

        
        batch_subgrid_inpaint = batch_subgrid_flatten[sampled_tu_idx_T]

        pos_embedding_inpaint = pos_embedding[sampled_tu_idx_T].unsqueeze(1)

        batch_subgrid_emb_input = batch_subgrid_flatten[sampled_tu_idx_F].reshape(B, self.L*self.L-1, self.K*self.K*C)
        pos_embedding_emb_input = pos_embedding[sampled_tu_idx_F].reshape(B, self.L*self.L-1, -1)

        # concat at seq dimension
        batch_subgrid_input = torch.cat([x_inpaint + pos_embedding_inpaint, lin_proj(batch_subgrid_emb_input) + pos_embedding_emb_input], dim=1)
    
        return batch_subgrid_input, batch_subgrid_inpaint

    def _infer_one_image(self, image):
        image_recon, gt, loss = self._process_infer_image(image)
        _, msgms_map, _ = self._compute_loss(image_recon, gt)

        return image_recon, gt, loss, msgms_map

    def _process_infer_image(self, image):
        patches_recon = []
        patches_gt = []
        patches_loss = []
        # get img size
        B, C, H, W = image.size()
        assert B == 1
        # confusing notations.. we use M x N not N x M for original papers.
        M = int(H / self.K)
        N = int(W / self.K)

        subgrid_inputs = []
        subgrid_outputs = []
        for t in range(M):
            for u in range(N):
                r = self._g(t) - max(0, self._g(t) + self.L - M - 1)
                s = self._g(u) - max(0, self._g(u) + self.L - N - 1)

                subgrid_input, subgrid_inpaint = self._process_subgrid(image, self.x_inpaint, self.pos_embedding_glb, self.lin_proj, M, N, r, s, t, u)
                subgrid_inputs.append(subgrid_input)
                subgrid_outputs.append(subgrid_inpaint)

        subgrid_inputs = torch.vstack(subgrid_inputs)
        subgrid_outputs = torch.vstack(subgrid_outputs)
        with torch.no_grad():
            patches_recon = self.forward(subgrid_inputs)
            image_recon = self._combine_recon_patches(patches_recon, M, N)
            gt = self._combine_recon_patches(subgrid_outputs, M, N)
            loss = self._compute_loss(image_recon, gt)[0]

        return image_recon, gt, loss
        #         patch_recon = self.forward(subgrid_input)
        #         patches_recon.append(patch_recon)
        #         patches_gt.append(subgrid_inpaint)

        #         p_recon_r = patch_recon.reshape(patch_recon.size(0), self.C, self.K, self.K)
        #         p_gt_r = subgrid_inpaint.reshape(subgrid_inpaint.size(0), self.C, self.K, self.K)
        #         patches_loss.append(self._compute_loss(p_recon_r, p_gt_r)[0])

        # image_recon = self._combine_recon_patches(patches_recon, M, N)
        # gt = self._combine_recon_patches(patches_gt, M, N)
        # loss = torch.mean(torch.tensor(patches_loss)) / B
        # return image_recon, gt, loss

    def _process_subgrid(self, image, x_inpaint, pos_embedding_glb, lin_proj, M, N, r, s, t, u):
        # change r, s range from 1 <= r, s <= M-L+1, N-L+1
        #                     to 0 <= r, s <= M-L, N-L
        r = min(max(0, r-1), M-self.L)
        s = min(max(0, s-1), N-self.L)
        B, C, H, W =image.size()
        # subgrid -> [1, C, K*L, K*L]
        subgrid = image[:,:,self.K*r:self.K*(r+self.L),self.K*s:self.K*(s+self.L)]
        # subgrid_flatten : [1, L*L, K*K*C]
        subgrid_flatten = rearrange(subgrid, 'b c (h p1) (w p2) -> b (h w) (p1 p2 c)', p1=self.K, p2=self.K)

        # pos_embedding_glb_idx : [1, L*L]
        pos_embedding_glb_grid = torch.arange(1, M*N+1, dtype=torch.long).reshape(M, N)
        pos_embedding_glb_idx = pos_embedding_glb_grid[r:r+self.L, s:s+self.L].unsqueeze(0)
        pos_embedding_glb_idx = pos_embedding_glb_idx.reshape(pos_embedding_glb_idx.size(0), -1)
        pos_embedding_glb_idx -= 1

        # pos_embedding_grid : [1, L*L, d_model]
        pos_embedding = torch.zeros(1, self.L*self.L, pos_embedding_glb.size(2)).to(pos_embedding_glb.device)
        for n in range(pos_embedding_glb_idx.size(1)):
            pos_embedding[:,n,:] = pos_embedding_glb[:,pos_embedding_glb_idx[:,n],:]

        # r, s, t, u ... M x N
        # t, u : 0 <= t <= M / 0 <= u <= n

        # tu_1d_idx : 0 <= val < M*N
        # but it should be shape in L*L
        tu_1d_idx = torch.tensor([(t-r) * self.L + (u-s)], dtype=torch.long)

        tu_one_hot = F.one_hot(tu_1d_idx, self.L*self.L)
        tu_idx_T = tu_one_hot.bool()
        tu_idx_F = torch.logical_not(tu_idx_T)

        subgrid_inpaint = subgrid_flatten[tu_idx_T]
        pos_embedding_inpaint = pos_embedding[tu_idx_T].unsqueeze(1)

        subgrid_emb_input = subgrid_flatten[tu_idx_F].reshape(B, self.L*self.L-1, self.K*self.K*C)
        pos_embedding_emb_input = pos_embedding[tu_idx_F].reshape(B, self.L*self.L-1, -1)

        subgrid_input = torch.cat([x_inpaint + pos_embedding_inpaint, lin_proj(subgrid_emb_input) + pos_embedding_emb_input], dim=1)
        return subgrid_input, subgrid_inpaint

    # def _combine_recon_patches(self, patch_list, M, N):
    #     # patch_list : list of M*N [1, K*K*C] tensor
    #     # patches_concat : [M*N, 1, K*K*C]
    #     patch_list = [x.unsqueeze(0) for x in patch_list]
    #     patches_concat = torch.cat(patch_list, dim=0)
    #     # patches_concat : [1, M*N, K*K*C]
    #     patches_concat = patches_concat.permute(1, 0, 2)
    #     # recon_image : [1, C, H, W]
    #     recon_image = rearrange(patches_concat, 'b (h w) (p1 p2 c) -> b c (h p1) (w p2) ', h = M, w = N, p1=self.K, p2=self.K)
    #     return recon_image

    def _combine_recon_patches(self, patch_list, M, N):
        # patch_list : list of M*N [1, K*K*C] tensor
        # patches_concat : [M*N, 1, K*K*C]

        # patch_list = [x.unsqueeze(0) for x in patch_list]
        # patches_concat = torch.cat(patch_list, dim=0)
        # patches_concat : [1, M*N, K*K*C]
        patches_concat = patch_list.unsqueeze(0)
        # patches_concat = patches_concat.permute(1, 0, 2)
        # recon_image : [1, C, H, W]
        recon_image = rearrange(patches_concat, 'b (h w) (p1 p2 c) -> b c (h p1) (w p2) ', h = M, w = N, p1= self.K, p2=self.K)
        return recon_image

    def _compute_loss(self, patch_recon, patch_gt):
        mse_loss = self.mse(patch_gt, patch_recon)
        msgms_loss, msgms_map = self.msgms(patch_gt, patch_recon)
        ssim_loss, ssim_map = self.ssim(patch_gt, patch_recon)
        #total_loss = mse_loss + 0.01 * msgms_loss + 0.01 * ssim_loss 

        total_loss = mse_loss + msgms_loss + ssim_loss 
        return total_loss, msgms_map, ssim_map

    def _g(self, c):
        return max(1, c-int(self.L/2))

class InTra(object):
    def __init__(self, **kwargs):
        self.C = kwargs.get("n_channels", 3)
        self.device = kwargs.get("device", torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
        self.K = kwargs.get("patch_size", 16)
        self.L = kwargs.get("side_length", 7)
        assert (self.L - 1) % 2 == 0, 'side length should be a odd number'
        self.S = kwargs.get("image_size", 256)
        self.embed_dim = kwargs.get("embed_dim", 512)
        self.G = self.S//self.K

        self.model = TrfNet(embed_dim=self.embed_dim, channels=self.C, patch_size = self.K, window_length = self.L, grid_size_max = self.G).to(self.device)
        self.val_max_as = None
        self.val_min_as = None
        self.seg_thres = None
        self.cls_thres = None
        self.ref_map = None
    
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

        # train_data_cat = train_data
        # for i in range(10): # 600 windows per image
        #     train_data_cat = torch.utils.data.ConcatDataset([train_data_cat, train_data])

        train_dataloader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True, **loader_kwargs)
        val_dataloader = torch.utils.data.DataLoader(val_data, batch_size=1, shuffle=True, **loader_kwargs)

        if (optimizer_name == 'adam') or (optimizer_name == 'Adam'):
            optimizer = optim.Adam(filter(lambda p: p.requires_grad, self.model.parameters()), lr=lr, weight_decay=0.00001, amsgrad=True)
        elif (optimizer_name == 'sgd') or (optimizer_name == 'SGD'):
            optimizer = optim.SGD(filter(lambda p: p.requires_grad, self.model.parameters()), lr=lr, momentum=0.9, nesterov=True)
        elif (optimizer_name == 'radam') or (optimizer_name == 'RAdam'):
            optimizer = RAdam(filter(lambda p: p.requires_grad, self.model.parameters()), lr=lr, weight_decay=0.00001)
        elif (optimizer_name == 'adabelief') or (optimizer_name == 'Adabelief'):
            optimizer = AdaBelief(filter(lambda p: p.requires_grad, self.model.parameters()), lr=lr, weight_decay=0.00001, eps=1e-16, betas=(0.9,0.999), weight_decouple = True, rectify = True)
        elif (optimizer_name == 'adamw') or (optimizer_name == 'AdamW'):
            optimizer = optim.AdamW(filter(lambda p: p.requires_grad, self.model.parameters()), lr=lr)
        else:
            raise ValueError('Could Only Support optimizer in [Adam, SGD].')
        if scheduler_name == 'step':
            scheduler = optim.lr_scheduler.StepLR(optimizer, int(0.1 * epochs), 0.3)
        elif scheduler_name == 'cosine':
            scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs, eta_min=1e-8)

        x_ref, _, _ = iter(train_dataloader).next()
        assert (len(x_ref.shape) == 4), 'input tensor should be 4-dim.'
        assert (x_ref.shape[2] == x_ref.shape[3]), 'Input height should be equal to width.'

        # img_size = x_ref.shape[2]
        ssim =  SSIMLoss(kernel_size=11, sigma=1.5)
        mse = nn.MSELoss(reduction='mean')
        msgms = MSGMSLoss(num_scales=3, in_channels=3)
        
        epoch_time = AverageMeter()
        save_lowest = os.path.join(save_path, 'model_lowest_loss.pt')
        early_stop = EarlyStop(patience=int(0.1*epochs) if int(0.1*epochs) > 20 else 20, 
                                save_name=save_lowest)
        start_time = time.time()
        save_name = os.path.join(save_path, 'model.pt')
        val_loss_min = 1e10
        for epoch in range(0, epochs):
            self.model.train()
            l2_losses = AverageMeter()
            gms_losses = AverageMeter()
            ssim_losses = AverageMeter()
            losses = AverageMeter()
            # for (data, _, _) in tqdm(train_dataloader, '| training epoch %s |' % (epoch+1)):
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

                loss = self.model._train_one_batch(data)
                losses.update(loss.item(), data.size(0))
                loss.backward()
                optimizer.step()

            # logger.info('Train Epoch: {} L2_Loss: {:.6f} GMS_Loss: {:.6f} SSIM_Loss: {:.6f}'.format(
            #     epoch, l2_losses.avg, gms_losses.avg, ssim_losses.avg))
            logger.info('Train Epoch: {} Loss: {:.6f}'.format(
                epoch, losses.avg))
            scheduler.step()
            if (epoch) % int(0.01 * epochs) == 0:
                val_loss = self._val(val_dataloader)
                logger.info(f'Validation loss at Epoch {epoch} is {val_loss:.6f})')
                if val_loss < val_loss_min:
                    val_loss_min = val_loss
                    logger.info(f'Lowest Validation loss decreased ({val_loss_min:.6f} --> {val_loss:.6f}).')

            epoch_time.update(time.time() - start_time)
            start_time = time.time()
        
        self._get_ref_map(train_data)
        self.est_thres(val_data, expect_fpr=expect_fpr)
        self._save_checkpoint(save_name)

    def _val(self, val_loader):
        self.model.eval()
        losses = AverageMeter()
        ssim =  SSIMLoss(kernel_size=11, sigma=1.5)
        mse = nn.MSELoss(reduction='mean')
        msgms = MSGMSLoss(num_scales=3, in_channels=3)

        for (data) in tqdm(val_loader):
            if type(data) != torch.Tensor:
                if type(data) == list or type(data) == tuple:
                    data = data[0]
                    if type(data) != torch.Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')

            data = data.to(self.device)
            with torch.no_grad():
                _, _, loss, _ =  self.model._infer_one_image(data)
                losses.update(loss.item(), data.size(0))

        return losses.avg

    def _get_ref_map(self, train_data, **kwargs):
        batch_size = kwargs.get("batch_size", 1)

        loader_kwargs = {'num_workers': 8, 'pin_memory': True} if (torch.cuda.is_available() and platform.system() == 'Linux') else {}
        train_dataloader = torch.utils.data.DataLoader(train_data, batch_size=int(batch_size), shuffle=False, **loader_kwargs)

        self.model.eval()
        train_num = 0
        train_scores = []
        for (data) in tqdm(train_dataloader):
            if type(data) != torch.Tensor:
                if type(data) == list or type(data) == tuple:
                    data = data[0]
                    if type(data) != torch.Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
            B, C, H, W = data.shape
            data = data.to(self.device)
            with torch.no_grad():
                image_recon, gt, loss, msgms_map =  self.model._infer_one_image(data)
                score = msgms_map.squeeze().cpu().numpy()
            if score.ndim < 3:
                score = np.expand_dims(score, axis=0)
            for i in range(score.shape[0]):
                score[i] = 1 - gaussian_filter(score[i], sigma=7)
            
            train_scores.extend(score)

        train_scores = np.asarray(train_scores)
        self.ref_map = np.mean(train_scores, axis=0)
            
    def est_thres(self, val_data, expect_fpr=0.01, **kwargs):
        batch_size = kwargs.get("batch_size", 1)

        loader_kwargs = {'num_workers': 8, 'pin_memory': True} if (torch.cuda.is_available() and platform.system() == 'Linux') else {}
        val_dataloader = torch.utils.data.DataLoader(val_data, batch_size=int(batch_size), shuffle=False, **loader_kwargs)

        self.model.eval()
        # losses = AverageMeter()
        val_scores = []
        for (data) in tqdm(val_dataloader):
            if type(data) != torch.Tensor:
                if type(data) == list or type(data) == tuple:
                    data = data[0]
                    if type(data) != torch.Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')

            data = data.to(self.device)
            with torch.no_grad():
                image_recon, gt, loss, msgms_map =  self.model._infer_one_image(data)
                score = msgms_map.squeeze().cpu().numpy()
            
            if score.ndim < 3:
                score = np.expand_dims(score, axis=0)
            for i in range(score.shape[0]):
                score[i] = 1 - gaussian_filter(score[i], sigma=7)
                score[i] = (score[i] - self.ref_map) ** 2
            
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
        score = 0
        with torch.no_grad():
            data = test_data.to(self.device)
            image_recon, gt, loss, msgms_map =  self.model._infer_one_image(data)
            score = msgms_map.squeeze().cpu().numpy()
            
        if score.ndim < 3:
            score = np.expand_dims(score, axis=0)
        for i in range(score.shape[0]):
            score[i] = 1 - gaussian_filter(score[i], sigma=7)
            score[i] = (score[i] - self.ref_map) ** 2

        if (self.val_max_as is not None) and (self.val_min_as is not None):
            # print('Normalizing!')
            score = (score - self.val_min_as) / (self.val_max_as - self.val_min_as)

        img_score = score.reshape(score.shape[0], -1).max(axis=1)

        return img_score, score

    def load_weights(self, ckpt_path):
        if torch.cuda.is_available():
            params = torch.load(ckpt_path)
        else:
            params = torch.load(ckpt_path, map_location='cpu')
        try:
            self.ref_map = params['ref_map'] 
            self.val_max_as = params['val_max_as']
            self.val_min_as = params['val_min_as']
            self.seg_thres = params['seg_thres']
            self.cls_thres = params['cls_thres']
            params = params["state_dict"]
        except:
            params = params

        self.model.load_state_dict(remove_dataparallel(params))
        print('Pretrained weights from %s has been loaded.' %ckpt_path)

    def _save_checkpoint(self, save_name):
        '''Saves model when validation loss decrease.'''
        state = {'state_dict': self.model.state_dict(), 'ref_map': self.ref_map, 'val_max_as': self.val_max_as, 'val_min_as': self.val_min_as, 'seg_thres': self.seg_thres, 'cls_thres': self.cls_thres}
        torch.save(state, save_name)