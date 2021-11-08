#!/usr/bin/env python
# coding: utf-8

import scipy.io
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
from io import StringIO
from datetime import date, time, datetime, timedelta
from math import exp, log, sqrt, e
import ecg_analysis.EEMD as EMD

def ShannonEn(data, bins=55, Min=0.3, Max=1.6, base=None):

    edges = np.arange(Min, Max+(Max-Min)/bins, (Max-Min)/bins)
    edges = np.around(edges[0:-1], decimals=4)
    c = np.array
    
    c,bins = np.histogram(data,bins = edges)
    
    n_classes = np.count_nonzero(c)
    
    if n_classes <= 1:
        return 0
    
    ent = 0.

    for i in c[1:]:
        if i != 0:
            ent -= np.around((i/data.size), decimals=4) * np.around(np.log(i/data.size), decimals=4)
    ent = np.around(ent, decimals=4)
    return ent


def coarse_grained_EEE(data, scale=14, bins=55, Min=0.3, Max=1.6, base=None):
    
    N = data.size
    buf = np.array
    
    for i in range(0, np.int_(np.fix(N/scale))):
        buf = np.append(buf, ShannonEn(data[i*scale : (i+1)*scale], bins, Min, Max))

    return buf


def ShannonEn_2nd(buf):
    
    buf2 = np.sort(buf[1:])
    pos2 = np.array
    SE2 = 0.
    
    for i in range(0, buf2.size-1):
        if buf2[i] != buf2[i+1]:
            pos2 = np.append(pos2, i)

    if buf2.mean() == 0:
        return 0.0
            
    c2 = np.diff(pos2[1:], axis=0)
    
    for i in c2:
        if i != 0:
            SE2 -= np.around((i/buf[1:].size), decimals=4) * np.around(np.log(i/buf[1:].size), decimals=4)
    return SE2


def EEE(data, scale=20, bins=55, Min=0.3, Max=1.6, base=None):
    
    ShE = np.around(ShannonEn(data, bins, Min, Max), decimals=2)
    
    for i in range(1, scale+1):
        buf = coarse_grained_EEE(data, i, bins, Min, Max)
        globals()['EE%s'%i] = np.around(ShannonEn_2nd(buf), decimals=2)
        globals()['AE%s'%i] = np.around(np.mean(buf[1:]), decimals=2)
        globals()['EE_%s'%i] = pd.Series(globals()['EE%s'%i])
        globals()['AE_%s'%i] = pd.Series(globals()['AE%s'%i])
        
    D_E = {}
    D_A = {}
    for i in range(1, scale+1):
        D_E["EoE_s%s" % i] = globals()['EE_%s'%i]
        D_A["AE_s%s" % i] = globals()['AE_%s'%i]
        
    EoE = pd.DataFrame(D_E)
    AE = pd.DataFrame(D_A)
    
    return buf, EoE, AE, ShE


def coarse_grained_MSE(data, scale):
    
    N = data.size
    buf = np.array
    
    for i in range(0, np.int_(np.fix(N/scale))):
        buf = np.append(buf, data[i*scale : (i+1)*scale].mean())
    
    return buf[1:]


def SampEn(data, r):
    
    l = data.size
    Nn = 0
    Nd = 0
    for i in range(0, l-2):
        for j in range(i+1,l-2):
            if (abs(data[i]-data[j]) < r) and (abs(data[i+1]-data[j+1]) < r):
                Nn += 1
                if abs(data[i+2]-data[j+2]) < r:
                    Nd += 1
    sampen = np.around(np.log(Nn/Nd), decimals=2)
        
    return sampen


def MSE(data, scale=20, r=0.15):
    
    r = r*np.std(data, ddof=1)
    
    for i in range(1, scale+1):
        buf = coarse_grained_MSE(data, i)
        globals()['E%s'%i] = SampEn(buf, r)
        globals()['E_%s'%i] = pd.Series(globals()['E%s'%i])
        
    D = {}
    for i in range(1, scale+1):
        D["MSE_s%s" % i] = globals()['E_%s'%i] 
        
    MSE = pd.DataFrame(D)
    
    return MSE


def EEEE(data, scale=20, bins=55, Min=0.3, Max=1.6, r=0.15, base=None):
    
    r = r*np.std(data, ddof=1)
    
    emd = EMD.EEMD(data, 0, 1)
    emd.shape[1]
    trend = emd.iloc[:,-1]
    DRRs = data.values - trend.values   
    
    for i in range(1, scale+1):
        buf = coarse_grained_EEE(data, i, bins, Min, Max)
        buf_MSE = coarse_grained_MSE(DRRs, i)
        globals()['EE%s'%i] = np.around(ShannonEn_2nd(buf), decimals=2)
        globals()['AE%s'%i] = np.around(np.mean(buf[1:]), decimals=2)
        globals()['E%s'%i] = SampEn(buf_MSE, r)
        globals()['EE_%s'%i] = pd.Series(globals()['EE%s'%i])
        globals()['AE_%s'%i] = pd.Series(globals()['AE%s'%i])
        globals()['E_%s'%i] = pd.Series(globals()['E%s'%i])
        
    D_E = {}
    D_A = {}
    D = {}
    for i in range(1, scale+1):
        D_E["EoE_s%s" % i] = globals()['EE_%s'%i]
        D_A["AE_s%s" % i] = globals()['AE_%s'%i]
        D["MSE_s%s" % i] = globals()['E_%s'%i] 
        
    EoE = pd.DataFrame(D_E)
    AE = pd.DataFrame(D_A)
    MSE = pd.DataFrame(D)
    
    return EoE, AE, MSE