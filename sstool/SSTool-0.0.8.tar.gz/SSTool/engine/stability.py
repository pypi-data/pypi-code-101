import numpy as np
import pandas as pd
import sympy as sym
import matplotlib.pyplot as plt
from control.matlab import *
from collections import Counter
import sys

# import os.path
# from control.matlab import *
# import matplotlib.pyplot as plt
# import numpy as np
from SSTool.engine.devices import auxiliaries


def bode_YZ(ss_class, f_ini=0, f_fin=3, name_in=[], name_out=[], n_p=1000, logx = False, dBy = False, invert = False):
    '''
    Bode plot of a 2x2 system

    :param ss_class: class with the space state, the inputs and the outputs
    :param lim_ini: log of the initial frequency. For instance, -1 represents 10^(-1) Hz
    :param lim_fin: log of the final frequency. For instance, 4 represents 10^(4) Hz
    :param name_in: name of the 2 inputs
    :param name_out: name of the 2 outputs
    :param n_p: number of points to represent. For instance, 1000    
    :param logx: if the horizontal axis has to be logarithmic
    :param dBy: if the vertical axis has to be in dB
    :param invert: divide in / out instead of out / in
    :return: nothing, it just plots
    '''
    # initial definitions
    n_points = n_p
    wfreq = np.logspace(f_ini, f_fin, num=n_points) * 2 * np.pi
    ffreq = np.logspace(f_ini, f_fin, num=n_points)
    (mag, phase, freq) = ss_class.ssm.freqresp(wfreq)

    # print(ss_class.outputs.index('vqx_0'))
    ii0 = ss_class.inputs.index(name_in[0])
    ii1 = ss_class.inputs.index(name_in[1])
    oo0 = ss_class.outputs.index(name_out[0])
    oo1 = ss_class.outputs.index(name_out[1])

    # extract indices for inputs/outputs
    if invert is False:
        in0 = ii0
        in1 = ii1
        out0 = oo0
        out1 = oo1
    else:
        in0 = oo0
        in1 = oo1
        out0 = ii0
        out1 = ii1

    # plot
    fig, axs = plt.subplots(4, 2)

    if logx is True and dBy is True:
        axs[0, 0].semilogx(ffreq, 20 * np.log10(abs(mag[out0, in0])))
        axs[0, 1].semilogx(ffreq, 20 * np.log10(abs(mag[out0, in1])))

        axs[1, 0].semilogx(ffreq, 180 / np.pi * (phase[out0, in0]))
        axs[1, 1].semilogx(ffreq, 180 / np.pi * (phase[out0, in1]))

        axs[2, 0].semilogx(ffreq, 20 * np.log10(abs(mag[out1, in0])))
        axs[2, 1].semilogx(ffreq, 20 * np.log10(abs(mag[out1, in1])))

        axs[3, 0].semilogx(ffreq, 180 / np.pi * (phase[out1, in0]))
        axs[3, 1].semilogx(ffreq, 180 / np.pi * (phase[out1, in1]))

        axs[0, 0].set_xlabel('Frequency (Hz)')
        axs[0, 0].set_ylabel('Magnitude (dB)')

        axs[0, 1].set_xlabel('Frequency (Hz)')
        axs[0, 1].set_ylabel('Magnitude (dB)')

        axs[1, 0].set_xlabel('Frequency (Hz)')
        axs[1, 0].set_ylabel('Phase (deg)')

        axs[1, 1].set_xlabel('Frequency (Hz)')
        axs[1, 1].set_ylabel('Phase (deg)')

        axs[2, 0].set_xlabel('Frequency (Hz)')
        axs[2, 0].set_ylabel('Magnitude (dB)')

        axs[2, 1].set_xlabel('Frequency (Hz)')
        axs[2, 1].set_ylabel('Magnitude (dB)')

        axs[3, 0].set_xlabel('Frequency (Hz)')
        axs[3, 0].set_ylabel('Phase (deg)')

        axs[3, 1].set_xlabel('Frequency (Hz)')
        axs[3, 1].set_ylabel('Phase (deg)')

    if logx is False and dBy is True:
        axs[0, 0].plot(ffreq, 20 * np.log10(abs(mag[out0, in0])))
        axs[0, 1].plot(ffreq, 20 * np.log10(abs(mag[out0, in1])))

        axs[1, 0].plot(ffreq, 180 / np.pi * (phase[out0, in0]))
        axs[1, 1].plot(ffreq, 180 / np.pi * (phase[out0, in1]))

        axs[2, 0].plot(ffreq, 20 * np.log10(abs(mag[out1, in0])))
        axs[2, 1].plot(ffreq, 20 * np.log10(abs(mag[out1, in1])))

        axs[3, 0].plot(ffreq, 180 / np.pi * (phase[out1, in0]))
        axs[3, 1].plot(ffreq, 180 / np.pi * (phase[out1, in1]))

        axs[0, 0].set_xlabel('Frequency (Hz)')
        axs[0, 0].set_ylabel('Magnitude (dB)')

        axs[0, 1].set_xlabel('Frequency (Hz)')
        axs[0, 1].set_ylabel('Magnitude (dB)')

        axs[1, 0].set_xlabel('Frequency (Hz)')
        axs[1, 0].set_ylabel('Phase (deg)')

        axs[1, 1].set_xlabel('Frequency (Hz)')
        axs[1, 1].set_ylabel('Phase (deg)')

        axs[2, 0].set_xlabel('Frequency (Hz)')
        axs[2, 0].set_ylabel('Magnitude (dB)')

        axs[2, 1].set_xlabel('Frequency (Hz)')
        axs[2, 1].set_ylabel('Magnitude (dB)')

        axs[3, 0].set_xlabel('Frequency (Hz)')
        axs[3, 0].set_ylabel('Phase (deg)')

        axs[3, 1].set_xlabel('Frequency (Hz)')
        axs[3, 1].set_ylabel('Phase (deg)')

    if logx is True and dBy is False:
        axs[0, 0].semilogx(ffreq, 20 * np.abs(abs(mag[out0, in0])))
        axs[0, 1].semilogx(ffreq, 20 * np.abs(abs(mag[out0, in1])))

        axs[1, 0].semilogx(ffreq, 180 / np.pi * (phase[out0, in0]))
        axs[1, 1].semilogx(ffreq, 180 / np.pi * (phase[out0, in1]))

        axs[2, 0].semilogx(ffreq, 20 * np.abs(abs(mag[out1, in0])))
        axs[2, 1].semilogx(ffreq, 20 * np.abs(abs(mag[out1, in1])))

        axs[3, 0].semilogx(ffreq, 180 / np.pi * (phase[out1, in0]))
        axs[3, 1].semilogx(ffreq, 180 / np.pi * (phase[out1, in1]))

        axs[0, 0].set_xlabel('Frequency (Hz)')
        axs[0, 0].set_ylabel('Magnitude ')

        axs[0, 1].set_xlabel('Frequency (Hz)')
        axs[0, 1].set_ylabel('Magnitude ')

        axs[1, 0].set_xlabel('Frequency (Hz)')
        axs[1, 0].set_ylabel('Phase (deg)')

        axs[1, 1].set_xlabel('Frequency (Hz)')
        axs[1, 1].set_ylabel('Phase (deg)')

        axs[2, 0].set_xlabel('Frequency (Hz)')
        axs[2, 0].set_ylabel('Magnitude ')

        axs[2, 1].set_xlabel('Frequency (Hz)')
        axs[2, 1].set_ylabel('Magnitude ')

        axs[3, 0].set_xlabel('Frequency (Hz)')
        axs[3, 0].set_ylabel('Phase (deg)')

        axs[3, 1].set_xlabel('Frequency (Hz)')
        axs[3, 1].set_ylabel('Phase (deg)')

    else:
        axs[0, 0].plot(ffreq, 20 * np.abs(abs(mag[out0, in0])))
        axs[0, 1].plot(ffreq, 20 * np.abs(abs(mag[out0, in1])))

        axs[1, 0].plot(ffreq, 180 / np.pi * (phase[out0, in0]))
        axs[1, 1].plot(ffreq, 180 / np.pi * (phase[out0, in1]))

        axs[2, 0].plot(ffreq, 20 * np.abs(abs(mag[out1, in0])))
        axs[2, 1].plot(ffreq, 20 * np.abs(abs(mag[out1, in1])))

        axs[3, 0].plot(ffreq, 180 / np.pi * (phase[out1, in0]))
        axs[3, 1].plot(ffreq, 180 / np.pi * (phase[out1, in1]))

        axs[0, 0].set_xlabel('Frequency (Hz)')
        axs[0, 0].set_ylabel('Magnitude ')

        axs[0, 1].set_xlabel('Frequency (Hz)')
        axs[0, 1].set_ylabel('Magnitude ')

        axs[1, 0].set_xlabel('Frequency (Hz)')
        axs[1, 0].set_ylabel('Phase (deg)')

        axs[1, 1].set_xlabel('Frequency (Hz)')
        axs[1, 1].set_ylabel('Phase (deg)')

        axs[2, 0].set_xlabel('Frequency (Hz)')
        axs[2, 0].set_ylabel('Magnitude ')

        axs[2, 1].set_xlabel('Frequency (Hz)')
        axs[2, 1].set_ylabel('Magnitude ')

        axs[3, 0].set_xlabel('Frequency (Hz)')
        axs[3, 0].set_ylabel('Phase (deg)')

        axs[3, 1].set_xlabel('Frequency (Hz)')
        axs[3, 1].set_ylabel('Phase (deg)')


    axs[0, 0].set_title('Yqq')
    axs[0, 1].set_title('Yqd')
    axs[2, 0].set_title('Ydq')
    axs[2, 1].set_title('Ydd')

    axs[1, 0].set_ylim([-180, 180])
    axs[1, 1].set_ylim([-180, 180])
    axs[3, 1].set_ylim([-180, 180])
    axs[3, 1].set_ylim([-180, 180])

    plt.show()

    return ()


