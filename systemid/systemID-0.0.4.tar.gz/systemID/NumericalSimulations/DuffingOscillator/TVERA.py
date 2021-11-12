"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""


"""
Classic TVOKID/TVERA
Parameters are time-varying
Input is a square wave
"""



import numpy as np
from scipy import signal

from ClassesDynamics.ClassDuffingOscillatorDynamics import DuffingOscillatorDynamics
from SystemIDAlgorithms.DepartureDynamics import departureDynamics
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, addSignals, subtract2Signals
from Plotting.PlotSignals import plotSignals
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from ClassesSystemID.ClassMarkovParameters import TVOKIDObserver
from ClassesSystemID.ClassERA import TVERA




## Parameters for Dynamics
def delta(t):
    return 0.2 + 0.2*np.sin(2*np.pi*2*t)
def alpha(t):
    return 1 + 0.1*np.sin(2*np.pi*3*t + np.pi/2)
def beta(t):
    return -1 + 0.1*np.sin(2*np.pi*4*t + np.pi)



## Import Dynamics
dynamics = DuffingOscillatorDynamics(delta, alpha, beta)



## Parameters for identification
total_time = 11
frequency = 10
dt = 1 / frequency
number_steps = int(total_time * frequency) + 1
tspan = np.round(np.linspace(0, total_time, number_steps), decimals=2)
assumed_order = 2
p, q = getOptimizedHankelMatrixSize(assumed_order, dynamics.output_dimension, dynamics.input_dimension)
deadbeat_order = 4



## Number Experiments
number_free_decay_experiments = q * dynamics.input_dimension
number_forced_response_experiments = round(dynamics.input_dimension + max(p + 1 + q - 1, deadbeat_order) * (dynamics.input_dimension + dynamics.output_dimension))
number_forced_response_experiments = number_forced_response_experiments * 2



## Create System
initial_states = [(np.array([0.1, -0.2]), 0)]
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)
nominal_system_d = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System Discrete', dynamics.A, dynamics.B, dynamics.C, dynamics.D)



## Nominal Input Signal
def u_nominal(t):
    return 0.1 * signal.square(2 * np.pi * t)
nominal_input_signal = ContinuousSignal(dynamics.input_dimension, signal_shape='External', u=u_nominal)



## Nominal Output Signal
nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan)



## Update dynamics with nominal trajectory
r = 2
total_time_test = total_time - r / frequency
number_steps_test = number_steps - r
tspan_test = tspan[:-r]
dynamics = DuffingOscillatorDynamics(delta, alpha, beta, nominal=True, initial_states=initial_states, nominal_u=nominal_input_signal, dt=1/frequency, tspan=tspan_test)
nominal_output_signal_test = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan_test)
tspan_test = np.round(tspan_test, decimals=2)



## Deviations dx0
deviations_dx0 = []
for i in range(number_free_decay_experiments):
    deviations_dx0.append(0.05 * np.random.randn(dynamics.state_dimension))



# Deviations du
deviations_input_signal = []
random_inputs_numbers = 0.02 * np.random.randn(number_forced_response_experiments, number_steps_test)
for i in range(number_forced_response_experiments):
    def make_du(i):
        def du(t):
            if type(t) == np.ndarray:
                return random_inputs_numbers[i, :]
            else:
                return random_inputs_numbers[i, int(t * frequency)]
        return du
    deviations_input_signal.append(ContinuousSignal(dynamics.input_dimension, signal_shape='External', u=make_du(i)))



## Full experiment
full_deviation_dx0 = np.array([0.012, -0.015])
full_amplitude = 0.01
full_omega = 0.0236
full_phase = 3
def full_du(t):
    return full_amplitude * np.sin((full_omega) * t + full_phase)
full_deviation_input_signal = ContinuousSignal(dynamics.input_dimension, signal_shape='External', u=full_du)
full_deviation_input_signal_d = DiscreteSignal(dynamics.input_dimension, total_time_test, frequency, signal_shape='External', data=full_du(tspan_test))



## Departure Dynamics
free_decay_experiments, free_decay_experiments_deviated, forced_response_experiments, forced_response_experiments_deviated, full_experiment, full_experiment_deviated = departureDynamics(nominal_system, nominal_input_signal, tspan_test, deviations_dx0, deviations_input_signal, full_deviation_dx0, full_deviation_input_signal)



## TVOKID
okid = TVOKIDObserver(forced_response_experiments_deviated, deadbeat_order)



## TVERA
tvera = TVERA(free_decay_experiments_deviated, okid.hki, okid.D, full_experiment_deviated, dynamics.state_dimension, p, q, apply_transformation=True)


# Test Signal
test_amplitude = 0.05
test_omega = 0.32
test_phase = 12
def test_du(t):
    return test_amplitude * np.sin(test_omega * t + test_phase)
def test_u(t):
    return nominal_input_signal.u(t) + test_du(t)
data = test_du(tspan_test)
test_deviation_input_signal = DiscreteSignal(dynamics.input_dimension, total_time_test, frequency, signal_shape='External', data=data)
test_input_signal = ContinuousSignal(dynamics.input_dimension, signal_shape='External', u=test_u)



