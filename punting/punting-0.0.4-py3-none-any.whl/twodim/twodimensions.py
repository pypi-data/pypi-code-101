import numpy as np
import math


def from_list(x:[[float]], diag_val=None)->np.ndarray:
    """ Convert list of lists to 2-d array
        Inverse of tolist() for 2-d array
    :param x:
    :return:
    """
    n = len(x)
    a = np.ndarray(shape=(n,n))
    for i in range(n):
        for j in range(n):
            a[i,j] = x[i][j]
    if diag_val is not None:
        for i in range(n):
            a[i,i]=diag_val
    return a


def to_list(a, diag_val=None):
    """ Convert array to list of lists
       More or less np .tolist() method but can set diag values as a convenience
    """
    ll = a.tolist()
    n = len(ll[0])
    if diag_val is not None:
        for i in range(n):
            ll[i][i] = diag_val
    return ll


def all_exacta_close(a,b):
    return np.allclose(a=from_list(a,diag_val=0),b=from_list(b,diag_val=0),atol=1e-6, equal_nan=True)


def all_exacta_close(a,b):
    return np.allclose(a=from_list(a,diag_val=0),b=from_list(b,diag_val=0),atol=1e-6, equal_nan=True)


def to_flat_quinella(q, with_ndx=False) -> [float]:
    """  Maps to list of length n-choose-2 using only upper diagonal
    :param  q: List of List or dim-2 np array
    """
    a = from_list(q,diag_val=7777777)
    ndx = np.triu_indices_from(a,k=1)
    if with_ndx:
        return [ (ndxi,ai) for ndxi, ai in zip(ndx,a[ndx]) if ai!=7777777]
    else:
        return [ai for ai in a[ndx] if ai!=7777777]


def from_flat_quinella(q:[float], diag_val=-1)->np.ndarray:
    """
         Inverse of to_flat_quinella
    """

    def n_from_n_choose_2(m):
        # The computer-scientists way :)
        # Somebody forgot their high-school math temporarily
        # Left here as a testament to my stupidity
        max_n = int(math.ceil(math.sqrt(2 * m) + 1))
        min_n = int(math.floor(math.sqrt(2 * m)))
        candidates = [(n, n * (n - 1) / 2) for n in range(min_n - 1, max_n + 1)]
        valid = [n for (n, m_) in candidates if m_ == m]
        return valid[0]

    m = len(q)
    n = n_from_n_choose_2(m)
    assert m==n*(n-1)/2

    a = np.ndarray(shape=(n,n))
    ndx = np.triu_indices_from(a,k=1)
    assert len(ndx[0])==m

    for k,(i,j) in enumerate(zip(*ndx)):
        a[i,j] = q[k]

    for i in range(n):
        a[i,i] = diag_val

    for i in range(n):
        for j in range(n):
            if j<i:
                a[i,j] = a[j,i]
    return a


def exacta_indexes_from(a:np.ndarray):
    up0, up1 = np.triu_indices_from(a, k=1)
    dn0, dn1 = np.tril_indices_from(a, k=-1)
    ndx0 = list(up0) + list(dn0)
    ndx1 = list(up1) + list(dn1)
    return ndx0,ndx1


def to_flat_exacta(a, with_ndx=False)->[float]:
    """ Convert list of lists or 2-d array into single list that ignores diagonals
    :param a:
    :return:
    """
    x = from_list(a,diag_val=7777777)
    ndx0, ndx1 = exacta_indexes_from(x)
    if not with_ndx:
        return [x[i,j] for (i,j) in zip(ndx0,ndx1)]
    else:
        return [((i,j),x[i,j]) for (i,j) in zip(ndx0,ndx1) ]



def from_flat_exacta(x: [float], diag_value=-1) -> np.ndarray:
    """ Map list of length n(n-1) to an exacta matrix

         Inverse of to_flat_exacta

    """
    def n_from_n_permute_2(m):
        # The mathematican's way, for variety :)
        return int(0.5+0.5*math.sqrt(1+4*m))

    m = len(x)
    n = n_from_n_permute_2(m)
    assert m==n*(n-1)

    a = np.ndarray(shape=(n, n))
    ndx0, ndx1 = exacta_indexes_from(a)
    for k,(i,j) in enumerate(zip(ndx0,ndx1)):
        a[i,j] = x[k]

    for i in range(n):
        a[i,i] = diag_value

    return from_list(a)




if __name__=='__main__':
    x = np.ndarray(shape=(5,5))
    xl = to_list(x, diag_val=-1)
    xl1 = to_list(x, diag_val=-1)
    assert all_exacta_close(xl,xl1 )
    q = to_flat_quinella(xl)
    print(len(q))
