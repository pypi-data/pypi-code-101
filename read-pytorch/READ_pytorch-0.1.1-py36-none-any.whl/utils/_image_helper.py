import os
import torch
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from skimage import morphology
from skimage.segmentation import mark_boundaries

__all__ = ['get_patch', 'patch2img', 'visualize_loc_result']

def get_patch(image, new_size, stride=32):
    '''
    Only work for batch == 1, image 1xCxHxW
    '''
    # h, w = image.shape[1:]
    assert (type(image) is torch.Tensor)
    assert (image.shape[0] == 1)
    image = torch.squeeze(image) # 
    c, h, w = image.shape
    assert (new_size <= h and new_size <= w)
    i, j = new_size, new_size
    patch = []
    while i <= h:
        while j <= w:
            patch.append(torch.unsqueeze(image[:,i - new_size:i, j - new_size:j], dim=0))
            j += stride
        j = new_size
        i += stride
    return torch.vstack(patch)

def patch2img(patches, im_size, patch_size, stride=32):
    '''
    Use after get_patch(), patches NxCxHxW, return 1xCxHxW
    '''
    assert (type(patches) is torch.Tensor)
    img = torch.zeros((patches.shape[1]+1, im_size, im_size))
    # img = np.zeros((im_size, im_size, patches.shape[3]+1))
    i, j = patch_size, patch_size
    k = 0
    while i <= im_size:
        while j <= im_size:
            img[:-1, i - patch_size:i, j - patch_size:j] += patches[k]
            img[-1, i - patch_size:i, j - patch_size:j] += torch.ones((patch_size, patch_size))
            k += 1
            j += stride
        j = patch_size
        i += stride
    # mask=np.repeat(img[:,:,-1][...,np.newaxis], patches.shape[3], 2)
    mask = torch.unsqueeze(img[-1, :,:],dim=0).repeat(patches.shape[1],1,1)
    img = img[:-1,:,:,]/mask
    return torch.unsqueeze(img,dim=0)

def visualize_loc_result(args, test_img, gts, scores, threshold, 
                        save_dir, class_name, vis_num=5):
    num = len(scores)
    vmax = scores.max() * 255.
    vmin = scores.min() * 255.
    for i in range(vis_num):
        img = test_img[i]
        img = denormalization(img, args.mean, args.std)
        gt = gts[i].transpose(1, 2, 0).squeeze()
        heat_map = scores[i] * 255
        mask = scores[i]
        # mask[mask > threshold] = 1
        # mask[mask <= threshold] = 0
        mask[mask <= threshold] = 0
        mask[mask != 0] = 1
        kernel = morphology.disk(4)
        mask = morphology.opening(mask, kernel)
        mask *= 255
        vis_img = mark_boundaries(img, mask, color=(1, 0, 0), mode='thick')
        fig_img, ax_img = plt.subplots(1, 5, figsize=(12, 3))
        fig_img.subplots_adjust(right=0.9)
        norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
        for ax_i in ax_img:
            ax_i.axes.xaxis.set_visible(False)
            ax_i.axes.yaxis.set_visible(False)
        ax_img[0].imshow(img)
        ax_img[0].title.set_text('Image')
        ax_img[1].imshow(gt, cmap='gray')
        ax_img[1].title.set_text('GroundTruth')
        ax = ax_img[2].imshow(heat_map, cmap='jet', norm=norm)
        ax_img[2].imshow(img, cmap='gray', interpolation='none')
        ax_img[2].imshow(heat_map, cmap='jet', alpha=0.5, interpolation='none')
        ax_img[2].title.set_text('Predicted heat map')
        ax_img[3].imshow(mask, cmap='gray')
        ax_img[3].title.set_text('Predicted mask')
        ax_img[4].imshow(vis_img)
        ax_img[4].title.set_text('Segmentation result')
        left = 0.92
        bottom = 0.15
        width = 0.015
        height = 1 - 2 * bottom
        rect = [left, bottom, width, height]
        cbar_ax = fig_img.add_axes(rect)
        cb = plt.colorbar(ax, shrink=0.6, cax=cbar_ax, fraction=0.046)
        cb.ax.tick_params(labelsize=8)
        font = {
            'family': 'serif',
            'color': 'black',
            'weight': 'normal',
            'size': 8,
        }
        cb.set_label('Anomaly Score', fontdict=font)

        fig_img.savefig(os.path.join(save_dir, class_name + '_{}'.format(i)), dpi=100)
        plt.close()

def denormalization(x, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]):

    mean = [float(x) for x in mean]
    std = [float(x) for x in std]
    x = (((x.transpose(1, 2, 0) * std) + mean) * 255.).astype(np.uint8)
    # x = (x.transpose(1, 2, 0) * 255.).astype(np.uint8)
    return x