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


from ClassesDynamics.ClassTwoMassSpringDamperDynamics import TwoMassSpringDamperDynamics
from ClassesGeneral.ClassSystem import DiscreteLinearSystem
from SystemIDAlgorithms.IdentificationInitialCondition import identificationInitialCondition
from ClassesSystemID.ClassMarkovParameters import OKIDWithObserver, FrequencyResponseFunction
from ClassesGeneral.ClassSignal import DiscreteSignal, OutputSignal, subtract2Signals, addSignals
from ClassesSystemID.ClassERA import ERA, ERADC, ERAFromInitialConditionResponse, ERADCFromInitialConditionResponse
from SystemIDAlgorithms.GetObserverGainMatrix import getObserverGainMatrix
from ClassesGeneral.ClassExperiments import Experiments
from Plotting.PlotSignals import plotSignals
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassERA import TVERA
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck
# from SystemIDAlgorithms.Prediction import prediction
from SystemIDAlgorithms.WeightingSequenceDescription import weightingSequenceDescription
from SystemIDAlgorithms.CalculateNaturalFrequenciesAndDampingRatios import calculateNaturalFrequenciesAndDampingRatios
from SystemIDAlgorithms.GetMarkovParameters import getMarkovParameters


## Dynamics
dt = 0.1
mass = 1
spring_constant = 1
damping_coefficient = 5
dynamics = TwoMassSpringDamperDynamics(dt, mass, mass, spring_constant, spring_constant, damping_coefficient, damping_coefficient, ['mass1', 'mass2'], ['position', 'velocity'], ['position', 'velocity'])


## Initial Condition
x0 = np.zeros(dynamics.state_dimension)
# x0 = np.random.randn(dynamics.state_dimension)
# x0 = np.array([0.1, 0.2, 0.3, 0.4])


## Frequency and total time
frequency = 10
total_time = 1500
total_time_training = 100
number_steps = round(total_time * frequency + 1)
number_steps_training = round(total_time_training * frequency + 1)
tspan = np.linspace(0, total_time, number_steps)
tspan_training = np.linspace(0, total_time_training, number_steps_training)


## System
nominal_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(x0, 0)], 'Nominal System', lambda t: dynamics.A(0), lambda t: dynamics.B(0), lambda t: dynamics.C(0), lambda t: dynamics.D(0))
# nominal_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(x0, 0)], 'Nominal System', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


## Input Signals
gaussian_input_signal = DiscreteSignal(dynamics.input_dimension, total_time, frequency, signal_shape='White Noise', covariance=np.eye(dynamics.input_dimension))
# square_wave_input_signal = DiscreteSignal(dynamics.input_dimension, total_time, frequency, signal_shape='External', data=signal.square(2 * np.pi * 5 * tspan))
# cosine_wave_input_signal = DiscreteSignal(dynamics.input_dimension, total_time, frequency, signal_shape='External', data=np.cos(2 * np.pi * 2 * tspan))


## Noise
sigma = 0.001
noise = DiscreteSignal(dynamics.output_dimension, total_time, frequency, signal_shape='White Noise', covariance=sigma * np.eye(dynamics.output_dimension))


## Output Signals
gaussian_output_signal = OutputSignal(gaussian_input_signal, nominal_system, measurement_noise=False, measurement_noise_signal=noise, process_noise=False, process_noise_signal=noise)
# square_wave_output_signal = OutputSignal(square_wave_input_signal, nominal_system)
# cosine_wave_output_signal = OutputSignal(cosine_wave_input_signal, nominal_system)



## Parameters for identification
assumed_order = 4
p = 200
q = p
deadbeat_order = 4
number_system_markov_parameters = 500




## Input Signal for training
gaussian_input_signal_training = DiscreteSignal(dynamics.input_dimension, total_time_training, frequency, signal_shape='External', data=gaussian_input_signal.data[:, 0:number_steps_training])

gaussian_input_signal_training1 = DiscreteSignal(dynamics.input_dimension, 100, frequency, signal_shape='External', data=gaussian_input_signal.data[:, 0:1000])
gaussian_input_signal_training2 = DiscreteSignal(dynamics.input_dimension, 100, frequency, signal_shape='External', data=gaussian_input_signal.data[:, 100:1100])
gaussian_input_signal_training3 = DiscreteSignal(dynamics.input_dimension, 100, frequency, signal_shape='External', data=gaussian_input_signal.data[:, 200:1200])


