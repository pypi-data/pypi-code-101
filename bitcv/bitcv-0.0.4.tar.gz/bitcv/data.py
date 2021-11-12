import torch
import matplotlib.pyplot as plt


def get_mean_std(dataset, ratio=0.1):
    """
    用来统计数据集的均值和方差，数据集形状：N*C*H*W
    :param dataset: 数据集（torch.util.data.Dataset）
    :param ratio: 采样的比例，不推荐太大
    :return: mean, std
    """
    batch_size = int(len(dataset) * ratio)
    loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)
    X = next(iter(loader))[0]
    return X.mean(dim=(0, 2, 3)), X.std(dim=(0, 2, 3))


if __name__ == '__main__':
    class MyDataset(torch.utils.data.Dataset):
        def __init__(self):
            super().__init__()
            self.X = torch.randn((100, 1, 10, 10))
            self.y = torch.randn(100)

        def __len__(self):
            return self.X.shape[0]

        def __getitem__(self, index):
            return self.X[index], self.y[index]


    dataset = MyDataset()
    print(get_mean_std(dataset))