def eigenval_YZ(ss_class, f_ini=0, f_fin=3, name_in=[], name_out=[], n_p=1000, invert = False, type_plot = 're_im'):
    '''
    Eigenvalues plot of a 2x2 system

    :param ss_class: class with the space state, the inputs and the outputs
    :param lim_ini: log of the initial frequency. For instance, -1 represents 10^(-1) Hz
    :param lim_fin: log of the final frequency. For instance, 4 represents 10^(4) Hz
    :param name_in: name of the 2 inputs
    :param name_out: name of the 2 outputs
    :param n_p: number of points to represent. For instance, 1000
    :param invert: divide in / out instead of out / in
    :param type_plot: string to identify if plot in re/im or mag/phase...
    :return: nothing, it just plots
    '''
    # initial definitions
    n_points = n_p
    wfreq = np.logspace(f_ini, f_fin, num=n_points) * 2 * np.pi
    ffreq = np.logspace(f_ini, f_fin, num=n_points)
    (mag, phase, freq) = ss_class.ssm.freqresp(wfreq)

    # print(ss_class.outputs.index('vqx_0'))
    ii0 = ss_class.inputs.index(name_in[0])
    ii1 = ss_class.inputs.index(name_in[1])
    oo0 = ss_class.outputs.index(name_out[0])
    oo1 = ss_class.outputs.index(name_out[1])

    # extract indices for inputs/outputs
    if invert is False:
        in0 = ii0
        in1 = ii1
        out0 = oo0
        out1 = oo1
    else:
        in0 = oo0
        in1 = oo1
        out0 = ii0
        out1 = ii1


    # for each frequency, 2x2 matrix, diagonalize, generate eigen and plot them
    def calc_eig(mag, phase, in0, in1, out0, out1):
        """
        Calculate the eigenvalues of the 2x2 matrix

        :param mag: matrix of magnitudes
        :param phase: matrix of phases
        :return: matrix of the eigenvalues
        """
        lam0vec = []
        lam1vec = []
        for ll in range(n_points):
            # print(mag[0, 0])
            Yqq = mag[out0, in0][ll] * np.exp(1j * phase[out0, in0][ll])
            Yqd = mag[out0, in1][ll] * np.exp(1j * phase[out0, in1][ll])
            Ydq = mag[out1, in0][ll] * np.exp(1j * phase[out1, in0][ll])
            Ydd = mag[out1, in1][ll] * np.exp(1j * phase[out1, in1][ll])
            meig = np.array([[Yqq, Yqd], [Ydq, Ydd]])

            w, v = np.linalg.eig(meig)
            lam0 = w[0]
            lam1 = w[1]

            lam0vec.append(lam0)
            lam1vec.append(lam1)

        return np.array(lam0vec), np.array(lam1vec)


    lam0vec, lam1vec = calc_eig(mag, phase, in0, in1, out0, out1)

    # plot
    fig, axs = plt.subplots(2, 1)

    if type_plot == 're_im':
        # one plot for real, one for imaginary
        axs[0].plot(ffreq, np.real(lam0vec))
        axs[0].plot(ffreq, np.real(lam1vec))
        axs[0].set_xlabel('Frequency (Hz)')
        axs[0].set_ylabel('Magnitude')
        axs[0].set_title('Real')
        axs[0].legend(['lam1', 'lam2'])
        axs[0].axhline(y=0.0, color='r', linestyle='-')

        axs[1].plot(ffreq, np.imag(lam0vec))
        axs[1].plot(ffreq, np.imag(lam1vec))
        axs[1].set_xlabel('Frequency (Hz)')
        axs[1].set_ylabel('Magnitude')
        axs[1].set_title('Imag')
        axs[1].legend(['lam1', 'lam2'])
        axs[1].axhline(y=0.0, color='r', linestyle='-')

    elif type_plot == 'mag_ph':
        # one plot for magnitude, one for phase
        axs[0].plot(ffreq, np.abs(lam0vec))
        axs[0].plot(ffreq, np.abs(lam1vec))
        axs[0].set_xlabel('Frequency (Hz)')
        axs[0].set_ylabel('Magnitude')
        axs[0].set_title('Mag')
        axs[0].legend(['lam1', 'lam2'])
        # axs[0].axhline(y=0.0, color='r', linestyle='-')

        axs[1].plot(ffreq, np.angle(lam0vec) * 90 / (np.pi / 2))
        axs[1].plot(ffreq, np.angle(lam1vec) * 90 / (np.pi / 2))
        axs[1].set_xlabel('Frequency (Hz)')
        axs[1].set_ylabel('Phase')
        axs[1].set_title('Ph')
        axs[1].legend(['lam1', 'lam2'])
        # axs[1].axhline(y=0.0, color='r', linestyle='-')

    plt.show()

    return ()


