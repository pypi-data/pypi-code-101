import os
import tarfile
from PIL import Image
import cv2
from tqdm import tqdm
import urllib.request
import numpy as np
import torch
from torch.utils.data import Dataset
from torchvision import transforms as T
from random import choice

import numpy as np
import math
import cv2
import random
import os
import logging
from tqdm import tqdm
from collections import OrderedDict
from albumentations.pytorch import ToTensor
from albumentations import(
    Resize, Normalize, Compose,
    HorizontalFlip, VerticalFlip, GaussNoise
)
import skimage

def read_img(img_path, img_color='BGR'):
    if img_color == 'gray':
        im = cv2.imread(img_path, 0)
    elif img_color == 'BGR':
        im = cv2.imread(img_path)
    elif img_color == 'RGB':
        im = cv2.imread(img_path)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    return im

class Imagenetpatch(Dataset):
    '''
    Imagenet dataset, mainly used for self-supervised or knowledge distillation \
    to pre-train models.
    Contains transformations including randonm filp, random gray and normalize.
    '''
    def __init__(self, img_list, patch_size=65, batch_size=64, img_color='RGB'):
        super(Imagenetpatch, self).__init__()
        self.img_list = img_list
        self.size_list = np.arange(patch_size*4, 16*patch_size)
        self.ori_color = img_color
        self.path_size = patch_size
        self.transform = Compose([
            VerticalFlip(p=0.5),
            HorizontalFlip(p=0.5),
        ])
        self.totensor = T.Compose([
            T.RandomGrayscale(p=0.1),
            T.ToTensor(),
            T.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ])
        self.batch_size = batch_size
    
    def __len__(self):
        return int(self.batch_size * 100)

    def __getitem__(self, idx):
        pos_idx = np.random.randint(0, len(self.img_list))
        neg_idx = np.random.randint(0, len(self.img_list))
        while pos_idx == neg_idx:
            neg_idx = np.random.randint(0, len(self.img_list))
        anchor_img = read_img(self.img_list[pos_idx], img_color=self.ori_color)
        neg_img = read_img(self.img_list[neg_idx], img_color=self.ori_color)
        anchor_img = self._random_resize(anchor_img)
        neg_img = self._random_resize(neg_img)
        anchor_img = self.transform(image=anchor_img)['image']
        neg_img = self.transform(image=neg_img)['image']
        anchor_img, pos_img= self._random_crop(anchor_img)
        pos_img = GaussNoise(0.1, p=1)(image=pos_img)['image']
        # pos_img = skimage.util.random_noise(pos_img, mode='gaussian', clip=False, var=0.1)
        neg_img,_ = self._random_crop(neg_img)
        anchor_img, pos_img, neg_img=Image.fromarray(anchor_img), Image.fromarray(pos_img), Image.fromarray(neg_img)

        return [self.totensor(anchor_img), \
                self.totensor(pos_img), \
                self.totensor(neg_img)]
    
    def _random_resize(self,image):
        new_size = choice(self.size_list)
        image = cv2.resize(image, (new_size, new_size))
        return image
    
    def _random_crop(self, image):
        new_size = self.path_size
        h, w = image.shape[:2]
        try:
            y = min(max(0, np.random.randint(0, h - new_size)), h - new_size)
            x = min(max(0, np.random.randint(0, w - new_size)), w - new_size)
            image_anchor = image[y:y+new_size, x:x+new_size]
            y_plus = min(max(0, y + np.random.randint(-int((new_size-1)/4), int((new_size-1)/4))), h - new_size)
            x_plus = min(max(0, x + np.random.randint(-int((new_size-1)/4), int((new_size-1)/4))), w - new_size)
            image_plus = image[y_plus:y_plus+new_size, x_plus:x_plus+new_size]
            return image_anchor, image_plus
        except:
            return image, image

# if __name__ == "__main__":
#     dataset = Imagenetpatch()
#     print(dataset.size_list)