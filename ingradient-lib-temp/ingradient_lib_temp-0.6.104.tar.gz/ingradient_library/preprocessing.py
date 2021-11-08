import torch
import numpy as np
import pickle
import os
import SimpleITK as sitk
import torch.nn.functional as F
import cc3d
import copy


class MAIC_Sampling(object):
    def __init__(self,  train = True, transform = Transform(*get_maic_params())):
        self.transform = transform
        self.train = train
        self.lung_cut = CT_Lung_Cropping()
        
    def __call__(self, images, seg = None, is_CT = True):
        temp = copy.deepcopy(images)
        if is_CT:
            temp[np.where(temp < - 700)] = 0
        non_zero_index = np.where(temp.astype(int) != 0)
        min_val = np.min(non_zero_index, axis = 1)
        max_val = np.max(non_zero_index, axis = 1)
        if self.train:
            random_move = np.random.randint([-5,-5,-5], [5, 5, 5])
        else:
            random_move = np.array([0,0,0])
        images = images[:, min_val[-3]:max_val[-3]+1, min_val[-2]:max_val[-2]+1, min_val[-1]:max_val[-1]+1]
        z_start = int(images.shape[-1] * 0.25)
        z_term = 128
        y_start = images.shape[-2]//2 - 40
        y_end= images.shape[-2]//2 + 40
        x_term = 128
        images = images[:, 5 + random_move[0]:x_term+random_move[0]+5, y_start+random_move[1]:y_end+random_move[1],
                       -(z_start + z_term) + random_move[2]:-z_start + random_move[2]]
        
        lung_index = self.lung_cut(images[0])
        lung_center = (lung_index[0] + lung_index[1])//2
        lung_center[2] = min(lung_center[2], 128 - 48)
        images = images[:, lung_center[0]-24:lung_center[0]+24, lung_center[1] - 24: lung_center[1] + 24, lung_center[2]-48:lung_center[2]+48]
        if self.train:
            seg = seg[min_val[-3]:max_val[-3]+1, min_val[-2]:max_val[-2]+1, min_val[-1]:max_val[-1]+1]
            seg = seg[5 + random_move[0]:x_term+random_move[0]+5, y_start+random_move[1]:y_end+random_move[1],
                       -(z_start + z_term) + random_move[2]:-z_start + random_move[2]]
            seg = seg[lung_center[0]-24:lung_center[0]+24, lung_center[1] - 24: lung_center[1] + 24, lung_center[2]-48:lung_center[2]+48]
            images = torch.tensor(images).unsqueeze(0).double()
            seg = torch.tensor(seg).unsqueeze(0).long()
            if self.transform != None:
                images, seg = self.transform(images, seg, None)
            images = images.squeeze(0).numpy()
            seg = seg.squeeze(0).numpy()
        else: 
            seg = None

        return images, seg


class CT_Lung_Cropping(object):
    def __init__(self, clip = False, threshold_clip = [-900, -200 ], threshold_cut = [-1000, -350]):
        self.clip = clip
        self.threshold_clip = threshold_clip
        self.threshold_cut = threshold_cut
    
    def __call__(self, image):
        if self.clip:
            clip_img = np.clip(image, self.threshold_clip[0], self.threshold_clip[1])
        else:
            clip_img = image
        mask =  (clip_img > self.threshold_cut[0]) * (clip_img < self.threshold_cut[1])
        if not isinstance(mask, np.ndarray):
            mask = mask.numpy()
        conected_component_mask = cc3d.connected_components(mask, connectivity = 26)
        count = np.unique(conected_component_mask, return_counts = True)[1]
        lung_index = np.argsort(count)[::-1]
        if len(lung_index) > 2:
            lung_index = lung_index[2]
        
        else:
            lung_index = lung_index[-1]
        lung_max = np.max(np.where(conected_component_mask == lung_index), axis = 1)
        lung_min = np.min(np.where(conected_component_mask == lung_index), axis = 1)
        
        return lung_min, lung_max

class Normalizer(object):
    def __init__(self, percentile_clipping_ratio = None):
        self.percentile = percentile_clipping_ratio
        self.device = None

    def __call__(self, images):
        if isinstance(images, np.ndarray):
            images = torch.Tensor(images)
        
        if images.device.index != self.device and self.device:
            images = images.to(self.device)
        
        if len(images.shape) == 3:
            images = images.unsqueeze(0)
        
        images = images.float()
        if self.percentile != None:
            images = self.percentile_clipping(images)
        n_modalities, nx, ny, nz = images.shape
        mmean = torch.mean(images.reshape(n_modalities, -1), -1, True).reshape(n_modalities,1,1,1)
        mstd = torch.std(images.reshape(n_modalities, -1), -1, True).reshape(n_modalities,1,1,1)
        
        return (images - mmean) / mstd
        
    
    def percentile_clipping(self,images):
        n_modalities, nx, ny, nz = images.shape
        images = images.reshape(n_modalities, -1)
        vals, indices = torch.sort(images, -1)
        upper_index = indices[:, int(indices.shape[1] * self.percentile[1]):]
        lower_index = indices[:, :int(indices.shape[1] * self.percentile[0])]
        upper_val = vals[:, int(indices.shape[1] * self.percentile[1])]
        lower_val = vals[:, int(indices.shape[1] * self.percentile[0])]

        for i in range(n_modalities):
            images[i, upper_index[i]] = upper_val[i]
            images[i, lower_index[i]] = lower_val[i]
        
        return images.reshape(n_modalities, nx, ny, nz)


