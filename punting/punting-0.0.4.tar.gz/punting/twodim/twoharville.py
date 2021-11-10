from punting.onedim.onenormalization import to_normalized_probabilities
from punting.twodim.twonormalization import to_normalized_quinella_dividends


def harville_exacta_probabilities(p,scr=-1):
    """ Harville exactas permitting scratching """
    ps = to_normalized_probabilities(p,scr=scr)
    n = len(ps)
    exactas = [[-1 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        if ps[j]>0:
            pj_first = ps[j] / (1-ps[j])
            exactas[j] = [ pj_first*pk if (k!=j) and (pk>0) else scr for k, pk in enumerate(ps) ]
        else:
            exactas[j] = [ scr for _ in ps ]
    return exactas


def harville_quinella_probabilities(p,scr=-1):
    """ Harville quinella permitting scratchings """
    exactas = harville_exacta_probabilities(p)
    quinellas = [[scr for _ in p] for _ in p ]
    n = len(p)
    for i in range(n):
        for j in range(n):
            if (i!=j) and (exactas[i][j]>0):
                quinellas[i][j] = exactas[i][j]+exactas[j][i]
    return quinellas


def harville_quinella_dividends(p,scr=-1):
    return to_normalized_quinella_dividends(harville_quinella_probabilities(p=p,scr=scr))


if __name__=='__main__':
    from pprint import pprint
    pprint(harville_quinella_dividends(p=[6,3,2,-1,6]))




