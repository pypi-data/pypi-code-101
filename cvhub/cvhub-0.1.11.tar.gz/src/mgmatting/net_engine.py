import cv2
import numpy as np
import torch

from . import networks
from . import utils
from .utils import CONFIG


class MGEngine:

    def __init__(self, checkpoint):
        self.checkpoint = checkpoint

        # build model
        model = networks.Generator()
        model.cuda()

        # load checkpoint
        checkpoint = torch.load(self.checkpoint)
        model.load_state_dict(utils.remove_prefix_state_dict(checkpoint['state_dict']), strict=True)

        # inference
        self.net_model = model.eval()

    def single_inference(self, image_dict, post_process=False):
        with torch.no_grad():
            image, mask = image_dict['image'], image_dict['mask']
            alpha_shape = image_dict['alpha_shape']
            image = image.cuda()
            mask = mask.cuda()
            pred = self.net_model(image, mask)
            alpha_pred_os1, alpha_pred_os4, alpha_pred_os8 = pred['alpha_os1'], pred['alpha_os4'], pred['alpha_os8']

            # refinement
            alpha_pred = alpha_pred_os8.clone().detach()
            weight_os4 = utils.get_unknown_tensor_from_pred(alpha_pred, rand_width=CONFIG.model.self_refine_width1, train_mode=False)
            alpha_pred[weight_os4 > 0] = alpha_pred_os4[weight_os4 > 0]
            weight_os1 = utils.get_unknown_tensor_from_pred(alpha_pred, rand_width=CONFIG.model.self_refine_width2, train_mode=False)
            alpha_pred[weight_os1 > 0] = alpha_pred_os1[weight_os1 > 0]

            h, w = alpha_shape
            alpha_pred = alpha_pred[0, 0, ...].data.cpu().numpy()
            if post_process:
                alpha_pred = utils.postprocess(alpha_pred)
            alpha_pred = alpha_pred * 255
            alpha_pred = alpha_pred.astype(np.uint8)
            alpha_pred = alpha_pred[32:h + 32, 32:w + 32]

            h, w = image_dict['src_shape'][:2]
            alpha_pred = cv2.resize(alpha_pred, (w, h), interpolation=cv2.INTER_AREA)

            return alpha_pred

    def generator_tensor_dict(self, image_path, mask_path, guidance_thres=128):
        """
        :param guidance_thres default=128, guidance input threshold
        """

        # read images
        image = cv2.imread(image_path)
        mask = cv2.imread(mask_path, 0)

        src_shape = mask.shape

        image = cv2.resize(image, (512, 512), interpolation=cv2.INTER_AREA)
        mask = cv2.resize(mask, (512, 512), interpolation=cv2.INTER_AREA)

        # only keep FG part of trimap
        mask = (mask >= guidance_thres).astype(np.float32)

        # mask = mask.astype(np.float32) / 255.0 ### soft trimap

        sample = {
            'image': image,
            'mask': mask,
            'alpha_shape': mask.shape,
            'src_shape': src_shape
        }

        # reshape
        h, w = sample["alpha_shape"]

        if h % 32 == 0 and w % 32 == 0:
            padded_image = np.pad(sample['image'], ((32, 32), (32, 32), (0, 0)), mode="reflect")
            padded_mask = np.pad(sample['mask'], ((32, 32), (32, 32)), mode="reflect")
            sample['image'] = padded_image
            sample['mask'] = padded_mask
        else:
            target_h = 32 * ((h - 1) // 32 + 1)
            target_w = 32 * ((w - 1) // 32 + 1)
            pad_h = target_h - h
            pad_w = target_w - w
            padded_image = np.pad(sample['image'], ((32, pad_h + 32), (32, pad_w + 32), (0, 0)), mode="reflect")
            padded_mask = np.pad(sample['mask'], ((32, pad_h + 32), (32, pad_w + 32)), mode="reflect")
            sample['image'] = padded_image
            sample['mask'] = padded_mask

        # ImageNet mean & std
        mean = torch.tensor([0.485, 0.456, 0.406]).view(3, 1, 1)
        std = torch.tensor([0.229, 0.224, 0.225]).view(3, 1, 1)
        # convert GBR images to RGB
        image, mask = sample['image'][:, :, ::-1], sample['mask']
        # swap color axis
        image = image.transpose((2, 0, 1)).astype(np.float32)

        mask = np.expand_dims(mask.astype(np.float32), axis=0)

        # normalize image
        image /= 255.

        # to tensor
        sample['image'], sample['mask'] = torch.from_numpy(image), torch.from_numpy(mask)
        sample['image'] = sample['image'].sub_(mean).div_(std)

        # add first channel
        sample['image'], sample['mask'] = sample['image'][None, ...], sample['mask'][None, ...]

        return sample
