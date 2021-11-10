from punting.onedim.onenormalization import normalize_probabilities, to_normalized_dividends
from punting.twodim.twonormalization import to_normalized_quinella_dividends, to_normalized_exacta_dividends
from punting.twodim.twoharville import harville_exacta_probabilities, harville_quinella_probabilities
from punting.twodim.twodimensions import to_flat_exacta, to_flat_quinella, from_flat_exacta, from_flat_quinella
import numpy as np
import math


def random_win_probabilities(n, scr, p_scr=0.2):
    is_scr = [ np.random.rand()<p_scr for _ in range(n) ]
    p = [ scr if is_scr_i else np.random.rand()**2 for is_scr_i in is_scr ]
    return normalize_probabilities(p=p, scr=scr )


def random_win_dividends(n, scr, p_scr=0.2):
    return to_normalized_dividends(random_win_probabilities(n=n,scr=scr,p_scr=p_scr))


def random_harville_market(n, scr, p_scr=0.2):
    """  Create some market prices based loosely on Harville
    :param n:
    :param scr:
    :param p_scr:
    :return:   dict:
                w_prob     -  "true" win probs
                w_div      -  market win dividends
                q_div      -  market quinella dividends
                x_div      -  market exacta (foreast) dividends
    """
    market = dict()
    market['w_prob'] = random_win_probabilities(n, scr=scr, p_scr=p_scr)
    market['w_div'] = to_normalized_dividends( jiggle_win_probabilities( market['w_prob'], scr=scr ),scr=scr)
    market_x_prob = jiggle_exacta_probabilities( harville_exacta_probabilities(p=market['w_div'], scr=scr ),scr=scr )
    market_q_prob = jiggle_quinella_probabilities( harville_quinella_probabilities(p=market['w_div']), scr=scr)
    market['q_div'] = to_normalized_quinella_dividends(market_q_prob,scr=scr)
    market['x_div'] = to_normalized_exacta_dividends(market_x_prob, scr=scr)
    return market


def jiggle_win_probabilities(p,scr,log_noise=0.1):
    p_jiggle = [ math.exp(math.log(pi)+log_noise*np.random.randn()) if pi>1e-8 else pi for pi in p ]
    return normalize_probabilities(p=p_jiggle,scr=scr)


def jiggle_exacta_probabilities(x,scr):
    fx = to_flat_exacta(x)
    ex_jiggle = jiggle_win_probabilities(p=fx,scr=scr)
    return from_flat_exacta(ex_jiggle,diag_value=scr)


def jiggle_quinella_probabilities(x,scr):
    qx = to_flat_quinella(x)
    qx_jiggle= jiggle_win_probabilities(p=qx,scr=scr)
    return from_flat_quinella(qx_jiggle,diag_val=scr)





if __name__=='__main__':
    from pprint import pprint
    n = 5
    pprint(random_harville_market(n=n, scr=-1))

