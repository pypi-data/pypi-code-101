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
from scipy import signal
from scipy.interpolate import interp1d

from ClassesDynamics.ClassVanDerPolOscillatorDynamics import VanDerPolOscillatorDynamics
from SystemIDAlgorithms.DepartureDynamics import departureDynamics
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, add2Signals, subtract2Signals
from Plotting.PlotSignals import plotSignals
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems, plotHistoryEigenValues1System
from ClassesSystemID.ClassMarkovParameters import TVOKIDObserver
from ClassesSystemID.ClassERA import TVERA

from SystemIDAlgorithms.Prediction import prediction, prediction2

from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck

from SystemIDAlgorithms.ZZZTimeVaryingObserverKalmanIdentificationAlgorithmObserver import timeVaryingObserverKalmanIdentificationAlgorithmObserver


# Parameters for Dynamics
def beta(t):
    return -0.8 + 0.05*np.sin(2*np.pi*2*t)
def mu(t):
    return 2 + 0.05*np.sin(2*np.pi*3*t + np.pi/2)
def alpha(t):
    return -10 + 0.5*np.sin(2*np.pi*4*t + np.pi)


# Import Dynamics
dynamics = VanDerPolOscillatorDynamics(beta, mu, alpha)


# Parameters for identification
total_time = 11
frequency = 20
number_steps = int(total_time * frequency) + 1
assumed_order = 2
p, q = getOptimizedHankelMatrixSize(assumed_order, dynamics.output_dimension, dynamics.input_dimension)
deadbeat_order = 10


# Number Experiments
number_free_decay_experiments = q * dynamics.input_dimension + 2
number_forced_response_experiments = round(dynamics.input_dimension + max(p + 1 + q - 1, deadbeat_order) * (dynamics.input_dimension + dynamics.output_dimension)) +10
number_forced_response_experiments = number_forced_response_experiments + 10


# Create System
initial_states = [(np.array([0.5, 0.5]), 0)]
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)
nominal_system_d = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System Discrete', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


# tspan
tspan = np.round(np.linspace(0, total_time, number_steps), decimals=2)


# Nominal Input Signal
def u_nominal(t):
    return 0 * np.sin(10 * t + 2)
nominal_input_signal = ContinuousSignal(dynamics.input_dimension, 'Nominal Input Signal', signal_shape='External', u=u_nominal)

# Nominal Output Signal
nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal', tspan=tspan)


# Plot Signal
plotSignals([[nominal_output_signal]], 1)
plt.plot(nominal_output_signal.data[0, :], nominal_output_signal.data[1, :])
plt.show()


# Update dynamics with nominal trajectory
r = 1
total_time_test = total_time - r / frequency
number_steps_test = number_steps - r
tspan_test = tspan[:-r]
dynamics = VanDerPolOscillatorDynamics(beta, mu, alpha, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, 'Nominal Trajectory', total_time, frequency, signal_shape='External', data=nominal_output_signal.state), nominal_u=DiscreteSignal(dynamics.input_dimension, 'Nominal Input Signal', total_time, frequency, signal_shape='External', data=nominal_input_signal.u(tspan)), dt=1/frequency)
nominal_output_signal_test = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal Test', tspan=tspan_test)
nominal_input_signal_test = DiscreteSignal(dynamics.input_dimension, 'Nominal Input Signal', total_time_test, frequency, signal_shape='External', data=u_nominal(tspan_test))
tspan_test = np.round(tspan_test, decimals=2)


# Deviations dx0
deviations_dx0 = []
for i in range(number_free_decay_experiments):
    deviations_dx0.append(0.2 * np.random.randn(dynamics.state_dimension))


# Deviations du
deviations_input_signal = []
interp_du = []
random_inputs_numbers = 0.05 * np.random.randn(number_forced_response_experiments, number_steps_test)
for i in range(number_forced_response_experiments):
    def make_du(i):
        def du(t):
            if type(t) == np.ndarray:
                return random_inputs_numbers[i, :]
            else:
                return random_inputs_numbers[i, int(t * frequency)]

        return du
    deviations_input_signal.append(ContinuousSignal(dynamics.input_dimension, 'Deviation Input Signal ' + str(i), signal_shape='External', u=make_du(i)))
