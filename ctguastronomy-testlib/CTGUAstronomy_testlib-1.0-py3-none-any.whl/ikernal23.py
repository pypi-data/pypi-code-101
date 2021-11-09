import numpy as np
import math


class Ikernal23:
    """
    实现对局部数据的拟合，并求出相应的各阶偏导数,
    进而得到相应的滤波算子
    程序可以对二维数据和三维数据进行工作
    """
    def __init__(self, ker_size, p1, p2, sigam2, gama, step, dimension):
        """
            :param ker_size:核的“半径”，卷积核的尺寸为:2n+1*2n+1
            :param p1:多项式的阶数
            :param p2:多项式和高斯的比例
            :param sigam2:RBF核函数中的参数
            :param gama:对错误(误差)的容忍程度
            :param step:步长
            :param ker_n:卷积核的尺寸为:2n+1*2n+1*2n+1
            :param dimension:卷积核的维度
        """
        self.ker_size = ker_size
        self.p1 = p1
        self.p2 = p2
        self.sigam2 = sigam2
        self.gama = gama
        self.step = step
        self.ker_n = (2 * ker_size + 1) ** dimension
        self.dimension = dimension

    def get_alpa(self):
        """
        基于最小二乘支持向量机的中间结果
        :return:
        """
        ker_size_ = self.ker_size
        ker_n = self.ker_n
        x_index = []
        if self.dimension == 3:
            for i in range(2 * ker_size_ + 1):
                for j in range(2 * ker_size_ + 1):
                    for k in range(2 * ker_size_ + 1):
                        x_index.append([i - ker_size_, j - ker_size_, k - ker_size_])
            x_index = np.array(x_index)
        else:
            for i in range(2 * ker_size_ + 1):
                for j in range(2 * ker_size_ + 1):
                    x_index.append([i - ker_size_, j - ker_size_])
            x_index = np.array(x_index)

        K = np.zeros((ker_n, ker_n), np.float)
        for i in range(ker_n):
            for j in range(ker_n):
                temp = x_index[i] - x_index[j]
                K[i][j] = math.exp(-(temp.dot(np.transpose(temp))) / self.sigam2)

        K = K + np.eye(ker_n) * self.gama ** (-1)
        A = np.linalg.inv(K)

        L = np.ones((1, ker_n))
        temp = np.matmul(L, A)
        B = temp / np.matmul(temp, np.transpose(L))

        alpa = np.matmul(A, (np.eye(ker_n) - np.matmul(np.transpose(L), B)))
        return alpa, x_index, B

    def f(self, alpa, x_index, B, varible):
        """
        求解函数本身的数值
        """
        if varible == 'f':
            index_ = 0
        else:
            return False

        F1 = []
        ker_n = self.ker_n
        for i in range(ker_n):
            temp1 = x_index[int((ker_n + 1) / 2) - 1] - x_index[i]
            # 求函数本身
            temp = math.exp(-(temp1.dot(np.transpose(temp1))) / self.sigam2)
            F1.append(temp)
        F1 = np.array(F1)
        Fr = np.add(np.matmul(F1, alpa), B)

        return Fr

    def f_rch(self, alpa, x_index, varible):
        """
        对函数求一阶偏导
        """
        if varible == 'r':
            index_ = 0
        elif varible == 'c':
            index_ = 1
        elif varible == 'h':
            index_ = 2
        else:
            return False

        F1 = []
        ker_n = self.ker_n
        for i in range(ker_n):
            temp1 = x_index[int((ker_n + 1) / 2) - 1] - x_index[i]
            # 求偏导数
            temp = (- 2 / self.sigam2) * (0 - x_index[i][index_]) * math.exp(-(temp1.dot(np.transpose(temp1))) /
                                                                           self.sigam2)
            F1.append(temp)
        F1 = np.array(F1)
        Fr = np.matmul(F1, alpa)
        return Fr

    def f_rrcchh(self, alpa, x_index, varible):
        """
        对函数求二阶偏导
        """
        if varible == 'r':
            index_ = 0
        elif varible == 'c':
            index_ = 1
        elif varible == 'h':
            index_ = 2
        else:
            return False
        F22 = []
        ker_n = self.ker_n
        for i in range(ker_n):
            temp1 = x_index[int((ker_n + 1) / 2) - 1] - x_index[i]
            temp = (2 / self.sigam2) * (2 / self.sigam2 * (0 - x_index[i][index_]) ** 2 - 1) * math.exp(
                -(temp1.dot(np.transpose(temp1))) / self.sigam2)
            F22.append(temp)
        F22 = np.array(F22)
        Fcc = np.matmul(F22, alpa)
        return Fcc

    def f_rchrch(self, alpa, x_index, varible):
        """
                对函数求混合二阶偏导
                """
        if varible == 'rc':
            index_ = [0, 1]
        elif varible == 'ch':
            index_ = [1, 2]
        elif varible == 'rh':
            index_ = [0, 2]
        else:
            return False
        F12 = []
        ker_n = self.ker_n
        for i in range(ker_n):
            temp1 = x_index[int((ker_n + 1) / 2) - 1] - x_index[i]
            temp = (2 / self.sigam2) ** 2 * (0 - x_index[i][index_[0]]) * (0 - x_index[i][index_[1]])\
                * math.exp(-(temp1.dot(np.transpose(temp1))) / self.sigam2)
            F12.append(temp)
        F12 = np.array(F12)
        Frc = np.matmul(F12, alpa)
        return Frc

    def f_reshape(self, Fr, x_index):
        """
        对卷积算子进行重构  得到矩阵
        经过验证，发现和直接reshape的效果一样
        :param Fr:
        :param x_index:
        :return:
        """
        n = 2 * self.ker_size + 1
        Fr_1 = np.zeros((n, n, n), np.float)
        x_index_1 = x_index + self.ker_size
        for i, item in enumerate(x_index_1):
            Fr_1[item[0], item[1], item[2]] = Fr[i]
        return Fr_1


