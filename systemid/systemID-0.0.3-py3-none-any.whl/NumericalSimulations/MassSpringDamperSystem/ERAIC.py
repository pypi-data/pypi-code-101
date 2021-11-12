"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np
import random
from scipy import linalg as LA
from numpy.linalg import matrix_power
from scipy import signal
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

plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
rc('text', usetex=True)


from ClassesDynamics.ClassMassSpringDamperDynamics import MassSpringDamperDynamics
from ClassesGeneral.ClassSystem import DiscreteLinearSystem
from SystemIDAlgorithms.IdentificationInitialCondition import identificationInitialCondition
from ClassesSystemID.ClassMarkovParameters import OKIDObserver, OKIDObserverWithInitialCondition
from ClassesGeneral.ClassSignal import DiscreteSignal, OutputSignal, subtract2Signals, addSignals
from ClassesSystemID.ClassERA import ERA, ERADC, ERAFromInitialConditionResponse, ERADCFromInitialConditionResponse
from SystemIDAlgorithms.GetObserverGainMatrix import getObserverGainMatrix
from ClassesGeneral.ClassExperiments import Experiments
from Plotting.PlotSignals import plotSignals
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassMarkovParameters import TVOKIDObserver
from ClassesSystemID.ClassERA import TVERA
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck
# from SystemIDAlgorithms.Prediction import prediction



## Dynamics
dt = 0.1
mass = 1
spring_constant = 1
damping_coefficient = 0.2
dynamics = MassSpringDamperDynamics(dt, mass, spring_constant, damping_coefficient, [''], ['position', 'velocity'])


## Initial Condition
x0 = np.array([0.1, -0.2])


## Frequency and total time
frequency = 10
total_time = 50
total_time_training = 30
number_steps = round(total_time * frequency + 1)
number_steps_training = round(total_time_training * frequency + 1)
tspan = np.linspace(0, total_time, number_steps)
tspan_training = np.linspace(0, total_time_training, number_steps_training)


## System
# nominal_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(x0, 0)], 'Nominal System', lambda t: dynamics.A(0), lambda t: dynamics.B(0), lambda t: dynamics.C(0), lambda t: dynamics.D(0))
nominal_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(x0, 0)], 'Nominal System', dynamics.A, dynamics.B, dynamics.C, dynamics.D)
zero = DiscreteSignal(dynamics.input_dimension, total_time, frequency)
true_output_signal = OutputSignal(zero, nominal_system)


## Noise
sigma = 0.1
noise = DiscreteSignal(dynamics.input_dimension, total_time, frequency, signal_shape='White Noise', covariance=np.array([[sigma**2]]))


## Input Signals
number_experiments = 10
input_signals = []
systems = []
for i in range(number_experiments):
    input_signals.append(zero)
    systems.append(DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.random.randn(dynamics.state_dimension), 0)], 'Nominal System', dynamics.A, dynamics.B, dynamics.C, dynamics.D))
experiments = Experiments(systems, input_signals, measurement_noise=True, measurement_noise_signal=noise, process_noise=True, process_noise_signal=noise)



## Parameters for identification
assumed_order = 2
p = 20
q = p
deadbeat_order = 4
number_system_markov_parameters = 500


## ERA
era = ERAFromInitialConditionResponse(experiments.output_signals, true_output_signal, assumed_order, dynamics.input_dimension)
eradc = ERADCFromInitialConditionResponse(experiments.output_signals, true_output_signal, assumed_order, dynamics.input_dimension, p=p, tau=8)


## Identified System
identified_system_era = DiscreteLinearSystem(frequency, assumed_order, dynamics.input_dimension, dynamics.output_dimension, [(era.x0, 0)], 'Nominal System', era.A, era.B, era.C, era.D)
identified_system_eradc = DiscreteLinearSystem(frequency, assumed_order, dynamics.input_dimension, dynamics.output_dimension, [(eradc.x0, 0)], 'Nominal System', eradc.A, eradc.B, eradc.C, eradc.D)


## Identified Signals
output_signal_identified_era = OutputSignal(zero, identified_system_era)
output_signal_identified_eradc = OutputSignal(zero, identified_system_eradc)



