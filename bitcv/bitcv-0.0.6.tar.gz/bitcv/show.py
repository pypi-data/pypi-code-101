import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from torchvision import transforms as T


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
    input()
