# -*- coding: utf-8 -*-
import numpy as np
import sympy
from sympy.plotting import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pylab import mpl

import ikernal23 as ker
from scipy.ndimage.filters import convolve as convolveim

# 解决画图是中文显示的问题
mpl.rcParams['font.sans-serif'] = ['SimHei']


def function_fxy():
    # 声明符号 x
    s_x = sympy.Symbol("x")
    # 声明 y 符号表达式
    s_y = sympy.Symbol("y")
    # 数值 x
    num_x = np.arange(-10, 10, 0.1)
    num_y = np.arange(-10, 10, 0.1)
    # print(num_x,num_x.shape)
    # num_y = np.zeros((1,len(num_x)))
    num_z = np.zeros((len(num_x), len(num_y)), np.float)
    # print(num_y, num_x.shape)
    sign_z = 2 * (1 - s_x) ** 2 * sympy.exp(-s_x ** 2 - (s_y + 1) ** 2) - 10 * (0.2 * s_x ** 4 - s_y ** 5) * sympy.exp(
        -s_y ** 2 - s_x ** 2) - (1 / 3) * sympy.exp(-(s_x + 1) ** 2 - s_y ** 2)

    num_z = 2 * (1 - num_x) ** 2 * np.exp(-num_x ** 2 - (num_y + 1) ** 2) - 10 * (0.2 * num_x ** 4 - num_y ** 5) * np.exp(
        -num_y ** 2 - num_x ** 2) - (1 / 3) * np.exp(-(num_x + 1) ** 2 - num_y ** 2)
    return s_x, s_y, sign_z, num_z


def function_fxy_1():
    # 声明符号 x
    s_x = sympy.Symbol("x")
    # 声明 y 符号表达式
    s_y = sympy.Symbol("y")
    # 数值 x
    num_x = np.arange(-10, 10, 0.1)
    num_y = np.arange(-10, 10, 0.1)
    num_x, num_y = np.meshgrid(num_x, num_y)

    sign_z = sympy.exp(-(s_x ** 2 + s_y ** 2)/25)

    num_z = np.exp(-(num_x ** 2 + num_y ** 2)/25)
    return s_x, s_y, sign_z, num_x, num_y, num_z


def function_fxy_2_x():
    # 声明符号 x
    s_x = sympy.Symbol("x")
    s_y = sympy.Symbol("y")

    num_x = np.arange(-10, 10, 0.01)
    num_y = np.arange(-10, 10, 0.01)
    num_x, num_y = np.meshgrid(num_x, num_y)

    s_z = - 0.08 * sympy.exp(-(s_x ** 2 + s_y ** 2)/25) * s_x
    num_z1 = - 0.08 * np.exp(-(num_x ** 2 + num_y ** 2)/25) * num_x
    return s_x, s_y, s_z, num_x, num_y, num_z1


def function_fxy_2_y():
    # 声明符号 x
    s_x = sympy.Symbol("x")
    s_y = sympy.Symbol("y")

    num_x = np.arange(-10, 10, 0.01)
    num_y = np.arange(-10, 10, 0.01)
    num_x, num_y = np.meshgrid(num_x, num_y)

    s_z = - 0.08 * sympy.exp(-(s_x ** 2 + s_y ** 2)/25) * s_y
    num_z1 = - 0.08 * np.exp(-(num_x ** 2 + num_y ** 2)/25) * num_y
    return s_x, s_y, s_z, num_x, num_y, num_z1


def function_fxy_2_xx():
    # 声明符号 x
    s_x = sympy.Symbol("x")
    s_y = sympy.Symbol("y")

    num_x = np.arange(-10, 10, 0.01)
    num_y = np.arange(-10, 10, 0.01)
    num_x, num_y = np.meshgrid(num_x, num_y)

    s_z = (4 / 625) * sympy.exp(-(s_x ** 2 + s_y ** 2)/25) * s_x ** 2 - \
          (2 / 25) * sympy.exp(-(s_x ** 2 + s_y ** 2) / 25)
    num_z1 = (4 / 625) * np.exp(-(num_x ** 2 + num_y ** 2)/25) * num_x ** 2 - \
             (2 / 25) * np.exp(-(num_x ** 2 + num_y ** 2) / 25)
    return s_x, s_y, s_z, num_x, num_y, num_z1


def function_fxy_2_xy():
    # 声明符号 x
    s_x = sympy.Symbol("x")
    s_y = sympy.Symbol("y")

    num_x = np.arange(-10, 10, 0.01)
    num_y = np.arange(-10, 10, 0.01)
    num_x, num_y = np.meshgrid(num_x, num_y)

    s_z = (4 / 625) * sympy.exp(-(s_x ** 2 + s_y ** 2)/25) * s_x * s_y
    num_z1 = (4 / 625) * np.exp(-(num_x ** 2 + num_y ** 2)/25) * num_x * num_y
    return s_x, s_y, s_z, num_x, num_y, num_z1


