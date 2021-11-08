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


def polcmplx(bvec, eig1, eig2, e0):
    """
    Main SUBROUTINE for Polarization (Imaginary axis) : Theta(- E1) * Theta(E2) / (E2 - E1 - iw)
    :param bvec:
    :param eig1:
    :param eig2:
    :param e0:
    :return:
    """
    ng = numpy.array(eig1.shape[0:3])
    nk = ng.prod(0)
    nb = eig1.shape[3]
    ne = e0.shape[0]
    wlsm, ikv = libtetrabz_common.libtetrabz_initialize(ng, bvec)

    wght = numpy.zeros([ng[0], ng[1], ng[2], nb, nb, ne], dtype=numpy.complex_)
    #
    thr = 1.0e-8
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
        w1 = numpy.zeros([nb, nb, ne, 4], dtype=numpy.complex_)
        w2t = numpy.zeros([nb, ne, 4], dtype=numpy.complex_)
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
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polcmplx2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
            elif e[1] <= 0.0 < e[2]:
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_b1(e)
                #
                if v > thr:
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polcmplx2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_b2(e)
                #
                if v > thr:
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polcmplx2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_b3(e)
                #
                if v > thr:
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polcmplx2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
            elif e[2] <= 0.0 < e[3]:
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_c1(e)
                #
                if v > thr:
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polcmplx2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_c2(e)
                #
                if v > thr:
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polcmplx2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_c3(e)
                #
                if v > thr:
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_polcmplx2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
            elif e[3] <= 0.0:
                #
                ei2 = ei1[0:4, ib]
                ej2 = ej1[0:4, 0:nb]
                w2 = libtetrabz_polcmplx2(e0, ei2, ej2)
                w1[ib, 0:nb, 0:ne, 0:4] += w2[0:nb, 0:ne, 0:4]
                #
            else:
                continue
            #
        for ii in range(20):
            wght[ikv[it, ii, 0], ikv[it, ii, 1], ikv[it, ii, 2], 0:nb, 0:nb, 0:ne] += w1.dot(wlsm[:, ii])
        #
    wght[0:ng[0], 0:ng[1], 0:ng[2], 0:nb, 0:nb, 0:ne] /= (6.0 * nk)
    return wght


def libtetrabz_polcmplx2(e0, ei1, ej1):
    """
    Tetrahedra method for theta( - E2)
    :param e0:
    :param ei1:
    :param ej1:
    :return:
    """
    ne = e0.shape[0]
    nb = ej1.shape[1]
    thr = 1.0e-8
    w1 = numpy.zeros([nb, ne, 4], dtype=numpy.complex_)
    w2t = numpy.zeros([ne, 4], dtype=numpy.complex_)

    for ib in range(nb):
        #
        e = -ej1[0:4, ib]
        indx = e.argsort(0)
        e.sort(0)
        #
        if e[0] <= 0.0 < e[1] or e[0] < 0.0 <= e[1]:
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_a1(e)
            #
            if v > thr:
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polcmplx3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
            #
        elif e[1] <= 0.0 < e[2] or e[1] < 0.0 <= e[2]:
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_b1(e)
            #
            if v > thr:
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polcmplx3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_b2(e)
            #
            if v > thr:
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polcmplx3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_b3(e)
            #
            if v > thr:
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polcmplx3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
            #
        elif e[2] <= 0.0 < e[3] or e[2] < 0.0 <= e[3]:
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_c1(e)
            #
            if v > thr:
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polcmplx3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_c2(e)
            #
            if v > thr:
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polcmplx3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_c3(e)
            #
            if v > thr:
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_polcmplx3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
            #
        elif e[3] <= 0.0:
            de = ej1[0:4, ib] - ei1[0:4]
            w2 = libtetrabz_polcmplx3(e0, de)
            w1[ib, 0:ne, 0:4] += w2

    return w1


