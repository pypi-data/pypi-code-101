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


def libtetrabz_initialize(ng, bvec):
    """
    define shortest diagonal line & define type of tetragonal
    :param ng:
    :param bvec:
    :return:
    """
    bvec2 = numpy.empty([3, 3], dtype=numpy.float_)
    for i1 in range(3):
        bvec2[i1, 0:3] = bvec[i1, 0:3] / ng[i1]
    #
    bvec3 = numpy.empty([4, 3], dtype=numpy.float_)
    bvec3[0, 0:3] = -bvec2[0, 0:3] + bvec2[1, 0:3] + bvec2[2, 0:3]
    bvec3[1, 0:3] = bvec2[0, 0:3] - bvec2[1, 0:3] + bvec2[2, 0:3]
    bvec3[2, 0:3] = bvec2[0, 0:3] + bvec2[1, 0:3] - bvec2[2, 0:3]
    bvec3[3, 0:3] = bvec2[0, 0:3] + bvec2[1, 0:3] + bvec2[2, 0:3]
    #
    # length of delta bvec
    #
    bnorm = numpy.empty(4, dtype=numpy.float_)
    for i1 in range(4):
        bnorm[i1] = numpy.linalg.norm(bvec3[i1, 0:3])
    #
    itype = bnorm.argmin(0)
    #
    # start & last
    #
    ivvec0 = numpy.zeros(4, dtype=numpy.int_)
    #
    divvec = numpy.identity(4, dtype=numpy.int_)
    #
    ivvec0[itype] = 1
    divvec[itype, itype] = - 1
    #
    # Corners of tetrahedra
    #
    ivvec = numpy.empty([6, 20, 3], dtype=numpy.float_)
    it = 0
    for i1 in range(3):
        for i2 in range(3):
            if i2 == i1:
                continue
            for i3 in range(3):
                if i3 == i1 or i3 == i2:
                    continue
                #
                ivvec[it, 0, 0:3] = ivvec0[0:3]
                ivvec[it, 1, 0:3] = ivvec[it, 0, 0:3] + divvec[i1, 0:3]
                ivvec[it, 2, 0:3] = ivvec[it, 1, 0:3] + divvec[i2, 0:3]
                ivvec[it, 3, 0:3] = ivvec[it, 2, 0:3] + divvec[i3, 0:3]
                #
                it += 1
    #
    # Additional points
    #
    ivvec[0:6,  4, 0:3] = 2 * ivvec[0:6, 0, 0:3] - ivvec[0:6, 1, 0:3]
    ivvec[0:6,  5, 0:3] = 2 * ivvec[0:6, 1, 0:3] - ivvec[0:6, 2, 0:3]
    ivvec[0:6,  6, 0:3] = 2 * ivvec[0:6, 2, 0:3] - ivvec[0:6, 3, 0:3]
    ivvec[0:6,  7, 0:3] = 2 * ivvec[0:6, 3, 0:3] - ivvec[0:6, 0, 0:3]
    #
    ivvec[0:6,  8, 0:3] = 2 * ivvec[0:6, 0, 0:3] - ivvec[0:6, 2, 0:3]
    ivvec[0:6,  9, 0:3] = 2 * ivvec[0:6, 1, 0:3] - ivvec[0:6, 3, 0:3]
    ivvec[0:6, 10, 0:3] = 2 * ivvec[0:6, 2, 0:3] - ivvec[0:6, 0, 0:3]
    ivvec[0:6, 11, 0:3] = 2 * ivvec[0:6, 3, 0:3] - ivvec[0:6, 1, 0:3]
    #
    ivvec[0:6, 12, 0:3] = 2 * ivvec[0:6, 0, 0:3] - ivvec[0:6, 3, 0:3]
    ivvec[0:6, 13, 0:3] = 2 * ivvec[0:6, 1, 0:3] - ivvec[0:6, 0, 0:3]
    ivvec[0:6, 14, 0:3] = 2 * ivvec[0:6, 2, 0:3] - ivvec[0:6, 1, 0:3]
    ivvec[0:6, 15, 0:3] = 2 * ivvec[0:6, 3, 0:3] - ivvec[0:6, 2, 0:3]
    #
    ivvec[0:6, 16, 0:3] = ivvec[0:6, 3, 0:3] - ivvec[0:6, 0, 0:3] + ivvec[0:6, 1, 0:3]
    ivvec[0:6, 17, 0:3] = ivvec[0:6, 0, 0:3] - ivvec[0:6, 1, 0:3] + ivvec[0:6, 2, 0:3]
    ivvec[0:6, 18, 0:3] = ivvec[0:6, 1, 0:3] - ivvec[0:6, 2, 0:3] + ivvec[0:6, 3, 0:3]
    ivvec[0:6, 19, 0:3] = ivvec[0:6, 2, 0:3] - ivvec[0:6, 3, 0:3] + ivvec[0:6, 0, 0:3]
    #
    wlsm = numpy.empty([4, 20], dtype=numpy.float_)
    wlsm[0:4, 0: 4] = numpy.array([[1440.0,    0.0,   30.0,    0.0],
                                   [0.0,    1440.0,    0.0,   30.0],
                                   [30.0,      0.0, 1440.0,    0.0],
                                   [0.0,      30.0,    0.0, 1440.0]])
    #
    wlsm[0:4, 4: 8] = numpy.array([[-38.0,    7.0,   17.0,  -28.0],
                                   [-28.0,  -38.0,    7.0,   17.0],
                                   [17.0,   -28.0,  -38.0,    7.0],
                                   [7.0,     17.0,  -28.0,  -38.0]])
    #
    wlsm[0:4, 8:12] = numpy.array([[-56.0,    9.0,  -46.0,    9.0],
                                   [9.0,    -56.0,    9.0,  -46.0],
                                   [-46.0,    9.0,  -56.0,    9.0],
                                   [9.0,    -46.0,    9.0,  -56.0]])
    #
    wlsm[0:4, 12:16] = numpy.array([[-38.0,  -28.0,   17.0,    7.0],
                                   [7.0,     -38.0,  -28.0,   17.0],
                                   [17.0,      7.0,  -38.0,  -28.0],
                                   [-28.0,    17.0,    7.0,  -38.0]])
    #
    wlsm[0:4, 16:20] = numpy.array([[-18.0,  -18.0,   12.0,  -18.0],
                                    [-18.0,  -18.0,  -18.0,   12.0],
                                    [12.0,   -18.0,  -18.0,  -18.0],
                                    [-18.0,   12.0,  -18.0,  -18.0]])
    #
    wlsm[0:4, 0:20] /= 1260.0
    #
    # k-index for energy
    #
    nk = ng.prod(0)
    ikv = numpy.empty([nk*6, 20, 3], dtype=numpy.int_)
    ikv0 = numpy.empty(3, dtype=numpy.int_)
    nt = 0
    for i2 in range(ng[2]):
        for i1 in range(ng[1]):
            for i0 in range(ng[0]):
                #
                for it in range(6):
                    #
                    for ii in range(20):
                        #
                        ikv0[0:3] = [i0, i1, i2] + ivvec[it, ii, 0:3]
                        ikv[nt, ii, 0:3] = ikv0[0:3] % ng[0:3]
                        #
                    nt += 1
    return wlsm, ikv


