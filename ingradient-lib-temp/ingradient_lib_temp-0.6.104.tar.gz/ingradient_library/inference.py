from ingradient_library.dataloads import CustomDataset
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import cc3d
import time
import os

def get_pad_images(images, patch_size):
    images = torch.tensor(images)
    image_shape = torch.tensor([images.shape[-3], images.shape[-2], images.shape[-1]])
    prev_shape = torch.tensor(image_shape)
    patch_size = torch.tensor(patch_size)
    while len(images.shape) < 5:
        images = images.unsqueeze(0)
    
    new_shape = torch.tensor([0,0,0])
    for i in range(len(patch_size)):
        if patch_size[i] > image_shape[i]:
            new_shape[i] = (patch_size[i]//2) - prev_shape[i] % (patch_size[i]//2)
       
    is_div_two = new_shape % 2 != 0
    pad_shape = new_shape.repeat_interleave(2) // 2
    for i in range(len(is_div_two)):
        if is_div_two[i]:
            pad_shape[i*2] += 1

    images = F.pad(images, pad_shape.tolist()[::-1], "constant", 0)

    while len(images.shape) > 4:
        images = images.squeeze(0)

    return images


def get_coords_arr(images, patch_size, step_size):
    grid_list = []
    for i in range(3):
        grid_list.append(torch.arange(1+(images.shape[i+1] - patch_size[i])/(patch_size[i] * step_size[i])))
    grid_x, grid_y, grid_z = torch.meshgrid(*grid_list)
    grid_x = torch.round(grid_x * step_size[0] * patch_size[0]).long()
    grid_y = torch.round(grid_y * step_size[1] * patch_size[1]).long()
    grid_z = torch.round(grid_z * step_size[2] * patch_size[2]).long()
    max_gx = grid_x.max()
    max_gy = grid_y.max()
    max_gz = grid_z.max()

    grid_x[torch.where(grid_x == max_gx)] = images.shape[-3] - patch_size[0]
    grid_y[torch.where(grid_y == max_gy)] = images.shape[-2] - patch_size[1]
    grid_z[torch.where(grid_z == max_gz)] = images.shape[-1] - patch_size[2]
    grid_x = grid_x.reshape(-1, 1)
    grid_y = grid_y.reshape(-1, 1)
    grid_z = grid_z.reshape(-1, 1)
    
    grids = torch.cat((grid_x, grid_y, grid_z), -1)
    patch_coords = []
    for i in range(grids.shape[0]):
        patch_coords.append((torch.arange(grids[i][0], grids[i][0]  + patch_size[0]), torch.arange(grids[i][1], grids[i][1] + patch_size[1]), torch.arange(grids[i][2], grids[i][2] + patch_size[2]) ) )
    return patch_coords


def get_patch_from_coords(image, patch_coords, index):
    for i in range(image.shape[0]):
        if i == 0:
            result = image[0][torch.meshgrid(*patch_coords[index])].unsqueeze(0)
        else:
            result = torch.cat((result, image[i][torch.meshgrid(*patch_coords[index])].unsqueeze(0)))
    return result

def change_value_from_coords(image, patch_coords, index, patch):
    for i in range(image.shape[0]):
        image[i][torch.meshgrid(*patch_coords[index])] += patch[i]
    return image

class CC_Remover(object):
    def __init__(self, remain_num = 2, frequency_order = [2,3]):
        self.remain_num = remain_num
        self.frequency_order = frequency_order
    

    def __call__(self, mask):
        conected_component_mask = cc3d.connected_components(mask, connectivity = 26)
        count = np.unique(conected_component_mask, return_counts = True)[1]
        result = torch.zeros(mask.shape)
        for i in range(self.remain_num):
            try:
                result += (np.argsort(count)[::-1][self.frequency_order[i]-1] == conected_component_mask)
            except IndexError as e:
                print(e)
        return result

class InferenceV2(object):
    def __init__(self, dataset, model, patch_size, n_classes, mode = 'npy', step_size = [0.5, 0.5, 0.5], postprocessing = None, device = None,
                 batch_size = 2, gaussian_filter = False, deep_supervision = False, save_path = None):
        self.dataset = dataset
        self.model = model.to(device)
        self.bs = batch_size
        self.patch_size = patch_size
        self.step_size = step_size
        self.n_classes = n_classes
        self.deep_supervision = deep_supervision
        self.device = device
        self.postprocessing = postprocessing
        self.mode = mode
        if save_path != None:
            self.make_dir(save_path)

    def make_dir(self, save_path):
        now = time.localtime()
        now = "%04d%02d%02d_%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

        self.save_path = os.path.join(save_path, now)
        self.soft_path = os.path.join(self.save_path, r'soft_result')
        self.model_path = os.path.join(self.save_path, r'result')
        self.postprocessing_path = os.path.join(self.save_path, r'postprocessing_result')
        self.image_path = os.path.join(self.save_path, r'image')

        try:
            os.mkdir(self.save_path)
            os.mkdir(self.soft_path)
            os.mkdir(self.image_path)
            os.mkdir(self.model_path)
            os.mkdir(self.postprocessing_path)
        
        except FileExistsError as e:
            print('Folders already exist. Please be careful to overwrite exising files.')

    def save(self, image, path, index, identifier, mode = 'seg'):
        if 'npy' in self.mode:
            np.save(os.path.join(path, identifier + mode + '{0:03}.npy'.format(index)),image.numpy())

    def valid_run(self):
        final_score = []
        self.model = self.model.eval()
        for data_index in range(len(self.dataset)):
            if isinstance(self.dataset, CustomDataset):
                current_name = self.dataset.image_name[data_index][:-4]
            image = self.dataset[data_index][0]
            seg = self.dataset[data_index][1]
            image = get_pad_images(image, self.patch_size)
            seg = get_pad_images(seg, self.patch_size)
            coords = get_coords_arr(image, self.patch_size, self.step_size)

            for coords_index in range(len(coords)):
                if coords_index == 0:
                    patch_bundle = get_patch_from_coords(image, coords, coords_index).unsqueeze(0)
                    index_bundle = torch.tensor(coords_index).reshape(1,)
                else:
                    patch_bundle = torch.cat((patch_bundle, get_patch_from_coords(image, coords, coords_index).unsqueeze(0)), 0)
                    index_bundle = torch.cat((index_bundle, torch.tensor(coords_index).reshape(1,)))

            patch_bundle = torch.split(patch_bundle, self.bs)
            index_bundle = torch.split(index_bundle, self.bs)
            result = torch.zeros((self.n_classes, image.shape[-3], image.shape[-2], image.shape[-1]))
            for mini_batch_patch, mini_batch_index in zip(patch_bundle, index_bundle):
                output = self.model(mini_batch_patch.to(self.device))
                output = output.detach().cpu()
                if self.deep_supervision:
                    output = output[:, 0]
                for batch_index in range(mini_batch_index.shape[0]):
                    result = change_value_from_coords(result, coords, mini_batch_index[batch_index], output[batch_index])
            
            if self.save_path != None:
                self.save(result, self.soft_path, data_index, current_name)
            result = torch.argmax(result, 0)
            
            
            if self.save_path != None:
                self.save(result, self.model_path, data_index, current_name)
                self.save(image, self.image_path, data_index, current_name, mode = 'image')
            if self.postprocessing != None:
                result = self.postprocessing(result.numpy()) 
                if self.save_path != None:
                    self.save(result, self.postprocessing_path, data_index, current_name)

            dice_score = []
            for i in range(1, self.n_classes):
                temp_seg = (seg == i)
                temp_img = (result == i)
                intersection = (temp_seg * temp_img).sum()
                union = temp_seg.sum() + temp_img.sum()
                dice = 2 * intersection / union
                dice_score.append(dice.numpy())
            print(dice_score)
            final_score.append(dice_score)
        
        self.final_score = final_score
        return final_score
