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


def fermieng(bvec, eig, nelec):
    """
    Calculate Fermi energy
    :param ndarray([3, 3], float) bvec: Reciprocal-lattice vectors
    :param ndarray([ng0, ng1, ng2, nb], float) eig: Energy eigenvalue
    :param float nelec:
    :return:
    """
    #
    maxiter = 300
    eps = 1.0e-10
    #
    elw = eig.min()
    eup = eig.max()
    #
    # Bisection method
    #
    for iteration in range(maxiter):
        #
        ef = (eup + elw) * 0.5
        #
        # Calc. # of electrons
        #
        wght = occ(bvec, eig-ef)
        sumkmid = wght.sum()
        #
        # convergence check
        #
        if abs(sumkmid - nelec) < eps:
            return ef, wght, iteration
        elif sumkmid < nelec:
            elw = ef
        else:
            eup = ef
        #
    raise ValueError("libtetrabz_fermieng")


def occ(bvec=numpy.array([1.0, 0.0, 0.0]), eig=numpy.array([0.0])):
    """
    Main SUBROUTINE for occupation : Theta(EF - E1)
    :param ndarray([3, 3], float) bvec: Reciprocal-lattice vectors
    :param ndarray([ng0, ng1, ng2, nb], float) eig: Energy eigenvalue
    :return ndarray([ng0, ng1, ng2, nb], float) wght: Weight
    """
    #
    ng = numpy.array(eig.shape[0:3])
    nk = ng.prod(0)
    nb = eig.shape[3]
    wlsm, ikv = libtetrabz_common.libtetrabz_initialize(ng, bvec)
    #
    wght = numpy.zeros([ng[0], ng[1], ng[2], nb], dtype=numpy.float_)
    #
    for it in range(6 * nk):
        #
        eigt = numpy.empty([20, nb], dtype=numpy.float_)
        for ii in range(20):
            eigt[ii, 0:nb] = eig[ikv[it, ii, 0], ikv[it, ii, 1], ikv[it, ii, 2], 0:nb]
        ei1 = wlsm.dot(eigt)
        #
        w1 = numpy.zeros([nb, 4], dtype=numpy.float_)
        for ib in range(nb):
            #
            e = ei1[0:4, ib].copy()
            indx = e.argsort(0)
            e.sort(0)
            #
            if e[0] <= 0.0 < e[1]:
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_a1(e)
                w1[ib, indx[0:4]] += v * tsmall.sum(0) * 0.25
                #
            elif e[1] <= 0.0 < e[2]:
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_b1(e)
                w1[ib, indx[0:4]] += v * tsmall.sum(0) * 0.25
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_b2(e)
                w1[ib, indx[0:4]] += v * tsmall.sum(0) * 0.25
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_b3(e)
                w1[ib, indx[0:4]] += v * tsmall.sum(0) * 0.25
                #
            elif e[2] <= 0.0 < e[3]:
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_c1(e)
                w1[ib, indx[0:4]] += v * tsmall.sum(0) * 0.25
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_c2(e)
                w1[ib, indx[0:4]] += v * tsmall.sum(0) * 0.25
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_c3(e)
                w1[ib, indx[0:4]] += v * tsmall.sum(0) * 0.25
                #
            elif e[3] <= 0.0:
                w1[ib, 0:4] = 0.25
            else:
                continue
            #
        #
        for ii in range(20):
            wght[ikv[it, ii, 0], ikv[it, ii, 1], ikv[it, ii, 2], 0:nb] += w1.dot(wlsm[:, ii])
        #
    wght[0:ng[0], 0:ng[1], 0:ng[2], 0:nb] /= (6.0 * nk)
    return wght
