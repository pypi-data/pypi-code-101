import scipy.io
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
import scipy as sp
import scipy.interpolate as spi  # scipy.interpolate.UnivariateSpline
from io import StringIO
from datetime import date, time, datetime, timedelta
from math import exp, log, sqrt, e


def extrema(in_data):

    flag = 1
    dsize = in_data.size
    
    spmax_1 = []
    spmax_2 = []
    spmax_1.append(0)
    spmax_2.append(in_data[0])
    jj = 1
    kk = 1

    while jj < dsize - 1:
        if (in_data[jj-1] <= in_data[jj]) and (in_data[jj] >= in_data[jj+1]):
            spmax_1.append(jj)
            spmax_2.append(in_data[jj])
            kk += 1
        jj += 1
    
    spmax_1.append(dsize-1)
    spmax_2.append(in_data[-1])

    if kk >= 3:
        slope1 = (spmax_2[1] - spmax_2[2]) / (spmax_1[1] - spmax_1[2])
        tmp1 = slope1*(spmax_1[0] - spmax_1[1]) + spmax_2[1]
        if tmp1 > spmax_2[0]:
            spmax_2[0] = tmp1
    
        slope2 = (spmax_2[kk-1] - spmax_2[kk-2]) / (spmax_1[kk-1] - spmax_1[kk-2])
        tmp2 = slope2*(spmax_1[kk] - spmax_1[kk-1]) + spmax_2[kk-1]
    
        if tmp2 > spmax_2[kk]:
            spmax_2[kk] = tmp2
    else:
        flag = -1
    
    msize = in_data.size
    dsize = np.max(msize)
    xsize = dsize/3
    xsize2 = 2*xsize

    spmin_1 = []
    spmin_2 = []
    spmin_1.append(0)
    spmin_2.append(in_data[0])
    jj = 1
    kk = 1

    while jj < dsize-1:
        if (in_data[jj-1] >= in_data[jj]) and (in_data[jj] <= in_data[jj+1]):
            spmin_1.append(jj)
            spmin_2.append(in_data[jj])
            kk += 1
        jj += 1

    spmin_1.append(dsize-1)
    spmin_2.append(in_data[-1])

    if kk >= 3:
        slope1 = (spmin_2[1] - spmin_2[2]) / (spmin_1[1] - spmin_1[2])
        tmp1 = slope1*(spmin_1[0] - spmin_1[1]) + spmin_2[1]
        if tmp1 < spmin_2[0]:
            spmin_2[0] = tmp1
    
        slope2 = (spmin_2[kk-1] - spmin_2[kk-2]) / (spmin_1[kk-1] - spmin_1[kk-2])
        tmp2 = slope2*(spmin_1[kk] - spmin_1[kk-1]) + spmin_2[kk-1]
        if tmp2 < spmin_2[kk]:
            spmin_2[kk] = tmp2
    else:
        flag = -1
    flag = 1
    
    return spmax_1, spmax_2, spmin_1, spmin_2, flag

def cubic_spline_3pts(x, y, T):
    """
    Apperently scipy.interpolate.interp1d does not support
    cubic spline for less than 4 points.
    """

    x0, x1, x2 = x
    y0, y1, y2 = y

    x1x0, x2x1 = x1-x0, x2-x1
    y1y0, y2y1 = y1-y0, y2-y1
    _x1x0, _x2x1 = 1./x1x0, 1./x2x1

    m11, m12, m13= 2*_x1x0, _x1x0, 0
    m21, m22, m23 = _x1x0, 2.*(_x1x0+_x2x1), _x2x1
    m31, m32, m33 = 0, _x2x1, 2.*_x2x1

    v1 = 3*y1y0*_x1x0*_x1x0
    v3 = 3*y2y1*_x2x1*_x2x1
    v2 = v1+v3

    M = np.array([[m11,m12,m13],[m21,m22,m23],[m31,m32,m33]])
    v = np.array([v1,v2,v3]).T
    k = np.array(np.linalg.inv(M).dot(v))

    a1 = k[0]*x1x0 - y1y0
    b1 =-k[1]*x1x0 + y1y0
    a2 = k[1]*x2x1 - y2y1
    b2 =-k[2]*x2x1 + y2y1

    t = T[np.r_[T>=x0] & np.r_[T<=x2]]
    t1 = (T[np.r_[T>=x0]&np.r_[T< x1]] - x0)/x1x0
    t2 = (T[np.r_[T>=x1]&np.r_[T<=x2]] - x1)/x2x1
    t11, t22 = 1.-t1, 1.-t2

    q1 = t11*y0 + t1*y1 + t1*t11*(a1*t11 + b1*t1)
    q2 = t22*y1 + t2*y2 + t2*t22*(a2*t22 + b2*t2)
    q = np.append(q1,q2)

    return t, q


def EEMD(Y, Nstd, NE):
    
    xsize = Y.size
    dd = range(0, xsize)
    Ystd = np.std(Y, ddof=1)
    Y = Y/Ystd

    TNM = np.int_(np.fix(log(xsize, 2))) - 1
    TNM2 = TNM + 2
    
    X1 = []
    global mode_1
    mode_1 = []
    
    for iii in range(1, NE+1):
    
        for i in Y:
            temp = np.random.normal(loc=0, scale=Nstd, size=None)
            X1.append(i + temp)
            mode_1.append(i)
                
        xorigin = X1
        xend = xorigin
        
        nmode = 1
        
        mode_1 = np.array(mode_1)
        dd = np.array(dd)
        while nmode <= TNM:
            xstart = xend
            xstart = np.array(xstart)
            xend = np.array(xend)
        
            itera = 1
            
            while itera <= 10:
                spmax_1, spmax_2, spmin_1, spmin_2, flag = extrema(xstart)

                if len(spmax_2) == 3:
                    cs = spi.CubicSpline(spmax_1, spmax_2)
                    upper = cs(dd)
                    #dd_u, upper = cubic_spline_3pts(spmax_1, spmax_2, dd)
                elif len(spmax_2) > 3:
                    tck_u = spi.splrep(spmax_1, spmax_2, k=3)
                    upper = spi.splev(dd, tck_u)
                else:
                    upper = np.linspace(spmax_2[0], spmax_2[-1], dd.size)
                        
                if len(spmin_2) == 3:
                    cs = spi.CubicSpline(spmin_1, spmin_2)
                    lower = cs(dd)
                    #dd_l, lower = cubic_spline_3pts(spmin_1, spmin_2, dd)
                elif len(spmin_2) > 3:
                    tck_l = spi.splrep(spmin_1, spmin_2, k=3)
                    lower = spi.splev(dd, tck_l)
                else:
                    lower = np.linspace(spmin_2[0], spmin_2[-1], dd.size)
                    
                mean_ul = (upper + lower)/2 
                xstart -= mean_ul
                itera += 1
    
            xend -= xstart
    
            nmode += 1
    
            globals()['mode_%s'%nmode] = xstart
    
        nmode += 1
        globals()['mode_%s'%nmode] = xend
    
    for i in range(1, nmode+1):
        globals()['mode_%s'%i] = globals()['mode_%s'%i]*Ystd/NE
        globals()['modes%s'%i] = pd.Series(globals()['mode_%s'%i])

    D = {}
    for i in range(1, nmode+1):
        D["mode%s" % i] = globals()['modes%s'%i] 
        
    dfmode = pd.DataFrame(D)
    return dfmode

