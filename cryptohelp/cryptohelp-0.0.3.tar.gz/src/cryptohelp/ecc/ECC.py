from sage.all import *
from Crypto.Util.number import *

__all__ = ['getDlog']

#Returns the discrete log for an Elliptic Curve given the base point and public end point along with curve parameters
def getDlog(p, a, b, Q, G=None, printDlog=False):
    E = EllipticCurve(GF(p), [a,b])
    if (G == None): G = E.gens()[0]
    else: G = E(G[0], G[1])
    Q = E(Q[0], Q[1])
    d = discrete_log(Q, G, E.order(), operation='+')
    #Prints dlog bytes if option to print dlog is true
    if printDlog: print(long_to_bytes(d))
    return d

#Test
#getFlag(17459102747413984477, 2, 3,(8859996588597792495, 2628834476186361781), (15579091807671783999,4313814846862507155))
