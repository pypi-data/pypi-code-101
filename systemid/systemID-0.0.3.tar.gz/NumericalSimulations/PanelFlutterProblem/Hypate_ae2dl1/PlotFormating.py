"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


colors = [(11/255, 36/255, 251/255),
          (27/255, 161/255, 252/255),
          (77/255, 254/255, 193/255),
          (224/255, 253/255, 63/255),
          (253/255, 127/255, 35/255),
          (221/255, 10/255, 22/255),
          (255/255, 0/255, 127/255),
          (127/255, 0/255, 255/255),
          (255/255, 0/255, 255/255),
          (145/255, 145/255, 145/255),
          (0, 0, 0)]



def plotModeShapes(true_output_signals, identified_output_signals, time_steps, perturbP, num):

    number_signals = len(true_output_signals)
    number_time_steps = len(time_steps)

    plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
    rc('text', usetex=True)

    plt.figure(num=num, figsize=[3 * number_signals, 2 * number_time_steps])

    for i in range(number_signals):
        for j in range(number_time_steps):
            plt.subplot(number_time_steps, number_signals, 1 + j * number_signals + i)
            plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signals[i].data[:, time_steps[j]], color=colors[0])
            plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signals[i].data[:, time_steps[j]], color=colors[5], linestyle='--')
            if j == number_time_steps-1:
                plt.xlabel('$x$ [m]')
            if j == 0:
                plt.title(r"\textbf{perturbP = " + str(perturbP[i]) + ' [Pa]}\n {}')
            plt.legend(['True', 'ID'])
            if i == 0:
                if j == number_time_steps-1:
                    plt.ylabel(r"\textbf{Time = " + str((time_steps[j] + 1) / 1000) + ' [sec]}\n \n Displacement')
                else:
                    plt.ylabel(r"\textbf{Time = " + str(time_steps[j] / 1000) + ' [sec]}\n \n Displacement')

    plt.tight_layout()

    plt.savefig(str(num) + '.eps', format='eps')
    plt.show()


def plotMidPoint(true_output_signals, identified_output_signals, mid_point, tspan, perturbP, num):

    plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
    rc('text', usetex=True)

    number_signals = len(true_output_signals)

    plt.figure(num=num, figsize=[20, 2 * number_signals])

    for i in range(number_signals):
        plt.subplot(number_signals, 2, 1 + i * 2)
        plt.plot(tspan, true_output_signals[i].data[mid_point, 0:2000], color=colors[0])
        plt.plot(tspan, identified_output_signals[i].data[mid_point, 0:2000], color=colors[5], linestyle='--')
        if i == 0:
            plt.title(r"\textbf{Mid-point displacement}")
        if i == number_signals - 1:
            plt.xlabel('Time [sec]')
        plt.ylabel(r"\textbf{perturbP = " + str(perturbP[i]) + ' [Pa]}\n \n Displacement')
        plt.legend(['True', 'ID'], loc='lower right')
        plt.subplot(number_signals, 2, 2 + i * 2)
        plt.plot(tspan, true_output_signals[i].data[mid_point, 0:2000] - identified_output_signals[i].data[mid_point, 0:2000], color=colors[7])
        if i == 0:
            plt.title(r"\textbf{Error}")
        if i == number_signals - 1:
            plt.xlabel('Time [sec]')
        plt.ylabel('Error')

    plt.tight_layout()

    plt.savefig(str(num) + '.eps', format='eps')
    plt.show()


def plotSVD(sigma, time_steps, num):

    plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
    rc('text', usetex=True)

    number_time_steps = len(time_steps)
    legend = []

    plt.figure(num=num, figsize=[7, 5])

    for i in range(number_time_steps):
        plt.semilogy(np.linspace(1, len(sigma[time_steps[i]]), len(sigma[time_steps[i]])), sigma[time_steps[i]], '*', color=colors[i])
        plt.xlabel('\# Singular Values')
        plt.ylabel('Magnitude')
        if i == number_time_steps - 1:
            legend.append('Time = ' + str((time_steps[i] + 1) / 1000) + ' [sec]')
        else:
            legend.append('Time = ' + str((time_steps[i]) / 1000) + ' [sec]')
        plt.title(r"\textbf{Singular Value Decomposition}")
    plt.legend(legend, loc='lower left', ncol=2)

    plt.tight_layout()

    plt.savefig(str(num) + '.eps', format='eps')

    plt.show()


def plotSurface(X, Y, Z, time_steps, num):

    plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
    rc('text', usetex=True)

    number_time_steps = len(time_steps)


    for i in range(number_time_steps):
        fig = plt.figure(num=num+i, figsize=[4, 3])
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z[:, :, i], rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        if i == number_time_steps - 1:
            plt.title('Time = ' + str((time_steps[i] + 1) / 1000) + ' [sec]')
        else:
            plt.title('Time = ' + str((time_steps[i]) / 1000) + ' [sec]')

        plt.tight_layout()

        plt.savefig('Shape' + str(num+i) + '.eps', format='eps')

        plt.show()
