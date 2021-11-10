from punting.twodim.twodimensions import from_list


def scratch_quinella(q,ndx)->[[float]]:
    qx = from_list(q)
    n_starters = len(ndx)
    q_starters = [[-1 for _ in range(n_starters)] for _ in range(n_starters)]
    for i,i1 in enumerate(ndx):
        for j,j1 in enumerate(ndx):
            q_starters[i][j] = qx[i1,j1]
    return q_starters


def unscratch_quinella(q,ndx,n):
    q_full = [[-1 for _ in range(n)] for _ in range(n)]
    for i, i1 in enumerate(ndx):
        for j, j1 in enumerate(ndx):
            q_full[i1][j1] = q[i][j]
    return q_full
