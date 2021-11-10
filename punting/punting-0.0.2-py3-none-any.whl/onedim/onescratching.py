
def scratch_win(p):
    p_starters = [pi for pi in p if pi > 0]
    ndx = [k for k,pi in enumerate(p) if pi>0]
    return p_starters, ndx, len(p)


def unscratch_win(x, ndx, n, scr=-1):
    """
    :param x:      Vector of info (e.g. win price) for starters only
    :param ndx:    Indexes of starters
    :param n:      Original number of runners
    :param scr:
    :return:
    """
    p = [scr for _ in range(n)]
    for ndx,xi in zip(ndx,x):
        p[ndx] = xi
    return p