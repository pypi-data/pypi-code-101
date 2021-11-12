from sage.all import *
from Crypto.Util.number import *
from math import gcd
from math import lcm

#Returns the discrete log for an Elliptic Curve given the base point and public end point along with curve parameters
def getDlog(p, a, b, Q, G=None):
    E = EllipticCurve(GF(p), [a,b])
    if (G == None): G = E.gens()[0]
    else: G = E(G[0], G[1])
    Q = E(Q[0], Q[1])
    return discrete_log(Q, G, E.order(), operation='+')


#Singular Curve Attack
def singularCurveAttack(p, gx, gy, qx, qy):
    F = GF(p)
    M = Matrix(F, [[gx,1],[qx,1]])
    a,b = M.solve_right(vector([gy^2-gx^3,qy^2-qx^3]))

    assert 4*a^3 + 27*b^2 == 0

    K.<x> = F[]
    f = x^3 + a*x + b
    roots = f.roots()
    if roots[0][1] == 1:
        beta, alpha = roots[0][0], roots[1][0]
    else:
        alpha, beta = roots[0][0], roots[1][0]

    slope = (alpha - beta).sqrt()
    u = (gy + slope*(gx-alpha))/(gy - slope*(gx-alpha))
    v = (qy + slope*(qx-alpha))/(qy - slope*(qx-alpha))

    return discrete_log(v, u)


#MOV Attack
def MOV_Attack(p, a, b, G, Q):

    E = EllipticCurve(GF(p), [a,b])
    G = E(G[0], G[1])
    Q = E(Q[0], Q[1])

    """
    Solves the discrete logarithm problem using the MOV attack.
    :param base: the base point
    :param multiplication_result: the point multiplication result
    :return: l such that l * base == multiplication_result
    """
    curve = base.curve()
    p = curve.base_ring().order()
    n = base.order()

    assert gcd(n, p) == 1, "GCD of curve base ring order and generator order should be 1."

    print("Calculating embedding degree...")

    # Embedding degree k.
    k = 1
    while (p ** k - 1) % n != 0:
        k += 1

    print(f"Found embedding degree {k}, computing discrete logarithm...")

    pairing_curve = curve.base_extend(GF(p ** k))
    pairing_base = pairing_curve(base)
    pairing_multiplication_result = pairing_curve(multiplication_result)

    ls = []
    ds = []
    while lcm(*ds) != n:
        rand = pairing_curve.random_point()
        o = rand.order()
        d = gcd(o, n)
        rand = (o // d) * rand
        assert rand.order() == d

        u = pairing_base.weil_pairing(rand, n)
        v = pairing_multiplication_result.weil_pairing(rand, n)
        print(f"Calculating ({v}).log({u}) modulo {d}")
        l = v.log(u)
        print(f"Found discrete log {l} modulo {d}")
        ls.append(int(l))
        ds.append(int(d))

    return ls[0] if len(ls) == 1 else int(crt(ls, ds))