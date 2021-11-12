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
frequency = 10
dt = 1 / frequency
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
    deviations_dx0.append(0.1 * np.random.randn(dynamics.state_dimension))


# Deviations du
deviations_input_signal = []
interp_du = []
random_inputs_numbers = 0.01 * np.random.randn(number_forced_response_experiments, number_steps_test)
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
def test_du(t):
    return test_amplitude * np.sin(t)
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






########################################################################################################################
############                                             Sim 2                                              ############
########################################################################################################################


# Parameters for identification
total_time_sim_2 = 51
number_steps_sim_2 = int(total_time_sim_2 * frequency) + 1

# Create System
initial_states_sim_2 = [(np.array([-0.75, 0.25]), 0)]
nominal_system_sim_2 = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states_sim_2, 'Nominal System', dynamics.F, dynamics.G)
nominal_system_d_sim_2 = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states_sim_2, 'Nominal System Discrete', dynamics.A, dynamics.B, dynamics.C, dynamics.D)

# tspan
tspan_sim_2 = np.round(np.linspace(0, total_time_sim_2, number_steps_sim_2), decimals=2)

# Nominal Input Signal
def u_nominal_sim_2(t):
    return 0 * np.sin(10 * t + 2)
nominal_input_signal_sim_2 = ContinuousSignal(dynamics.input_dimension, 'Nominal Input Signal', signal_shape='External', u=u_nominal_sim_2)

# Nominal Output Signal
nominal_output_signal_sim_2 = OutputSignal(nominal_input_signal_sim_2, nominal_system_sim_2, 'Nominal Output Signal', tspan=tspan_sim_2)

# Plot Signal
plotSignals([[nominal_output_signal_sim_2]], 1)
plt.plot(nominal_output_signal_sim_2.data[0, :], nominal_output_signal_sim_2.data[1, :])
plt.show()

# Update dynamics with nominal trajectory
r = 1
total_time_test_sim_2 = total_time_sim_2 - r / frequency
number_steps_test_sim_2 = number_steps_sim_2 - r
tspan_test_sim_2 = tspan_sim_2[:-r]
dynamics_sim_2 = VanDerPolOscillatorDynamics(beta, mu, alpha, tspan=tspan_sim_2, nominal_x=DiscreteSignal(dynamics.state_dimension, 'Nominal Trajectory', total_time_sim_2, frequency, signal_shape='External', data=nominal_output_signal_sim_2.state), nominal_u=DiscreteSignal(dynamics.input_dimension, 'Nominal Input Signal', total_time_sim_2, frequency, signal_shape='External', data=nominal_input_signal_sim_2.u(tspan_sim_2)), dt=1/frequency)
nominal_output_signal_test_sim_2 = OutputSignal(nominal_input_signal_sim_2, nominal_system_sim_2, 'Nominal Output Signal Test', tspan=tspan_test_sim_2)
# nominal_input_signal_d = DiscreteSignal(dynamics.input_dimension, 'Nominal Input Signal', total_time_test_sim_2, frequency, signal_shape='External', data=u(tspan_test))
tspan_test_sim_2 = np.round(tspan_test_sim_2, decimals=2)

# Deviations dx0
deviations_dx0_sim_2 = []
for i in range(number_free_decay_experiments):
    deviations_dx0_sim_2.append(0.1 * np.random.randn(dynamics.state_dimension))

# Deviations du
deviations_input_signal_sim_2 = []
random_inputs_numbers_sim_2 = 0.01 * np.random.randn(number_forced_response_experiments, number_steps_test_sim_2)
for i in range(number_forced_response_experiments):
    def make_du_sim_2(i):
        def du(t):
            if type(t) == np.ndarray:
                return random_inputs_numbers_sim_2[i, :]
            else:
                return random_inputs_numbers_sim_2[i, int(t * frequency)]

        return du
    deviations_input_signal_sim_2.append(ContinuousSignal(dynamics.input_dimension, 'Deviation Input Signal ' + str(i), signal_shape='External', u=make_du_sim_2(i)))

# Full experiment
full_deviation_dx0_sim_2 = np.array([0.02, 0.02])
full_amplitude_sim_2 = 0.01
full_omega_sim_2 = 0.0236
full_phase_sim_2 = 3
def full_du_sim_2(t):
    return full_amplitude_sim_2 * np.sin((full_omega_sim_2) * t + full_phase_sim_2)
