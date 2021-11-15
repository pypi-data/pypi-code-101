import argparse
import numpy as np
import os
import torch
import torch.nn as nn
import torch.optim as optim
import utils
# from torchvision import datasets, transforms
from matplotlib import pyplot as plt
from torch.autograd import Variable
from torch.utils.data import DataLoader, Dataset

import constant

torch.manual_seed(777)

""" 基于径向基函数的神经网络在回归问题上的实现 """


# 数据集加载类
class CustomDataset(Dataset):
    def __init__(self, inputs, repeat=1):
        # 输入inputs中有有个条目
        # 格式为np.array，前N-1个维度为特征，最后一个维度为参考评分值
        # 考虑到实际评分过程中参考值不会参与评分，需要手动补全，在该位上填0即可
        self.len = len(inputs)
        self.inputs = inputs

        # 数据增标志位，int型数值，将输入的条目复制多次
        self.repeat = repeat

    def _pre_processing(self, raw):
        # 转换数据格式，由np.array转至tensor
        data = torch.tensor(raw)
        return data

    def __getitem__(self, i):
        # 数据集索引的相关实现，可以通过索引index访问到具体条目
        """
        raw, label = self.inputs[i]
        if type(raw) is not list and type(raw) is not np.ndarray:
            raw = [raw]
        features = self._pre_processing(raw)
        """

        instance = self.inputs[i]
        raw = np.float32(instance[:-1])
        label = instance[-1]

        features = self._pre_processing(raw)
        return features, label

    def __len__(self):
        # 返回数据集的实际大小（根据repeat的值不同，可能存在数据增强）
        if self.repeat is None:
            data_len = 10000000
        else:
            data_len = self.len * self.repeat
        return data_len


# 径向基函数类的实现
class RbfNet(nn.Module):
    def __init__(self, centers, num_class=10):
        super(RbfNet, self).__init__()

        # 神经网络多用于分类问题中，此处待解决的是回归问题，因此类数设为1
        # 该网络结构也可用于分类问题，详见RFB_img_cla.py文件
        self.num_class = num_class  # num_class = 1

        # 该网络结构分为3层：输入层；隐藏层；输出层
        # 输入层节点数 等于 数据维度
        # 隐含层节点数 等于 num_centers，需要手动配置
        # 输出层节点数 等于 num_class，此处只预测一个值，因此为1
        self.num_centers = centers.size(0)

        # 输入层--隐含层参数
        self.centers = nn.Parameter(centers)

        self.beta = nn.Parameter(torch.rand(1, self.num_centers) * 2 - 1)

        # 隐含层--输出层参数
        self.linear = nn.Linear(self.num_centers, self.num_class, bias=True)

        # 权值初始化
        utils.initialize_weights(self)

    def kernel_fun(self, batches):
        # kernel_fun包含正向传播中从input layer至hidden layer的运算实现
        if len(batches.shape) == 1:
            # 该情况下数据集仅有一条数据
            n_input = 1
        else:
            n_input = batches.size(0)

        # 径向基函数的具体实现，以批(batch)为基本单位进行运算，一个batch中有固定数量的数据条目
        A = self.centers.view(self.num_centers, -1).repeat(n_input, 1, 1)
        B = batches.view(n_input, -1).unsqueeze(1).repeat(1, self.num_centers, 1)

        # 基于指数函数的径向基函数
        C = torch.exp(-(A - B).pow(2).sum(2, keepdim=False).sqrt())

        return C

    def forward(self, batches):
        # 正向传播forward propagation的具体实现
        radial_val = self.kernel_fun(batches)   # 调用核函数获取隐藏层输出值

        # 隐藏层(hidden layer)至输出层(output layer)的相关实现
        # 实际上是隐藏层节点输出的加权和
        class_score = self.linear(radial_val)

        # 至此，前向传播结束，网络给出最终的输出值
        return class_score
    # 对于后向传播(back propagation)部分，pytorch已经内置了相关实现，此处不需要再次实现


