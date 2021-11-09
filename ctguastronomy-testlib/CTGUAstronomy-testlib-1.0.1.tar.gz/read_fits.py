from astropy.io import fits
import scipy.io as sio
from scipy.ndimage.filters import convolve as convolveim
import matplotlib.pyplot as plt
import ikernal23 as iker
import cv2
import os
from sklearn import cluster
import numpy as np
import pandas as pd


"""
fits.getdata()
return file style:numpy.ndarray

"""


def dbscan_la():
    """
    采用DBSCAN聚类算法，对返回的极大值点进行聚类
    :return:
    """
    X = [[7, 11, 70],
         [7, 47, 171],
         [7, 59, 32],
         [7, 91, 85],
         [7, 92, 85],
         [7, 170, 51],
         [7, 198, 53]]
    X = pd.DataFrame(X)

    dbscan = cluster.DBSCAN(eps=1.73, min_samples=1)
    """cluster.DBSCAN(eps=0.5, min_samples=5, metric='euclidean',
                   metric_params=None, algorithm='auto',
                   leaf_size=30, p=None, n_jobs=1)
    eps：用于设置密度聚类中的ε领域，即半径，默认为0
    .5；
    min_samples：用于设置ε领域内最少的样本量，默认为5；
    metric：用于指定计算点之间距离的方法，默认为欧氏距离；
    metric_params：用于指定metric所对应的其他参数值；
    algorithm：在计算点之间距离的过程中，用于指点搜寻最近邻样本点的算法；默认为
    'auto'，表示密度聚类会自动选择一个合适的搜寻方法；如果为
    'ball_tree'，则表示使用球树搜寻最近邻；如果为
    'kd_tree'，则表示使用K - D树搜寻最近邻；如果为
    'brute'，则表示使用暴力法搜寻最近邻；
    leaf_size：当参数algorithm为'ball_tree'或'kd_tree'时，用于指定树的叶子节点中所包含的最多样本量，默认为30；
        该参数会影响搜寻树的构建和搜寻最近邻的速度；
    p：当参数metric为闵可夫斯基距离时（'minkowski'），p = 1，表示计算点之间的曼哈顿距离；
        p = 2，表示计算点之间的欧氏距离；该参数的默认值为2；
    n_jobs：用于设置密度聚类算法并行计算所需的CPU数量，默认为1表示仅使用1个CPU运行算法，即不使用并行运算功能；
    """
    # 模型拟合
    a=dbscan.fit(X)


