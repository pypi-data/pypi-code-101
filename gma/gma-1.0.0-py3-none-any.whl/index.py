# -*- coding: utf-8 -*-
"""
Created on Wed May 19 17:42:50 2021

@author: admin
"""
import numpy as np

def EVI(Nir, Red, Blue):
    '''
    简介
    ----------
    增强植被指数。

    参数
    ----------
	Nir: 近红外

	Red: 红

	Blue:蓝

	'''
    _EVI = 2.5 * (Nir - Red) / (Nir + 6 * Red - 7.5 * Blue + 1)
    return _EVI

def NDBI(Nir, Swir):
    '''
    简介
	----------
	归一化建筑指数。

	参数
	----------
	Nir: 近红外

	Swir: 短波红外

	'''
    _NDBI = (Swir - Nir) / (Swir + Nir)
    return _NDBI

def NDVI(Nir, Red):
    '''
    简介
    ----------
    归一化植被指数。

    参数
    ----------
    Nir: 近红外

    Red: 红

    '''
    _NDVI = (Nir - Red) / (Nir + Red)

    return _NDVI

def NDWI(Nir, Green):
    '''
    简介
    ----------
    归一化水指数。

    参数
    ----------
    Nir: 近红外

    Green: 绿

    '''
    return (Green - Nir) / (Green + Nir)

def PM_ET0(Pres, Wind, MaxT, MinT, Rh, Shour, Lat, Day, Ele,
          AS = 0.25,
          BS = 0.5,
          A = 0.23
          ):
    '''
    简介
    ----------
    彭曼法（Penman Monteith）计算【日】【作物参考蒸散量（ET0）】。

    参数
    ----------
    Pres: number 或 array。日平均气压（hPa）。

    Wind: number 或 array。日平均10m风速（m/s）。

    MaxT: number 或 array。日最高气温（℃）。

    MaxT: number 或 array。日最低气温（℃）。

    Rh: number 或 array。日平均相对湿度（%）。

    Shour: number 或 array。日日照时数（hr）。

    Lat: number 或 array。纬度（°）。

    Day: int 或 array。以日序（儒略日）表示。1-365（平年）或366（闰年）。

    Ele: number 或 array。海拔高度（m）。

    **常量
    ----------
    AS = 0.25。

    BS = 0.5。

    A = 0.23。

    返回
    ----------
    类型: float 或 array。

    '''

    δ = 0.409 * np.sin(2 * np.pi * Day / 365 - 1.39)    #赤纬，取决于日序

    DR = 1 + 0.033 * np.cos(2 * np.pi * Day / 365)  #日地相对距离，取决于日序

    RAD = Lat * np.pi / 180  # 弧度，取决于纬度

    WS  = np.arccos(-np.tan(RAD) * np.tan(δ)) # 时角,取决于纬度

    RA = 24 * 60 / np.pi * 0.082 * DR * (WS * np.sin(RAD) * np.sin(δ) + np.cos(RAD) * np.cos(δ) * np.sin(WS)) #大气层外太阳辐射通量

    ND = 24 * WS / np.pi #白昼时数

    E0T_MAX = 0.6108 * np.exp((17.27 * MaxT) / (MaxT + 237.3))
    E0T_MIN = 0.6108 * np.exp((17.27 * MinT) / (MinT + 237.3))
    ES = 0.5 * (E0T_MAX + E0T_MIN) # 饱和水气压

    U = 4.87 * Wind / np.log(67.8 * 10 - 5.42) # 2m高风速

    EA = (Rh / 100) * ES # 水气压

    RSO = (0.75 + 2 * Ele / 100000) * RA # 晴天地表短波辐射通量
    RS = (AS + BS * Shour / ND) * RA   # 地表短波辐射

    RN = (1 - A) * RS - (4.903 / (10 ** 9) * 0.5 * ((MaxT + 273.15) ** 4 + (MinT + 273.15) ** 4) * (0.34 - 0.14 * (EA ** 0.5)) * (1.35 * RS / RSO - 0.35)) # 地表净辐射

    RC = 0.00163 * Pres * 0.1 / 2.45  # 干湿表常数
    DT = 4098 * 0.6108 * np.exp((17.27 * (MaxT + MinT) * 0.5) / ((MaxT + MinT) * 0.5 + 237.3)) / ((MaxT + MinT) * 0.5 + 237.3) ** 2 # Δ值

    ET0 = (RC * 900 * U * (ES - EA) / ((MaxT + MinT) * 0.5+ 273.15) / (DT + RC * (1 + 0.34 * U)) + 0.408 * DT * RN / (DT + RC * (1 + 0.34 * U)))

    return ET0