def libtetrabz_polcmplx3(e0, de):
    """
    Tetrahedron method for delta(om - ep + e)
    :param e0:
    :param de:
    :return:
    """
    ne = e0.shape[0]
    e = de[0:4].copy()
    indx = e.argsort(0)
    e.sort(0)
    w1 = numpy.zeros([ne, 4], dtype=numpy.complex_)
    w2 = numpy.empty([2, 4], dtype=numpy.float_)
    #
    for ie in range(ne):
        #
        # I am no sure which one is better.
        # The former is more stable.
        # The latter is more accurate ?
        #
        w1[ie, 0:4] = 0.25 / (de[0:4] + e0[ie])
        #
        continue
        #
        x = (e[0:4] + e0[ie].real) / e0[ie].imag
        # thr = maxval(de(1:4)) * 1d-3
        thr = max(1.0e-3,  numpy.abs(x).max() * 1.0e-2)
        #
        if abs(x[3] - x[2]) < thr:
            if abs(x[3] - x[1]) < thr:
                if abs(x[3] - x[0]) < thr:
                    #
                    # e[3] = e[2] = e[1] = e[0]
                    #
                    w2[0, 3] = 0.25 * x[3] / (1.0 + x[3]**2)
                    w2[1, 3] = 0.25 / (1.0 + x[3]**2)
                    w2[0:2, 2] = w2[0:2, 3]
                    w2[0:2, 1] = w2[0:2, 3]
                    w2[0:2, 0] = w2[0:2, 3]
                    #
                else:
                    #
                    # e[3] = e[2] = e[1]
                    #
                    w2[0:2, 3] = libtetrabz_polcmplx_1211(x[3], x[0])
                    w2[0:2, 2] = w2[0:2, 3]
                    w2[0:2, 1] = w2[0:2, 3]
                    w2[0:2, 0] = libtetrabz_polcmplx_1222(x[0], x[3])
                    #
                    # IF(ANY(w2(1:2,1:4) < 0.0)):
                    #   WRITE(*,*) ie
                    #   WRITE(*,'(100e15.5)') x[0:4]
                    #   WRITE(*,'(2e15.5)') w2(1:2,1:4)
                    #   STOP "weighting 4=3=2"
                    #
            elif abs(x[1] - x[0]) < thr:
                #
                # e[3] = e[2], e[1] = e[0]
                #
                w2[0:2, 3] = libtetrabz_polcmplx_1221(x[3], x[1])
                w2[0:2, 2] = w2[0:2, 3]
                w2[0:2, 1] = libtetrabz_polcmplx_1221(x[1], x[3])
                w2[0:2, 0] = w2[0:2, 1]
                #
                # IF(ANY(w2(1:2,1:4) < 0.0)):
                #   WRITE(*,*) ie
                #   WRITE(*,'(100e15.5)') x[0:4]
                #   WRITE(*,'(2e15.5)') w2(1:2,1:4)
                #   STOP "weighting 4=3 2=1"
                #
            else:
                #
                # e[3] = e[2]
                #
                w2[0:2, 3] = libtetrabz_polcmplx_1231(x[3], x[0], x[1])
                w2[0:2, 2] = w2[0:2, 3]
                w2[0:2, 1] = libtetrabz_polcmplx_1233(x[1], x[0], x[3])
                w2[0:2, 0] = libtetrabz_polcmplx_1233(x[0], x[1], x[3])
                #
                # IF(ANY(w2(1:2,1:4) < 0.0)):
                #   WRITE(*,*) ie
                #   WRITE(*,'(100e15.5)') x[0:4]
                #   WRITE(*,'(2e15.5)') w2(1:2,1:4)
                #   STOP "weighting 4=3"
                #
        elif abs(x[2] - x[1]) < thr:
            if abs(x[2] - x[0]) < thr:
                #
                # e[2] = e[1] = e[0]
                #
                w2[0:2, 3] = libtetrabz_polcmplx_1222(x[3], x[2])
                w2[0:2, 2] = libtetrabz_polcmplx_1211(x[2], x[3])
                w2[0:2, 1] = w2[0:2, 2]
                w2[0:2, 0] = w2[0:2, 2]
                #
                # IF(ANY(w2(1:2,1:4) < 0.0)):
                #   WRITE(*,*) ie
                #   WRITE(*,'(100e15.5)') x[0:4]
                #   WRITE(*,'(2e15.5)') w2(1:2,1:4)
                #   STOP "weighting 3=2=1"
                #
            else:
                #
                # e[2] = e[1]
                #
                w2[0:2, 3] = libtetrabz_polcmplx_1233(x[3], x[0], x[2])
                w2[0:2, 2] = libtetrabz_polcmplx_1231(x[2], x[0], x[3])
                w2[0:2, 1] = w2[0:2, 2]
                w2[0:2, 0] = libtetrabz_polcmplx_1233(x[0], x[3], x[2])
                #
                # IF(ANY(w2(1:2,1:4) < 0.0)):
                #   WRITE(*,*) ie
                #   WRITE(*,'(100e15.5)') x[0:4]
                #   WRITE(*,'(2e15.5)') w2(1:2,1:4)
                #   STOP "weighting 3=2"
                #
        elif abs(x[1] - x[0]) < thr:
            #
            # e[1] = e[0]
            #
            w2[0:2, 3] = libtetrabz_polcmplx_1233(x[3], x[2], x[1])
            w2[0:2, 2] = libtetrabz_polcmplx_1233(x[2], x[3], x[1])
            w2[0:2, 1] = libtetrabz_polcmplx_1231(x[1], x[2], x[3])
            w2[0:2, 0] = w2[0:2, 1]
            #
            # IF(ANY(w2(1:2,1:4) < 0.0)):
            #   WRITE(*,*) ie
            #   WRITE(*,'(100e15.5)') x[0:4]
            #   WRITE(*,'(2e15.5)') w2(1:2,1:4)
            #   STOP "weighting 2=1"
            #
        else:
            #
            # Different each other.
            #
            w2[0:2, 3] = libtetrabz_polcmplx_1234(x[3], x[0], x[1], x[2])
            w2[0:2, 2] = libtetrabz_polcmplx_1234(x[2], x[0], x[1], x[3])
            w2[0:2, 1] = libtetrabz_polcmplx_1234(x[1], x[0], x[2], x[3])
            w2[0:2, 0] = libtetrabz_polcmplx_1234(x[0], x[1], x[2], x[3])
            #
            # IF(ANY(w2(1:2,1:4) < 0.0)):
            #   WRITE(*,*) ie
            #   WRITE(*,'(100e15.5)') x[0:4]
            #   WRITE(*,'(2e15.5)') w2(1:2,1:4)
            #   STOP "weighting"
            #
        #
        w1[ie, indx[0:4]] = w2[0, 0:4] / e0[ie].imag + 1.0j * w2[1, 0:4] / (- e0[ie].imag)
        #
    return w1
