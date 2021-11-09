from multiprocessing import Pool
from collections import defaultdict


def get_dict(metas):

    """
    Recebe uma lista 1D com todas repetições.
                    
    Retorna um dict {'meta1': [rep1, rep2, ..., repN],
                    'meta2': [rep1, rep2, ..., repN],
                    'metaN':[rep1, rep2, ..., repN]}
    """
    d = defaultdict(list)
    for rep in metas:
        d[rep.meta.__class__.__name__].append(rep)
    
    return dict(d)

def get_list(metas):
    """
    Recebe um dict {'meta1': [rep1, rep2, ..., repN],
                    'meta2': [rep1, rep2, ..., repN],
                    'metaN':[rep1, rep2, ..., repN]}
                    
    Retorna uma lista 1D com todas repetições.
    """
    return [x for sublist in metas.values() for x in sublist]


def loop(rep):
    for g in range(1, rep.nGen):
        next(rep)
        
    return rep
        

def run(metas, cpu_count=None):
    with Pool(cpu_count) as p:
        #result = p.map(loop, metas)
        
        result = p.map_async(loop, metas)
        result = result.get()
        
        return result


## APAGAR TUDO ISSO AQUI PRA BAIXO E VOLTAR O LOOP2 PARA LOOP1 EM RUN()
import pandas as pd
import numpy as np


"""
class Fo:
    data = pd.read_excel('marko/data50-2015.xlsx', index_col='Date')
    returns = np.log(data/data.shift(1))
    ret_mean = returns.mean()
    ret_cov = returns.cov()

    def __init__(self, aversao_risco=0, K=10):
        self.aversao_risco = aversao_risco
        self.K = K

    def fo_1(self, weights):

        port_return = np.sum(Fo.ret_mean * weights) * 252
        port_vol = np.dot(weights.T, np.dot(Fo.ret_cov * 252, weights))
        #port_sigma = np.sqrt(port_vol)
        #sharpe = port_return/port_sigma

        fo = self.aversao_risco*port_vol - (1 - self.aversao_risco) * port_return

        # Restrição de cardinalidade:
        k = np.count_nonzero(weights)
        if k != self.K:
            fo += abs(k-self.K)

        # Restrição pesos = 1
        w_total = weights.sum()
        if w_total > 1:
            fo += w_total

        return fo
"""