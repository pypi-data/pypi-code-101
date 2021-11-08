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
import numpy
from . import libtetrabz_common


def dos(bvec, eig, e0):
    """
    Compute Dos : Delta(E - E1)
    :param ndarray([3, 3], float) bvec: Reciprocal-lattice vectors
    :param ndarray([ng0, ng1, ng2, nb], float) eig: Energy eigenvalue
    :param ndarray(ne, float) e0: Energy grid
    :return ndarray([ng0, ng1, ng2, nb, ne], float) wght: Weight
    """
    ng = numpy.array(eig.shape[0:3])
    nk = ng.prod(0)
    nb = eig.shape[3]
    ne = e0.shape[0]
    wlsm, ikv = libtetrabz_common.libtetrabz_initialize(ng, bvec)
    #
    wght = numpy.zeros([ng[0], ng[1], ng[2], nb, ne], dtype=numpy.float_)
    #
    for it in range(6*nk):
        #
        eigt = numpy.empty([20, nb], dtype=numpy.float_)
        for ii in range(20):
            eigt[ii, 0:nb] = eig[ikv[it, ii, 0], ikv[it, ii, 1], ikv[it, ii, 2], 0:nb]
        ei1 = wlsm.dot(eigt)
        #
        w1 = numpy.zeros([nb, ne, 4], dtype=numpy.float_)
        #
        for ib in range(nb):
            #
            e = ei1[0:4, ib].copy()
            indx = e.argsort(0)
            e = e[indx[0:4]]
            #
            for ie in range(ne):
                #
                if e[0] < e0[ie] <= e[1] or e[0] <= e0[ie] < e[1]:
                    #
                    v, tsmall = libtetrabz_common.libtetrabz_triangle_a1(e[0:4] - e0[ie])
                    w1[ib, ie, indx[0:4]] += v * tsmall.sum(0) / 3.0
                    #
                elif e[1] < e0[ie] <= e[2] or e[1] <= e0[ie] < e[2]:
                    #
                    v, tsmall = libtetrabz_common.libtetrabz_triangle_b1(e[0:4] - e0[ie])
                    w1[ib, ie, indx[0:4]] += v * tsmall.sum(0) / 3.0
                    #
                    v, tsmall = libtetrabz_common.libtetrabz_triangle_b2(e[0:4] - e0[ie])
                    w1[ib, ie, indx[0:4]] += v * tsmall.sum(0) / 3.0
                    #
                elif e[2] < e0[ie] <= e[3] or e[2] <= e0[ie] < e[3]:
                    #
                    v, tsmall = libtetrabz_common.libtetrabz_triangle_c1(e[0:4] - e0[ie])
                    w1[ib, ie, indx[0:4]] += v * tsmall.sum(0) / 3.0
                    #
                else:
                    continue
                #
            #
        #
        for ii in range(20):
            wght[ikv[it, ii, 0], ikv[it, ii, 1], ikv[it, ii, 2], 0:nb, 0:ne] += w1.dot(wlsm[:, ii])
        #
    #
    wght[0:ng[0], 0:ng[1], 0:ng[2], 0:nb, 0:ne] /= (6.0 * nk)
    return wght


def intdos(bvec, eig, e0):
    """
    Compute integrated Dos : theta(E - E1)
    :param ndarray([3, 3], float) bvec: Reciprocal-lattice vectors
    :param ndarray([ng0, ng1, ng2, nb], float) eig: Energy eigenvalue
    :param ndarray(ne, float) e0: Energy grid
    :return ndarray([ng0, ng1, ng2, nb, ne], float) wght: Weight
    """
    ng = numpy.array(eig.shape[0:3])
    nk = ng.prod(0)
    nb = eig.shape[3]
    ne = e0.shape[0]
    wlsm, ikv = libtetrabz_common.libtetrabz_initialize(ng, bvec)
    #
    wght = numpy.zeros([ng[0], ng[1], ng[2], nb, ne], dtype=numpy.float_)
    #
    for it in range(6*nk):
        #
        eigt = numpy.empty([20, nb], dtype=numpy.float_)
        for ii in range(20):
            eigt[ii, 0:nb] = eig[ikv[it, ii, 0], ikv[it, ii, 1], ikv[it, ii, 2], 0:nb]
        ei1 = wlsm.dot(eigt)
        #
        w1 = numpy.zeros([nb, ne, 4], dtype=numpy.float_)
        #
        for ib in range(nb):
            #
            e = ei1[0:4, ib].copy()
            indx = e.argsort(0)
            e.sort(0)
            #
            for ie in range(ne):
                #
                if e[0] <= e0[ie] < e[1] or e[0] < e0[ie] <= e[1]:
                    #
                    v, tsmall = libtetrabz_common.libtetrabz_tsmall_a1(e - e0[ie])
                    w1[ib, ie, indx[0:4]] += v * tsmall.sum(0) * 0.25
                    #
                elif e[1] <= e0[ie] < e[2] or e[1] < e0[ie] <= e[2]:
                    #
                    v, tsmall = libtetrabz_common.libtetrabz_tsmall_b1(e - e0[ie])
                    w1[ib, ie, indx[0:4]] += v * tsmall.sum(0) * 0.25
                    #
                    v, tsmall = libtetrabz_common.libtetrabz_tsmall_b2(e - e0[ie])
                    w1[ib, ie, indx[0:4]] += v * tsmall.sum(0) * 0.25
                    #
                    v, tsmall = libtetrabz_common.libtetrabz_tsmall_b3(e - e0[ie])
                    w1[ib, ie, indx[0:4]] += v * tsmall.sum(0) * 0.25
                    #
                elif e[2] <= e0[ie] < e[3] or e[2] < e0[ie] <= e[3]:
                    #
                    v, tsmall = libtetrabz_common.libtetrabz_tsmall_c1(e - e0[ie])
                    w1[ib, ie, indx[0:4]] += v * tsmall.sum(0) * 0.25
                    #
                    v, tsmall = libtetrabz_common.libtetrabz_tsmall_c2(e - e0[ie])
                    w1[ib, ie, indx[0:4]] += v * tsmall.sum(0) * 0.25
                    #
                    v, tsmall = libtetrabz_common.libtetrabz_tsmall_c3(e - e0[ie])
                    w1[ib, ie, indx[0:4]] += v * tsmall.sum(0) * 0.25
                    #
                elif e[3] <= e0[ie]:
                    w1[ib, ie, 0:4] = 0.25
                else:
                    continue
                #
            #
        #
        for ii in range(20):
            wght[ikv[it, ii, 0], ikv[it, ii, 1], ikv[it, ii, 2], 0:nb, 0:ne] += w1.dot(wlsm[:, ii])
        #
    wght[0:ng[0], 0:ng[1], 0:ng[2], 0:nb, 0:ne] /= (6.0 * nk)
    return wght
