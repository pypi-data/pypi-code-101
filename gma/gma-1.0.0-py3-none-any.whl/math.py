# -*- coding: utf-8 -*-
"""
Some basic Mathematical operation!
=====

Update date: 2021.5.19

"""
import numpy as np
from scipy import signal, stats
import pandas as pd

def _DFToNumeric(DataFrame):

    '''
    简介
    ----------
    强制转换 DataFrame 中非数字字符串为 NAN。

    参数
    ----------
    DataFrame: pandas数据帧。

    '''

    StrData = DataFrame.select_dtypes(include = ['object'])
    if StrData.empty is False:
        DataFrame[StrData.columns] = pd.to_numeric(StrData.values.ravel(), errors = 'coerce').reshape(StrData.shape)

    return DataFrame

def FillNoData(Data, FillValue = None, Method = 'linear', **kwargs):
    '''
    简介
    ----------
    对缺失值或异常值值进行【插补】。

    参数
    ----------
    Data: list, tuple, Series, DataFrame。需要插补的数据。

    **可选参数
    ----------
    FillValue = number 或 list。标记需要进行插补的缺失值。可为数字（number）或数字列表（list）。默认不标记缺失值（None）。

        注：1.当 FillValue 为列表时，列表内所有值都将被插补。2.数据内原有的NAN、INF以及不能被转化为数字的字符串等异常值也将被插补。

    Method = str。插补方法。默认线性插值（'linear'）。其他的插补方法还包括：

        'Time'(时间),  ['index', 'values'](索引序列), 'pad'(现有值替换),
        'nearest'（最邻近）, 'nearest-up'（向上最邻近）, 'zero'（零值）, 'slinear'（滑动线性）,
        'quadratic'（2次插值）, 'cubic'（3次插值）, 'previous'（前向填充）, 'next'（后向填充）,
        'krogh'（克罗格）, 'piecewise'（分段线性）, 'polynomial'（分段多项式）, 'spline'（样条函数）,
        'pchip'（分段三次 Hermite 多项式插值）, 'akima'（akima光滑插值）, 'cubicspline'（3次样条）。

    **kwargs。传递给插值函数的其他参数。例如： Method 为 polynomial 或 spline 需要设置 order(阶数)。

    返回
    ----------
    类型: Series，DataFrame 返回输入类型；list, tuple 返回 array。

    '''

    TypeArray = 0

    # 格式化数据
    if isinstance(Data, pd.DataFrame):
        Data = _DFToNumeric(Data)
    elif isinstance(Data, pd.Series):
        Data = pd.to_numeric(Data, errors = 'coerce')
    else:
        Data = _DFToNumeric(pd.DataFrame(Data))
        TypeArray = 1

    # 格式化填充值
    if FillValue is None:
        FillValue = [np.nan, np.inf]
    elif isinstance(FillValue, list) is False:
        FillValue = [FillValue, np.inf]
    else:
        FillValue = FillValue + np.inf

    # 格式化边缘值填充方法
    if Method in ['pad', 'ffill']:
        LD = 'forward'
    elif Method in ['backfill', 'bfill']:
        LD = 'backwards'
    else:
        LD = 'both'

    Data = Data.replace(FillValue, np.nan).interpolate(method = Method, limit_direction = LD, **kwargs)

    if TypeArray == 1:
        Data = Data.values.squeeze()

    return Data