## Plotting

## Plot input and output Training
fig = plt.figure(num=1, figsize=[12, 3])
ax = fig.add_subplot(1, 2, 1)
ax.plot(tspan, true_output_signal.data[0, :], color=colors[1])
plt.xlabel('Time [sec]')
plt.ylabel('Position')
plt.title('Testing')
ax = fig.add_subplot(1, 2, 2)
ax.plot(tspan, true_output_signal.data[1, :], color=colors[1])
plt.xlabel('Time [sec]')
plt.ylabel('Velocity')
plt.title('Testing')
plt.show()


# Plot SVD
plt.figure(num=2, figsize=[4, 4])
plt.semilogy(np.linspace(1, np.min((p * dynamics.output_dimension, q * dynamics.input_dimension)), np.min((p * dynamics.output_dimension, q * dynamics.input_dimension))), np.diag(era.Sigma)[0:np.min((p * dynamics.output_dimension, q * dynamics.input_dimension))], '.', color=colors[7], label='ERA')
plt.semilogy(np.linspace(1, np.min((p * dynamics.output_dimension, q * dynamics.input_dimension)), np.min((p * dynamics.output_dimension, q * dynamics.input_dimension))), np.diag(eradc.Sigma)[0:np.min((p * dynamics.output_dimension, q * dynamics.input_dimension))], '.', color=colors[8], label='ERADC')
plt.xlabel('Number of singular values')
plt.ylabel('Magnitude of singular values')
plt.legend(loc='best')
plt.show()


# Check Eigenvalues
plt.figure(num=3, figsize=[4, 4])
plt.scatter(np.real(LA.eig(dynamics.A(0))[0]), np.imag(LA.eig(dynamics.A(0))[0]), color=colors[1], label='True')
plt.scatter(np.real(LA.eig(era.A(0))[0]), np.imag(LA.eig(era.A(0))[0]), color=colors[4], facecolors='none', label='ERA')
plt.scatter(np.real(LA.eig(eradc.A(0))[0]), np.imag(LA.eig(eradc.A(0))[0]), color=colors[5], facecolors='none', label='ERADC')
plt.legend(loc='best')
plt.xlabel('Real part of eigenvalues')
plt.ylabel('Imaginary part of eigenvalues')
plt.show()


# Plot input and output Training
fig = plt.figure(num=4, figsize=[12, 6])

ax = fig.add_subplot(2, 2, 1)
ax.plot(tspan, true_output_signal.data[0, :], color=colors[1], label='True')
ax.plot(tspan, output_signal_identified_era.data[0, :], color=colors[4], linestyle='-.', label='ERA')
ax.plot(tspan, output_signal_identified_eradc.data[0, :], color=colors[5], linestyle='-.', label='ERADC')
plt.ylabel('Position')
plt.legend(loc='best')
ax = fig.add_subplot(2, 2, 2)
ax.plot(tspan, true_output_signal.data[1, :], color=colors[1], label='True')
ax.plot(tspan, output_signal_identified_era.data[1, :], color=colors[4], linestyle='-.', label='ERA')
ax.plot(tspan, output_signal_identified_eradc.data[1, :], color=colors[5], linestyle='-.', label='ERADC')
plt.ylabel('Velocity')
plt.legend(loc='best')
ax = fig.add_subplot(2, 2, 3)
ax.plot(tspan, true_output_signal.data[0, :] - output_signal_identified_era.data[0, :], color=colors[7], label='ERA')
ax.plot(tspan, true_output_signal.data[0, :] - output_signal_identified_eradc.data[0, :], color=colors[8], label='ERADC')
plt.ylabel('Error Position')
plt.legend(loc='best')
ax = fig.add_subplot(2, 2, 4)
ax.plot(tspan, true_output_signal.data[1, :] - output_signal_identified_era.data[1, :], color=colors[7], label='ERA')
ax.plot(tspan, true_output_signal.data[1, :] - output_signal_identified_eradc.data[1, :], color=colors[8], label='ERADC')
plt.ylabel('Error Velocity')
plt.legend(loc='best')
plt.xlabel('Time [sec]')

plt.show()



























