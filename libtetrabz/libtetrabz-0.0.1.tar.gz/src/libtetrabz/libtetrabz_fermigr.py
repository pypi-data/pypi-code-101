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


def fermigr(bvec, eig1, eig2, e0):
    """
    Main SUBROUTINE for Fermi's Golden rule : Theta(- E1) * Theta(E2) * Delta(E2 - E1 - w)
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

    wght = numpy.zeros([ng[0], ng[1], ng[2], nb, nb, ne], dtype=numpy.float_)

    thr = 1.0e-10
    #
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
        w1 = numpy.zeros([nb, nb, ne, 4], dtype=numpy.float_)
        w2t = numpy.zeros([nb, ne, 4], dtype=numpy.float_)
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
                    #
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_fermigr2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
            elif e[1] <= 0.0 < e[2]:
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_b1(e)
                #
                if v > thr:
                    #
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_fermigr2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_b2(e)
                #
                if v > thr:
                    #
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_fermigr2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_b3(e)
                #
                if v > thr:
                    #
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_fermigr2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
            elif e[2] <= 0.0 < e[3]:
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_c1(e)
                #
                if v > thr:
                    #
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_fermigr2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_c2(e)
                #
                if v > thr:
                    #
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_fermigr2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
                v, tsmall = libtetrabz_common.libtetrabz_tsmall_c3(e)
                #
                if v > thr:
                    #
                    ei2 = tsmall.dot(ei1[indx[0:4], ib])
                    ej2 = tsmall.dot(ej1[indx[0:4], 0:nb])
                    w2 = libtetrabz_fermigr2(e0, ei2, ej2)
                    w2t[0:nb, 0:ne, indx[0:4]] = w2.dot(tsmall)
                    w1[ib, 0:nb, 0:ne, 0:4] += v * w2t
                #
            elif e[3] <= 0.0:
                #
                ei2 = ei1[0:4, ib]
                ej2 = ej1[0:4, 0:nb]
                w2 = libtetrabz_fermigr2(e0, ei2, ej2)
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


def libtetrabz_fermigr2(e0, ei1, ej1):
    """
    Tetrahedra method for theta( - E2)
    :param e0:
    :param ei1:
    :param ej1:
    :return:
    """
    #
    ne = e0.shape[0]
    nb = ej1.shape[1]
    w1 = numpy.zeros([nb, ne, 4], dtype=numpy.float_)
    w2t = numpy.zeros([ne, 4], dtype=numpy.float_)
    thr = 1.0e-8
    #
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
                #
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_fermigr3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
                #
            #
        elif e[1] <= 0.0 < e[2] or e[1] < 0.0 <= e[2]:
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_b1(e)
            #
            if v > thr:
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_fermigr3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_b2(e)
            #
            if v > thr:
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_fermigr3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_b3(e)
            #
            if v > thr:
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_fermigr3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
            #
        elif e[2] <= 0.0 < e[3] or e[2] < 0.0 <= e[3]:
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_c1(e)
            #
            if v > thr:
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_fermigr3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_c2(e)
            #
            if v > thr:
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_fermigr3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
            #
            v, tsmall = libtetrabz_common.libtetrabz_tsmall_c3(e)
            #
            if v > thr:
                de = tsmall.dot(ej1[indx[0:4], ib] - ei1[indx[0:4]])
                w2 = libtetrabz_fermigr3(e0, de)
                w2t[0:ne, indx[0:4]] = w2.dot(tsmall)
                w1[ib, 0:ne, 0:4] += v * w2t
            #
        elif e[3] <= 0.0:
            de = ej1[0:4, ib] - ei1[0:4]
            w2 = libtetrabz_fermigr3(e0, de)
            w1[ib, 0:ne, 0:4] += w2
            #
    return w1


def libtetrabz_fermigr3(e0, de):
    #
    ne = e0.shape[0]
    e = de[0:4].copy()
    indx = e.argsort(0)
    e.sort(0)
    w1 = numpy.zeros([ne, 4], dtype=numpy.float_)
    #
    for ie in range(ne):
        #
        if e[0] < e0[ie] <= e[1]:
            #
            v, tsmall = libtetrabz_common.libtetrabz_triangle_a1(e[0:4] - e0[ie])
            w1[ie, indx[0:4]] += v * tsmall.sum(0) / 3.0
            #
        elif e[1] < e0[ie] <= e[2]:
            #
            v, tsmall = libtetrabz_common.libtetrabz_triangle_b1(e[0:4] - e0[ie])
            w1[ie, indx[0:4]] += v * tsmall.sum(0) / 3.0
            #
            v, tsmall = libtetrabz_common.libtetrabz_triangle_b2(e[0:4] - e0[ie])
            w1[ie, indx[0:4]] += v * tsmall.sum(0) / 3.0
            #
        elif e[2] < e0[ie] < e[3]:
            #
            v, tsmall = libtetrabz_common.libtetrabz_triangle_c1(e[0:4] - e0[ie])
            w1[ie, indx[0:4]] += v * tsmall.sum(0) / 3.0
            #
    return w1