# for i in range(number_forced_response_experiments):
#     def make_du(i):
#         def du(t):
#             return interp_du[i](t)
#         return du
#    deviations_input_signal.append(ContinuousSignal(dynamics.input_dimension, 'Deviation Input Signal ' + str(i), signal_shape='External', u=make_du(i)))




# Full experiment
#full_deviation_dx0 = 0.5 * np.random.randn(dynamics.state_dimension)
#full_deviation_dx0 = deviations_dx0[0]
full_deviation_dx0 = np.array([0.05, 0.05])
full_amplitude = 0.01
full_omega = 0.0236
full_phase = 3
def full_du(t):
    return full_amplitude * np.sin((full_omega) * t + full_phase)
full_deviation_input_signal = ContinuousSignal(dynamics.input_dimension, 'Full Deviation Input Signal', signal_shape='External', u=full_du)
full_deviation_input_signal_d = DiscreteSignal(dynamics.input_dimension, 'Full Deviation Input Signal', total_time_test, frequency, signal_shape='External', data=full_du(tspan_test))


# Departure Dynamics
free_decay_experiments, free_decay_experiments_deviated, forced_response_experiments, forced_response_experiments_deviated, full_experiment, full_experiment_deviated = departureDynamics(nominal_system, nominal_input_signal, tspan_test, deviations_dx0, deviations_input_signal, full_deviation_dx0, full_deviation_input_signal)


# TVOKID
okid = TVOKIDObserver(forced_response_experiments_deviated, free_decay_experiments_deviated, p, q, deadbeat_order)


# TVERA
tvera = TVERA(okid.Y, okid.hki, okid.D, full_experiment_deviated, dynamics.state_dimension, p, q, apply_transformation=True)


# Test Signal
test_amplitude = 0.01
test_omega = 1.32
test_phase = 12
def test_du(t):
    return test_amplitude * np.sin((test_omega) * t + test_phase)
# def test_du(t):
#     return deviations_input_signal[0].u(t)
def test_u(t):
    return nominal_input_signal.u(t) + test_du(t)
data = test_du(tspan_test)
test_deviation_input_signal_d = DiscreteSignal(dynamics.input_dimension, 'Test Deviation Input Signal', total_time_test, frequency, signal_shape='External', data=data)
test_input_signal = ContinuousSignal(dynamics.input_dimension, 'Test Input Signal', signal_shape='External', u=test_u)


# Test System
test_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_states[0][0] + full_deviation_dx0, 0)], 'Test System', dynamics.F, dynamics.G)


# True Output Signal
true_output_signal = OutputSignal(test_input_signal, test_system, 'True Output Signal', tspan=tspan_test)
#true_output_signal = full_experiment.output_signals[0]


# Identified System
identified_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(tvera.x0, 0)], 'System ID', tvera.A, tvera.B, tvera.C, tvera.D)


# # Get state history from Identified system and full response
# full_deviation_for_state_history = full_experiment.output_signals[0].state - nominal_output_signal_test.state


# Identified Output Signal
#identified_deviation_output_signal = OutputSignal(test_deviation_input_signal_d, identified_system, 'Identified Deviation Output Signal', state_propagation=True, signal_input_history=nominal_input_signal_d.data, signal_output_history=nominal_output_signal_test.data)
identified_deviation_output_signal = OutputSignal(test_deviation_input_signal_d, identified_system, 'Identified Deviation Output Signal')
#, state_propagation=False, signal_input_history=full_deviation_input_signal_d.data, signal_output_history=full_experiment_deviated.output_signals[0].data)
# plt.plot(identified_deviation_output_signal.state[0, :], identified_deviation_output_signal.state[1, :])
# plt.show()
identified_output_signal = add2Signals(nominal_output_signal_test, identified_deviation_output_signal)

