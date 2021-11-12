"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np
from scipy import signal
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

from ClassesDynamics.ClassPanelFlutterDynamics import PanelFlutterDynamics3
from SystemIDAlgorithms.DepartureDynamics import departureDynamics
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, add2Signals, subtract2Signals
from Plotting.PlotSignals import plotSignals
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems, plotHistoryEigenValues1System
from ClassesSystemID.ClassMarkovParameters import TVOKIDObserver
from ClassesSystemID.ClassERA import TVERA
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck

from SystemIDAlgorithms.ZZZTimeVaryingObserverKalmanIdentificationAlgorithmObserver import timeVaryingObserverKalmanIdentificationAlgorithmObserver



## Parameters for Dynamics
print('Define Parameters')
def RT(t):
    return 0
def mu(t):
    return 0.01
def M(t):
    return 5
l = 280

print('## Parameters for Dynamics')

## Import Dynamics
dynamics = PanelFlutterDynamics3(RT)

print('## Import Dynamics')

## Parameters for identification
total_time = 2
frequency = 100
dt = 1 / frequency
number_steps = int(total_time * frequency) + 1
tspan = np.round(np.linspace(0, total_time, number_steps), decimals=2)
assumed_order = 4
p, q = getOptimizedHankelMatrixSize(assumed_order, dynamics.output_dimension, dynamics.input_dimension)
deadbeat_order = 8

print('## Parameters for identification')

## Number Experiments
number_free_decay_experiments = q * dynamics.input_dimension + 2
number_forced_response_experiments = round(dynamics.input_dimension + max(p + 1 + q - 1, deadbeat_order) * (dynamics.input_dimension + dynamics.output_dimension)) + 2


print('## Number Experiments')

## Create System
initial_states = [(np.array([0, 0.001, 0, 0]), 0)]
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)
nominal_system_d = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System Discrete', dynamics.A, dynamics.B, dynamics.C, dynamics.D)

print('## Create System')

## Nominal Input Signal
def u_nominal(t):
    return np.array([l + 0 * t, np.sqrt(l * mu(t) / M(t)) + 0 * t])
nominal_input_signal = ContinuousSignal(dynamics.input_dimension, 'Nominal Input Signal', signal_shape='External', u=u_nominal)

print('## Nominal Input Signal')

## Nominal Output Signal
nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal', tspan=tspan)

print('## Nominal Output Signal')

## Update dynamics with nominal trajectory
r = 2
total_time_test = total_time - r / frequency
number_steps_test = number_steps - r
tspan_test = tspan[:-r]
dynamics = PanelFlutterDynamics3(RT, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, 'Nominal Trajectory', total_time, frequency, signal_shape='External', data=nominal_output_signal.state), nominal_u=DiscreteSignal(dynamics.input_dimension, 'Nominal Input Signal', total_time, frequency, signal_shape='External', data=nominal_input_signal.u(tspan)), dt=1/frequency)
nominal_output_signal_test = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal Test', tspan=tspan_test)
tspan_test = np.round(tspan_test, decimals=2)

print('## Update dynamics with nominal trajectory')

## Deviations dx0
deviations_dx0 = []
for i in range(number_free_decay_experiments):
    deviations_dx0.append(0.00001 * np.random.randn(dynamics.state_dimension))

print('## Deviations dx0')

# # Deviations du
# print('## Deviations du')
# deviations_input_signal = []
# interp_du = []
# random_inputs_numbers = 1 * np.random.randn(number_forced_response_experiments, number_steps_test)
# for i in range(number_forced_response_experiments):
#     def make_du(i):
#         def du(t):
#             if type(t) == np.ndarray:
#                 return random_inputs_numbers[i, :]
#             else:
#                 return random_inputs_numbers[i, int(t * frequency)]
#
#         return du
#     deviations_input_signal.append(ContinuousSignal(dynamics.input_dimension, 'Deviation Input Signal ' + str(i), signal_shape='External', u=make_du(i)))



# # Deviations du
# print('## Deviations du')
# deviations_input_signal = []
# random_magnitudes = 2 * np.random.randn(number_forced_response_experiments)
# random_frequencies = 0.5 * np.random.randn(number_forced_response_experiments)
# random_phases = np.random.randn(number_forced_response_experiments)
# for i in range(number_forced_response_experiments):
#     def make_du(i):
#         def du(t):
#             dlambda = random_magnitudes[i] * np.sin(2 * np.pi * random_frequencies[i] * t + random_phases[i])
#             return np.array([dlambda, np.sqrt(l * mu(t) / M(t)) * (dlambda / l) / 2])
#         return du
#     deviations_input_signal.append(ContinuousSignal(dynamics.input_dimension, 'Deviation Input Signal ' + str(i), signal_shape='External', u=make_du(i)))