class Smooth:
    '''
    类简介
    ----------
    数据平滑（滤波）。

    初始化
    ----------
    Data: 1D data。需要平滑的 1 维数据。

    WindowSize: int。平滑窗口大小。必须为正奇数。

    Times = int。平滑次数。默认平滑 1 次。

    '''

    def __init__(self, Data, WindowSize, Times = 1):

        self.Data = Data
        self.WindowSize = WindowSize
        self.Times = Times

    def SavitzkyGolay(self, Polyorder = 2, Delta = 1, Mode = 'interp'):
        '''
        简介
        ----------
        【Savitzky-Golay】平滑。

        **可选参数
        ----------
        Polyorder = int。平滑多项式阶数。默认为 2 。

        Delta = float。将应用过滤器的样本间距。默认为 1。

        Mode = str。边缘数据处理方法。默认为 插补（'interp'）。

            其他方法：'mirror', 'nearest', 'wrap'。

        返回
        ----------
        类型: Array。

        '''
        SGData = self.Data
        for i in range(self.Times):
            SGData = signal.savgol_filter(SGData, self.WindowSize, Polyorder,
                                          delta = Delta, mode = Mode)

        return SGData

    def MovingAverage(self, Mode = 'nearest'):
        '''
        简介
        ----------
        【滑动平均】平滑。

         **可选参数
        ----------
        Mode = str。边缘数据处理方法。默认为 采用最近数据填充（'nearest'）。

            其他方法：'mirror', 'interp', 'wrap'。

        返回
        ----------
        类型: Array。

        '''

        return Smooth.SavitzkyGolay(self, Polyorder = 1, Delta = 1, Mode = Mode)

class Evaluation:
    '''
    类简介
    ----------
    数据评估。

    初始化
    ----------
    Measure: list。实测数据。

    Simulation: list。模拟数据。

    '''
    def __init__(self, Measure, Simulation):

        self.M = np.array(Measure)
        self.S = np.array(Simulation)

    def RMSE(self):
        '''均方根误差'''
        return np.sqrt(np.sum((self.M - self.S)**2) / len(self.M))

    def NRMSE(self):
        '''归一化均方根误差'''
        return Evaluation.RMSE(self) / np.mean(self.M)

    def D(self):
        '''D指标'''
        DUp = np.sum((self.S - self.M)**2)
        MAVG = np.mean(self.M)
        DDown = np.sum((abs(self.S-MAVG) + abs(self.M - MAVG))**2)
        return 1 - DUp / DDown

    def r(self):
        '''相关系数和显著性水平'''
        return stats.pearsonr(self.M, self.S)

    def R2(self):
        '''决定系数'''
        return Evaluation.r(self)[0] ** 2

    def MaxAE(self):
        '''最大绝对误差'''
        return max(abs(self.M - self.S))

    def Select(self, Method = 'ALL'):
        '''
        按选择的方法返回结果。
        -------

    	**可选参数
        -------
        Method = str, list 或 tuple。默认为输出所有方法的结果（'ALL'）。也可为：

            list 或 tuple: 列表内所有方法（ Evaluation 已经定义过算法）的结果，未定义的方法将被忽略。

            str: 单个评价方法（Evaluation 已经定义过算法，例如'RMSE'）的结果。

            若设置的方法或格式不存在，则选择 RMSE 结果输出。

        '''
        # 格式化 Method
        if isinstance(Method, str):
            if Method == 'ALL':
                SECMethod = Evaluation.Methods()
            elif Method in Evaluation.Methods():
                SECMethod = [Method]
            else:
                print('方法 %s 不存在，返回 RMSE 结果。' % [Method])
                SECMethod = ['RMSE']

        elif isinstance(Method, (list, tuple)):
            NUM = len(Method)

            SECMethod = list(set(Evaluation.Methods()) & set(Method))

            if SECMethod == []:
                print('设置方法全部不存在，返回 RMSE 结果')
                SECMethod = ['RMSE']
            elif len(SECMethod) != NUM:
                print('方法 %s 不存在，已被忽略。' % list(set(Method) - set(SECMethod)))

        else:
            print('参数格式不正确，返回 RMSE 结果。')
            SECMethod = ['RMSE']

        # 计算所有结果
        re = {}
        for Me in SECMethod:
            if Me != 'r':
                re[Me] = getattr(Evaluation, Me)(self)
            else:
                re['r'], re['P'] = getattr(Evaluation, Me)(self)

        return re

    def Methods():
        '''记录Evaluation类中所有的评估方法。'''
        return [Method for Method in dir(Evaluation) if
                '__' not in Method and Method not in ['Methods', 'Select']]