class RBFN(object):
    def __init__(self, args):
        # args参数的具体含义见应用实例中的相关注释
        self.max_epoch = args.epoch
        self.batch_size = args.batch_size
        self.save_dir = args.save_dir
        self.manually = args.manually
        self.dataset = args.dataset
        #self.cuda = args.cuda
        self.model_name = args.model_name
        self.lr = args.lr
        self.num_class = args.num_class
        self.num_centers = args.num_centers
        self.num_features = args.num_features
        self.epoch_count = 0

        self.visualize_res = False

        self.train_data = None
        self.test_data = None
        self.data_loader = None

        # 自动状态下自行加载相关测试数据并初始化
        # 测试数据为1维/2维的sin函数，用以展示RBFN的拟合效果
        if not self.manually:
            self._auto_startup()

    def _auto_startup(self):
        # 加载虚拟生成的数据
        self._load_data()
        # 初始化模型
        self._init_model()

    def _init_model(self):
        self._get_center()

        self.model = RbfNet(self.centers, num_class=self.num_class)

        # 在支持cuda的设备上使用GPU加速，否则在CPU上运行，CPU上的运行效率比较低
        # if self.cuda:
        #     self.model.cuda()

        # 输出网络结构
        utils.print_network(self.model)

        # 优化器及损失函数，涉及到训练过程中的反向传播 back-propagation
        # 此处的parameters为训练模型中每个节点、每条边上的权重weight，是训练过程中需要优化的值
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.lr)

        # MSE: Mean Square Error，均方损失函数，计算预测值和原始值之间的偏差，并反向传播至各个节点
        #      最终由优化器根据偏差对各个节点上的值做优化
        self.loss_fun = nn.MSELoss()

    def _load_data(self):
        # 加载__人造__数据集，用于验证模型的有效性
        if self.dataset == '':
            # 数据集为三角函数，y=sin(x)
            # 相当于使用RBFN网络对sin函数中的某一段进行拟合
            raw = utils.data_generate_1d(0, np.pi*2, 1000)  # 区间为[0, 2*PI]

            # 按照一定比例区分训练集与测试集
            # 测试集用于验证模型的有效性
            split_ratio = 0.1
            split_index = int(len(raw) * split_ratio)
            self.train_data = CustomDataset(raw[:split_index])
            self.test_data = CustomDataset(raw[split_index:])

            # self.train_data = CustomDataset(raw)
            # self.test_data = CustomDataset(raw)

        elif self.dataset == '2d':
            # 人造数据集，3D空间中的sin函数，性质及目的同上
            raw = utils.data_generate_2d(-np.pi, np.pi, 30)     # 20*20 共400个实例用于训练
            self.train_data = CustomDataset(raw)

            raw = utils.data_generate_2d(-np.pi, np.pi, 50)     # 50*50 共2500个实例用于测试
            self.test_data = CustomDataset(raw)
        else:
            raise ValueError('No valid input')

        self.data_loader = DataLoader(dataset=self.train_data,
                                      batch_size=self.batch_size,
                                      shuffle=True,
                                      num_workers=1,
                                      pin_memory=True)

    def _get_center(self):
        # 初始化隐藏层节点
        self.centers = torch.rand(self.num_centers, self.num_features)

    def load_training(self, input_arr):
        # 手动加载数据，输入格式为np.array，其中最后一列为Label
        # 注意：需要保证所有输入值为数值
        self.train_data = CustomDataset(input_arr)

        self.data_loader = DataLoader(dataset=self.train_data,
                                      batch_size=self.batch_size,
                                      shuffle=True,
                                      num_workers=1,
                                      pin_memory=True)

    def load_testing(self, input_arr):
        # 手动加载测试集，待评分条目的输入接口
        self.test_data = CustomDataset(input_arr)

    def init_model(self):
        self._init_model()

    def set_visualize_mode(self, flag):
        # 仅支持2维/3维数据的可视化
        self.visualize_res = flag

    def train(self):
        # 训练流程启动接口
        self.epoch_count = -1
        if self.visualize_res:
            self.plt_compare()
            plt.pause(3)

        # 前向传播
        self.model.train()
        for epoch in range(self.max_epoch):
            # 当循环周期大于收敛条件时，停止训练
            self.epoch_count = epoch

            # 计时器，查看每个周期内的训练耗时
            utils.tic()
            avg_cost = 0
            total_batch = len(self.data_loader.dataset) // self.batch_size

            for i, (single_batch, batch_labels) in enumerate(self.data_loader):
                # 以batch为单位，加载训练
                if self.cuda:
                    x_ = Variable(single_batch).cuda()
                    y_ = Variable(batch_labels).cuda()
                # import ipdb; ipdb.set_trace(context=20)
                else:
                    x_ = Variable(single_batch)
                    # y为参考值，也成为ground truth
                    y_ = Variable(batch_labels)

                y_ = y_.reshape([len(y_), 1])

                # 将所有参数的梯度清0，因为上一轮的梯度信息已在反向传播中被更新至网络中了
                self.optimizer.zero_grad()      # Zero Gradient Container

                # 根据当前网络各个节点权值，给出相关条目的预测值
                y_prediction = self.model(x_)    # Forward Propagation

                # 计算预测值与参考值之间的差距
                cost = self.loss_fun(y_prediction, y_)    # compute cost

                # 若出现nan，通常是因为梯度爆炸，分子中有无穷大值或是分母为0.
                if np.isnan(float(cost)):
                    # 出现梯度爆炸时训练失败，模型失效
                    print('err')

                # 反向传播，根据cost值更新各个节点的梯度
                cost.backward()                   # compute gradient

                # 按照梯度方向更新各个节点权值，更新步长受learning rate影响
                self.optimizer.step()                  # gradient update

                ck = self.model.centers.cpu()
                if np.count_nonzero(ck != ck):
                    # 检查节点中是否存在无穷值Inf或无效值nan
                    print('err!')
                # import ipdb; ipdb.set_trace(context=20)

                avg_cost += cost / total_batch

            # 计时器，计算从上一次计时开始，到当前位置所消耗的时间
            time_taken = utils.toc()

            print("[Epoch: {:>4}] cost = {:>.9}, takes: {:>.2} seconds".format(epoch + 1, avg_cost, time_taken))
            if self.visualize_res:
                self.plt_compare()
        print(" [*] Training finished!")

    def plt_compare(self):
        # 数据可视化相关函数
        plt_type = 0

        res = np.array(self.test())
        x_ = []
        for instance, labels in self.test_data:
            x_.append(np.array(instance))

        if len(x_[0]) > 2:
            return
        elif len(x_[0]) == 2:
            plt_type = 1
        x_ = np.array(x_)

        train_x_ = []
        train_y_ = []
        for instance, labels in self.train_data:
            train_x_.append(np.array(instance))
            train_y_.append(labels)
        train_x_ = np.array(train_x_)
        train_y_ = np.array(train_y_)

        # plt.close('fig1')
        plt.clf()
        fig = plt.figure('fig1')
        fig.suptitle('Epoch: {:>4}'.format(self.epoch_count))

        if plt_type:
            # 三维数据可视化
            num = int(np.sqrt(len(train_x_)))
            ax1 = fig.add_subplot(121, projection='3d')    # visualization of train data
            train_f1 = train_x_[:, 0].reshape(num, num)
            train_f2 = train_x_[:, 1].reshape(num, num)
            train_y_ = train_y_.reshape(num, num)
            ax1.plot_surface(train_f1, train_f2, train_y_, cmap=plt.get_cmap('rainbow'))

            num = int(np.sqrt(len(x_)))
            ax2 = fig.add_subplot(122, projection='3d')
            test_f1 = x_[:, 0].reshape(num, num)
            test_f2 = x_[:, 1].reshape(num, num)
            res = res.reshape(num, num)
            ax2.plot_surface(test_f1, test_f2, res, cmap=plt.get_cmap('rainbow'))
            plt.pause(1)
        else:
            # 二维数据可视化
            ax = fig.add_subplot(111)
            ax.set(xlim=(-0.1, 1.1), ylim=(-1.1, 1.1))
            order = x_[:, 0].argsort()
            x_ = x_[order]
            res = res[order]

            order = train_x_[:, 0].argsort()
            train_x_ = train_x_[order]
            train_y_ = train_y_[order]

            plt.plot(train_x_, train_y_, 'b-')
            plt.plot(x_, res, 'r-')
        plt.pause(0.1)
        self.model.train()

    # 模型评分的调用接口
    def test(self):
        # 切换至eval()模式，该模式下固化了网络参数
        # 不计算或是更新网络参数的梯度，运行效率更高
        self.model.eval()
        total = len(self.test_data)
        local_count = 0
        last = 0
        print('Totally {} instances to be predicted'.format(total))
        predicted_list = []
        for instance, labels in self.test_data:
            # 逐个对待评分数据进行打分，存放至predicted_list中，最后一起输出
           # if self.cuda:
           #     x_ = Variable(instance).cuda()
           # else:
            x_ = Variable(instance)
            outputs = self.model(x_)
            predicted_list.append(float(outputs))
            # print('predicted: {:>.4} vs. ground_truth: {:>.4}'.format(float(outputs), labels))
            local_count += 1

            if int(local_count * 20 / total) != last:
                last = int(local_count * 20 / total)
                print('\r', '{}%'.format(last*5), end='')

        print(" [*] Testing finished!")
        return predicted_list

    def save_model(self):
        # 保存模型的训练结果
        save_dir = os.path.join(self.save_dir, self.dataset)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        torch.save(self.model.state_dict(), os.path.join(save_dir, self.model_name+'.pkl'))
        print(" [*] Done saving check point yo!")

    def load_model(self):
        # 加载模型的上一次训练结果
        save_dir = os.path.join(self.save_dir, self.dataset)
        self.model.load_state_dict(torch.load(os.path.join(save_dir, self.model_name+'.pkl'),map_location='cpu'))
        print(" [*] Done weight loading!")

    def load_with_given_name(self, name):
        save_dir = os.path.join(self.save_dir, name)
        self.model.load_state_dict(torch.load(save_dir,map_location='cpu'))
        print(" [*] Done weight loading!")