# Deviations du
print('## Deviations du')
deviations_input_signal = []
min_l = -2
max_l = 2
magnitudes = np.linspace(min_l, max_l, number_forced_response_experiments)
for i in range(number_forced_response_experiments):
    def make_du(i):
        def du(t):
            return np.array([magnitudes[i] + 0*t, np.sqrt(l * mu(t) / M(t)) * ((magnitudes[i] + 0 * t) / l) / 2])
        return du
    deviations_input_signal.append(ContinuousSignal(dynamics.input_dimension, 'Deviation Input Signal ' + str(i), signal_shape='External', u=make_du(i)))



## Full experiment
full_deviation_dx0 = 0.00001 * np.random.randn(dynamics.state_dimension)
full_amplitude = 1
full_frequency = 0.0236
full_phase = 3
def full_du(t):
    # dlambda_full = full_amplitude * np.sin(2 * np.pi * full_frequency * t + full_phase)
    dlambda_full = 0.123 + 0 * t
    return np.array([dlambda_full, np.sqrt(l * mu(t) / M(t)) * (dlambda_full / l) / 2])
full_deviation_input_signal = ContinuousSignal(dynamics.input_dimension, 'Deviation Input Signal ', signal_shape='External', u=full_du)
full_deviation_input_signal_d = DiscreteSignal(dynamics.input_dimension, 'Full Deviation Input Signal', total_time_test, frequency, signal_shape='External', data=full_du(tspan_test))

print('## Full experiment')

## Departure Dynamics
free_decay_experiments, free_decay_experiments_deviated, forced_response_experiments, forced_response_experiments_deviated, full_experiment, full_experiment_deviated = departureDynamics(nominal_system, nominal_input_signal, tspan_test, deviations_dx0, deviations_input_signal, full_deviation_dx0, full_deviation_input_signal)

print('## Departure Dynamics')

## TVOKID
okid = TVOKIDObserver(forced_response_experiments_deviated, free_decay_experiments_deviated, p, q, deadbeat_order)

print('## TVOKID')

## TVERA
tvera = TVERA(okid.Y, okid.hki, okid.D, full_experiment_deviated, dynamics.state_dimension, p, q, apply_transformation=True)

print('## TVERA')

# Test Signal
test_amplitude = 1
test_frequency = 0.32
test_phase = 12
def test_du(t):
    # dlambda_test = test_amplitude * np.sin(2 * np.pi * test_frequency * t + test_phase)
    dlambda_test = 0.456 + 0 * t
    return np.array([dlambda_test, np.sqrt(l * mu(t) / M(t)) * (dlambda_test / l) / 2])
def test_u(t):
    return nominal_input_signal.u(t) + test_du(t)
data = test_du(tspan_test)
test_deviation_input_signal = DiscreteSignal(dynamics.input_dimension, 'Test Deviation Input Signal', total_time_test, frequency, signal_shape='External', data=data)
test_input_signal = ContinuousSignal(dynamics.input_dimension, 'Test Input Signal', signal_shape='External', u=test_u)

print('# Test Signal')

## Test System
test_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_states[0][0] + full_deviation_dx0, 0)], 'Test System', dynamics.F, dynamics.G)

print('## Test System')

## True Output Signal
true_output_signal = OutputSignal(test_input_signal, test_system, 'True Output Signal', tspan=tspan_test)

print('## True Output Signal')

# Identified System
identified_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(tvera.x0, 0)], 'System ID', tvera.A, tvera.B, tvera.C, tvera.D)

print('# Identified System')

## Identified Output Signal
identified_output_signal = add2Signals(nominal_output_signal_test, OutputSignal(test_deviation_input_signal, identified_system, 'Identified Deviation Output Signal'))

print('## Identified Output Signal')

# # Linearized System
# linearized_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(full_deviation_dx0, 0)], 'System Linearized', dynamics.A, dynamics.B, dynamics.C, dynamics.D)
#
#
# # Linearized Output Signal
# linearized_output_signal = add2Signals(nominal_output_signal_test, OutputSignal(full_deviation_input_signal_d, linearized_system, 'Linearized Deviation Output Signal'))



## Plotting
plotSignals([[nominal_output_signal, true_output_signal, identified_output_signal], [subtract2Signals(true_output_signal, identified_output_signal)]], 5, percentage=0.03)
# plotSignals([[true_output_signal, identified_output_signal, linearized_output_signal], [subtract2Signals(true_output_signal, identified_output_signal), subtract2Signals(true_output_signal, linearized_output_signal)]], 5, percentage=0.2)


# # True Corrected System
# corrected_system = correctSystemForEigenvaluesCheck(nominal_system_d, number_steps_test - p, p)
#
# # Identified Corrected System
# corrected_system_id = correctSystemForEigenvaluesCheck(identified_system, number_steps_test - p, p)
#
# # Linearized Corrected System
# corrected_system_linearized = correctSystemForEigenvaluesCheck(linearized_system, number_steps_test - p, p)



