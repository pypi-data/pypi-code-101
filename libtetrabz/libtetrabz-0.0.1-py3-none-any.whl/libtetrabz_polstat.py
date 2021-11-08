#
# Copyright (c) 2014 Mitsuaki Kawamura
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
import math
import numpy
from . import libtetrabz_common


def polstat(bvec, eig1, eig2):
    """
    Compute Static polarization function
    :param bvec:
    :param eig1:
    :param eig2:
    :return:
    """
    thr = 1.0e-10

    ng = numpy.array(eig1.shape[0:3])
    nk = ng.prod(0)
    nb = eig1.shape[3]
    wlsm, ikv = libtetrabz_common.libtetrabz_initialize(ng, bvec)

    wght = numpy.zeros([ng[0], ng[1], ng[2], nb, nb], dtype=numpy.float_)

    for it in range(6 * nk):
        #
        eig1t = numpy.empty([20, nb], dtype=numpy.float_)
        eig2t = numpy.empty([20, nb], dtype=numpy.float_)
        for ii in range(20):
            eig1t[ii, 0:nb] = eig1[ikv[it, ii, 0], ikv[it, ii, 1], ikv[it, ii, 2], 0:nb]
            eig2t[ii, 0:nb] = eig2[ikv[it, ii, 0], ikv[it, ii, 1], ikv[it, ii, 2], 0:nb]
        ei1 = wlsm.dot(eig1t)
        ej1 = wlsm.dot(eig2t)
        #
        w1 = numpy.zeros([nb, nb, 4], dtype=numpy.float_)
        w2t = numpy.zeros([nb, 4], dtype=numpy.float_)
        for ib in range(nb):
            #
            e = ei1[0:4, ib].copy()
            indx = e.argsort(0)
            e.sort(0)
            #
            if e[0] <= 0.0 < e[1]:
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_a1(e)
                #
                if v > thr:
                    ei2 = tsmall.dot(ei1[indx[0:4],   ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polstat2(ei2, ej2)
                    w2t[0:nb, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:4] += v * w2t[0:nb, 0:4]
                #
            elif e[1] <= 0.0 < e[2]:
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_b1(e)
                #
                if v > thr:
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polstat2(ei2, ej2)
                    w2t[0:nb, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:4] += v * w2t[0:nb, 0:4]
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_b2(e)
                #
                if v > thr:
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polstat2(ei2, ej2)
                    w2t[0:nb, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:4] += v * w2t[0:nb, 0:4]
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_b3(e)
                #
                if v > thr:
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polstat2(ei2, ej2)
                    w2t[0:nb, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:4] += v * w2t[0:nb, 0:4]
                #
            elif e[2] <= 0.0 < e[3]:
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_c1(e)
                #
                if v > thr:
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polstat2(ei2, ej2)
                    w2t[0:nb, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:4] += v * w2t[0:nb, 0:4]
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_c2(e)
                #
                if v > thr:
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polstat2(ei2, ej2)
                    w2t[0:nb, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:4] += v * w2t[0:nb, 0:4]
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_c3(e)
                #
                if v > thr:
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polstat2(ei2, ej2)
                    w2t[0:nb, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:4] += v * w2t[0:nb, 0:4]
                #
            elif e[3] <= 0.0:
                ei2 = ei1[0:4,   ib]
                ej2 = ej1[0:4, 0:nb]
                w2 = libtetrabz_polstat2(ei2, ej2)
                w1[ib, 0:nb, 0:4] += w2[0:nb, 0:4]
            else:
                continue
            #
        #
        for ii in range(20):
            wght[ikv[it, ii, 0], ikv[it, ii, 1], ikv[it, ii, 2], 0:nb, 0:nb] += w1.dot(wlsm[:, ii])
        #
    wght[0:ng[0], 0:ng[1], 0:ng[2], 0:nb, 0:nb] /= (6.0 * nk)
    return wght


def libtetrabz_polstat2(ei1, ej1):
    """
    Tetrahedron method for theta( - E2)
    :param ei1:
    :param ej1:
    :return:
    """
    #
    thr = 1.0e-8
    nb = ej1.shape[1]
    w1 = numpy.zeros([nb, 4], dtype=numpy.float_)

    for ib in range(nb):
        e = -ej1[0:4, ib]
        indx = e.argsort(0)
        e.sort(0)
        #
        if e[0] <= 0.0 < e[1] or e[0] < 0.0 <= e[1]:
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_a1(e)
            #
            if v > thr:
                #
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polstat3(de)
                w1[ib, indx[0:4]] += v * w2.dot(tsmall)
            #
        elif e[1] <= 0.0 < e[2] or e[1] < 0.0 <= e[2]:
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_b1(e)
            #
            if v > thr:
                #
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polstat3(de)
                w1[ib, indx[0:4]] += v * w2.dot(tsmall)
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_b2(e)
            #
            if v > thr:
                #
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polstat3(de)
                w1[ib, indx[0:4]] += v * w2.dot(tsmall)
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_b3(e)
            #
            if v > thr:
                #
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polstat3(de)
                w1[ib, indx[0:4]] += v * w2.dot(tsmall)
        #
        elif e[2] <= 0.0 < e[3] or e[2] < 0.0 <= e[3]:
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_c1(e)
            #
            if v > thr:
                #
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polstat3(de)
                w1[ib, indx[0:4]] += v * w2.dot(tsmall)
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_c2(e)
            #
            if v > thr:
                #
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polstat3(de)
                w1[ib, indx[0:4]] += v * w2.dot(tsmall)
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_c3(e)
            #
            if v > thr:
                #
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polstat3(de)
                w1[ib, indx[0:4]] += v * w2.dot(tsmall)
            #
        elif e[3] <= 0.0:
            #
            de = ej1[0:4, ib] - ei1[0:4]
            w2 = libtetrabz_polstat3(de)
            w1[ib, 0:4] += w2
    #
    return w1


def libtetrabz_polstat3(de):
    """
    Tetrahedron method for delta(om - ep + e)
    :param de:
    :return:
    """
    #
    e = de[0:4].copy()
    indx = e.argsort(0)
    e.sort(0)
    #
    thr = e.max(0) * 1.0e-3
    thr2 = 1.0e-8
    #
    ln = numpy.empty(4, dtype=numpy.float_)
    for ii in range(4):
        if e[ii] < thr2:
            if ii == 3:
                raise ValueError("  Nesting # ")
            ln[ii] = 0.0
            e[ii] = 0.0
        else:
            ln[ii] = math.log(e[ii])
    #
    w1 = numpy.empty(4, dtype=numpy.float_)
    if abs(e[3] - e[2]) < thr:
        if abs(e[3] - e[1]) < thr:
            if abs(e[3] - e[0]) < thr:
                #
                # e[3] = e[2] = e[1] = e[0]
                #
                w1[indx[3]] = 0.25 / e[3]
                w1[indx[2]] = w1[indx[3]]
                w1[indx[1]] = w1[indx[3]]
                w1[indx[0]] = w1[indx[3]]
                #
            else:
                #
                # e[3] = e[2] = e[1]
                #
                w1[indx[3]] = libtetrabz_polstat_1211(e[3], e[0], ln[3], ln[0])
                w1[indx[2]] = w1[indx[3]]
                w1[indx[1]] = w1[indx[3]]
                w1[indx[0]] = libtetrabz_polstat_1222(e[0], e[3], ln[0], ln[3])
                #
                if w1.min(initial=w1[0]) < 0.0:
                    print(e[0], e[1], e[2], e[3])
                    print(w1[indx[0]], w1[indx[1]], w1[indx[2]], w1[indx[3]])
                    raise ValueError("weighting 4=3=2")
                #
        elif abs(e[1] - e[0]) < thr:
            #
            # e[3] = e[2], e[1] = e[0]
            #
            w1[indx[3]] = libtetrabz_polstat_1221(e[3], e[1], ln[3], ln[1])
            w1[indx[2]] = w1[indx[3]]
            w1[indx[1]] = libtetrabz_polstat_1221(e[1], e[3], ln[1], ln[3])
            w1[indx[0]] = w1[indx[1]]
            #
            if w1.min(initial=w1[0]) < 0.0:
                print(e[0], e[1], e[2], e[3])
                print(w1[indx[0]], w1[indx[1]], w1[indx[2]], w1[indx[3]])
                raise ValueError("weighting 4=3 2=1")
            #
        else:
            #
            # e[3] = e[2]
            #
            w1[indx[3]] = libtetrabz_polstat_1231(e[3], e[0], e[1], ln[3], ln[0], ln[1])
            w1[indx[2]] = w1[indx[3]]
            w1[indx[1]] = libtetrabz_polstat_1233(e[1], e[0], e[3], ln[1], ln[0], ln[3])
            w1[indx[0]] = libtetrabz_polstat_1233(e[0], e[1], e[3], ln[0], ln[1], ln[3])
            #
            if w1.min(initial=w1[0]) < 0.0:
                print(e[0], e[1], e[2], e[3])
                print(w1[indx[0]], w1[indx[1]], w1[indx[2]], w1[indx[3]])
                raise ValueError("weighting 4=3")
            #
    elif abs(e[2] - e[1]) < thr:
        if abs(e[2] - e[0]) < thr:
            #
            # e[2] = e[1] = e[0]
            #
            w1[indx[3]] = libtetrabz_polstat_1222(e[3], e[2], ln[3], ln[2])
            w1[indx[2]] = libtetrabz_polstat_1211(e[2], e[3], ln[2], ln[3])
            w1[indx[1]] = w1[indx[2]]
            w1[indx[0]] = w1[indx[2]]
            #
            if w1.min(initial=w1[0]) < 0.0:
                print(e[0], e[1], e[2], e[3])
                print(w1[indx[0]], w1[indx[1]], w1[indx[2]], w1[indx[3]])
                raise ValueError("weighting 3=2=1")
            #
        else:
            #
            # e[2] = e[1]
            #
            w1[indx[3]] = libtetrabz_polstat_1233(e[3], e[0], e[2], ln[3], ln[0], ln[2])
            w1[indx[2]] = libtetrabz_polstat_1231(e[2], e[0], e[3], ln[2], ln[0], ln[3])
            w1[indx[1]] = w1[indx[2]]
            w1[indx[0]] = libtetrabz_polstat_1233(e[0], e[3], e[2], ln[0], ln[3], ln[2])
            #
            if w1.min(initial=w1[0]) < 0.0:
                print(e[0], e[1], e[2], e[3])
                print(w1[indx[0]], w1[indx[1]], w1[indx[2]], w1[indx[3]])
                raise ValueError("weighting 3=2")
            #
    elif abs(e[1] - e[0]) < thr:
        #
        # e[1] = e[0]
        #
        w1[indx[3]] = libtetrabz_polstat_1233(e[3], e[2], e[1], ln[3], ln[2], ln[1])
        w1[indx[2]] = libtetrabz_polstat_1233(e[2], e[3], e[1], ln[2], ln[3], ln[1])
        w1[indx[1]] = libtetrabz_polstat_1231(e[1], e[2], e[3], ln[1], ln[2], ln[3])
        w1[indx[0]] = w1[indx[1]]
        #
        if w1.min(initial=w1[0]) < 0.0:
            print(e[0], e[1], e[2], e[3])
            print(w1[indx[0]], w1[indx[1]], w1[indx[2]], w1[indx[3]])
            raise ValueError("weighting 2=1")
        #
    else:
        #
        # Different each other.
        #
        w1[indx[3]] = libtetrabz_polstat_1234(e[3], e[0], e[1], e[2], ln[3], ln[0], ln[1], ln[2])
        w1[indx[2]] = libtetrabz_polstat_1234(e[2], e[0], e[1], e[3], ln[2], ln[0], ln[1], ln[3])
        w1[indx[1]] = libtetrabz_polstat_1234(e[1], e[0], e[2], e[3], ln[1], ln[0], ln[2], ln[3])
        w1[indx[0]] = libtetrabz_polstat_1234(e[0], e[1], e[2], e[3], ln[0], ln[1], ln[2], ln[3])
        #
        if w1.min(initial=w1[0]) < 0.0:
            print(e[0], e[1], e[2], e[3])
            print(w1[indx[0]], w1[indx[1]], w1[indx[2]], w1[indx[3]])
            raise ValueError("weighting")
        #
    #
    return w1
#
# Results of Integration (1-x-y-z)/(g0+(g1-g0)x+(g2-g0)y+(g3-g0))
#  for 0<x<1, 0<y<1-x, 0<z<1-x-y
#


def libtetrabz_polstat_1234(g1, g2, g3, g4, lng1, lng2, lng3, lng4):
    """
    1, Different each other
    :param g1:
    :param g2:
    :param g3:
    :param g4:
    :param lng1:
    :param lng2:
    :param lng3:
    :param lng4:
    :return:
    """
    w2 = ((lng2 - lng1)/(g2 - g1)*g2 - 1.0)*g2/(g2 - g1)
    w3 = ((lng3 - lng1)/(g3 - g1)*g3 - 1.0)*g3/(g3 - g1)
    w4 = ((lng4 - lng1)/(g4 - g1)*g4 - 1.0)*g4/(g4 - g1)
    w2 = ((w2 - w3)*g2)/(g2 - g3)
    w4 = ((w4 - w3)*g4)/(g4 - g3)
    w = (w4 - w2)/(g4 - g2)
    return w


def libtetrabz_polstat_1231(g1, g2, g3, lng1, lng2, lng3):
    """
    2, g4 = g1
    :param g1:
    :param g2:
    :param g3:
    :param lng1:
    :param lng2:
    :param lng3:
    :return:
    """
    w2 = ((lng2 - lng1)/(g2 - g1)*g2 - 1.0)*g2**2/(g2 - g1) - g1/2.0
    w2 = w2/(g2 - g1)
    w3 = ((lng3 - lng1)/(g3 - g1)*g3 - 1.0)*g3**2/(g3 - g1) - g1/2.0
    w3 = w3/(g3 - g1)
    w = (w3 - w2)/(g3 - g2)
    return w


def libtetrabz_polstat_1233(g1, g2, g3, lng1, lng2, lng3):
    """
    # 3, g4 = g3
    :param g1:
    :param g2:
    :param g3:
    :param lng1:
    :param lng2:
    :param lng3:
    :return:
    """
    w2 = (lng2 - lng1)/(g2 - g1)*g2 - 1.0
    w2 = (g2*w2)/(g2 - g1)
    w3 = (lng3 - lng1)/(g3 - g1)*g3 - 1.0
    w3 = (g3*w3)/(g3 - g1)
    w2 = (w3 - w2)/(g3 - g2)
    w3 = (lng3 - lng1)/(g3 - g1)*g3 - 1.0
    w3 = 1.0 - (2.0*w3*g1)/(g3 - g1)
    w3 = w3/(g3 - g1)
    w = (g3*w3 - g2*w2)/(g3 - g2)
    return w


def libtetrabz_polstat_1221(g1, g2, lng1, lng2):
    """
    4, g4 = g1 and g3 = g2
    :param g1:
    :param g2:
    :param lng1:
    :param lng2:
    :return:
    """
    w = 1.0 - (lng2 - lng1)/(g2 - g1)*g1
    w = -1.0 + (2.0*g2*w)/(g2 - g1)
    w = -1.0 + (3.0*g2*w)/(g2 - g1)
    w = w/(2.0*(g2 - g1))
    return w


def libtetrabz_polstat_1222(g1, g2, lng1, lng2):
    """
    5, g4 = g3 = g2
    :param g1:
    :param g2:
    :param lng1:
    :param lng2:
    :return:
    """
    w = (lng2 - lng1)/(g2 - g1)*g2 - 1.0
    w = (2.0*g1*w)/(g2 - g1) - 1.0
    w = (3.0*g1*w)/(g2 - g1) + 1.0
    w = w/(2.0*(g2 - g1))
    return w


def libtetrabz_polstat_1211(g1, g2, lng1, lng2):
    """
    6, g4 = g3 = g1
    :param g1:
    :param g2:
    :param lng1:
    :param lng2:
    :return:
    """
    w = -1.0 + (lng2 - lng1)/(g2 - g1)*g2
    w = -1.0 + (2.0*g2*w)/(g2 - g1)
    w = -1.0 + (3.0*g2*w)/(2.0*(g2 - g1))
    w = w/(3.0*(g2 - g1))
    return w