#
# # Linearized System
# linearized_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(full_deviation_dx0, 0)], 'System Linearized', dynamics.A, dynamics.B, dynamics.C, dynamics.D)
#
#
# # Linearized Output Signal
# linearized_output_signal = add2Signals(nominal_output_signal_test, OutputSignal(full_deviation_input_signal_d, linearized_system, 'Linearized Deviation Output Signal'))
#

# Plotting
plotSignals([[nominal_output_signal_test, true_output_signal, identified_output_signal], [subtract2Signals(true_output_signal, identified_output_signal)]], 5, percentage=0.98)
# plt.plot(nominal_output_signal.data[0, 0:582], nominal_output_signal.data[1, 0:582])
# plt.plot(true_output_signal.data[0, 0:582], true_output_signal.data[1, 0:582])
# plt.plot(identified_output_signal.data[0, 0:582], identified_output_signal.data[1, 0:582])
# plt.show()
# plt.plot(nominal_output_signal.data[0, :], nominal_output_signal.data[1, :])
# plt.plot(true_output_signal.data[0, :], true_output_signal.data[1, :])
# plt.plot(identified_output_signal.data[0, :], identified_output_signal.data[1, :])
# plt.show()
#plotSignals([[nominal_output_signal_test, true_output_signal, identified_output_signal, linearized_output_signal], [subtract2Signals(true_output_signal, identified_output_signal), subtract2Signals(true_output_signal, linearized_output_signal)]], 5, percentage=0.3)
plt.plot(nominal_output_signal.data[0, :], nominal_output_signal.data[1, :])
plt.plot(true_output_signal.data[0, :], true_output_signal.data[1, :])
plt.plot(identified_output_signal.data[0, :], identified_output_signal.data[1, :])
plt.show()

# # # True Corrected System
# # corrected_system = correctSystemForEigenvaluesCheck(nominal_system_d, number_steps_test - p, p)
# #
# # # Identified Corrected System
# # corrected_system_id = correctSystemForEigenvaluesCheck(identified_system, number_steps_test - p, p)
# #
# # # Linearized Corrected System
# # corrected_system_linearized = correctSystemForEigenvaluesCheck(linearized_system, number_steps_test - p, p)
#
#
#
# #plotSignals([forced_response_experiments_deviated.input_signals[0:10], [nominal_output_signal] + forced_response_experiments.output_signals[0:10], forced_response_experiments_deviated.output_signals[0:10]], 11)
# # plotSignals([free_decay_experiments_deviated.input_signals[0:4], free_decay_experiments_deviated.output_signals[0:4], free_decay_experiments.output_signals[0:4]], 12)
# # plotSignals([[true_output_signal]], 13)
#
# plotSignals([[nominal_output_signal_test] + free_decay_experiments.output_signals, [nominal_output_signal_test] + forced_response_experiments.output_signals, [nominal_output_signal_test] + full_experiment.output_signals], 11)
# plotSignals([free_decay_experiments_deviated.input_signals, forced_response_experiments_deviated.input_signals, full_experiment_deviated.input_signals], 12)
# plotSignals([free_decay_experiments_deviated.output_signals, forced_response_experiments_deviated.output_signals, full_experiment_deviated.output_signals], 13)

#
# #Mk = timeVaryingObserverKalmanIdentificationAlgorithmObserver(forced_response_experiments_deviated, p, q, deadbeat_order, 2)
#
#
#
# #plotHistoryEigenValues2Systems([corrected_system_linearized, corrected_system_id], number_steps_test - p, 23)
#
#
#
# import matplotlib.pyplot as plt
# plt.plot(nominal_output_signal.data[0, :], nominal_output_signal.data[1, :])
# plt.plot(forced_response_experiments.output_signals[0].data[0, :], forced_response_experiments.output_signals[0].data[1, :])
# plt.show()

# plt.figure(55)
# for i in range(20):
#     plt.semilogy(np.linspace(1, len(tvera.sigma[i]), len(tvera.sigma[i])), tvera.sigma[i])
# plt.show()