def get_par_der_3d_operator(dimension=3, ker_size=3, sigam2=100, gama=0.01):
    # 构建卷积核的对象
    f = Ikernal23(ker_size, 1, 1, sigam2, gama, 1, dimension)

    # 调用对象的函数，得到alpa、x_index
    alpa, x_index, B = f.get_alpa()

    # 求原函数
    F = f.f(alpa, x_index, B, 'f')

    # 求一阶偏导
    Fr = f.f_rch(alpa, x_index, 'r')
    Fc = f.f_rch(alpa, x_index, 'c')
    Fh = f.f_rch(alpa, x_index, 'h')

    # 求二阶偏导
    Frr = f.f_rrcchh(alpa, x_index, 'r')
    Fcc = f.f_rrcchh(alpa, x_index, 'c')
    Fhh = f.f_rrcchh(alpa, x_index, 'h')

    # 求二阶混合偏导
    Frc = f.f_rchrch(alpa, x_index, 'rc')
    Fch = f.f_rchrch(alpa, x_index, 'ch')
    Frh = f.f_rchrch(alpa, x_index, 'rh')

    return [F, Fr, Fc, Fh, Frr, Fcc, Fhh, Frc, Fch, Frh]


def get_par_der_2d_operator(dimension=2, ker_size=3, sigam2=10, gama=1):
    """
    对2维数据进行求偏导滤波算子
    :param dimension: 维度1
    :param ker_size: 核的尺寸
    :param sigam2: 高斯函数中的方差
    :param gama: 惩罚因子
    :return:
    """
    # 构建卷积核的对象
    f = Ikernal23(ker_size, 1, 1, sigam2, gama, 1, dimension)

    # 调用对象的函数，得到alpa、x_index
    alpa, x_index, B = f.get_alpa()

    # 求原函数
    F = f.f(alpa, x_index, B, 'f')

    # 求一阶偏导
    Fr = f.f_rch(alpa, x_index, 'r')
    Fc = f.f_rch(alpa, x_index, 'c')

    # 求二阶偏导
    Frr = f.f_rrcchh(alpa, x_index, 'r')
    Fcc = f.f_rrcchh(alpa, x_index, 'c')

    # 求二阶混合偏导
    Frc = f.f_rchrch(alpa, x_index, 'rc')

    return [F, Fr, Fc, Frr, Fcc, Frc]


if __name__ == '__main__':
    # [Fr, Fc, Frr, Fcc, Frc] = test1()
    pass
