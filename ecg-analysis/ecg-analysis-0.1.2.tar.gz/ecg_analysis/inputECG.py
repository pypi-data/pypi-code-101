import scipy.io
import numpy as np
import pandas as pd
from io import StringIO
from datetime import datetime


def ezsleep(filepath):
    F = open(filepath).read()
    data = pd.read_csv(StringIO(F),header=None)
    data = data.values.ravel().astype(np.float64)
    return data

def MKmat(matfilepath):
    data = scipy.io.loadmat(matfilepath)
    df = pd.DataFrame.from_dict(data, orient='index', columns=['A'])
    df = df['A']
    PatID = df.loc['PatID']
    Starttime_str = df.loc['Starttime']
    Starttime = datetime(Starttime_str[0], Starttime_str[1], Starttime_str[2], Starttime_str[3], Starttime_str[4], Starttime_str[5])
    Starttime_str = str(Starttime_str[0])+str(Starttime_str[1])+str(Starttime_str[2])+str(Starttime_str[3])+str(Starttime_str[4])+str(Starttime_str[5])
    ECG_SRate = df.loc['ECG_3_SRate']
    beatpos = df.loc['beatpos']
    ECG_1 = df.loc['ECG_1']
    ECG_2 = df.loc['ECG_2']
    ECG_3 = df.loc['ECG_3']
    print('File ', matfilepath,' was loaded.' )
    return PatID, Starttime, Starttime_str, ECG_SRate, beatpos, ECG_1, ECG_2, ECG_3

def X1rpk(filepath):
    F = open(filepath).read()
    lines = F.split('\n')
    newlines = []

    for line in lines:
        if len(line.split(',')) == 5:
            newlines.append(line)

    c = '\n'
    s = c.join(newlines)
    df = pd.read_csv(StringIO(s))

    RR = df['DelTime']
    Acc_X = df['Acceleration_X']
    Acc_Y = df['Acceleration_Y']
    Acc_Z = df['Acceleration_Z']
    print('File ', filepath,' was loaded.' )
    return RR, Acc_X, Acc_Y, Acc_Z