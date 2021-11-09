import glob
import os

import torch
from PIL import Image
from skimage import io
from torch import cuda
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torchvision.transforms import Compose
from .data_loader import RescaleT
from .data_loader import SalObjDataset
from .data_loader import ToTensorLab
from .model import U2NET


class DataSetIter:

    def __init__(self, image_path, dimen):
        self.image_path = image_path
        self.dimen = dimen

        # --------- 1. get image path and name ---------
        self.image_list = glob.glob(self.image_path + os.sep + '*')

        # --------- 2. dataloader ---------
        # 1. dataloader
        salobj_dataset = SalObjDataset(img_name_list=self.image_list,
                                       lbl_name_list=[],
                                       transform=Compose([RescaleT(self.dimen), ToTensorLab(flag=0)])
                                       )

        self.salobj_data_loader = DataLoader(salobj_dataset,
                                             batch_size=1,
                                             shuffle=False,
                                             num_workers=1
                                             )

    def __call__(self, *args, **kwargs):
        return self.salobj_data_loader

    def get_image_dataset(self, data_set):
        return data_set['image'].type(torch.FloatTensor)

    def deacidizing(self, index, mid_image):
        image_abspath = self.image_list[index]
        src_image = io.imread(image_abspath)

        image_mask = mid_image.resize((src_image.shape[1], src_image.shape[0]), resample=Image.BILINEAR)

        del src_image

        return image_mask


class U2NetEngine:

    def __init__(self, model_path, op_gpu=True):
        self.model_path = model_path

        self.is_cuda_available = op_gpu and cuda.is_available()

        self.net_model = U2NET(3, 1)

        if self.is_cuda_available:
            self.net_model.load_state_dict(torch.load(model_path))
            self.net_model.cuda()
        else:
            self.net_model.load_state_dict(torch.load(model_path, map_location='cpu'))

        self.net_model.eval()

    def load_dataset(self, image_path, dimen):
        return DataSetIter(image_path, dimen)

    def wrap_variable(self, img_data):

        return Variable(img_data.cuda()) if self.is_cuda_available else Variable(img_data)

    def _norm_pred(self, d):
        ma = torch.max(d)
        mi = torch.min(d)

        dn = (d - mi) / (ma - mi)

        return dn

    def forward(self, data_set):

        d1, d2, d3, d4, d5, d6, d7 = self.net_model(self.wrap_variable(data_set))

        # normalization
        predict = self._norm_pred(d1[:, 0, :, :])
        predict = predict.squeeze()
        predict_np = predict.cpu().data.numpy()

        img = Image.fromarray(predict_np * 255).convert('RGB')

        del d1, d2, d3, d4, d5, d6, d7

        return img
