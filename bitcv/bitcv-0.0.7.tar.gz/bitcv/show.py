import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from torchvision import transforms as T
import torch
import torch.nn as nn

# 假设一个float 4个字节大小, 显示大小为MB
MEM_SIZE = (1024 ** 2) / 4

def sample_show(dataset, classes, each_num=4, boxsize=1, fontsize=20):
    """ 用于抽样打印dataset集合中的图片
    :param dataset: 数据集
    :param classes: 类名字列表
    :param each_num: 每个类打印的数目
    :param boxsize: 图片显示大小
    :param fontsize: 标题大小
    :return: None
    """
    transform = T.ToPILImage()
    num_classes = len(classes)
    plt.figure(figsize=(boxsize * num_classes, boxsize * each_num))

    for y, class_name in enumerate(classes):
        for i in range(each_num):
            # 抽取目标类图片
            while True:
                idx = np.random.randint(0, len(dataset))
                img, label = dataset[idx]
                if label == y:
                    break
            # 绘图
            plt_idx = num_classes * i + y + 1
            plt.subplot(each_num, num_classes, plt_idx)
            plt.imshow(transform(img))
            plt.axis('off')

            if i == 0:
                plt.title(classes[y], fontsize=fontsize)
    plt.show()

def summary(model, input_size, device="cuda"):
    def register_hook(module):
        def hook(module, input, output):
            # 模块名
            class_name = str(module.__class__).split(".")[-1].split("'")[0]
            module_idx = len(summary)

            # 输出的大小 
            m_key = "%s-%i" % (class_name, module_idx)
            summary[m_key] = {}
            summary[m_key]["output_shape"] = list(output.size())

            # 参数大小
            params = 0
            if hasattr(module, "weight"):
                params += np.prod(list(module.weight.shape))
                summary[m_key]["trainable"] = module.weight.requires_grad
            if hasattr(module, "bias"):
                params += np.prod(list(module.bias.shape))
            summary[m_key]["nb_params"] = params
        
        # 只给做运算的module注册hook
        if not isinstance(module, (nn.Sequential, nn.ModuleList)) and module != model:
            hooks.append(module.register_forward_hook(hook))

    # 存储属性
    summary = {}
    hooks = []

    # 注册钩子
    model.apply(register_hook)

    # 做一次模拟（利用1个batch的大小）
    x = torch.rand(1, *input_size[1:]).to(device) 
    model(x)

    # 移除钩子
    for h in hooks:
        h.remove()

    print("----------------------------------------------------------------")
    print(f"{'Layer (type)':>20}  {'Output Shape':>25} {'Param #':>15}")
    print("================================================================")
    total_params = 0
    total_output = 0
    trainable_params = 0
    for layer in summary:
        total_params += summary[layer]["nb_params"]
        total_output += np.prod(summary[layer]["output_shape"])
        if summary[layer].get("trainable"):
            trainable_params += summary[layer]["nb_params"]
        print("{:>20}  {:>25} {:>15}".format(layer, str(summary[layer]["output_shape"]), "{0:,}".format(summary[layer]["nb_params"])))

    batch_size = input_size[0]
    total_input_size = np.prod(input_size) / MEM_SIZE
    total_output_size = batch_size * 2 * total_output / MEM_SIZE # x2 for gradients
    total_params_size = total_params / MEM_SIZE
    total_size = total_params_size + total_output_size + total_input_size

    print("================================================================")
    print("Total params: {0:,}".format(total_params))
    print("Trainable params: {0:,}".format(trainable_params))
    print("Non-trainable params: {0:,}".format(total_params - trainable_params))
    print("----------------------------------------------------------------")
    print("Input size (MB): %0.2f" % total_input_size)
    print("Forward/backward pass size (MB): %0.2f" % total_output_size)
    print("Params size (MB): %0.2f" % total_params_size)
    print("Estimated Total Size (MB): %0.2f" % total_size)
    print("----------------------------------------------------------------")

if __name__ == '__main__':
    import torch


    class Mydataset(torch.utils.data.Dataset):
        def __init__(self):
            self.paths = [f'./img/cat/{i}.jpg' for i in range(6)] + [f'./img/dog/{i}.jpg' for i in range(6)]
            self.y = [0] * 6 + [1] * 6
            self.transforms = T.ToTensor()

        def __len__(self):
            return len(self.y)

        def __getitem__(self, index):
            X = Image.open(self.paths[index])
            X = self.transforms(X)

            y = torch.tensor(self.y[index], dtype=torch.long)

            return X, y


    sample_show(Mydataset(), [0, 1], boxsize=1)