def libtetrabz_tsmall_a1(e):
    """Cut small tetrahedron A1
    """
    a10 = (0.0 - e[0]) / (e[1] - e[0])
    a20 = (0.0 - e[0]) / (e[2] - e[0])
    a30 = (0.0 - e[0]) / (e[3] - e[0])
    #
    v = a10 * a20 * a30
    #
    tsmall = numpy.array([[1.0,       0.0, 0.0, 0.0],
                          [1.0 - a10, a10, 0.0, 0.0],
                          [1.0 - a20, 0.0, a20, 0.0],
                          [1.0 - a30, 0.0, 0.0, a30]])
    return v, tsmall


def libtetrabz_tsmall_b1(e):
    """
    Cut small tetrahedron B1
    :param e: numpy
    :return:
    """
    #
    #
    a13 = (0.0 - e[3]) / (e[1] - e[3])
    a20 = (0.0 - e[0]) / (e[2] - e[0])
    a30 = (0.0 - e[0]) / (e[3] - e[0])
    #
    v = a20 * a30 * a13
    tsmall = numpy.array([[1.0,       0.0, 0.0,       0.0],
                          [1.0 - a20, 0.0, a20,       0.0],
                          [1.0 - a30, 0.0, 0.0,       a30],
                          [0.0,       a13, 0.0, 1.0 - a13]])
    return v, tsmall


def libtetrabz_tsmall_b2(e):
    """
    Cut small tetrahedron B2
    :param e:
    :return:
    """
    a21 = (0.0 - e[1]) / (e[2] - e[1])
    a31 = (0.0 - e[1]) / (e[3] - e[1])
    #
    v = a21 * a31
    #
    tsmall = numpy.array([[1.0,       0.0, 0.0, 0.0],
                          [0.0,       1.0, 0.0, 0.0],
                          [0.0, 1.0 - a21, a21, 0.0],
                          [0.0, 1.0 - a31, 0.0, a31]])
    return v, tsmall


def libtetrabz_tsmall_b3(e):
    """
    Cut small tetrahedron B3
    :param e:
    :return:
    """
    a12 = (0.0 - e[2]) / (e[1] - e[2])
    a20 = (0.0 - e[0]) / (e[2] - e[0])
    a31 = (0.0 - e[1]) / (e[3] - e[1])
    #
    v = a12 * a20 * a31
    #
    tsmall = numpy.array([[1.0,     0.0,     0.0, 0.0],
                          [1.0-a20, 0.0,     a20, 0.0],
                          [0.0,     a12, 1.0-a12, 0.0],
                          [0.0, 1.0-a31,     0.0, a31]])
    return v, tsmall