#
# Results of Integration (1-x-y-z)/(g0+(g1-g0)x+(g2-g0)y+(g3-g0))
#  for 0<x<1, 0<y<1-x, 0<z<1-x-y


def libtetrabz_polcmplx_1234(g1, g2, g3, g4):
    """
    1, Different each other
    :param g1:
    :param g2:
    :param g3:
    :param g4:
    :return:
    """
    w = numpy.empty(2, dtype=numpy.float_)
    #
    # Real
    #
    w2 = 2.0*(3.0*g2**2 - 1.0)*(math.atan(g2) - math.atan(g1)) + (g2**2 - 3.0)*g2*math.log((1.0 + g2**2)/(1.0 + g1**2))
    w2 = -2.0*(g2**2 - 1.0) + w2/(g2 - g1)
    w2 = w2/(g2 - g1)
    w3 = 2.0*(3.0*g3**2 - 1.0)*(math.atan(g3) - math.atan(g1)) + (g3**2 - 3.0)*g3*math.log((1.0 + g3**2)/(1.0 + g1**2))
    w3 = -2.0*(g3**2 - 1.0) + w3/(g3 - g1)
    w3 = w3/(g3 - g1)
    w4 = 2.0*(3.0*g4**2 - 1.0)*(math.atan(g4) - math.atan(g1)) + (g4**2 - 3.0)*g4*math.log((1.0 + g4**2)/(1.0 + g1**2))
    w4 = -2.0*(g4**2 - 1.0) + w4/(g4 - g1)
    w4 = w4/(g4 - g1)
    w2 = (w2 - w3)/(g2 - g3)
    w4 = (w4 - w3)/(g4 - g3)
    w[0] = (w4 - w2)/(2.0*(g4 - g2))
    #
    # Imaginal
    #
    w2 = 2.0*(3.0 - g2**2)*g2*(math.atan(g2) - math.atan(g1)) + (3.0*g2**2 - 1.0)*math.log((1.0 + g2**2)/(1.0 + g1**2))
    w2 = 4.0*g2 - w2/(g2 - g1)
    w2 = w2/(g2 - g1)
    w3 = 2.0*(3.0 - g3**2)*g3*(math.atan(g3) - math.atan(g1)) + (3.0*g3**2 - 1.0)*math.log((1.0 + g3**2)/(1.0 + g1**2))
    w3 = 4.0*g3 - w3/(g3 - g1)
    w3 = w3/(g3 - g1)
    w4 = 2.0*(3.0 - g4**2)*g4*(math.atan(g4) - math.atan(g1)) + (3.0*g4**2 - 1.0)*math.log((1.0 + g4**2)/(1.0 + g1**2))
    w4 = 4.0*g4 - w4/(g4 - g1)
    w4 = w4/(g4 - g1)
    w2 = (w2 - w3)/(g2 - g3)
    w4 = (w4 - w3)/(g4 - g3)
    w[1] = (w4 - w2)/(2.0*(g4 - g2))
    #
    return w