## Output Signal for training
gaussian_output_signal_training = DiscreteSignal(dynamics.output_dimension, total_time_training, frequency, signal_shape='External', data=gaussian_output_signal.data[:, 0:number_steps_training])


## OKID
stable_order = 0
okid = OKIDWithObserver(gaussian_input_signal_training, gaussian_output_signal_training, observer_order=deadbeat_order, stable_order=stable_order, number_of_parameters=800)
FRF = FrequencyResponseFunction(Experiments([nominal_system, nominal_system, nominal_system], [gaussian_input_signal_training1, gaussian_input_signal_training2, gaussian_input_signal_training3]))
# okid2 = OKID(gaussian_input_signal_training, gaussian_output_signal_training, stable_order=stable_order, number_of_parameters=600)
# okid = OKIDObserverWithInitialCondition(gaussian_input_signal_training, gaussian_output_signal_training, deadbeat_order, number_system_markov_parameters)

mp = getMarkovParameters(dynamics.A, dynamics.B, dynamics.C, dynamics.D, 1000)


print(LA.norm(gaussian_output_signal_training.data[:, stable_order:] - weightingSequenceDescription(gaussian_input_signal_training, okid.markov_parameters, observer=False, stable_order=stable_order).data[:, stable_order:]))
print(LA.norm(gaussian_output_signal_training.data[:, stable_order:] - weightingSequenceDescription(gaussian_input_signal_training, FRF.markov_parameters1, observer=False, stable_order=stable_order).data[:, stable_order:]))
# print(LA.norm(gaussian_output_signal_training.data[:, stable_order:] - weightingSequenceDescription(gaussian_input_signal_training, okid2.markov_parameters, observer=False, stable_order=stable_order).data[:, stable_order:]))
# print(LA.norm(gaussian_output_signal_training.data[:, stable_order:] - weightingSequenceDescription(gaussian_input_signal_training, mp, observer=False, stable_order=stable_order).data[:, stable_order:]))
print(LA.norm(gaussian_output_signal_training.data[:, stable_order:] - weightingSequenceDescription(gaussian_input_signal_training, okid.observer_markov_parameters, observer=True, stable_order=stable_order, reference_output_signal=gaussian_output_signal_training).data[:, stable_order:]))



# print(LA.norm(gaussian_output_signal_training.data[:, stable_order:] - weightingSequenceDescription(gaussian_input_signal_training, okid2.markov_parameters, observer=False, stable_order=stable_order).data[:, stable_order:]))
plt.plot(gaussian_output_signal_training.data[0, stable_order:])
plt.plot(weightingSequenceDescription(gaussian_input_signal_training, okid.observer_markov_parameters, observer=True, stable_order=stable_order, reference_output_signal=gaussian_output_signal_training).data[0, stable_order:])
plt.show()


## ERA
era = ERA(okid.markov_parameters, assumed_order, p=p)
eradc = ERADC(okid.markov_parameters, assumed_order, p=p, tau=8)







## Identified System
# identified_x0 = np.zeros(assumed_order)
identified_x0_era = identificationInitialCondition(gaussian_input_signal, gaussian_output_signal, era.A, era.B, era.C, era.D, 0, 200)
identified_x0_eradc = identificationInitialCondition(gaussian_input_signal, gaussian_output_signal, eradc.A, eradc.B, eradc.C, eradc.D, 0, 10)
identified_system_era = DiscreteLinearSystem(frequency, assumed_order, dynamics.input_dimension, dynamics.output_dimension, [(identified_x0_era, 0)], 'Nominal System', era.A, era.B, era.C, era.D)
identified_system_eradc = DiscreteLinearSystem(frequency, assumed_order, dynamics.input_dimension, dynamics.output_dimension, [(identified_x0_eradc, 0)], 'Nominal System', eradc.A, eradc.B, eradc.C, eradc.D)

nf, dr = calculateNaturalFrequenciesAndDampingRatios([identified_system_era, identified_system_eradc, nominal_system])

