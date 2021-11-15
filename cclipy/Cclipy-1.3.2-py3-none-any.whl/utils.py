import os
import torch.nn as nn
import numpy as np
import scipy.misc
import time


def data_generate_1d(bound_low, bound_high, num_instances, noise_ratio=0):
    # num_instances 为需要创建的人工数据的数据量
    x_ = np.linspace(bound_low, bound_high, num_instances)
    y_ = np.sin(x_)
    x_ = x_ / abs(bound_high - bound_low)

    noise = np.random.rand(num_instances) * noise_ratio * abs(bound_high - bound_low)
    y_ += noise
    # y_ = x_.copy()
    raw = np.vstack((x_, y_))
    raw = raw.transpose()
    np.random.shuffle(raw)
    return raw


def data_generate_2d(bound_low, bound_high, num_instances, noise_ratio=0):
    # 实际的数据量不是 num_instances，而是num_instances的平方！
    x_, y_ = np.meshgrid(np.linspace(bound_low, bound_high, num_instances),
                         np.linspace(bound_low, bound_high, num_instances))
    z_ = np.cos(np.sqrt(x_**2 + y_**2))

    x_ -= bound_low
    y_ -= bound_low
    x_ = x_ / abs(bound_high - bound_low)
    y_ = y_ / abs(bound_high - bound_low)

    x_ = x_.reshape(num_instances ** 2, 1)
    y_ = y_.reshape(num_instances ** 2, 1)
    z_ = z_.reshape(num_instances ** 2, 1)
    raw = np.concatenate((x_, y_, z_), axis=1)
    # np.random.shuffle(raw)
    return raw


def print_network(net):
    num_params = 0
    for param in net.parameters():
        num_params += param.numel()
    print(net)
    print('Total number of parameters: %d' % num_params)


def save_images(images, size, image_path):
    return imsave(images, size, image_path)


def imsave(images, size, path):
    image = np.squeeze(merge(images, size))
    return scipy.misc.imsave(path, image)


def merge(images, size):
    h, w = images.shape[1], images.shape[2]
    if (images.shape[3] in (3,4)):
        c = images.shape[3]
        img = np.zeros((h * size[0], w * size[1], c))
        for idx, image in enumerate(images):
            i = idx % size[1]
            j = idx // size[1]
            img[j * h:j * h + h, i * w:i * w + w, :] = image
        return img
    elif images.shape[3]==1:
        img = np.zeros((h * size[0], w * size[1]))
        for idx, image in enumerate(images):
            i = idx % size[1]
            j = idx // size[1]
            img[j * h:j * h + h, i * w:i * w + w] = image[:,:,0]
        return img
    else:
        raise ValueError('in merge(images,size) images parameter ''must have dimensions: HxW or HxWx3 or HxWx4')


def initialize_weights(net):
    for m in net.modules():
        if isinstance(m, nn.Conv2d):
            m.weight.data.normal_(0, 0.02)
            m.bias.data.zero_()
        elif isinstance(m, nn.ConvTranspose2d):
            m.weight.data.normal_(0, 0.02)
            m.bias.data.zero_()
        elif isinstance(m, nn.Linear):
            m.weight.data.normal_(0, 0.02)
            m.bias.data.zero_()


def tic():
    # Homemade version of matlab tic and toc functions
    global m_clock
    m_clock = time.time()


def toc():
    if 'm_clock' not in globals():
        return None
    return time.time() - m_clock