full_deviation_input_signal_sim_2 = ContinuousSignal(dynamics.input_dimension, 'Full Deviation Input Signal', signal_shape='External', u=full_du_sim_2)
full_deviation_input_signal_d_sim_2 = DiscreteSignal(dynamics.input_dimension, 'Full Deviation Input Signal', total_time_test_sim_2, frequency, signal_shape='External', data=full_du_sim_2(tspan_test_sim_2))

# Departure Dynamics
free_decay_experiments_sim_2, free_decay_experiments_deviated_sim_2, forced_response_experiments_sim_2, forced_response_experiments_deviated_sim_2, full_experiment_sim_2, full_experiment_deviated_sim_2 = departureDynamics(nominal_system_sim_2, nominal_input_signal_sim_2, tspan_test_sim_2, deviations_dx0_sim_2, deviations_input_signal_sim_2, full_deviation_dx0_sim_2, full_deviation_input_signal_sim_2)

# TVOKID
okid_sim_2 = TVOKIDObserver(forced_response_experiments_deviated_sim_2, free_decay_experiments_deviated_sim_2, p, q, deadbeat_order)

# TVERA
tvera_sim_2 = TVERA(okid_sim_2.Y, okid_sim_2.hki, okid_sim_2.D, full_experiment_deviated_sim_2, dynamics.state_dimension, p, q, apply_transformation=True)

# Test Signal
test_amplitude_sim_2 = 0.01
def test_du_sim_2(t):
    return test_amplitude_sim_2 * np.sin(t)
def test_u_sim_2(t):
    return nominal_input_signal_sim_2.u(t) + test_du_sim_2(t)
data_sim_2 = test_du_sim_2(tspan_test_sim_2)
test_deviation_input_signal_d_sim_2 = DiscreteSignal(dynamics.input_dimension, 'Test Deviation Input Signal', total_time_test_sim_2, frequency, signal_shape='External', data=data_sim_2)
test_input_signal_sim_2 = ContinuousSignal(dynamics.input_dimension, 'Test Input Signal', signal_shape='External', u=test_u_sim_2)

# Test System
test_system_sim_2 = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_states_sim_2[0][0] + full_deviation_dx0_sim_2, 0)], 'Test System', dynamics.F, dynamics.G)

# True Output Signal
true_output_signal_sim_2 = OutputSignal(test_input_signal_sim_2, test_system_sim_2, 'True Output Signal', tspan=tspan_test_sim_2)

# Identified System
identified_system_sim_2 = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(tvera_sim_2.x0, 0)], 'System ID', tvera_sim_2.A, tvera_sim_2.B, tvera_sim_2.C, tvera_sim_2.D)

# Identified Output Signal
#identified_deviation_output_signal = OutputSignal(test_deviation_input_signal_d, identified_system, 'Identified Deviation Output Signal', state_propagation=True, signal_input_history=nominal_input_signal_d.data, signal_output_history=nominal_output_signal_test.data)
identified_deviation_output_signal_sim_2 = OutputSignal(test_deviation_input_signal_d_sim_2, identified_system_sim_2, 'Identified Deviation Output Signal')
#, state_propagation=False, signal_input_history=full_deviation_input_signal_d.data, signal_output_history=full_experiment_deviated.output_signals[0].data)
# plt.plot(identified_deviation_output_signal.state[0, :], identified_deviation_output_signal.state[1, :])
# plt.show()
identified_output_signal_sim_2 = add2Signals(nominal_output_signal_test_sim_2, identified_deviation_output_signal_sim_2)

#
# # Linearized System
# linearized_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(full_deviation_dx0, 0)], 'System Linearized', dynamics.A, dynamics.B, dynamics.C, dynamics.D)
#
#
# # Linearized Output Signal
# linearized_output_signal = add2Signals(nominal_output_signal_test, OutputSignal(full_deviation_input_signal_d, linearized_system, 'Linearized Deviation Output Signal'))
#