# ## Identified Signals
gaussian_output_signal_identified_era = OutputSignal(gaussian_input_signal, identified_system_era)
# square_wave_output_signal_identified_era = OutputSignal(square_wave_input_signal, identified_system_era)
# cosine_wave_output_signal_identified_era = OutputSignal(cosine_wave_input_signal, identified_system_era)
# gaussian_output_signal_identified_eradc = OutputSignal(gaussian_input_signal, identified_system_eradc)
# square_wave_output_signal_identified_eradc = OutputSignal(square_wave_input_signal, identified_system_eradc)
# cosine_wave_output_signal_identified_eradc = OutputSignal(cosine_wave_input_signal, identified_system_eradc)
#
#
# ## Observer Gain Matrix
# G_era, _, _ = getObserverGainMatrix(era.A, era.C, okid.observer_gain_markov_parameters, 0, dt, deadbeat_order)
# G_eradc, _, _ = getObserverGainMatrix(eradc.A, eradc.C, okid.observer_gain_markov_parameters, 0, dt, deadbeat_order)
#
#
# identified_system_with_observer_era = DiscreteLinearSystem(frequency, assumed_order, dynamics.input_dimension, dynamics.output_dimension, [(np.random.randn(dynamics.state_dimension), 0)], 'Nominal System', era.A, era.B, era.C, era.D, observer_gain=G_era)
# identified_system_with_observer_eradc = DiscreteLinearSystem(frequency, assumed_order, dynamics.input_dimension, dynamics.output_dimension, [(np.random.randn(dynamics.state_dimension), 0)], 'Nominal System', eradc.A, eradc.B, eradc.C, eradc.D, observer_gain=G_eradc)
# gaussian_output_signal_identified_with_observer_era = OutputSignal(gaussian_input_signal, identified_system_with_observer_era, observer='True', reference_output_signal=gaussian_output_signal_identified_era)
# gaussian_output_signal_identified_with_observer_eradc = OutputSignal(gaussian_input_signal, identified_system_with_observer_eradc, observer='True', reference_output_signal=gaussian_output_signal_identified_eradc)
#
#
#
#
#
#
#
# ## Plotting
#
## Plot input and output Training
fig = plt.figure(num=1, figsize=[12, 6])
ax = fig.add_subplot(2, 2, 1)
ax.plot(tspan_training, gaussian_input_signal_training.data[0, :], color=colors[0])
plt.xlabel('Time [sec]')
plt.ylabel('Input')
plt.title('Training')
ax = fig.add_subplot(2, 2, 3)
ax.plot(tspan, gaussian_output_signal.data[0, :], color=colors[1])
ax.plot(tspan, gaussian_output_signal_identified_era.data[0, :], color=colors[2])
plt.xlabel('Time [sec]')
plt.ylabel('Position')
plt.title('Testing')
ax = fig.add_subplot(2, 2, 4)
ax.plot(tspan, gaussian_output_signal.data[1, :], color=colors[1])
ax.plot(tspan, gaussian_output_signal_identified_era.data[1, :], color=colors[2])
plt.xlabel('Time [sec]')
plt.ylabel('Velocity')
plt.title('Testing')
plt.show()
#
#
# # Plot SVD
# plt.figure(num=2, figsize=[4, 4])
# plt.semilogy(np.linspace(1, np.min((p * dynamics.output_dimension, q * dynamics.input_dimension)), np.min((p * dynamics.output_dimension, q * dynamics.input_dimension))), np.diag(era.Sigma), '.', color=colors[7], label='ERA')
# plt.semilogy(np.linspace(1, np.min((p * dynamics.output_dimension, q * dynamics.input_dimension)), np.min((p * dynamics.output_dimension, q * dynamics.input_dimension))), np.diag(eradc.Sigma)[0:np.min((p * dynamics.output_dimension, q * dynamics.input_dimension))], '.', color=colors[8], label='ERADC')
# plt.xlabel('Number of singular values')
# plt.ylabel('Magnitude of singular values')
# plt.legend(loc='best')
# plt.show()
#
#
# # Check Eigenvalues
# plt.figure(num=3, figsize=[4, 4])
# plt.scatter(np.real(LA.eig(dynamics.A(0))[0]), np.imag(LA.eig(dynamics.A(0))[0]), color=colors[1], label='True')
# plt.scatter(np.real(LA.eig(era.A(0))[0]), np.imag(LA.eig(era.A(0))[0]), color=colors[4], facecolors='none', label='ERA')
# plt.scatter(np.real(LA.eig(eradc.A(0))[0]), np.imag(LA.eig(eradc.A(0))[0]), color=colors[5], facecolors='none', label='ERADC')
# plt.legend(loc='best')
# plt.xlabel('Real part of eigenvalues')
# plt.ylabel('Imaginary part of eigenvalues')
# plt.show()
#
#
# # Plot input and output Training
# fig = plt.figure(num=4, figsize=[12, 18])
#
# ax = fig.add_subplot(6, 2, 1)
# ax.plot(tspan, gaussian_output_signal.data[0, :], color=colors[1], label='True')
# ax.plot(tspan, gaussian_output_signal_identified_era.data[0, :], color=colors[4], linestyle='-.', label='ERA')
# ax.plot(tspan, gaussian_output_signal_identified_eradc.data[0, :], color=colors[5], linestyle='-.', label='ERADC')
# plt.ylabel('Position')
# plt.legend(loc='best')
# ax = fig.add_subplot(6, 2, 2)
# ax.plot(tspan, gaussian_output_signal.data[1, :], color=colors[1], label='True')
# ax.plot(tspan, gaussian_output_signal_identified_era.data[1, :], color=colors[4], linestyle='-.', label='ERA')
# ax.plot(tspan, gaussian_output_signal_identified_eradc.data[1, :], color=colors[5], linestyle='-.', label='ERADC')
# plt.ylabel('Velocity')
# plt.legend(loc='best')
# ax = fig.add_subplot(6, 2, 3)
# ax.plot(tspan, gaussian_output_signal.data[0, :] - gaussian_output_signal_identified_era.data[0, :], color=colors[7], label='ERA')
# ax.plot(tspan, gaussian_output_signal.data[0, :] - gaussian_output_signal_identified_eradc.data[0, :], color=colors[8], label='ERADC')
# plt.ylabel('Error Position')
# plt.legend(loc='best')
# ax = fig.add_subplot(6, 2, 4)
# ax.plot(tspan, gaussian_output_signal.data[1, :] - gaussian_output_signal_identified_era.data[1, :], color=colors[7], label='ERA')
# ax.plot(tspan, gaussian_output_signal.data[1, :] - gaussian_output_signal_identified_eradc.data[1, :], color=colors[8], label='ERADC')
# plt.ylabel('Error Velocity')
# plt.legend(loc='best')
#
# ax = fig.add_subplot(6, 2, 5)
# ax.plot(tspan, square_wave_output_signal.data[0, :], color=colors[1], label='True')
# ax.plot(tspan, square_wave_output_signal_identified_era.data[0, :], color=colors[4], linestyle='-.', label='ERA')
# ax.plot(tspan, square_wave_output_signal_identified_eradc.data[0, :], color=colors[5], linestyle='-.', label='ERADC')
# plt.ylabel('Position')
# plt.legend(loc='best')
# ax = fig.add_subplot(6, 2, 6)
# ax.plot(tspan, square_wave_output_signal.data[1, :], color=colors[1], label='True')
# ax.plot(tspan, square_wave_output_signal_identified_era.data[1, :], color=colors[4], linestyle='-.', label='ERA')
# ax.plot(tspan, square_wave_output_signal_identified_eradc.data[1, :], color=colors[5], linestyle='-.', label='ERADC')
# plt.ylabel('Velocity')
# plt.legend(loc='best')
# ax = fig.add_subplot(6, 2, 7)
# ax.plot(tspan, square_wave_output_signal.data[0, :] - square_wave_output_signal_identified_era.data[0, :], color=colors[7], label='ERA')
# ax.plot(tspan, square_wave_output_signal.data[0, :] - square_wave_output_signal_identified_eradc.data[0, :], color=colors[8], label='ERADC')
# plt.ylabel('Error Position')
# plt.legend(loc='best')
# ax = fig.add_subplot(6, 2, 8)
# ax.plot(tspan, square_wave_output_signal.data[1, :] - square_wave_output_signal_identified_era.data[1, :], color=colors[7], label='ERA')
# ax.plot(tspan, square_wave_output_signal.data[1, :] - square_wave_output_signal_identified_eradc.data[1, :], color=colors[8], label='ERADC')
# plt.ylabel('Error Velocity')
# plt.legend(loc='best')
#
# ax = fig.add_subplot(6, 2, 9)
# ax.plot(tspan, cosine_wave_output_signal.data[0, :], color=colors[1], label='True')
# ax.plot(tspan, cosine_wave_output_signal_identified_era.data[0, :], color=colors[4], linestyle='-.', label='ERA')
# ax.plot(tspan, cosine_wave_output_signal_identified_eradc.data[0, :], color=colors[5], linestyle='-.', label='ERADC')
# plt.ylabel('Position')
# plt.legend(loc='best')
# ax = fig.add_subplot(6, 2, 10)
# ax.plot(tspan, cosine_wave_output_signal.data[1, :], color=colors[1], label='True')
# ax.plot(tspan, cosine_wave_output_signal_identified_era.data[1, :], color=colors[4], linestyle='-.', label='ERA')
# ax.plot(tspan, cosine_wave_output_signal_identified_eradc.data[1, :], color=colors[5], linestyle='-.', label='ERADC')
# plt.ylabel('Velocity')
# plt.legend(loc='best')
# ax = fig.add_subplot(6, 2, 11)
# ax.plot(tspan, cosine_wave_output_signal.data[0, :] - cosine_wave_output_signal_identified_era.data[0, :], color=colors[7], label='ERA')
# ax.plot(tspan, cosine_wave_output_signal.data[0, :] - cosine_wave_output_signal_identified_eradc.data[0, :], color=colors[8], label='ERADC')
# plt.ylabel('Error Position')
# plt.legend(loc='best')
# ax = fig.add_subplot(6, 2, 12)
# ax.plot(tspan, cosine_wave_output_signal.data[1, :] - cosine_wave_output_signal_identified_era.data[1, :], color=colors[7], label='ERA')
# ax.plot(tspan, cosine_wave_output_signal.data[1, :] - cosine_wave_output_signal_identified_eradc.data[1, :], color=colors[8], label='ERADC')
# plt.ylabel('Error Velocity')
# plt.legend(loc='best')
# plt.xlabel('Time [sec]')
#
# plt.show()
#
#
#
#
#
# # With observer
# fig = plt.figure(num=5, figsize=[12, 6])
#
# ax = fig.add_subplot(2, 2, 1)
# ax.plot(tspan, gaussian_output_signal.data[0, :], color=colors[1], label='True')
# ax.plot(tspan, gaussian_output_signal_identified_with_observer_era.data[0, :], color=colors[4], linestyle='-.', label='ERA')
# ax.plot(tspan, gaussian_output_signal_identified_with_observer_eradc.data[0, :], color=colors[5], linestyle='-.', label='ERADC')
# plt.ylabel('Position')
# plt.legend(loc='best')
# ax = fig.add_subplot(2, 2, 2)
# ax.plot(tspan, gaussian_output_signal.data[1, :], color=colors[1], label='True')
# ax.plot(tspan, gaussian_output_signal_identified_with_observer_era.data[1, :], color=colors[4], linestyle='-.', label='ERA')
# ax.plot(tspan, gaussian_output_signal_identified_with_observer_eradc.data[1, :], color=colors[5], linestyle='-.', label='ERADC')
# plt.ylabel('Velocity')
# plt.legend(loc='best')
# ax = fig.add_subplot(2, 2, 3)
# ax.plot(tspan, gaussian_output_signal.data[0, :] - gaussian_output_signal_identified_with_observer_era.data[0, :], color=colors[7], label='ERA')
# ax.plot(tspan, gaussian_output_signal.data[0, :] - gaussian_output_signal_identified_with_observer_eradc.data[0, :], color=colors[8], label='ERADC')
# plt.ylabel('Error Position')
# plt.legend(loc='best')
# ax = fig.add_subplot(2, 2, 4)
# ax.plot(tspan, gaussian_output_signal.data[1, :] - gaussian_output_signal_identified_with_observer_era.data[1, :], color=colors[7], label='ERA')
# ax.plot(tspan, gaussian_output_signal.data[1, :] - gaussian_output_signal_identified_with_observer_eradc.data[1, :], color=colors[8], label='ERADC')
# plt.ylabel('Error Velocity')
# plt.legend(loc='best')
# plt.xlabel('Time [sec]')
#
# plt.show()





















