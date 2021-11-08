#!/usr/bin/env python
# coding: utf-8


import scipy.io
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
from io import StringIO
from datetime import date, time, datetime, timedelta


def find_peaks_ezsleep(ECG):
    a = 0
    b = 0
    p = 0
    X = np.array
    Y = np.array
    i = 199
    L = ECG.size - 1001
    ECG = ECG/1000
    
    # homemade findpeaks
    while i < L:
        # slope2
        j = 0
        while ECG[i+j] > ECG[i+j+1]:
            j = j + 1
        slope2 = ECG[i] - ECG[i+j]
        
        # slope1
        if slope2 > 0.3: # parameter
            k = 0
            while ECG[i-k] > ECG[i-k-1]:
                k = k + 1
            slope1 = ECG[i] - ECG[i-k]
        else:
            slope1 = 0

        # conditions of R
        S = slope1 > 0.3
        S2 = slope2 > 0.5 * a # a is last slope2
        S3 = slope1 > 0.8 * b # b is last slope1
        S4 = slope2 > 1.3
        M = (ECG[i] == np.max(ECG[i-70 : i+71]))     # local Maximum
        M2 = (ECG[i] == np.max(ECG[i-120:i+121]))   # local Maximum 2
        A = (i-p) > 60 # p is last R position

        # extract peak
        if (S and S2 and M) or (S3 and A and M) or S4 or M2:
            # (S & S2 & M) is general
            # (S3 & A & M) for two-head
            # S4 for T>R (i = i + 55)
            # M2 for small amplitude
            X = np.append(X, i)
            Y = np.append(Y, ECG[i])
            a = slope2
            b = slope1
            p = i
            i = i + 55
        else:
            i = i + 1

    #X = np.array(X)
    #Y = np.array(Y)
    #Y = Y[:, np.newaxis]
    X = np.delete(X, 0)
    Y = np.delete(Y, 0)
    print('FindPeak is finished!')
    return X, Y

def find_peaks_MK(ECG):
    a = 0
    b = 0
    p = 0
    X = np.array
    Y = np.array
    i = 199
    L = ECG.size - 1001
    
    while i < L:
        j = 0
        while ECG[i+j] > ECG[i+j+1]:
            j = j + 1
        slope2 = ECG[i] - ECG[i+j]

        if slope2 > 0.3:
            k = 0
            while ECG[i-k] > ECG[i-k-1]:
                k = k + 1
            slope1 = ECG[i] - ECG[i-k]
        else:
            slope1 = 0

        S = slope1 > 0.3
        S2 = slope2 > 0.5 * a
        S3 = slope1 > 0.8 * b
        S4 = slope2 > 1.3
        M = (ECG[i] == np.max(ECG[i-70 : i+71]))
        M2 = (ECG[i] == np.max(ECG[i-120:i+121]))
        A = (i-p) > 120

        if (S and S2 and M) or (S3 and A and M) or S4 or M2:
            X = np.append(X, i)
            Y = np.append(Y, ECG[i])
            a = slope2
            b = slope1
            p = i
            i = i + 105
        else:
            i = i + 1

    #X = np.array(X)
    #Y = np.array(Y)
    #Y = Y[:, np.newaxis]
    X = np.delete(X, 0)
    Y = np.delete(Y, 0)
    print('FindPeak is finished!')
    return X, Y

def remove_outliers_std(X, Y, Starttime, fs=250):
    iRR = np.diff(X,axis=0) / fs
    LRR = iRR.size
    RR = np.array
    RRpos = np.array
    RRpks = np.array
    RRsec = np.array
    RRtime = np.array

    for i in range(20, (LRR-20)):
        RRL = iRR[i-20:i]
        RRR = iRR[i+1:i+21]
        OF = np.hstack((RRL,RRR))
        minRR = np.around(OF.mean(), decimals=4) - np.around(4*(np.std(OF, ddof=1)), decimals=4)
        maxRR = np.around(OF.mean(), decimals=4) + np.around(4*(np.std(OF, ddof=1)), decimals=4)
        if (minRR < iRR[i]) and (iRR[i] < maxRR):
            RR = np.append(RR, iRR[i])
            RRpos = np.append(RRpos, X[i])
            RRpks = np.append(RRpks, Y[i])
            RRsec = np.append(RRsec, X[i]/fs)
            RRtime = np.append(RRtime, Starttime + timedelta(seconds = X[i]/fs))
    
    #RR = np.delete(RR, 0)
    #RRpos = np.delete(RRpos, 0)
    #RRpks = np.delete(RRpks, 0)
    #RRsec = np.delete(RRsec, 0)
    
    outlier = 100*(iRR.size-RR.size)/iRR.size
    
    s1 = pd.Series(RRtime)
    s2 = pd.Series(RR)
    s3 = pd.Series(RRpos)
    s4 = pd.Series(RRpks)
    s5 = pd.Series(RRsec)

    dictionary = {
        'RRtime': s1,
        'RR': s2,
        'RRpos': s3,
        'RRpks': s4,
        'RRsec': s5,
    }

    df = pd.DataFrame(dictionary).drop([0]).reset_index(drop=True)
    df = df.set_index('RRtime')
    #df.to_pickle('/Users/PYLin/Desktop/complexity/data/'+PatID+'_RR.pkl')
    
    print('Remained rr1 percentage = %f %%' %(100*(RR.size/iRR.size)))
    print('Be careful if the remained rr percentage is lower than 99%.')
    return df