# Plotting
plotSignals([[nominal_output_signal_test_sim_2, true_output_signal_sim_2, identified_output_signal_sim_2], [subtract2Signals(true_output_signal_sim_2, identified_output_signal_sim_2)]], 11, percentage=0.98)
# plt.plot(nominal_output_signal.data[0, 0:582], nominal_output_signal.data[1, 0:582])
# plt.plot(true_output_signal.data[0, 0:582], true_output_signal.data[1, 0:582])
# plt.plot(identified_output_signal.data[0, 0:582], identified_output_signal.data[1, 0:582])
# plt.show()
# plt.plot(nominal_output_signal.data[0, :], nominal_output_signal.data[1, :])
# plt.plot(true_output_signal.data[0, :], true_output_signal.data[1, :])
# plt.plot(identified_output_signal.data[0, :], identified_output_signal.data[1, :])
# plt.show()
#plotSignals([[nominal_output_signal_test, true_output_signal, identified_output_signal, linearized_output_signal], [subtract2Signals(true_output_signal, identified_output_signal), subtract2Signals(true_output_signal, linearized_output_signal)]], 5, percentage=0.3)
# plt.plot(nominal_output_signal.data[0, :], nominal_output_signal.data[1, :])
# plt.plot(true_output_signal.data[0, :], true_output_signal.data[1, :])
# plt.plot(identified_output_signal.data[0, :], identified_output_signal.data[1, :])
# plt.show()










## Prediction
# Time spans for training and prediction
total_time_training = 10
total_time_prediction = 50
number_steps_training = int(total_time_training * frequency) + 1
number_steps_prediction = int(total_time_prediction * frequency) + 1
tspan_training = np.round(np.linspace(0, total_time_training , number_steps_training), decimals=2)
tspan_prediction = np.round(np.linspace(0, total_time_prediction, number_steps_prediction), decimals=2)

# Nominals
nominal_output_signal_prediction = OutputSignal(nominal_input_signal_sim_2, nominal_system_sim_2, 'Nominal Output Signal', tspan=tspan_prediction)
nominal_input_signal_prediction = DiscreteSignal(dynamics.input_dimension, 'Nominal u', total_time_prediction, frequency, signal_shape='External', data=u_nominal_sim_2(tspan_prediction))
nominal_output_signal_training = DiscreteSignal(dynamics.output_dimension, 'Nominal x', total_time_training, frequency, signal_shape='External', data=nominal_output_signal.data[:, 0:number_steps_training])
nominal_input_signal_training = DiscreteSignal(dynamics.input_dimension, 'Nominal u', total_time_training, frequency, signal_shape='External', data=u_nominal(tspan_training))
nominal_reference = DiscreteSignal(dynamics.input_dimension + dynamics.output_dimension, 'Nominal Reference', total_time_training, frequency, signal_shape='External', data=np.concatenate((nominal_input_signal_training.data, nominal_output_signal_training.data), axis=0))
nominal = DiscreteSignal(dynamics.input_dimension + dynamics.output_dimension, 'Nominal', total_time_prediction, frequency, signal_shape='External', data=np.concatenate((nominal_input_signal_prediction.data, nominal_output_signal_prediction.data), axis=0))

# Input signal
prediction_deviation_input_signal = DiscreteSignal(dynamics.input_dimension, 'Prediction Deviation Input Signal', total_time_prediction, frequency, signal_shape='External', data=test_du_sim_2(tspan_prediction))
prediction_input_signal = ContinuousSignal(dynamics.input_dimension, 'Prediction Input Signal', signal_shape='External', u=test_u_sim_2)

# Prediction
window_size = 20
starting_step = int(frequency * total_time_training)
selected_for_propagation, output_signal_predicted = prediction(nominal_reference, identified_system, nominal, identified_system_sim_2, prediction_deviation_input_signal, starting_step, window_size=window_size)

# Construction of predicted signal and systems
true_output_signal_prediction = OutputSignal(prediction_input_signal, test_system_sim_2, 'True Output Signal', tspan=tspan_prediction)
def A_chosen_f(t):
    return selected_for_propagation['A'][round(t * frequency)]
def B_chosen_f(t):
    return selected_for_propagation['B'][round(t * frequency)]
def C_chosen_f(t):
    return selected_for_propagation['C'][round(t * frequency)]
def D_chosen_f(t):
    return selected_for_propagation['D'][round(t * frequency)]
dumb_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(tvera_sim_2.x0, 0)], 'System ID', A_chosen_f, B_chosen_f, C_chosen_f, D_chosen_f)
identified_output_signal_prediction = add2Signals(nominal_output_signal_prediction, output_signal_predicted)

# Plotting
plotSignals([[nominal_output_signal_prediction, true_output_signal_prediction, identified_output_signal_prediction], [subtract2Signals(true_output_signal_prediction, identified_output_signal_prediction)]], 21, percentage=0.98)
#plotHistoryEigenValues1System(dumb_system, number_steps_training + number_steps_prediction, 2)


print('RMSE =', np.sqrt(((true_output_signal_prediction.data - identified_output_signal_prediction.data) ** 2).mean()))

















