def generate_video():
    path = "./result/"  # 文件路径

    filelist = os.listdir(path)

    fps = 3  # 视频每秒24帧
    picture_size = (640, 480)  # 需要转为视频的图片的尺寸
    # 可以使用cv2.resize()进行修改

    video = cv2.VideoWriter("VideoTest1.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, picture_size)
    # 视频保存在当前目录下

    for item in filelist:
        if item.endswith('.png'):
            # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
            item = path + item
            img = cv2.imread(item)
            img.resize(640, 480)
            video.write(img)

    video.release()
    cv2.destroyAllWindows()


def conv_3d():
        """
        对三维数据进行滤波
        """
        image1 = fits.getdata(r'data\noise.fits')
        [Fr, Fc, Fh, Frr, Fcc, Fhh, Frc, Fch, Frh] = iker.get_par_der_3d_operator()
        convl = []
        n = iker.ker_size * 2 + 1
        for i, item in enumerate([Fr, Fc, Fh, Frr, Fcc, Fhh, Frc, Fch, Frh]):
            kernel = item.reshape(n, n, n)
            convl.append(convolveim(image1, kernel, mode='constant'))

        thread = 0.0001
        [x_size, y_size, z_size] = image1.shape
        num = 1
        for i in range(x_size):
            for j in range(y_size):
                for k in range(z_size):
                    temp = positive_matrix(convl, i, j, k)
                    if (abs(convl[0][i, j, k]) < thread) and (abs(convl[1][i, j, k]) < thread) and (abs(convl[2][i, j, k]) < thread):
                        if (convl[3][i, j, k] < 0) and (convl[4][i, j, k] < 0) and (convl[5][i, j, k] < 0):
                            print([i, j, k])
                            # print(image1[i, j, k])
                            num += 1
            # 寻找最大值的下标
            # np.where(image1==np.max(image1))
        return num, convl

def positive_matrix(convl_0, i, j, k):
        pos_mat = np.zeros((3, 3), np.float)
        for ii in range(3):
            pos_mat[ii, ii] = convl_0[ii + 3][i, j, k]
        pos_mat[0, 1] = pos_mat[1, 0] = convl_0[6][i, j, k]
        pos_mat[0, 2] = pos_mat[2, 0] = convl_0[8][i, j, k]
        pos_mat[1, 2] = pos_mat[2, 1] = convl_0[7][i, j, k]

        temp = np.linalg.eig(pos_mat)
        stutas = True
        for item in range(3):
            if temp[0][item] > 0:
                stutas = False
        if np.linalg.det(pos_mat) < 0:
            stutas = False
        return stutas, pos_mat

def conv_2d():
        """
        对二维数据进行滤波
        :return:
        """
        image1 = fits.getdata(r'data\noise.fits')
        [F, Fr, Fc, Frr, Fcc, Frc] = iker.get_par_der_2d_operator(dimension=2, ker_size=5, sigam2=100, gama=0.01)
        img = image1[23, :, :]

        n = iker.ker_size * 2 + 1
        # img = convolveim(img, F.reshape(n, n), mode='constant')
        conv = []
        for item in [Fr, Fc, Frr, Fcc, Frc]:
            conv.append(convolveim(img, item.reshape(n, n), mode='constant'))
        # conv_r = convolveim(img, Fr.reshape(n, n), mode='constant')
        # conv_c = convolveim(img, Fc.reshape(n, n), mode='constant')
        # conv_rr = convolveim(img, Frr.reshape(n, n), mode='constant')
        # conv_cc = convolveim(img, Fcc.reshape(n, n), mode='constant')
        # conv_rc = convolveim(img, Frc.reshape(n, n), mode='constant')

        thread = 0.04
        [x_len, y_len] = img.shape

        # 输出找到极大值点与否和极大值点
        status, extreme_points = judging_extreme_points(conv, x_len, y_len, thread)
        plt.imshow(img)
        if not status:
            s = u'未找到极大值点'
            plt.title(s)

        # 将极大值点在图上绘制出来
        for item in extreme_points:
            plt.plot(item[0], item[1], 'r.')

        plt.show()
        # np.where(image1==np.max(image1))寻找最大值的下标
        return extreme_points

def judging_extreme_points(conv, x_len, y_len, thread):
        """
        :param conv: 各项偏导算子，数据类型为列表
                conv=[Fr, Fc, Frr, Fcc, Frc]
        :param x_len: 图像的高(多少行)
        :param y_len: 图像的宽(多少列)
        :param thread: 一阶偏导绝对值小于的阈值，按照极值理论，梯度为0的点为驻点
        :return:
         status:True or False 找到极大值点的状态
         points:极大值点坐标集合，数据类型为列表；没有极大值则为空。
        """
        points = []
        status = False
        for i in range(x_len):
            for j in range(y_len):
                if abs(conv[0][i, j]) < thread and abs(conv[1][i, j]) < thread:
                    if ((conv[2][i, j] * conv[3][i, j] - conv[4][i, j] ** 2) > 0.00001) and (conv[3][i, j] < 0):
                        points.append([j, i])
        #   Python的坐标轴是反的
                        status = True
        return status, points

def determine_core_edge_by_watershed(markers_1):
        """
        对图片用watershed来确定云核边界
        :return:
        """
        image1 = fits.getdata(r'data\noise.fits')
        for i in range(200):
            img = image1[23, :, :]

            img = ((img-img.min())/(img.max()-img.min())*255)
            img = img.astype(np.uint8)
            ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
            gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            # plt.imshow(gray)
            # plt.show()
            thresh = 255 - thresh
            # plt.imshow(thresh)
            # plt.show()

            # ret1, markers1 = cv2.connectedComponents(thresh)
            ret1, markers1 = cv2.connectedComponents(markers_1)
            markers3 = cv2.watershed(gray, markers1)
            gray[markers3 == -1] = [255, 0, 0]
            picture_name = str(i).zfill(3) + '.png'
            plt.title(str(i).zfill(3))
            plt.imshow(gray)
            # plt.savefig('result4/' + picture_name)
            plt.show()
            break

        # kernel = np.ones((3, 3), np.uint8)
        # opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
        # # sure background area
        # sure_bg = cv2.dilate(opening, kernel, iterations=3)
        """
        # Finding sure foreground area
    # 距离变换的基本含义是计算一个图像中非零像素点到最近的零像素点的距离，也就是到零像素点的最短距离
    # 个最常见的距离变换算法就是通过连续的腐蚀操作来实现，腐蚀操作的停止条件是所有前景像素都被完全
    # 腐蚀。这样根据腐蚀的先后顺序，我们就得到各个前景像素点到前景中心??像素点的
    # 距离。根据各个像素点的距离值，设置为不同的灰度值。这样就完成了二值图像的距离变换
       #cv2.distanceTransform(src, distanceType, maskSize)
    # 第二个参数 0,1,2 分别表示 CV_DIST_L1, CV_DIST_L2 , CV_DIST_C
        """
        # dist_transform = cv2.distanceTransform(opening, 1, 5)
        # ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
        # # Finding unknown region
        # sure_fg = np.uint8(sure_fg)
        # unknown = cv2.subtract(sure_bg, sure_fg)
        #
        # ret1, markers1 = cv2.connectedComponents(sure_fg)
        # markers = markers1 + 1
        #
        # markers[unknown == 255] = 0
        # markers1 = markers1.astype(cv2.CV_32SC1)
        # markers1 = cv2.cvtColor(markers1, cv2.CV_32SC1)

def save_text_picture():
        # image1 = fits.getdata(r'1clump\1clumpnoise.fits')
        image1 = fits.getdata(r'data\noise.fits')
        # plt.imshow(image1[23,:,:])

        sio.savemat('saveddata.mat', image1[23, :, :])

        for i in range(200):
            name = str(i).zfill(3)
            np.savetxt('result/' + name + "result.txt", image1[i, :, :])
        for i in range(200):
            # plt.imshow(image1[20:45, i+133,110 :135])
            plt.imshow(image1[i, :, :])
            picture_name = str(i).zfill(3) + '.png'
            # plt.imshow(image1[i,:,:])

            plt.title(str(i).zfill(3))
            plt.savefig('result4/' + picture_name)
            # plt.show()
            # plt.imshow(image1[i, :, :])
            picture_name = str(i).zfill(3) + '.png'
            # plt.imshow(image1[i,:,:])

            plt.title(str(i).zfill(3))
            plt.savefig('result4/' + picture_name)


if __name__ == '__main__':
    pass
    # num, convl = test_1()
    # print(convl[0][18, 18, 27])
    # print(convl[1][18, 18, 27])
    # print(convl[2][18, 18, 27])
    # print(positive_matrix(convl, 18, 18, 27))
    # print(np.linalg.det(temp[1]))
    # print(np.linalg.eig(temp[1])[0])
    # extreme_points = conv_2d()
    # marker = np.zeros((200, 200), np.uint8)
    for item in extreme_points:
        marker[item[1], item[0]] = 1
    #
    # plt.imshow(marker)
    # plt.show()
    #
    # determine_core_edge_by_watershed(marker)
    # pass
    # cv2.watershed()
