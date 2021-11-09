"""
MVTec Dataset code gently borrowed from
https://github.com/byungjae89/MahalanobisAD-pytorch/blob/master/src/datasets/mvtec.py
"""
import os
import tarfile
from PIL import Image
import cv2
from tqdm import tqdm
import urllib.request
import numpy as np
import mindspore
from ._transformations import centercrop_tranform

URL = 'ftp://guest:GU.205dldo@ftp.softronics.ch/mvtec_anomaly_detection/mvtec_anomaly_detection.tar.xz'
CLASS_NAMES = ['bottle', 'cable', 'capsule', 'carpet', 'grid',
               'hazelnut', 'leather', 'metal_nut', 'pill', 'screw',
               'tile', 'toothbrush', 'transistor', 'wood', 'zipper']
OBJECT = ['bottle', 'cable', 'capsule', 'hazelnut', 'metal_nut', 
            'pill', 'screw', 'toothbrush', 'transistor', 'zipper']
TEXTURE = ['carpet', 'grid', 'leather', 'tile', 'wood']
def read_img(img_path, img_color='BGR'):
    if img_color == 'gray':
        im = cv2.imread(img_path, 0)
    elif img_color == 'BGR':
        im = cv2.imread(img_path)
    elif img_color == 'RGB':
        im = cv2.imread(img_path)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    return im


class MVTecDataset():
    def __init__(self, data_path='../data', class_name='bottle', is_train=True,
                 resize=256, cropsize=256, transform=None, length=None, img_color='RGB'):
        # assert class_name in CLASS_NAMES, 'class_name: {}, should be in {}'.format(class_name, CLASS_NAMES)
        self.mvtec_folder_path = data_path
        self.class_name = class_name
        self.is_train = is_train
        if (isinstance(resize, list) or isinstance(resize, tuple)) and len(resize) == 2:
            self.resize = resize
        elif isinstance(resize, int):
            self.resize = (resize, resize)
        else:
            raise ValueError
        if (isinstance(cropsize, list) or isinstance(cropsize, tuple)) and len(cropsize) == 2:
            self.cropsize = cropsize
        elif isinstance(cropsize, int):
            self.cropsize = (cropsize, cropsize)
        else:
            raise ValueError


        self.length = length
        self.color = img_color
        # download dataset if not exist
        self.download()

        # load dataset
        self.x, self.y, self.mask = self.load_dataset_folder()

        # set transforms
        if transform is None:
            self.transform = centercrop_tranform(img_size=self.resize, 
                                                crop_size=self.cropsize,
                                                mean=[0.485, 0.456, 0.406],
                                                std=[0.229, 0.224, 0.225])
        else:
            self.transform = transform 

    def __getitem__(self, idx):
        if idx > len(self.x) - 1:
            idx = int(idx % len(self.x))
        x, y, mask = self.x[idx], self.y[idx], self.mask[idx]
        
        x = read_img(x, self.color)

        if y == 0:
            mask = np.zeros([self.cropsize[0], self.cropsize[1]])
        else:
            mask = cv2.imread(mask, 0)
            
        aug = self.transform(image=x, mask=mask)

        x = aug['image'].transpose((2, 0, 1)).astype(np.float32)
        if len(aug['mask'].shape) == 3:
            mask = aug['mask']
        else:
            mask = np.expand_dims(aug['mask'], 2)
        mask = mask.transpose((2, 0, 1)).astype(np.float32)/255.0
        return x, y, mask

    def __len__(self):
        if self.length is not None:
            return self.length
        else:
            return len(self.x)

    def load_dataset_folder(self):
        phase = 'train' if self.is_train else 'test'
        x, y, mask = [], [], []

        img_dir = os.path.join(self.mvtec_folder_path, self.class_name, phase)
        gt_dir = os.path.join(self.mvtec_folder_path, self.class_name, 'ground_truth')

        img_types = sorted(os.listdir(img_dir))
        for img_type in img_types:

            # load images
            img_type_dir = os.path.join(img_dir, img_type)
            if not os.path.isdir(img_type_dir):
                continue
            img_fpath_list = sorted([os.path.join(img_type_dir, f)
                                     for f in os.listdir(img_type_dir)
                                     if f.endswith('.png')])
            x.extend(img_fpath_list)

            # load gt labels
            if img_type == 'good':
                y.extend([0] * len(img_fpath_list))
                mask.extend([None] * len(img_fpath_list))
            else:
                y.extend([1] * len(img_fpath_list))
                gt_type_dir = os.path.join(gt_dir, img_type)
                img_fname_list = [os.path.splitext(os.path.basename(f))[0] for f in img_fpath_list]
                gt_fpath_list = [os.path.join(gt_type_dir, img_fname + '_mask.png')
                                 for img_fname in img_fname_list]
                mask.extend(gt_fpath_list)

        assert len(x) == len(y), 'number of x and y should be same'

        return list(x), list(y), list(mask)

    def download(self):
        """Download dataset if not exist"""

        if not os.path.exists(self.mvtec_folder_path):
            tar_file_path = self.mvtec_folder_path + '.tar.xz'
            if not os.path.exists(tar_file_path):
                download_url(URL, tar_file_path)
            print('unzip downloaded dataset: %s' % tar_file_path)
            tar = tarfile.open(tar_file_path, 'r:xz')
            tar.extractall(self.mvtec_folder_path)
            tar.close()
        return


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)