# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 21:23:50 2021

@author: ZSL
"""
import numpy as np
import math
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from vtda.util.util import weight_factor

#解决中文乱码问题
plt.rcParams["font.sans-serif"]='SimHei'
#解决负号无法正常显示问题
plt.rcParams["axes.unicode_minus"]= False
from tqdm import tqdm
from vtda.util.util import (
                                               weight_factor,
                                               fix_num,
                                               find_start_end
                                            )
from vtda.analysis.base import (               choose_windows,
                                               fft,
                                               octave_3,
                                               base_level,
                                               rms_time,
                                               rms_frec,
                                            )

def sperling(y, 
            sample_rate=4096,
            len_=5,
            window='hanning',
            cdxs=0,
            direction='vertical', #horizontal
            unit='m/ss',#g
            n=1 #保留结果小数点后位数
            ):
    '''
    计算平稳性函数
    Parameters
    ----------
    y : TYPE
        待计算数据，可以为np.ndarray或者 pd.Series格式
    sample_rate : TYPE, optional
        采样点数，默认为4096，如果待计算数据为pd.Series格式，其中有采样频率信息，则优先采用其信息。
    len : TYPE, optional
        分析长度，默认为5秒
    window : TYPE, optional
        加窗，默认为汉宁窗
    cdxs : TYPE, optional
        重叠系数，默认为0
    Returns
    -------
    返回两个结果list，一个为时间，另一个为随时间变化的平稳性

    '''

    if isinstance(y, pd.DataFrame) or isinstance(y, pd.Series):
        sample_rate=1/(y.index[1]-y.index[0])
        y=y.fillna(0)
        y=np.array(y)        
    elif isinstance(y, np.ndarray):
        pass
    else:
        print("{} 错误数据输入格式。。。".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))             
    
    
    fft_size=len_*sample_rate   
    n_zong=max(math.ceil((len(y)-fft_size)/(round((1-cdxs),5)*fft_size))+1,1)#上取整
    res=np.zeros(int(fft_size/2))
    res_sperling=[]

    for i in tqdm(np.arange(n_zong),desc='正在计算平稳性'):
        pass
        #i=4
        y_=y[int(i*round((1-cdxs),5)*fft_size):int(i*round((1-cdxs),5)*fft_size+fft_size)][:int(fft_size)] 
        if len(y_)>0:
            res_x,res_y_=fft(y_,
                             sample_rate=sample_rate,
                             fft_size =fft_size,
                             cdxs=cdxs,
                             fix_meth='能量修正',
                             window=window,
                             )
            if direction in ['vertical','v','V','chui','chuixiang','垂','垂向']: #垂向
                w=[]
                for i in np.arange(len(res_x)):
                    pass
                    x_fft=res_x[i]
                    y_fft=res_y_[i]
                    if x_fft>=0.5 and x_fft<5.9:
                        w_ls=3.57*math.pow((y_fft**3*0.325*x_fft), 1/10)
                        w.append(w_ls)
                    elif x_fft>=5.9 and x_fft<20:
                        w_ls=3.57*math.pow((y_fft**3*400*x_fft), 1/10)
                        w.append(w_ls)    
                    elif x_fft>=20 and x_fft<=40:
                        w_ls=3.57*math.pow((y_fft**3/x_fft), 1/10)
                        w.append(w_ls)
                ww=math.pow(sum([i**10 for i in w]), 1/10)
            elif direction in ['horizontal','h','H','heng','hengxiang','横','横向']: #横向
                w=[]
                for i in np.arange(len(res_x)):
                    pass
                    x_fft=res_x[i]
                    y_fft=res_y_[i]
                    if x_fft>=0.5 and x_fft<5.4:
                        w_ls=3.57*math.pow((y_fft**3*0.8*x_fft), 1/10)
                        w.append(w_ls)
                    elif x_fft>=5.4 and x_fft<26:
                        w_ls=3.57*math.pow((y_fft**3*650*x_fft), 1/10)
                        w.append(w_ls)    
                    elif x_fft>=26 and x_fft<=40:
                        w_ls=3.57*math.pow((y_fft**3/x_fft), 1/10)
                        w.append(w_ls)
                ww=math.pow(sum([i**10 for i in w]), 1/10)            

            res_sperling.append(ww)
            res_x=list(np.arange(len_,len_*n_zong,len_))
            res_x.append((len(y_)/fft_size)*len_+len_*(n_zong-1))
    return res_x,res_sperling

if __name__ == '__main__':


    
    import vtda
    
    dir_='E:/城轨中心/2项目/20210615昆明车辆异常晃动/昆明加速度数据/昆明1、2号线/上行-大学城南-北部汽车站'
    name='20210126昆明地铁1、2、呈贡支线测试'
    data,info=vtda.read_dasp_data(name,dir_=dir_,num_tongdao='1')
    i=1
    j=1
    y=data[i][j]
    t1=time.time()
    time_,spr=sperling(y,  #数据
            sample_rate=4096, #采样频率
            len_=5, #分析窗长
            window='hanning', #窗函数
            cdxs=0.8, #重叠系数
            direction='垂向', #或者填横向  #数据方向
            )
    print(time.time()-t1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(time_,spr)   