#
#
#
#
# # Prediction
# dt = 1 / frequency
# total_time_training = 2.95
# total_time_prediction = 7
# number_steps_training = int(total_time_training * frequency) + 1
# number_steps_prediction = int(total_time_prediction * frequency) + 1
# tspan_training_and_prediction = np.round(np.linspace(0, total_time_training + total_time_prediction + dt, number_steps_training + number_steps_prediction), decimals=2)
# tspan_training = np.round(np.linspace(0, total_time_training, number_steps_training), decimals=2)
# tspan_prediction = np.round(np.linspace(0, total_time_prediction, number_steps_prediction), decimals=2)
#
# # nominal_output_signal_training_and_prediction = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal', tspan=tspan_training_and_prediction)
# nominal_output_signal_training_and_prediction = nominal_output_signal_sim_2
# nominal_input_signal_training_and_prediction = DiscreteSignal(dynamics.input_dimension, 'Nominal u', total_time_training + total_time_prediction + dt, frequency, signal_shape='External', data=u_nominal(tspan_training_and_prediction))
# # nominal_input_signal_training_and_prediction = nominal_input_signal_sim_2
#
# nominal_output_signal_training = DiscreteSignal(dynamics.output_dimension, 'Nominal x', total_time_training, frequency, signal_shape='External', data=nominal_output_signal_training_and_prediction.data[:, 0:number_steps_training])
# nominal_input_signal_training = DiscreteSignal(dynamics.input_dimension, 'Nominal u', total_time_training, frequency, signal_shape='External', data=nominal_input_signal_training_and_prediction.data[:, 0:number_steps_training])
#
# nominal_output_signal_prediction = DiscreteSignal(dynamics.output_dimension, 'Nominal x', total_time_prediction, frequency, signal_shape='External', data=nominal_output_signal_training_and_prediction.data[:, number_steps_training:])
# nominal_input_signal_prediction = DiscreteSignal(dynamics.input_dimension, 'Nominal u', total_time_prediction, frequency, signal_shape='External', data=nominal_output_signal_training_and_prediction.data[:, number_steps_training:])
#
# def prediction_du(t):
#     return 0.01 * np.sin(1 * t)
# def prediction_u(t):
#     return nominal_input_signal_sim_2.u(t) + prediction_du(t)
# prediction_deviation_input_signal = DiscreteSignal(dynamics.input_dimension, 'Prediction Deviation Input Signal', total_time_training + total_time_prediction + dt, frequency, signal_shape='External', data=prediction_du(tspan_training_and_prediction))
# prediction_input_signal = ContinuousSignal(dynamics.input_dimension, 'Prediction Input Signal', signal_shape='External', u=prediction_u)
#
# A_list, B_list, C_list, D_list, A_chosen, indexes, nominal_state_history, nominal_input_history, x, y, output_signal_predicted = prediction2(nominal_output_signal_training_and_prediction, nominal_input_signal_training_and_prediction, identified_system_sim_2, nominal_output_signal_test, nominal_input_signal_test, identified_system, prediction_deviation_input_signal, 60, 141)
# #plotSignals([[output_signal, output_signal_id], [output_signal_predicted]], 2, percentage=0.9)
#
# true_output_signal_prediction = OutputSignal(prediction_input_signal, test_system_sim_2, 'True Output Signal', tspan=tspan_training_and_prediction)
# def A_chosen_f(t):
#     return A_chosen[round(t * frequency)]
# dumb_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(tvera_sim_2.x0, 0)], 'System ID', A_chosen_f, tvera_sim_2.B, tvera_sim_2.C, tvera_sim_2.D)
#
# identified_output_signal_prediction = add2Signals(nominal_output_signal_training_and_prediction, output_signal_predicted)
# plotSignals([[nominal_output_signal_training_and_prediction, true_output_signal_prediction, identified_output_signal_prediction], [subtract2Signals(true_output_signal_prediction, identified_output_signal_prediction)]], 2, percentage=0.98)
# plotHistoryEigenValues1System(dumb_system, number_steps_training + number_steps_prediction, 2)
# plotSignals([[nominal_output_signal_training_and_prediction]], 3)
# plotSignals([[nominal_input_signal_training_and_prediction]], 5)
#
#
#
#
# fig = plt.figure(num=4, figsize=[8, 3])
# plt.plot(np.linspace(1, number_steps_training + number_steps_prediction, number_steps_training + number_steps_prediction), indexes)
# plt.show()
#
#
#
#
#
#
#