## Test System
test_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_states[0][0] + full_deviation_dx0, 0)], 'Test System', dynamics.F, dynamics.G)



## True Output Signal
true_output_signal = OutputSignal(test_input_signal, test_system, tspan=tspan_test)



# Identified System
identified_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(tvera.x0, 0)], 'System ID', tvera.A, tvera.B, tvera.C, tvera.D)



## Identified Output Signal
identified_output_signal = addSignals([nominal_output_signal_test, OutputSignal(test_deviation_input_signal, identified_system)])



# Linearized System
linearized_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(full_deviation_dx0, 0)], 'System Linearized', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


# Linearized Output Signal
linearized_output_signal = addSignals([nominal_output_signal_test, OutputSignal(full_deviation_input_signal_d, linearized_system)])



## Plotting
plotSignals([[nominal_output_signal, true_output_signal, identified_output_signal], [subtract2Signals(true_output_signal, identified_output_signal)]], 5, percentage=0.95)
#plotSignals([[true_output_signal, identified_output_signal, linearized_output_signal], [subtract2Signals(true_output_signal, identified_output_signal), subtract2Signals(true_output_signal, linearized_output_signal)]], 5, percentage=0.2)


# # True Corrected System
# corrected_system = correctSystemForEigenvaluesCheck(nominal_system_d, number_steps_test - p, p)
#
# # Identified Corrected System
# corrected_system_id = correctSystemForEigenvaluesCheck(identified_system, number_steps_test - p, p)
#
# # Linearized Corrected System
# corrected_system_linearized = correctSystemForEigenvaluesCheck(linearized_system, number_steps_test - p, p)



#plotSignals([forced_response_experiments_deviated.input_signals[0:10], [nominal_output_signal_test] + forced_response_experiments.output_signals[0:10], forced_response_experiments_deviated.output_signals[0:10]], 11)
# plotSignals([free_decay_experiments_deviated.input_signals[0:4], free_decay_experiments_deviated.output_signals[0:4], free_decay_experiments.output_signals[0:4]], 12)
# plotSignals([[true_output_signal]], 13)
# plotSignals([[nominal_output_signal] + free_decay_experiments.output_signals, [nominal_output_signal] + forced_response_experiments.output_signals, [nominal_output_signal] + full_experiment.output_signals], 11)
#plotSignals([free_decay_experiments_deviated.input_signals[0:1], forced_response_experiments_deviated.input_signals[0:1], full_experiment_deviated.input_signals], 12)
# plotSignals([free_decay_experiments_deviated.output_signals, forced_response_experiments_deviated.output_signals, full_experiment_deviated.output_signals], 13)
#plotHistoryEigenValues2Systems([corrected_system_linearized, corrected_system_id], number_steps_test - p, 23)


print('RMSE =', np.sqrt(((true_output_signal.data - linearized_output_signal.data) ** 2).mean()))













































########################################################################################################################
#####################################################  PLOTTING  #######################################################
########################################################################################################################

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


# Phase plots
fig = plt.figure(num=1, figsize=[6, 6])
plt.plot(nominal_output_signal.data[0, :-2], nominal_output_signal.data[1, :-2], color=colors[5])
plt.plot(true_output_signal.data[0, :-2], true_output_signal.data[1, :-2], color=colors[7])
plt.plot(identified_output_signal.data[0, :-2], identified_output_signal.data[1, :-2], color=colors[8], linestyle='-.')
plt.plot(linearized_output_signal.data[0, :-2], linearized_output_signal.data[1, :-2], color=colors[4], linestyle=':')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Nominal', 'True', 'Identified', 'Linearized'], loc='lower left')
plt.tight_layout()
# plt.savefig('Phase_plot_TVERA.eps', format='eps')
plt.show()

# xy plots
fig = plt.figure(num=2, figsize=[6, 3])
plt.plot(tspan_test[:-2], nominal_output_signal.data[0, :-4], color=colors[5])
plt.plot(tspan_test[:-2], true_output_signal.data[0, :-2], color=colors[7])
plt.plot(tspan_test[:-2], identified_output_signal.data[0, :-2], color=colors[8], linestyle='-.')
plt.plot(tspan_test[:-2], linearized_output_signal.data[0, :-2], color=colors[4], linestyle=':')
plt.xlabel('Time [sec]')
plt.ylabel('x')
plt.legend(['Nominal', 'True', 'Identified', 'Linearized'], loc='lower right')
plt.tight_layout()
# plt.savefig('x_plot_TVERA.eps', format='eps')
plt.show()

fig = plt.figure(num=3, figsize=[6, 3])
plt.plot(tspan_test[:-2], nominal_output_signal.data[1, :-4], color=colors[5])
plt.plot(tspan_test[:-2], true_output_signal.data[1, :-2], color=colors[7])
plt.plot(tspan_test[:-2], identified_output_signal.data[1, :-2], color=colors[8], linestyle='-.')
plt.plot(tspan_test[:-2], linearized_output_signal.data[1, :-2], color=colors[4], linestyle=':')
plt.xlabel('Time [sec]')
plt.ylabel('y')
plt.legend(['Nominal', 'True', 'Identified', 'Linearized'], loc='lower right')
plt.tight_layout()
# plt.savefig('y_plot_TVERA.eps', format='eps')
plt.show()