def eigen(ss_class, plot=False, prnt=False):
    """
    Graphically show the eigenvalues and print them
    :param ss_class: class from where to extract the ss
    :param plot: if true, plots the eigenvalues map
    :param prnt: if true, prints the eigenvalues
    :return: print eigenvalues
    """

    if prnt is True:
        damp(ss_class.ss)

    if plot is True:
        pp = pole(ss_class.ss)
        pp_re = [ele.real for ele in pp]
        pp_im = [ele.imag for ele in pp]
        plt.scatter(pp_re, pp_im)
        plt.ylabel('Imaginary')
        plt.xlabel('Real')
        plt.show()

    return ()


def nyquist_YZ(ss_class_act, ss_class_psv, f_ini=0, f_fin=3, name_in=[], name_out=[], n_p=1000, n_arrows=10, invert = False):
    '''
    Nyquist plot with the eigenvalues for a 2x2 system, for the active and the passive part

    :param ss_class_act: active class with the space state, the inputs and the outputs
    :param ss_class_psv: passive class with the space state, the inputs and the outputs
    :param lim_ini: log of the initial frequency. For instance, -1 represents 10^(-1) Hz
    :param lim_fin: log of the final frequency. For instance, 4 represents 10^(4) Hz
    :param name_in: name of the 2 inputs
    :param name_out: name of the 2 outputs
    :param n_p: number of points to represent. For instance, 1000
    :param n_arrows: number of arrows indicating the direction
    :param invert: divide in / out instead of out / in
    :return: nothing, it just plots
    '''
    # initial definitions
    n_points = n_p
    wfreq = np.logspace(f_ini, f_fin, num=n_points, base=10.0) * 2 * np.pi
    ffreq = np.logspace(f_ini, f_fin, num=n_points, base=10.0)
    (mag_act, phase_act, freq) = ss_class_act.ssm.freqresp(wfreq)
    (mag_psv, phase_psv, freq) = ss_class_psv.ssm.freqresp(wfreq)

    # print(ss_class.outputs.index('vqx_0'))
    ii0_act = ss_class_act.inputs.index(name_in[0])
    ii1_act = ss_class_act.inputs.index(name_in[1])
    oo0_act = ss_class_act.outputs.index(name_out[0])
    oo1_act = ss_class_act.outputs.index(name_out[1])

    ii0_psv = ss_class_psv.inputs.index(name_out[0])
    ii1_psv = ss_class_psv.inputs.index(name_out[1])
    oo0_psv = ss_class_psv.outputs.index(name_in[0])
    oo1_psv = ss_class_psv.outputs.index(name_in[1])


    # for each frequency, 2x2 matrix, diagonalize, generate eigen and plot them
    def calc_eig(mag_act, phase_act, mag_psv, phase_psv, in0_act, in1_act, out0_act, out1_act, in0_psv, in1_psv, out0_psv, out1_psv):
        """
        Calculate the eigenvalues of the 2x2 matrix

        :param mag: matrix of magnitudes
        :param phase: matrix of phases
        :return: matrix of the eigenvalues
        """
        lam0vec = []
        lam1vec = []
        lam0_sub2 = 0
        lam0_sub1 = 0
        lam1_sub2 = 0  # 2 previous lambda
        lam1_sub1 = 0  # previous lambda
        for ll in range(n_points):
            # print(mag[0, 0])
            Yqq = mag_act[out0_act, in0_act][ll] * np.exp(1j * phase_act[out0_act, in0_act][ll])
            Yqd = mag_act[out0_act, in1_act][ll] * np.exp(1j * phase_act[out0_act, in1_act][ll])
            Ydq = mag_act[out1_act, in0_act][ll] * np.exp(1j * phase_act[out1_act, in0_act][ll])
            Ydd = mag_act[out1_act, in1_act][ll] * np.exp(1j * phase_act[out1_act, in1_act][ll])

            Zqq = mag_psv[out0_psv, in0_psv][ll] * np.exp(1j * phase_psv[out0_psv, in0_psv][ll])
            Zqd = mag_psv[out0_psv, in1_psv][ll] * np.exp(1j * phase_psv[out0_psv, in1_psv][ll])
            Zdq = mag_psv[out1_psv, in0_psv][ll] * np.exp(1j * phase_psv[out1_psv, in0_psv][ll])
            Zdd = mag_psv[out1_psv, in1_psv][ll] * np.exp(1j * phase_psv[out1_psv, in1_psv][ll])

            mY = np.array([[Yqq, Yqd], [Ydq, Ydd]])
            mZ = np.array([[Zqq, Zqd], [Zdq, Zdd]])
            # mMat = np.multiply(mZ, mY)
            # mMat = mZ@mY
            mMat = np.dot(mZ,mY)

            # print(mZ)
            # print(mY)
            # print(mMat)

            w, v = np.linalg.eig(mMat)
            lam0 = w[0]
            lam1 = w[1]

            tol = 0.01
            tol_ang = np.pi / 100  # for instance, 30 degrees
            factt = 2

            if ll > 1:
                ang0_prev = (np.imag(lam0_sub1) - np.imag(lam0_sub2)) / (np.real(lam0_sub1) - np.real(lam0_sub2))
                ang1_prev = (np.imag(lam1_sub1) - np.imag(lam1_sub2)) / (np.real(lam1_sub1) - np.real(lam1_sub2))
                ang0 = (np.imag(lam0) - np.imag(lam0_sub1)) / (np.real(lam0) - np.real(lam0_sub1))
                ang1 = (np.imag(lam1) - np.imag(lam1_sub1)) / (np.real(lam1) - np.real(lam1_sub1))

                Ax0_prev = np.real(lam0_sub1) - np.real(lam0_sub2)
                Ay0_prev = np.imag(lam0_sub1) - np.imag(lam0_sub2)

                Ax1_prev = np.real(lam1_sub1) - np.real(lam1_sub2)
                Ay1_prev = np.imag(lam1_sub1) - np.imag(lam1_sub2)

                Ax0 = np.real(lam0) - np.real(lam0_sub1)
                Ay0 = np.imag(lam0) - np.imag(lam0_sub1)

                Ax1 = np.real(lam1) - np.real(lam1_sub1)
                Ay1 = np.imag(lam1) - np.imag(lam1_sub1)

                ang0_prev = Ay0_prev / Ax0_prev
                ang1_prev = Ay1_prev / Ax1_prev

                ang0 = np.arctan(Ay0 / Ax0)
                ang1 = np.arctan(Ay1 / Ax1)

                abs0 = abs(lam0)
                abs1 = abs(lam1)
                abs0_prev = abs(lam0_sub1)
                abs1_prev = abs(lam1_sub1)

                condition = abs(abs0 - abs0_prev) > tol and abs(abs1 - abs1_prev) > tol

                if abs(abs0 - abs0_prev) + tol > abs(abs0 - abs1_prev):
                    # print(condition)
                    lam_aux0 = lam0
                    lam0 = lam1
                    lam1 = lam_aux0
                else:
                    pass

            # update previous
            lam0_sub2 = lam0_sub1
            lam0_sub1 = lam0

            lam1_sub2 = lam1_sub1
            lam1_sub1 = lam1

            lam0vec.append(lam0)
            lam1vec.append(lam1)

        return np.real(np.array(lam0vec)), np.imag(np.array(lam0vec)), np.real(np.array(lam1vec)), np.imag(np.array(lam1vec))


    lam0_re, lam0_im ,lam1_re, lam1_im = calc_eig(mag_act, phase_act, mag_psv, phase_psv, ii0_act, ii1_act, oo0_act, oo1_act, ii0_psv, ii1_psv, oo0_psv, oo1_psv)

    plt.plot(lam0_re, lam0_im)
    plt.plot(lam1_re, lam1_im)

    u0 = np.diff(lam0_re)
    v0 = np.diff(lam0_im)
    pos_x0 = lam0_re[:-1] + u0 / 2
    pos_y0 = lam0_im[:-1] + v0 / 2
    norm0 = np.sqrt(u0 ** 2 + v0 ** 2)
    stp = int(n_points / n_arrows)
    indx_med = int(len(lam0_re) / 1.5)
    plt.quiver(pos_x0[indx_med], pos_y0[indx_med], u0[indx_med] / norm0[indx_med], v0[indx_med] / norm0[indx_med], angles="xy", zorder=5, pivot="mid", linewidth=0.1, width=0.01, headwidth=2, headlength=4, headaxislength=4, minlength=0.5, color='blue')

    u1 = np.diff(lam1_re)
    v1 = np.diff(lam1_im)
    pos_x1 = lam1_re[:-1] + u1 / 2
    pos_y1 = lam1_im[:-1] + v1 / 2
    norm1 = np.sqrt(u1 ** 2 + v1 ** 2)
    stp = int(n_points / n_arrows)
    indx_med = int(len(lam0_re) / 1.5)
    plt.quiver(pos_x1[indx_med], pos_y1[indx_med], u1[indx_med] / norm1[indx_med], v1[indx_med] / norm1[indx_med], angles="xy", zorder=5, pivot="mid", linewidth=0.1, width=0.01, headwidth=2, headlength=4, headaxislength=4, minlength=0.5, color='orange')

    plt.scatter(x=-1, y=0, c='r')

    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.legend(['lam1', 'lam2'])

    plt.show()

    return ()