class Min_Max_Normalizer(object):
    def __init__(self, min = -1024, max = 3024, device = None):
        self.min = min
        self.max = max
        self.device = device
    def __call__(self, images):
        if isinstance(images, np.ndarray):
            images = torch.Tensor(images)
        
        if images.device.index != self.device and self.device:
            images = images.to(self.device)
        
        if len(images.shape) == 3:
            images = images.unsqueeze(0)
        
        images = 2 * ((images - self.min) / (self.max - self.min)) - 1
        return images

class Fixed_Normalizer(object):
    def __init__(self, mean = -155.58, std = 324.70, min = -1024, max = 3025, device = None):
        self.mean = mean
        self.std = std
        self.min = min
        self.max = max
        self.device = device
    
    def __call__(self, images):
        if isinstance(images, np.ndarray):
            images = torch.Tensor(images)
        
        if images.device.index != self.device and self.device:
            images = images.to(self.device)
        
        if len(images.shape) == 3:
            images = images.unsqueeze(0)
        
        images = images.float()
        images = torch.clip(images, self.min, self.max)
        images = images - self.mean
        images = images / self.std
        return images

class Cropping(object):
    def __call__(self, images, seg = None, mode = 'train', is_CT = True):
        temp = copy.deepcopy(images)
        if is_CT:
            temp[np.where(temp < - 700)] = 0
        non_zero_index = np.where(temp.astype(int) != 0)
        min_val = np.min(non_zero_index, axis = 1)
        max_val = np.max(non_zero_index, axis = 1)
        if mode == 'train':
            return images[:, min_val[-3]:max_val[-3]+1, min_val[-2]:max_val[-2]+1, min_val[-1]:max_val[-1]+1], seg[ min_val[-3]:max_val[-3]+1, min_val[-2]:max_val[-2]+1, min_val[-1]:max_val[-1]+1]
        if mode == 'test':
            return images[:, min_val[-3]:max_val[-3]+1, min_val[-2]:max_val[-2]+1, min_val[-1]:max_val[-1]+1]


class Resampling(object):
    def __init__(self, anisotropy_axis_index = None, target_spacing = [1.0, 1.0, 1.0], random = False, device = None):
        self.device = device
        self.anisotropy_axis_index = self.new_anisotropy_axis(anisotropy_axis_index)
        self.target_spacing = np.array(target_spacing)
        self.random = random
    
    def new_anisotropy_axis(self, array):
        for i in range(len(array)):
            if array[i] == 2:
                array[i] = 0
            else:
                array[i] += 1
        return array


    def __call__(self, data, info_data, mode = 'x'):
        if isinstance(data, np.ndarray):
            data = torch.from_numpy(data.copy())
        if data.device.index != self.device and self.device:
            data = data.to(self.device)

        original_spacing = info_data['spacing']
        if self.random:
            self.target_spacing = original_spacing * np.random.uniform(0.20, 5.0, size = np.array(original_spacing).shape)
        new_shape = list((original_spacing/self.target_spacing * np.array([data.shape[-3], data.shape[-2], data.shape[-1]])).astype(int))
        data = F.interpolate(data.unsqueeze(0), new_shape).squeeze(0)

        return data



class Get_target_spacing(object):
    def __init__(self, anisotropy_threshold = 3.0, image_dimension = 3):
        self.spaces = None
        self.first = True
        self.anisotropy_threshold = anisotropy_threshold
        self.isotropy_percentile_value = 0.50
        self.anisotropy_percentile_value = 0.90
        self.image_dimension = image_dimension

    def run(self, dir_path, dtype = 'pkl'):
        """
        type은 pkl 또는 nifti
        """
        for file_name in os.listdir(dir_path):
            if dtype == 'pkl':
                if file_name[-3:] == 'pkl':
                    path = os.path.join(dir_path, file_name)
                    file = open(path, 'rb')
                    self.append(pickle.load(file)['spacing'])
                    file.close()
            
            if dtype == 'nifti':
                if 'nii' in file_name:
                    path = os.path.join(dir_path, file_name)
                    img = sitk.ReadImage(path)
                    spacing = img.GetSpacing()
                    self.append(spacing)
    
    def run_file_path(self, file_path):
        if type == 'pkl':
                if file_path[-3:] == 'pkl':
                    file = open(file_path, 'rb')
                    self.append(pickle.load(file)['spacing'])
                    file.close()
        if type == 'nifti':
            if 'nii' in file_path:
                img = sitk.ReadImage(file_path)
                spacing = img.GetSpacing()
                self.append(spacing)
    
    def reset(self):
        self.spaces = None

    def append(self, item):
        item = np.array(item).reshape(1,self.image_dimension)
        if self.first:
            self.spaces = item
            self.first = False
        else:
            self.spaces = np.vstack((self.spaces, item)) 
    
    def get_target_space(self):
        anisotropy_axis_index = self.is_anisotropy()
        isotropy_axis_index = np.arange(self.image_dimension) != anisotropy_axis_index
        iso = np.percentile(self.spaces, self.isotropy_percentile_value, 0)
        aniso = np.percentile(self.spaces, self.anisotropy_percentile_value, 0)
        result = np.zeros(self.image_dimension)
        result[anisotropy_axis_index] = aniso[anisotropy_axis_index]
        result[isotropy_axis_index] = iso[isotropy_axis_index]
        return result, anisotropy_axis_index
    
    def is_anisotropy(self):
        return np.where((np.max(self.spaces, axis = 0) / np.min(self.spaces, axis = 0)) > self.anisotropy_threshold)[0].astype(int)
    