# Error plots
fig = plt.figure(num=2, figsize=[4, 2])
plt.plot(tspan_test[:-2], true_output_signal.data[0, :-2] - identified_output_signal.data[0, :-2], color=colors[8])
plt.plot(tspan_test[:-2], true_output_signal.data[0, :-2] - linearized_output_signal.data[0, :-2], color=colors[4])
plt.xlabel('Time [sec]')
plt.ylabel('Error')
plt.legend(['Identified', 'Linearized'], loc='lower right')
plt.show()

fig = plt.figure(num=3, figsize=[4, 2])
plt.plot(tspan_test[:-2], true_output_signal.data[1, :-2] - identified_output_signal.data[1, :-2], color=colors[8])
plt.plot(tspan_test[:-2], true_output_signal.data[1, :-2] - linearized_output_signal.data[1, :-2], color=colors[4])
plt.xlabel('Time [sec]')
plt.ylabel('Error')
plt.legend(['Identified', 'Linearized'], loc='lower right')
plt.show()

#
# # Eigenvalues
# dt = identified_system.dt
# eig1 = np.zeros([number_steps - r-2, identified_system.state_dimension])
# eig2 = np.zeros([number_steps - r-2, identified_system.state_dimension])
#
# for i in range(number_steps - r-2):
#     eig1[i, :] = np.real(LA.eig(corrected_system_id.A(i * dt))[0])
#     eig2[i, :] = np.real(LA.eig(corrected_system_linearized.A(i * dt))[0])
#
# eig1.sort(axis=1)
# eig2.sort(axis=1)
#
# fig = plt.figure(num=4, figsize=[4, 2])
# plt.plot(tspan_test[:-r-1], np.transpose(eig2[:-1, 0]), color=colors[5])
# plt.plot(tspan_test[:-r-1], np.transpose(eig1[:-1, 0]), color=colors[7], linestyle='-.')
# plt.xlabel('Time [sec]')
# plt.ylabel('First eigenvalue')
# plt.legend(['True', 'Identified'])
# plt.show()
#
# fig = plt.figure(num=5, figsize=[4, 2])
# plt.plot(tspan_test[:-r-1], np.transpose(eig2[:-1, 0]) - np.transpose(eig1[:-1, 0]), color=colors[7])
# plt.xlabel('Time [sec]')
# plt.ylabel('Error in magnitude')
# plt.show()
#
# fig = plt.figure(num=6, figsize=[4, 2])
# plt.plot(tspan_test[:-r-1], np.transpose(eig2[:-1, 1]), color=colors[5])
# plt.plot(tspan_test[:-r-1], np.transpose(eig1[:-1, 1]), color=colors[7], linestyle='-.')
# plt.xlabel('Time [sec]')
# plt.ylabel('Second eigenvalue')
# plt.legend(['True', 'Identified'])
# plt.show()
#
# fig = plt.figure(num=7, figsize=[4, 2])
# plt.plot(tspan_test[:-r-1], np.transpose(eig2[:-1, 1]) - np.transpose(eig1[:-1, 1]), color=colors[7])
# plt.xlabel('Time [sec]')
# plt.ylabel('Error in magnitude')
# plt.show()
#
# fig = plt.figure(num=8, figsize=[4, 2])
# plt.plot(tspan_test[:-r-1], np.transpose(eig2[:-1, 2]), color=colors[5])
# plt.plot(tspan_test[:-r-1], np.transpose(eig1[:-1, 2]), color=colors[7], linestyle='-.')
# plt.xlabel('Time [sec]')
# plt.ylabel('Third eigenvalue')
# plt.legend(['True', 'Identified'])
# plt.show()
#
# fig = plt.figure(num=9, figsize=[4, 2])
# plt.plot(tspan_test[:-r-1], np.transpose(eig2[:-1, 2]) - np.transpose(eig1[:-1, 2]), color=colors[7])
# plt.xlabel('Time [sec]')
# plt.ylabel('Error in magnitude')
# plt.show()















# ## Plot singular values from TVOKID
# plt.figure(23)
# plt.subplot(3, 1, 1)
# plt.semilogy(okid.E1)
# plt.ylabel('||VVt - I||')
# plt.subplot(3, 1, 2)
# plt.semilogy(okid.E2)
# plt.ylabel('||VtV - I||')
# plt.subplot(3, 1, 3)
# plt.semilogy(okid.E3)
# plt.ylabel('||y - MV||')
# plt.show()
#
#
# svdec = np.zeros([19, 99])
# svdec[0:1, 0] = okid.sv[0]
# svdec[0:4, 1] = okid.sv[1]
# svdec[0:7, 2] = okid.sv[2]
# svdec[0:10, 3] = okid.sv[3]
# svdec[0:13, 4] = okid.sv[4]
# svdec[0:16, 5] = okid.sv[5]
# for i in range(6, 99):
#     svdec[:, i] = okid.sv[i]
#
#
# plt.figure(24)
# plt.semilogy(svdec.T)
# plt.show()