import numpy as np
import pandas as pd
import scanpy as sc

def normalized_sum(data):
    tempsum = np.sum(data, axis=1).reshape(data.shape[0],1)
    tempdata = data/tempsum*10000
    tempdata[tempdata==-np.inf] = 0
    return tempdata

def normalized_max(data):
    tempmax = np.max(data, axis=1).reshape(data.shape[0],1)
    tempdata = data/tempmax*10000
    tempdata[tempdata==-np.inf] = 0
    return tempdata

def clr_normalize(data):
    tempdata = data+1
    result = np.log(tempdata/gmean(tempdata))
    return result