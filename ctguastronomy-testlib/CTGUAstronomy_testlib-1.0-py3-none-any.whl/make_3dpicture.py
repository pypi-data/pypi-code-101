import pylab as pb
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from astropy.io import fits
import seaborn as sb
import pyrr.matrix44
from typing import Callable, NamedTuple, Sequence
import cufflinks as cf
import plotly
import plotly.graph_objs as go


def test(image1):
    """
    调用浏览器显示3D的散点图
    :return:
    """
    # image1 = fits.getdata(r'data\m.fits')
    matrix = [i for i in range(20)]
    fig1 = go.Scatter3d(x=matrix, y=matrix, z=matrix,
                        marker=dict(opacity=0.9, reversescale=True, color=np.random.rand(20), size=5
                                    ), line=dict(width=0.02), mode='markers')

    mylayout = go.Layout(scene=dict(xaxis=dict(title="curb-weight"),
                                    yaxis=dict(title="horsepower"),
                                    zaxis=dict(title="price")
                                    ))

    plotly.offline.plot({"data": [fig1], "layout": mylayout}, auto_open=True, filename="3DPlot.html")


def test1():
    fig = pb.figure()
    ax = Axes3D(fig)
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
    pb.show()


def test2():

    x1 = [1, 2, 3, 4]
    y1 = [1, 2, 3, 4]  # 第一组数据
    z1 = [1, 2, 3, 4]

    x2 = [1, 2, 3, 4]
    y2 = [2, 3, 4, 5]  # 第二组数据

    n = 10
    x3 = np.random.randint(0, 5, n)
    y3 = np.random.randint(0, 5, n)  # 使用随机数产生

    plt.scatter(x1, y1, z1, marker='x', color='red', s=40, label='First')
    # plt.scatter(x2, y2, marker='+', color='blue', s=40, label='Second')
    # plt.scatter(x3, y3, marker='o', color='green', s=40, label='Third')
    # plt.legend(loc='best')  # 设置 图例所在的位置 使用推荐位置

    plt.show()
    # ---------------------
    # 版权声明：本文为CSDN博主「MirrorN」的原创文章，遵循CC
    # 4.0
    # by - sa版权协议，转载请附上原文出处链接及本声明。
    # 原文链接：https: // blog.csdn.net / sinat_34328764 / article / details / 80355060


def randrange(n, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return (vmax - vmin) * np.random.rand(n) + vmin


def test3():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    n = 100

    # For each set of style and range settings, plot n random points in the box
    # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
    for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
        xs = randrange(n, 23, 32)
        ys = randrange(n, 0, 100)
        zs = randrange(n, zlow, zhigh)
        ax.scatter(xs, ys, zs, c=c, marker=m, alpha=0.5)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()


def test4():
    image1 = fits.getdata(r'data\hdu0_mosaic_L.fits')
    # image1 = fits.getdata(r'data\m.fits')
    x_min = image1.min()
    x_max = image1.max()
    x_max_min = x_max - x_min
    alp = (image1 - x_min) / x_max_min
    alp[alp < 0.4] = 0
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    [x_len, y_len, z_len] = image1.shape
    i = 1
    for xs in range(x_len):
        print(i)
        i += 1
        for ys in range(y_len-160):
            for zs in range(z_len-340):
                ax.scatter(xs, ys, zs, c='b', marker='.', alpha=alp[xs, ys, zs])
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()


if __name__ == '__main__':
    test()
    # test2()
    # test3()
    # test4()
    # pass