def merge_all_minus1(excel_file, syst, side1_type, side1_index):
    """
    Merges all elements except 1 device

    :param excel_file: path to the excel file to reread external inputs and outputs
    :param syst: full class with all information built
    :param side1_type: type of the element to exclude (for instance, VSC)
    :param side1_index: index of the element to exclude
    :return: nothing, focus on Nyquist plot
    """

    xlsx = pd.ExcelFile(excel_file)
    df_ext_inputs = pd.read_excel(xlsx, 'External_inputs')
    df_ext_outputs = pd.read_excel(xlsx, 'External_outputs')

    # remove the disconnected element
    past_VSCs = syst.VSCs
    past_SGs = syst.SGs
    extra_outputs = []

    if side1_type == 'VSC':
        extra_outputs = syst.VSCs[side1_index].outputs
        VSCs_out = syst.VSCs.pop(side1_index)
    elif side1_type == 'SG':
        extra_outputs = syst.SGs[side1_index].ext_outputs
        SGs_out = syst.SGs.pop(side1_index)

    # merge the side 2 system
    full_inputs, full_outputs, full_states, syst.Xdivs = auxiliaries.adapt_all_names(syst.RLs, syst.Cs, syst.VSCs, syst.SGs, syst.ISum)


    # all_classes2 = [syst.RLs, syst.Cs, VSCs_mod, SGs_mod, syst.ISum, syst.Xdivs]
    all_classes2 = [syst.RLs, syst.Cs, syst.VSCs, syst.SGs, syst.ISum, syst.Xdivs]
    ext_inputs, ext_outputs = auxiliaries.exterior_ins_outs(df_ext_inputs, df_ext_outputs, [])  # pass [] because no additional inputs/outputs

    # add the outputs of the removed component as external inputs to the side2 system
    ext_inputs += extra_outputs

    # prepare the connect of the side2 system
    ss_complete = auxiliaries.append_ss(all_classes2)
    dic_inputs, dic_outputs, dic_states = auxiliaries.dics_in_out_sts(full_inputs, full_outputs, full_states)
    Qq, list_indx_x, list_indx_in, list_indx_out, list_name_x, list_name_in, list_name_out = auxiliaries.Qvec_builder_full(ext_inputs, ext_outputs, dic_inputs, dic_outputs, dic_states)

    # final connect
    ss_side2 = connect(ss_complete, Qq, list_indx_in, list_indx_out)


    class Ss_side2:
        def __init__(self, ss_side2, inputs, outputs):
            self.ssm = ss_side2
            self.ss = ss_side2
            self.inputs = inputs
            self.outputs = outputs

    side2 = Ss_side2(ss_side2, list_name_in, list_name_out)


    return side2


