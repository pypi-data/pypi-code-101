import mindspore
import mindspore.nn as nn
import mindspore.ops as ops
import mindspore.numpy as mnp
from mindspore import Tensor
from mindspore import context
from mindspore import load_checkpoint,load_param_into_net
import sys
import os
import gc
import platform
import time
import logging
import numpy as np
from tqdm import tqdm
from scipy.ndimage import gaussian_filter
from READ_mindspore.optimizer import RAdam
from READ_mindspore.scheduler import CosineAnnealingScheduler
import READ_mindspore.backbones as models
from READ_mindspore.utils import set_logger, AverageMeter, EarlyStop
from READ_mindspore.optimizer import TrainOneStepCell, TrainOneStepCellTwoParameters
from READ_mindspore.utils import remove_dataparallel
from READ_mindspore.utils import estimate_thred_with_fpr
from READ_mindspore.scheduler import _scheduler
from READ_mindspore.optimizer import _optimizer

backbones = ['resnet18', 'resnet34', 'resnet50', 'resnet101', 'resnet152', 'resnext50',
             'resnext101', 'wide_resnet50', 'wide_resnet101', 'se_resnext50', 'se_resnext101', 'se_resnet18',
             'se_resnet34', 'se_resnet50', 'se_resnet101', 'se_resnet152']

class LossWithTeacher(nn.Cell):
    def __init__(self, teacher, student, layers):
        super(LossWithTeacher, self).__init__()
        self.teacher = teacher
        self.student = student
        self.layers = layers
        self.teacher.set_train(False)
        self.teacher.set_grad(False)
        self.criterion = nn.MSELoss(reduction='sum')
        self.div = ops.Div()
    def construct(self, data):
        '''
        Args:
        tout_list: list of 3 layers' output
        sout_list: list of 3 layers' output

        '''

        features_t = self.teacher(data)
        features_s = self.student(data)

        total_loss = 0

        for i in self.layers:
            tout = features_t[i-1]
            sout = features_s[i-1]
            b, c, h, w = tout.shape
            tout_norm = self.div(tout,mnp.norm(tout, axis=1, keepdims=True))
            sout_norm = self.div(sout,mnp.norm(sout, axis=1, keepdims=True))
            loss_cache = (0.5 / (w * h)) * self.criterion(sout_norm, tout_norm)
            total_loss += loss_cache
        return total_loss, []


##############################################################
####################### STPM Model ###########################
##############################################################

