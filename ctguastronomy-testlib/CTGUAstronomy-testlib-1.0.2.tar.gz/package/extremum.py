# -*- coding: utf-8 -*-
# author:           inspurer(月小水长)
# pc_type           lenovo
# create_time:      2019/5/26 13:19
# file_name:        my_differ.py
# github            https://github.com/inspurer
# 微信公众号         月小水长(ID: inspurer)


from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist


def count_extreme(args):
    """
    求曲线的偏导，得到极值点的位置及极值
    :param args:
    :return:
    """
    # 声明符号 x
    sign_x = Symbol("x")
    # 声明 y 符号表达式
    sign_y = 0
    # 数值 x
    num_x = np.arange(-5, 3, 0.01)
    # print(num_x,num_x.shape)
    # num_y = np.zeros((1,len(num_x)))
    num_y = np.zeros(len(num_x))
    # print(num_y, num_x.shape)
    for item in args:
        sign_y += item[0]*sign_x**item[1]
        num_y += item[0]*num_x**item[1]
    # y 对 x 求导
    dy = diff(sign_y, sign_x)
    # 返回导函数的零点
    extreme_x_list = solve(dy, sign_x)
    if len(extreme_x_list) == 0:
        return "no extrem vaule"
    print(extreme_x_list)
    # 声明定义域
    fig = plt.figure()
    # 使用axisartist.Subplot方法创建一个绘图区对象ax
    ax = axisartist.Subplot(fig, 111)
    # 将绘图区对象添加到画布中
    fig.add_axes(ax)

    # 引入 axisartist 会再次造成乱码,可以通过annotate解决
    plt.annotate('X轴', xy=(max(num_x), 0), xycoords='data', xytext=(0, 5),
                 textcoords='offset points', fontsize=16, fontproperties='SimHei')
    plt.annotate('Y轴', xy=(0, max(num_y)), xycoords='data', xytext=(5, 0),
                 textcoords='offset points', fontsize=16, fontproperties='SimHei')
    # plt.xlabel("X轴",fontproperties='SimHei',fontsize=14)
    # # 标签里面必须添加字体变量：fontproperties='SimHei',fontsize=14。不然中文显示可能会乱码
    # plt.ylabel("Y轴",fontproperties='SimHei',fontsize=14)
    # sympy 转成 str
    plt.title('y=' + str(sign_y))
    plt.plot(num_x, num_y)
    for i, extreme_x in enumerate(extreme_x_list):
        # 用evalf函数，传入变量的值，对表达式进行求值
        extreme_y = sign_y.evalf(subs={sign_x: extreme_x})
        # if the slove is not real
        # the class is sympy,core.numbers.Zero
        if isinstance(extreme_y, numbers. Zero):
            return "extreme value is not real"

        p = plt.scatter(extreme_x, extreme_y, s=50, c="red")
        #  xytext -- 为注解内容位置坐标，当该值为None时，注解内容放置在xy处
        #  xycoords and textcoords 是坐标xy与xytext的说明，若textcoords=None，则默认textNone与xycoords相同，
        #  若都未设置，默认为data，
        #  arrowprops 用于设置箭头的形状，类型为字典类型
        plt.annotate('y(%.6s)=%.6s ' % (extreme_x, extreme_y), xy=(extreme_x, extreme_y), xycoords='data', xytext=((-1)**(i+1)*30, (-1)**(i+1)*30),
                     textcoords='offset points', fontsize=16, fontproperties='SimHei',
                     arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

        plt.legend(handles=[p], labels=['points of extreme value'], loc='best')

        # 通过set_visible方法设置绘图区所有坐标轴隐藏
        ax.axis[:].set_visible(False)

        # ax.new_floating_axis代表添加新的坐标轴
        ax.axis["x"] = ax.new_floating_axis(0, 0)

        # 给x坐标轴加上箭头
        ax.axis["x"].set_axisline_style("->", size=1.0)
        # 添加y坐标轴，且加上箭头
        ax.axis["y"] = ax.new_floating_axis(1, 0)
        ax.axis["y"].set_axisline_style("-|>", size=1.0)
        # 设置x、y轴上刻度显示方向

        ax.axis["x"].set_axis_direction("top")
        ax.axis["y"].set_axis_direction("right")

        # 我们先把原始的如上图的所有坐标轴隐藏，即长方形的四个边。
        #
        # 然后用ax.new_floating_axis在绘图区添加坐标轴x、y，这里的ax.new_floating_axis(0, 0)，第一个0代表平行直线，第二个0代表该直线经过0点。同样，ax.axis[
        #     "y"] = ax.new_floating_axis(1, 0)，则代表竖直曲线且经过0点。
        #
        # 再次，x.axis["x"].set_axisline_style("->", size=1.0)
        # 表示给x轴加上箭头，"->"
        # 表示是空箭头，size = 1.0
        # 表示箭头大小。ax.axis["y"].set_axisline_style("-|>", size=1.0)
        # 中
        # "-|>"
        # 则是实心箭头。
        #
        # 最后，设置x、y轴上刻度显示方向，对于x轴是刻度标签在上面还是下面，y轴则是刻度标签在左边还是右边。

    plt.grid(True)
    plt.grid(color='black', linestyle='--')  # 修改网格颜色，类型为虚线,网格是跟坐标刻度来的
    plt.show()


def function_of_several_variables(args):
    # 声明符号 x
    sign_x = Symbol("x")
    # 声明 y 符号表达式
    sign_y = Symbol("y")
    # 数值 x
    sign_z = 0

    num_x = np.arange(-5, 5, 0.01)
    # print(num_x,num_x.shape)
    # num_y = np.zeros((1,len(num_x)))
    num_y = np.zeros(-5, 5, 0.01)

    num_z = np.zeros(len(num_x), len(num_y))
    # print(num_y, num_x.shape)
    for item in args:
        sign_z += item[0]*sign_x**item[1]*sign_y**item[2]
        num_z += item[0]*num_x**item[1]*num_y**item[2]


if __name__ == "__main__":
    # examples
    # wanted: 1/3*x**3-3/2*x**2+2*x
    # args: [(1/3,3),(-3/2,2),(2,1)]
    # print(count_extreme([(1/3, 3),(-3/2, 2),(2, 1)]))
    print(count_extreme([(1, 3), (4, 2), (-4, 1), (-16, 0)]))