def libtetrabz_polcmplx_1231(g1, g2, g3):
    """
    2, g4 = g1
    :param g1:
    :param g2:
    :param g3:
    :return:
    """
    w = numpy.empty(2, dtype=numpy.float_)
    #
    # Real
    #
    w2 = 2.0*(-1.0 + 3.0*g2**2)*(math.atan(g2) - math.atan(g1))\
        + g2*(-3.0 + g2**2)*math.log((1.0 + g2**2)/(1.0 + g1**2))
    w2 = 2.0*(1.0 - g2**2) + w2/(g2 - g1)
    w2 = -g1 + w2/(g2 - g1)
    w2 = w2/(g2 - g1)
    w3 = 2.0*(-1.0 + 3.0*g3**2)*(math.atan(g3) - math.atan(g1))\
        + g3*(-3.0 + g3**2)*math.log((1.0 + g3**2)/(1.0 + g1**2))
    w3 = 2.0*(1 - g3**2) + w3/(g3 - g1)
    w3 = -g1 + w3/(g3 - g1)
    w3 = w3/(g3 - g1)
    w[0] = (w3 - w2)/(2.0*(g3 - g2))
    #
    # Imaginal
    #
    w2 = 2.0*g2*(3.0 - g2**2)*(math.atan(g2) - math.atan(g1)) + (-1.0 + 3.0*g2**2)*math.log((1.0 + g2**2)/(1.0 + g1**2))
    w2 = 4.0*g2 - w2/(g2 - g1)
    w2 = 1 + w2/(g2 - g1)
    w2 = w2/(g2 - g1)
    w3 = 2.0*g3*(3.0 - g3**2)*(math.atan(g3) - math.atan(g1)) + (-1.0 + 3.0*g3**2)*math.log((1.0 + g3**2)/(1.0 + g1**2))
    w3 = 4.0*g3 - w3/(g3 - g1)
    w3 = 1 + w3/(g3 - g1)
    w3 = w3/(g3 - g1)
    w[1] = (w3 - w2)/(2.0*(g3 - g2))
    #
    return w


def libtetrabz_polcmplx_1233(g1, g2, g3):
    """
    3, g4 = g3
    :param g1:
    :param g2:
    :param g3:
    :return:
    """
    w = numpy.empty(2, dtype=numpy.float_)
    #
    # Real
    #
    w2 = 2.0*(1.0 - 3.0*g2**2)*(math.atan(g2) - math.atan(g1)) + g2*(3.0 - g2**2)*math.log((1.0 + g2**2)/(1.0 + g1**2))
    w2 = 2.0*(1 - g2**2) - w2/(g2 - g1)
    w2 = w2/(g2 - g1)
    w3 = 2.0*(1.0 - 3.0*g3**2)*(math.atan(g3) - math.atan(g1)) + g3*(3.0 - g3**2)*math.log((1.0 + g3**2)/(1.0 + g1**2))
    w3 = 2.0*(1 - g3**2) - w3/(g3 - g1)
    w3 = w3/(g3 - g1)
    w2 = (w3 - w2)/(g3 - g2)
    w3 = 4.0*(1.0 - 3.0*g1*g3)*(math.atan(g3) - math.atan(g1))\
        + (3.0*g1 + 3.0*g3 - 3.0*g1*g3**2 + g3**3) * math.log((1.0 + g3**2)/(1.0 + g1**2))
    w3 = -4.0*(1.0 - g1**2) + w3/(g3 - g1)
    w3 = 4.0*g1 + w3/(g3 - g1)
    w3 = w3/(g3 - g1)
    w[0] = (w3 - w2)/(2.0*(g3 - g2))
    #
    # Imaginal
    #
    w2 = 2.0*g2*(3.0 - g2**2)*(math.atan(g2) - math.atan(g1)) + (-1.0 + 3.0*g2**2)*math.log((1.0 + g2**2)/(1.0 + g1**2))
    w2 = 4.0*g2 - w2/(g2 - g1)
    w2 = w2/(g2 - g1)
    w3 = 2.0*g3*(3.0 - g3**2)*(math.atan(g3) - math.atan(g1)) + (-1.0 + 3.0*g3**2)*math.log((1.0 + g3**2)/(1.0 + g1**2))
    w3 = 4.0*g3 - w3/(g3 - g1)
    w3 = w3/(g3 - g1)
    w2 = (w3 - w2)/(g3 - g2)
    w3 = (3.0*g1 - 3.0*g1*g3**2 + 3.0*g3 + g3**3)*(math.atan(g3) - math.atan(g1)) \
        + (3.0*g1*g3 - 1.0)*math.log((1.0 + g3**2)/(1.0 + g1**2))
    w3 = w3/(g3 - g1) - 4.0*g1
    w3 = w3/(g3 - g1) - 2.0
    w3 = (2.0*w3)/(g3 - g1)
    w[1] = (w3 - w2)/(2.0*(g3 - g2))
    #
    return w