def make_pic(x, y, value_, title):
    fig2 = plt.figure()
    ax1 = Axes3D(fig2)
    surf = ax1.plot_surface(x, y, value_)
    plt.title(title)
    plt.show()


def test2():
    s_x, s_y, s_z, num_x, num_y, num_z = function_fxy_1()

    # 将函数表面画出
    p1 = plot3d(s_z, (s_x, -10, 10), (s_y, -10, 10))

    s_x1, s_y1, s_z1, num_x, num_y, num_z1 = function_fxy_2_y()

    p12 = plot3d(s_z1, (s_x1, -10, 10), (s_y1, -10, 10))
    s_x1, s_y1, s_z1, num_x, num_y, num_z1 = function_fxy_2_x()

    p12 = plot3d(s_z1, (s_x1, -10, 10), (s_y1, -10, 10))

    s_x22, s_y22, s_z22, num_x, num_y, num_z1 = function_fxy_2_xx()
    p22 = plot3d(s_z22, (s_x22, -10, 10), (s_y22, -10, 10))

    s_x21, s_y21, s_z21, num_x, num_y, num_z1 = function_fxy_2_xy()
    p22 = plot3d(s_z21, (s_x21, -10, 10), (s_y21, -10, 10))

    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_surface(num_x, num_y, num_z1)
    plt.show()
    # make_pic(num_x, num_y, num_z)
    #
    # # fig1 = plt.figure()
    # # ax1 = Axes3D(fig1)
    # # surf = ax1.plot_surface(num_x, num_y, num_z1)
    # # plt.show()
    # make_pic(num_x, num_y, num_z1)

    # [Fr, Fc, Frr, Fcc, Frc] = ker.test1()
    # result = convolveim(num_z, Fc.reshape((7, 7), order='A'), mode='constant')
    # # fig2 = plt.figure()
    # # ax1 = Axes3D(fig2)
    # # surf = ax1.plot_surface(num_x[50:1950, 50:1950], num_y[50:1950, 50:1950], result[50:1950, 50:1950])
    # # plt.show()
    # make_pic(num_x[50:1950, 50:1950], num_y[50:1950, 50:1950], result[50:1950, 50:1950])
    #
    # result = convolveim(num_z, Fr.reshape((7, 7), order='A'), mode='constant')
    # # fig2 = plt.figure()
    # # ax1 = Axes3D(fig2)
    # # surf = ax1.plot_surface(num_x[50:1950, 50:1950], num_y[50:1950, 50:1950], result[50:1950, 50:1950])
    # # plt.show()
    # make_pic(num_x[50:1950, 50:1950], num_y[50:1950, 50:1950], result[50:1950, 50:1950])
    #


def test3():
    s_x, s_y, s_z, num_x, num_y, num_z = function_fxy_1()
    s_x21, s_y21, s_z21, num_x, num_y, num_z1 = function_fxy_2_xy()
    value_ = np.zeros((20, 20), np.float)
    for i in range(-10, 10):
        for j in range(-10, 10):
            value_[i+10, j+10] = s_z.evalf(subs={'x': i, 'y': j})

    x = np.linspace(-10, 10, 20)
    y = np.linspace(-10, 10, 20)
    x, y = np.meshgrid(x, y)

    [F, Fr, Fc, Frr, Fcc, Frc] = ker.get_par_der_2d_operator()
    size_n = ker.ker_size * 2 + 1
    result = convolveim(value_, F.reshape((size_n, size_n), order='A'), mode='constant')
    result_r = convolveim(value_, Fr.reshape((size_n, size_n), order='A'), mode='constant')
    result_c = convolveim(value_, Fc.reshape((size_n, size_n), order='A'), mode='constant')
    result_cc = convolveim(value_, Fcc.reshape((size_n, size_n), order='A'), mode='constant')
    result_rr = convolveim(value_, Frr.reshape((size_n, size_n), order='A'), mode='constant')
    result_rc = convolveim(value_, Frc.reshape((size_n, size_n), order='A'), mode='constant')
    make_pic(x, y, result, u"拟合高斯图")
    # print(result.max())
    # print(value_.max())
    make_pic(x, y, value_, u'原始高斯图')
    make_pic(x, y, result_r, 'fr')
    make_pic(x, y, result_c, 'fc')
    make_pic(x, y, result_rr, 'frr')
    make_pic(x, y, result_rc, 'frc')
    make_pic(x, y, result_cc, 'fcc')


def test():
    pass


if __name__ == '__main__':
    test3()