def libtetrabz_tsmall_c1(e):
    """
    Cut small tetrahedron C1
    :param e:
    :return:
    """
    a32 = (0.0 - e[2]) / (e[3] - e[2])
    #
    v = a32
    #
    tsmall = numpy.array([[1.0, 0.0,       0.0, 0.0],
                          [0.0, 1.0,       0.0, 0.0],
                          [0.0, 0.0,       1.0, 0.0],
                          [0.0, 0.0, 1.0 - a32, a32]])
    return v, tsmall


def libtetrabz_tsmall_c2(e):
    """
    Cut small tetrahedron C2
    :param e:
    :return:
    """
    a23 = (0.0 - e[3]) / (e[2] - e[3])
    a31 = (0.0 - e[1]) / (e[3] - e[1])
    #
    v = a23 * a31
    #
    tsmall = numpy.array([[1.0,       0.0, 0.0,       0.0],
                          [0.0,       1.0, 0.0,       0.0],
                          [0.0, 1.0 - a31, 0.0,       a31],
                          [0.0,       0.0, a23, 1.0 - a23]])
    return v, tsmall


def libtetrabz_tsmall_c3(e):
    """
    Cut small tetrahedron C3
    :param e:
    :return:
    """
    a23 = (0.0 - e[3]) / (e[2] - e[3])
    a13 = (0.0 - e[3]) / (e[1] - e[3])
    a30 = (0.0 - e[0]) / (e[3] - e[0])
    #
    v = a23 * a13 * a30
    #
    tsmall = numpy.array([[1.0,       0.0, 0.0,       0.0],
                          [1.0 - a30, 0.0, 0.0,       a30],
                          [0.0,       a13, 0.0, 1.0 - a13],
                          [0.0,       0.0, a23, 1.0 - a23]])
    return v, tsmall


def libtetrabz_triangle_a1(e):
    """
    Cut triangle A1
    :param e:
    :return:
    """
    a10 = (0.0 - e[0]) / (e[1] - e[0])
    a20 = (0.0 - e[0]) / (e[2] - e[0])
    a30 = (0.0 - e[0]) / (e[3] - e[0])
    #
    # v = 3.0 * a[1,0] * a[2,0] * a[3,0] / (0.0 - e[0])
    v = 3.0 * a10 * a20 / (e[3] - e[0])
    #
    tsmall = numpy.array([[1.0 - a10, a10, 0.0, 0.0],
                          [1.0 - a20, 0.0, a20, 0.0],
                          [1.0 - a30, 0.0, 0.0, a30]])
    return v, tsmall


def libtetrabz_triangle_b1(e):
    """
    Cut triangle B1
    :param e:
    :return:
    """
    a30 = (0.0 - e[0]) / (e[3] - e[0])
    a13 = (0.0 - e[3]) / (e[1] - e[3])
    a20 = (0.0 - e[0]) / (e[2] - e[0])
    #
    # v = 3.0 * a[2,0] * a[3,0] * a[1,3] / (0.0 - e[0])
    v = 3.0 * a30 * a13 / (e[2] - e[0])
    #
    tsmall = numpy.array([[1.0 - a20, 0.0, a20,       0.0],
                          [1.0 - a30, 0.0, 0.0,       a30],
                          [0.0,       a13, 0.0, 1.0 - a13]])
    return v, tsmall


def libtetrabz_triangle_b2(e):
    """Cut triangle B2
    :param e:
    :return:
    """
    a12 = (0.0 - e[2]) / (e[1] - e[2])
    a31 = (0.0 - e[1]) / (e[3] - e[1])
    a20 = (0.0 - e[0]) / (e[2] - e[0])
    #
    # v = 3.0 * a[1,2] * a[2,0] * a[3,1] / (0.0 - e[0])
    v = 3.0 * a12 * a31 / (e[2] - e[0])
    #
    tsmall = numpy.array([[1.0 - a20, 0.0, a20,     0.0],
                          [0.0, a12, 1.0 - a12,     0.0],
                          [0.0, 1.0 - a31,     0.0, a31]])
    return v, tsmall


def libtetrabz_triangle_c1(e):
    """Cut triangle C1
    :param e:
    :return:
    """
    a03 = (0.0 - e[3]) / (e[0] - e[3])
    a13 = (0.0 - e[3]) / (e[1] - e[3])
    a23 = (0.0 - e[3]) / (e[2] - e[3])
    #
    # v = 3.0 * a[0,3] * a[1,3] * a[2,3] / (e[3] - 0.0)
    v = 3.0 * a03 * a13 / (e[3] - e[2])
    #
    tsmall = numpy.array([[a03, 0.0,     0.0, 1.0 - a03],
                          [0.0, a13,     0.0, 1.0 - a13],
                          [0.0,     0.0, a23, 1.0 - a23]])
    return v, tsmall