def libtetrabz_polcmplx_1221(g1, g2):
    """
    4, g4 = g1 and g3 = g2
    :param g1:
    :param g2:
    :return:
    """
    w = numpy.empty(2, dtype=numpy.float_)
    #
    # Real
    #
    w[0] = -2.0*(-1.0 + 2.0*g1*g2 + g2**2)*(math.atan(g2) - math.atan(g1)) \
        + (g1 + 2.0*g2 - g1*g2**2)*math.log((1.0 + g2**2)/(1.0 + g1**2))
    w[0] = 2.0*(-1.0 + g1**2) + w[0]/(g2 - g1)
    w[0] = 3.0*g1 + w[0]/(g2 - g1)
    w[0] = 2.0 + (3.0*w[0])/(g2 - g1)
    w[0] = w[0]/(2.0*(g2 - g1))
    #
    # Imaginal
    #
    w[1] = 2.0*(g1 + 2.0*g2 - g1*g2**2)*(math.atan(g2) - math.atan(g1)) \
        + (-1.0 + 2.0*g1*g2 + g2**2)*math.log((1 + g2**2)/(1 + g1**2))
    w[1] = -4.0*g1 + w[1]/(g2 - g1)
    w[1] = -3.0 + w[1]/(g2 - g1)
    w[1] = (3.0*w[1])/(2.0*(g2 - g1)**2)
    #
    return w


def libtetrabz_polcmplx_1222(g1, g2):
    """
    5, g4 = g3 = g2
    :param g1:
    :param g2:
    :return:
    """
    w = numpy.empty(2, dtype=numpy.float_)
    #
    # Real
    #
    w[0] = 2.0*(-1.0 + g1**2 + 2.0*g1*g2)*(math.atan(g2) - math.atan(g1)) \
        + (-2.0*g1 - g2 + g1**2*g2) * math.log((1.0 + g2**2)/(1.0 + g1**2))
    w[0] = 2.0*(1.0 - g1**2) + w[0]/(g2 - g1)
    w[0] = g1 - w[0]/(g2 - g1)
    w[0] = 1.0 - (3.0*w[0])/(g2 - g1)
    w[0] = w[0]/(2.0*(g2 - g1))
    #
    # Imaginal
    #
    w[1] = 2.0*(-2.0*g1 - g2 + g1**2*g2)*(math.atan(g2) - math.atan(g1)) \
        + (1.0 - g1**2 - 2.0*g1*g2) * math.log((1.0 + g2**2)/(1.0 + g1**2))
    w[1] = 4.0*g1 + w[1]/(g2 - g1)
    w[1] = 1.0 + w[1]/(g2 - g1)
    w[1] = (3.0*w[1])/(2.0*(g2 - g1)**2)
    #
    return w


def libtetrabz_polcmplx_1211(g1, g2):
    """
    6, g4 = g3 = g1
    :param g1:
    :param g2:
    :return:
    """
    w = numpy.empty(2, dtype=numpy.float_)
    #
    # Real
    #
    w[0] = 2.0*(3.0*g2**2 - 1.0)*(math.atan(g2) - math.atan(g1)) \
        + g2*(g2**2 - 3.0)*math.log((1.0 + g2**2)/(1.0 + g1**2))
    w[0] = 2.0*(1.0 - g1**2) + w[0]/(g2 - g1)
    w[0] = -5.0*g1 + w[0]/(g2 - g1)
    w[0] = -11.0 + (3.0*w[0])/(g2 - g1)
    w[0] = w[0]/(6.0*(g2 - g1))
    #
    # Imaginal
    #
    w[1] = 2.0*g2*(-3.0 + g2**2)*(math.atan(g2) - math.atan(g1)) \
        + (1.0 - 3.0*g2**2)*math.log((1.0 + g2**2)/(1.0 + g1**2))
    w[1] = 4.0*g2 + w[1]/(g2 - g1)
    w[1] = 1.0 + w[1]/(g2 - g1)
    w[1] = w[1]/(2.0*(g2 - g1)**2)
    #
    return w