plotSignals([forced_response_experiments_deviated.input_signals[0:10], [nominal_output_signal_test] + forced_response_experiments.output_signals[0:10], forced_response_experiments_deviated.output_signals[0:10]], 11)
# plotSignals([free_decay_experiments_deviated.input_signals[0:4], free_decay_experiments_deviated.output_signals[0:4], free_decay_experiments.output_signals[0:4]], 12)
# plotSignals([[true_output_signal]], 13)
# plotSignals([[nominal_output_signal] + free_decay_experiments.output_signals, [nominal_output_signal] + forced_response_experiments.output_signals, [nominal_output_signal] + full_experiment.output_signals], 11)
#plotSignals([free_decay_experiments_deviated.input_signals[0:1], forced_response_experiments_deviated.input_signals[0:1], full_experiment_deviated.input_signals], 12)
# plotSignals([free_decay_experiments_deviated.output_signals, forced_response_experiments_deviated.output_signals, full_experiment_deviated.output_signals], 13)
#plotHistoryEigenValues2Systems([corrected_system_linearized, corrected_system_id], number_steps_test - p, 23)
















































########################################################################################################################
#####################################################  PLOTTING  #######################################################
########################################################################################################################


# from matplotlib import rc
#
# colors = [(11/255, 36/255, 251/255),
#           (27/255, 161/255, 252/255),
#           (77/255, 254/255, 193/255),
#           (224/255, 253/255, 63/255),
#           (253/255, 127/255, 35/255),
#           (221/255, 10/255, 22/255),
#           (255/255, 0/255, 127/255),
#           (127/255, 0/255, 255/255),
#           (255/255, 0/255, 255/255),
#           (145/255, 145/255, 145/255),
#           (0, 0, 0)]
#
#
# plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
# rc('text', usetex=True)
#
#
# # Phase plots
# fig = plt.figure(num=1, figsize=[4, 4])
# plt.plot(nominal_output_signal.data[0, :-2], nominal_output_signal.data[1, :-2], color=colors[5])
# plt.plot(true_output_signal.data[0, :-2], true_output_signal.data[1, :-2], color=colors[7])
# plt.plot(identified_output_signal.data[0, :-2], identified_output_signal.data[1, :-2], color=colors[8], linestyle='-.')
# plt.plot(linearized_output_signal.data[0, :-2], linearized_output_signal.data[1, :-2], color=colors[4], linestyle=':')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(['Nominal', 'True', 'Identified', 'Linearized'], loc='lower left')
# plt.show()

# # xy plots
# fig = plt.figure(num=2, figsize=[4, 2])
# plt.plot(tspan_test[:-2], nominal_output_signal.data[0, :-4], color=colors[5])
# plt.plot(tspan_test[:-2], true_output_signal.data[0, :-2], color=colors[7])
# plt.plot(tspan_test[:-2], identified_output_signal.data[0, :-2], color=colors[8], linestyle='-.')
# plt.plot(tspan_test[:-2], linearized_output_signal.data[0, :-2], color=colors[4], linestyle=':')
# plt.xlabel('Time [sec]')
# plt.ylabel('Error')
# plt.legend(['Nominal', 'True', 'Identified', 'Linearized'], loc='lower left')
# plt.show()
#
# fig = plt.figure(num=3, figsize=[4, 2])
# plt.plot(tspan_test[:-2], true_output_signal.data[1, :-2] - identified_output_signal.data[1, :-2], color=colors[8])
# plt.plot(tspan_test[:-2], true_output_signal.data[1, :-2] - linearized_output_signal.data[1, :-2], color=colors[4])
# plt.xlabel('Time [sec]')
# plt.ylabel('Error')
# plt.legend(['Nominal', 'True', 'Identified', 'Linearized'], loc='lower left')
# plt.show()


# # Error plots
# fig = plt.figure(num=2, figsize=[4, 2])
# plt.plot(tspan_test[:-2], true_output_signal.data[0, :-2] - identified_output_signal.data[0, :-2], color=colors[8])
# plt.plot(tspan_test[:-2], true_output_signal.data[0, :-2] - linearized_output_signal.data[0, :-2], color=colors[4])
# plt.xlabel('Time [sec]')
# plt.ylabel('Error')
# plt.legend(['Identified', 'Linearized'], loc='lower right')
# plt.show()
#
# fig = plt.figure(num=3, figsize=[4, 2])
# plt.plot(tspan_test[:-2], true_output_signal.data[1, :-2] - identified_output_signal.data[1, :-2], color=colors[8])
# plt.plot(tspan_test[:-2], true_output_signal.data[1, :-2] - linearized_output_signal.data[1, :-2], color=colors[4])
# plt.xlabel('Time [sec]')
# plt.ylabel('Error')
# plt.legend(['Identified', 'Linearized'], loc='lower right')
# plt.show()

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