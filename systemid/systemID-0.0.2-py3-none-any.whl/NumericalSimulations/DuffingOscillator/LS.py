"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np
from scipy import linalg as LA
import matplotlib.pyplot as plt

from ClassesDynamics.ClassDuffingOscillatorDynamics import DuffingOscillatorDynamics
from SystemIDAlgorithms.DepartureDynamics import departureDynamics
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, add2Signals, subtract2Signals
from Plotting.PlotSignals import plotSignals
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassMarkovParameters import TVOKIDObserver
from ClassesSystemID.ClassERA import TVERA
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck

from SystemIDAlgorithms.ZZZTimeVaryingObserverKalmanIdentificationAlgorithmObserver import timeVaryingObserverKalmanIdentificationAlgorithmObserver


# Parameters for Dynamics
delta = 0.2
alpha = -1
beta = 1


# Import Dynamics
dynamics = DuffingOscillatorDynamics(delta, alpha, beta)


# Parameters for identification
total_time = 100
frequency = 100
number_steps = int(total_time * frequency) + 1


# Create System
initial_states = [(np.array([0.1, 0.1]), 0)]
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)


# tspan
tspan = np.linspace(0, total_time, number_steps)


# Nominal Input Signal
gamma = 0.3
f = 1.1 / (2*np.pi)
phi = 1
nominal_input_signal = ContinuousSignal(dynamics.input_dimension, 'Nominal Input Signal', signal_shape='Sinusoid', magnitude_sinusoid=gamma, frequency_sinusoid=f, phase_sinusoid=phi)


# Nominal Output Signal
nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal', tspan=tspan)


plt.plot(nominal_output_signal.data[0, :], nominal_output_signal.data[1, :])
plt.show()


# Generate acceleration and create D
D_1 = np.zeros([number_steps, 3])
y = np.zeros(number_steps)
u = np.zeros(number_steps)
for i in range(number_steps):
    y[i] = - delta * nominal_output_signal.data[1, i] - beta * nominal_output_signal.data[0, i] - alpha * nominal_output_signal.data[0, i] ** 3 + nominal_output_signal.data[0, i]
    D_1[i, 0] = - nominal_output_signal.data[1, i]
    D_1[i, 1] = - nominal_output_signal.data[0, i]
    D_1[i, 2] = - nominal_output_signal.data[0, i] ** 3
    u[i] = nominal_output_signal.data[0, i]


# Solve for theta
theta_1 = np.dot(LA.pinv(D_1), y-u)


# Generate polynomials dictionnary
D_polynomial = np.zeros([number_steps, 10])
for i in range(number_steps):
    D_polynomial[i, 0] = nominal_output_signal.data[0, i] ** 2
    D_polynomial[i, 1] = nominal_output_signal.data[0, i] ** 4
    D_polynomial[i, 2] = nominal_output_signal.data[0, i] ** 5
    D_polynomial[i, 3] = nominal_output_signal.data[0, i] ** 6
    D_polynomial[i, 4] = nominal_output_signal.data[0, i] ** 7
    D_polynomial[i, 5] = nominal_output_signal.data[0, i] ** 8
    D_polynomial[i, 6] = nominal_output_signal.data[0, i] ** 9
    D_polynomial[i, 7] = nominal_output_signal.data[0, i] ** 10
    D_polynomial[i, 8] = nominal_output_signal.data[0, i] ** 11
    D_polynomial[i, 9] = nominal_output_signal.data[0, i] ** 12
D_2 = np.concatenate((D_1, D_polynomial), axis=1)


#Solve for theta
theta_2 = np.dot(LA.pinv(D_2), y-u)


# Generate sinusoidal dictionnary
D_sinusoidal = np.zeros([number_steps, 12])
for i in range(number_steps):
    D_sinusoidal[i, 0] = np.sin(nominal_output_signal.data[0, i])
    D_sinusoidal[i, 1] = np.sin(2 * nominal_output_signal.data[0, i])
    D_sinusoidal[i, 2] = np.sin(3 * nominal_output_signal.data[0, i])
    D_sinusoidal[i, 3] = np.sin(4 * nominal_output_signal.data[0, i])
    D_sinusoidal[i, 4] = np.sin(5 * nominal_output_signal.data[0, i])
    D_sinusoidal[i, 5] = np.sin(6 * nominal_output_signal.data[0, i])
    D_sinusoidal[i, 6] = np.sin(7 * nominal_output_signal.data[0, i])
    D_sinusoidal[i, 7] = np.sin(8 * nominal_output_signal.data[0, i])
    D_sinusoidal[i, 8] = np.sin(9 * nominal_output_signal.data[0, i])
    D_sinusoidal[i, 9] = np.sin(10 * nominal_output_signal.data[0, i])
    D_sinusoidal[i, 10] = np.sin(11 * nominal_output_signal.data[0, i])
    D_sinusoidal[i, 11] = np.sin(12 * nominal_output_signal.data[0, i])
D_3 = np.concatenate((D_1[:, 0:1], D_sinusoidal), axis=1)


#Solve for theta
theta_3 = np.dot(LA.pinv(D_3), y-u)