class STPM(object):
    def __init__(self, backbone='resnet18', layers=[1, 2, 3], device='GPU'):
        #self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        context.set_context(mode=context.PYNATIVE_MODE,
                            device_target=device)
        self.backbone = backbone
        assert (self.backbone in backbones), f"Only support backbones in {backbones}."
        # Define teacher and student model

        self.teacher = getattr(models.resnet_model_zoo(), self.backbone)(pretrain=True)
        self.student = getattr(models.resnet_model_zoo(), self.backbone)(pretrain=False)
        self.teacher.set_train(False)
        for param in self.teacher.get_parameters():
            param.requires_grad = False

        for param in self.student.get_parameters():
            param.requires_grad = True

        self.layers = layers
        # Initialize parameters
        self.val_max_as = None
        self.val_min_as = None
        self.seg_thres = None
        self.cls_thres = None
        self.criterion = nn.MSELoss(reduction='sum')

    def train(self,
              train_data,
              save_path,
              val_data=None,
              expect_fpr=0.01,
              **kwargs):
        batch_size = kwargs.get("batch_size", 32)
        lr = kwargs.get("lr", 0.0001)
        epochs = kwargs.get("epochs", 300)
        optimizer_name = kwargs.get("optimizer", 'adam')
        scheduler_name = kwargs.get("scheduler", 'step')
        validation_ratio = kwargs.get("validation_ratio", 0.2)
        logger = logging.getLogger('READ.STPM.Train')
        set_logger(os.path.join(save_path, 'train.log'), 'READ')
        if val_data == None:
            train_data, val_data = train_data.split([1 - validation_ratio, validation_ratio])

        step_by_each_epoch = train_data.get_dataset_size()
        train_data = train_data.batch(batch_size)
        train_dataloader = train_data.create_dict_iterator()
        val_data_batch = val_data.batch(4*batch_size)
        val_dataloader = val_data_batch.create_dict_iterator()
        if scheduler_name == 'step':

            scheduler = _scheduler.StepLR(lr=lr, steps_per_epoch=step_by_each_epoch,
                                          gamma=0.5, epoch_size=epochs, max_epoch=epochs, warmup_epochs=epochs)
        elif scheduler_name == 'cosine':
            scheduler = _scheduler.CosineAnnealingLR(lr, max_epoch=int(step_by_each_epoch*epochs), steps_per_epoch=step_by_each_epoch,T_max=epochs, eta_min=1e-8)
        else:
            raise ValueError('Could Only Support scheduler in [Step, Cosine].')

        if (optimizer_name == 'adam') or (optimizer_name == 'Adam'):
            optimizer = nn.Adam(params=list(filter(lambda p: p.requires_grad, self.student.get_parameters())),
                                learning_rate=Tensor(scheduler.get_lr()), weight_decay=0.00001)  # , amsgrad=True

        elif (optimizer_name == 'sgd') or (optimizer_name == 'SGD'):

            optimizer = nn.SGD(params=list(filter(lambda p: p.requires_grad, self.student.get_parameters())),
                               learning_rate=Tensor(scheduler.get_lr()), momentum=0.9, nesterov=True)
        elif (optimizer_name == 'radam') or (optimizer_name == 'RAdam'):
            optimizer = _optimizer.RAdam(filter(lambda p: p.requires_grad, self.student.parameters()), learning_rate=Tensor(scheduler.get_lr()), weight_decay=0.00001)
        elif (optimizer_name == 'adabelief') or (optimizer_name == 'Adabelief'):
            optimizer = _optimizer.AdaBelief(filter(lambda p: p.requires_grad, self.student.parameters()), learning_rate=Tensor(scheduler.get_lr()), weight_decay=0.00001, eps=1e-16, betas=(0.9,0.999), weight_decouple = True, rectify = True)
        else:
            raise ValueError('Could Only Support optimizer in [Adam, SGD].')


        data_imshow = train_data.create_dict_iterator()
        dict_data = next(data_imshow)
        x_ref = dict_data["data"].asnumpy()
        assert (len(x_ref.shape) == 4), 'input tensor should be 4-dim.'
        assert (x_ref.shape[2] == x_ref.shape[3]), 'Input height should be equal to width.'
        net_loss = LossWithTeacher(self.teacher, self.student, self.layers)
        self.net_train = TrainOneStepCell(net_loss, self.student, optimizer)
        start_time = time.time()
        epoch_time = AverageMeter()
        save_lowest = os.path.join(save_path, 'model_lowest_loss.ckpt')
        early_stop = EarlyStop(patience=int(0.1 * epochs) if int(0.1 * epochs) > 20 else 20,
                                save_name=save_lowest)

        # print('Dataset size : Train set - {}'.format(dataset_sizes['train']))
        for epoch in range(epochs):
            losses = AverageMeter()

            for (data) in tqdm(train_dataloader, '| training epoch %s |' % (epoch + 1)):
                if type(data['data']) != Tensor:
                    if type(data['data']) == list or type(data['data']) == tuple:
                        data = data[0]
                        if type(data['data']) != Tensor:
                            raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                    else:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')

                data = data['data']
                # get loss using features.
                loss, loss_lst = self.net_train(data)
                losses.update(loss.asnumpy(), data.shape[0])

            logger.info('Train Epoch: {} L2_Loss: {:.6f}'.format(
                epoch, losses.avg))
            val_loss = self._val(val_dataloader)
            if (early_stop(val_loss, self.student, data.shape[2:])):
                 break

            epoch_time.update(time.time() - start_time)
            start_time = time.time()

        self.est_thres(val_dataloader, expect_fpr=expect_fpr, batch_size=batch_size)

    def _val(self, val_loader):
        self.teacher.set_train(False)
        self.teacher.set_grad(False)
        self.student.set_train(False)
        self.student.set_grad(False)
        div = ops.Div()
        losses = AverageMeter()
        # Start to evaluate
        for (data) in tqdm(val_loader):
            if type(data['data']) != Tensor:
                if type(data['data']) == list or type(data['data']) == tuple:
                    data = data[0]
                    if type(data['data']) != Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
            data = data['data']
            # generator mask
            img_size = data.shape[-1]
            features_t = self.teacher(data)
            features_s = self.student(data)
            total_loss = 0

            for i in self.layers:
                tout = features_t[i-1]
                sout = features_s[i-1]
                b, c, h, w = tout.shape
                tout_norm = div(tout, mnp.norm(tout, axis=1, keepdims=True))
                sout_norm = div(sout, mnp.norm(sout, axis=1, keepdims=True))
                loss_cache = (0.5 / (w * h)) * self.criterion(sout_norm, tout_norm)
                total_loss += loss_cache
            losses.update(total_loss.asnumpy(), data.shape[0])

        return losses.avg

    def load_weights(self, ckpt_path):
        params = load_checkpoint(ckpt_path)
        try:
            params = params["state_dict"]
        except:
            params = params
        try:
            load_param_into_net(self.student, params)
        except:
            params = params
        print('Pretrained weights from %s has been loaded.' % ckpt_path)

    def est_thres(self, val_dataloader, expect_fpr=0.01, **kwargs):

        self.teacher.set_train(False)
        self.teacher.set_grad(False)
        self.student.set_train(False)
        self.student.set_grad(False)

        val_scores = []

        for (data) in tqdm(val_dataloader, '|Estimating Threshold|'):
            if type(data["data"]) != Tensor:
                if type(data["data"]) == list or type(data["data"]) == tuple:
                    data = data[0]
                    if type(data["data"]) != Tensor:
                        raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')
                else:
                    raise ValueError('Input should be a torch.Tensor or a list of torch.Tensor.')

            data = data["data"]
            # cal img_size
            img_size = data.shape[-1]

            features_t = self.teacher(data)
            features_s = self.student(data)

            score_map = self._cal_score(features_s, features_t, img_size)

            score_map = score_map.squeeze().asnumpy()
            if len(score_map.shape) < 3:
                score = np.expand_dims(score_map, axis=0)

            for i in range(score_map.shape[0]):
                score_map[i] = gaussian_filter(score_map[i], sigma=4)

            val_scores.extend(score_map)
        val_scores = np.asarray(val_scores)
        self.val_max_as = val_scores.max()
        self.val_min_as = val_scores.min()
        val_scores = (val_scores - self.val_min_as) / (self.val_max_as - self.val_min_as)
        val_img_scores = val_scores.reshape(val_scores.shape[0], -1).max(axis=1)
        self.seg_thres = estimate_thred_with_fpr(val_scores, expect_fpr=expect_fpr)
        self.cls_thres = estimate_thred_with_fpr(val_img_scores, expect_fpr=expect_fpr)

    def predict(self, test_data, **kwargs):

        self.teacher.set_train(False)
        self.student.set_train(False)
        self.teacher.set_grad(False)
        self.student.set_grad(False)

        score = 0
        data = test_data
        # cal img size
        img_size = data.shape[-1]


        features_t = self.teacher(data)
        features_s = self.student(data)

        score_map = self._cal_score(features_s, features_t, img_size)
        score = score_map.squeeze().asnumpy()
        if score.ndim < 3:
            score = np.expand_dims(score, axis=0)
        for i in range(score.shape[0]):
            score[i] = gaussian_filter(score[i], sigma=7)
        if (self.val_max_as is not None) and (self.val_min_as is not None):
            # print('Normalizing!')
            score = (score - self.val_min_as) / (self.val_max_as - self.val_min_as)
        img_score = score.reshape(score.shape[0], -1).max(axis=1)
        return img_score, score
    def _cal_score(self, sout_list, tout_list, img_size):
        '''
        Args:
        tout_list: list of 3 layers' output
        sout_list: list of 3 layers' output

        '''
        criterion = nn.MSELoss(reduction='none')
        score_map = ops.Ones()((sout_list[0].shape[0], 1, img_size, img_size),mindspore.float32)

        resize_bilinear = ops.ResizeBilinear((img_size,img_size))
        # sqrt = ops.Sqrt()
        # div = ops.div()
        reduce_sum = ops.ReduceSum(keep_dims=True)
        for idx, i in enumerate(self.layers):
            if i == str('avgpool'):
                i = int(4)
            else:
                i = int(i) - 1
            tout = tout_list[i]
            sout = sout_list[i]

            tout_norm = ops.div(tout, mnp.norm(tout, axis=1, keepdims=True))
            sout_norm = ops.div(sout, mnp.norm(sout, axis=1, keepdims=True))
            loss_cache = (0.5) * criterion(sout_norm, tout_norm)

            loss_cache = 0.5 * ops.sqrt(reduce_sum(loss_cache, 1))
            loss_cache = resize_bilinear(loss_cache)
            score_map = ops.mul(score_map, loss_cache)
        return score_map