# 用于测试的简单示例
def main():
    parser = argparse.ArgumentParser(description='Radial Based Network')

    # lr：  学习率 (learning rate) ，决定个训练周期间反向传播的步长
    #       较大的lr能够加速模型的训练，但是由于步长过大，最终的结果有可能较差，并可能引入一些其他问题
    #       较小的lr会增加训练时的时间开销，不过通常能得到较好的模型
    parser.add_argument('--lr', default=constant.LEARNING_RATE, type=float, help='learning rate')

    # batch_size:   批尺寸，合适的batch size能够提高内存的利用率，并加速训练流程；
    #               若不了解参数设置，建议使用此处的默认值
    parser.add_argument('--batch_size', default=constant.BATCH_SIZE, type=int, help='batch size')

    # epoch:    即maximum epoch，限制最大的迭代次数，避免模型出现过拟合
    #           考虑到当前问题比较简单，通常不会用到该参数
    parser.add_argument('--epoch', default=constant.MAX_EPOCH, type=int, help='epoch size')

    # 此处class数量应当为1，因为当前处理的问题为回归问题
    parser.add_argument('--num_class', default=constant.NUM_CLASS, type=int, help='num labels')
    parser.add_argument('--num_centers', default=constant.NUM_CENTERS, type=int, help='num centers')
    parser.add_argument('--save_dir', default=constant.SAVE_DIR, type=str, help='ckpoint loc')
    parser.add_argument('--dataset', default=constant.DATASET, type=str)

    """ 
    manually = False：自动模式，根据dataset字段中提供的数据位置加载数据
    manually = True:  手动模式，手动加载数据，可根据需要提前做一些预处理
    """
    parser.add_argument('--manually', default=False, type=bool)
    parser.add_argument('--model_name', default=constant.MODEL_NAME, type=str)
    parser.add_argument('--num_features', default=constant.NUM_FEATURES, type=int)
    args = parser.parse_args()

    rbfn = RBFN(args)
    # rbfn.set_visualize_mode(True)
    rbfn.train()
    rbfn.save_model()
    rbfn.load_model()
    # rbfn.test()

    return 0


if __name__ == "__main__":
    plt.figure()
    main()
