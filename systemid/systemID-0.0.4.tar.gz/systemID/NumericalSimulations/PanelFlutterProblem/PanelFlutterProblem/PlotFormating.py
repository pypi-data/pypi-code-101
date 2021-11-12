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
import numpy.linalg as LA


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



def plotResponse3(signals, errors, tspan, last_time_step, ylabel, num):

    plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
    rc('text', usetex=True)

    fig = plt.figure(num=num, figsize=[12, 12])
    gs = fig.add_gridspec(8, 2)

    for i in range(4):
        ax = fig.add_subplot(gs[2*i:2*i+2, 0])
        ax.plot(tspan[0:last_time_step], signals[0].data[i, 0:last_time_step], color=colors[0])
        ax.plot(tspan[0:last_time_step], signals[1].data[i, 0:last_time_step], color=colors[5], linestyle='--')
        ax.plot(tspan[0:last_time_step], signals[2].data[i, 0:last_time_step], color=colors[7], linestyle='-.')
        plt.xlabel('Time [sec]')
        plt.ylabel(ylabel[i])
        plt.legend(['True', 'ID', 'Linearization'])

        ax = fig.add_subplot(gs[2*i:2*i+1, 1])
        ax.plot(tspan[0:last_time_step], errors[0].data[i, 0:last_time_step], color=colors[6], linestyle='--')
        plt.xlabel('Time [sec]')
        plt.ylabel('Error in ' + ylabel[i])
        plt.legend(['Error ID'])

        ax = fig.add_subplot(gs[2*i+1:2*i+2, 1])
        ax.plot(tspan[0:last_time_step], errors[1].data[i, 0:last_time_step], color=colors[8], linestyle='-.')
        plt.xlabel('Time [sec]')
        plt.ylabel('Error in ' + ylabel[i])
        plt.legend(['Error linearization'])

    plt.tight_layout()

    plt.savefig('Propagation.eps', format='eps')
    plt.show()


def plotEigenValues(systems, number_steps, num):

    plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
    rc('text', usetex=True)

    state_dimension = systems[0].state_dimension
    dt = systems[0].dt

    eig1 = np.zeros([number_steps, state_dimension])
    eig2 = np.zeros([number_steps, state_dimension])

    total_time = (number_steps - 1) * dt

    fig = plt.figure(num=num, figsize=[16, 8])

    time = np.linspace(0, total_time, number_steps)

    for i in range(number_steps):
        eig1[i, :] = np.real(LA.eig(systems[0].A(i * dt))[0])
        eig2[i, :] = np.real(LA.eig(systems[1].A(i * dt))[0])

    eig1.sort(axis=1)
    eig2.sort(axis=1)

    for i in range(state_dimension):
        plt.subplot(state_dimension, 2, 2 * i + 1)
        plt.plot(time, np.transpose(eig1[:, i]), '*', color=colors[5])
        plt.plot(time, np.transpose(eig2[:, i]), '.', color=colors[7])
        plt.xlabel('Time [sec]')
        if i == 0:
            plt.ylabel('Magnitude \n1st eigenvalue')
        if i == 1:
            plt.ylabel('Magnitude \n2nd eigenvalue')
        if i == 2:
            plt.ylabel('Magnitude \n3rd eigenvalue')
        if i == 3:
            plt.ylabel('Magnitude \n4th eigenvalue')
        plt.legend(['ID', 'Linearization'])

    for i in range(state_dimension):
        plt.subplot(state_dimension, 2, 2 * i + 2)
        plt.plot(time, np.transpose(eig1[:, i]) - np.transpose(eig2[:, i]), color=colors[1])
        plt.xlabel('Time [sec]')
        plt.ylabel('Error in magnitude')

    plt.tight_layout()

    plt.savefig('Eigenvalues.eps', format='eps')

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
            legend.append('Time = ' + str((time_steps[i] + 10) / 50) + ' [sec]')
        else:
            legend.append('Time = ' + str((time_steps[i]) / 50) + ' [sec]')
        plt.title(r"\textbf{Singular Value Decomposition}")
    plt.legend(legend, loc='lower left')

    plt.tight_layout()

    plt.savefig('SVDPlot_Panel.eps', format='eps')

    plt.show()



