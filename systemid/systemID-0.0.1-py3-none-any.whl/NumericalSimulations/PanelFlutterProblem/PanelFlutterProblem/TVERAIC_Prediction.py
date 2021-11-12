"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np

from ClassesDynamics.ClassPanelFlutterDynamics import PanelFlutterDynamics
from SystemIDAlgorithms.DepartureDynamics import departureDynamicsFromInitialConditionResponse
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, add2Signals, subtract2Signals
from Plotting.PlotSignals import plotSignals
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassERA import TVERAFromInitialConditionResponse
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck
from NumericalSimulations.PanelFlutterProblem.PanelFlutterProblem.PlotFormating import plotResponse3, plotEigenValues, plotSVD

from SystemIDAlgorithms.Prediction import prediction


# Parameters for Dynamics
RT = 0.01
mu = 0.01
M = 5
l = 80


# Import Dynamics
dynamics = PanelFlutterDynamics(RT, mu, M, l)


# Parameters for identification
total_time = 6
frequency = 50
number_steps = int(total_time * frequency) + 1
assumed_order = 4
p, q = getOptimizedHankelMatrixSize(assumed_order, dynamics.output_dimension, dynamics.input_dimension)
deadbeat_order = 4
p = 4


# Number Experiments
number_free_decay_experiments = (q * dynamics.input_dimension) * 2


# Create System
initial_states = [(np.array([0, 0.001, 0, 0]), 0)]
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)
nominal_system_d = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System Discrete', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


# tspan
tspan = np.linspace(0, total_time, number_steps)


# Nominal Input Signal
nominal_input_signal = ContinuousSignal(dynamics.input_dimension, 'Nominal Input Signal')


# Nominal Output Signal
nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal', tspan=tspan)


# Update dynamics with nominal trajectory
r = q
total_time_test = total_time - r / frequency
number_steps_test = number_steps - r
tspan_test = np.linspace(0, total_time_test, number_steps_test)
dynamics = PanelFlutterDynamics(RT, mu, M, l, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, 'Nominal Trajectory', total_time, frequency, signal_shape='External', data=nominal_output_signal.state), nominal_u=DiscreteSignal(dynamics.input_dimension, 'Nominal Input Signal', total_time, frequency), dt=1/frequency)
nominal_output_signal_test = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal Test', tspan=tspan_test)


# Deviations dx0
deviations_dx0 = []
for i in range(number_free_decay_experiments):
    deviations_dx0.append(0.00005 * np.random.randn(dynamics.state_dimension))


# Full experiment
# full_deviation_dx0 = 0.00005 * np.random.randn(dynamics.state_dimension)
# full_deviation_dx0 = deviations_dx0[0]
full_deviation_dx0 = np.array([3.94069271e-05, -3.63592283e-05, -3.48360494e-05, 2.82658503e-05])
full_deviation_input_signal = ContinuousSignal(dynamics.input_dimension, 'Full Deviation Input Signal')
full_deviation_input_signal_d = DiscreteSignal(dynamics.input_dimension, 'Full Deviation Input Signal', total_time_test, frequency)


# Departure Dynamics
free_decay_experiments, free_decay_experiments_deviated, full_experiment, full_experiment_deviated = departureDynamicsFromInitialConditionResponse(nominal_system, nominal_input_signal, tspan_test, deviations_dx0, full_deviation_dx0)


# TVERA
tvera = TVERAFromInitialConditionResponse(free_decay_experiments_deviated, full_experiment_deviated, dynamics.state_dimension, p)


# Test System
test_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_states[0][0] + full_deviation_dx0, 0)], 'Test System', dynamics.F, dynamics.G)


# True Output Signal
true_output_signal = full_experiment.output_signals[0]


# Identified System
identified_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(tvera.x0, 0)], 'System ID', tvera.A, tvera.B, tvera.C, tvera.D)


# Identified Output Signal
identified_output_signal = add2Signals(nominal_output_signal_test, OutputSignal(full_deviation_input_signal_d, identified_system, 'Identified Deviation Output Signal'))



# Linearized System
linearized_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(full_deviation_dx0, 0)], 'System Linearized', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


# Linearized Output Signal
linearized_output_signal = add2Signals(nominal_output_signal_test, OutputSignal(full_deviation_input_signal_d, linearized_system, 'Linearized Deviation Output Signal'))


# # Plotting
plotSignals([[true_output_signal, identified_output_signal, linearized_output_signal], [subtract2Signals(true_output_signal, identified_output_signal), subtract2Signals(true_output_signal, linearized_output_signal)]], 1, percentage=0.9)
#
#
# # True Corrected System
# corrected_system = correctSystemForEigenvaluesCheck(nominal_system_d, number_steps_test - p, p)
#
# # Identified Corrected System
# corrected_system_id = correctSystemForEigenvaluesCheck(identified_system, number_steps_test - p, p)
#
# # Linearized Corrected System
# corrected_system_linearized = correctSystemForEigenvaluesCheck(linearized_system, number_steps_test - p, p)
#
#
# #plotHistoryEigenValues2Systems([corrected_system_linearized, corrected_system_id], number_steps_test - p, 2)
# plotResponse3([true_output_signal, identified_output_signal, linearized_output_signal], [subtract2Signals(true_output_signal, identified_output_signal), subtract2Signals(true_output_signal, linearized_output_signal)], tspan, 244, ['$q_1$', '$q_2$', '$q_1\'$', '$q_2\'$'], 1)
# plotEigenValues([corrected_system_id, corrected_system_linearized], number_steps_test - p, 2)

# time_steps = np.array([0, 1, 2, 5, 10, 20, 50, 100, 200, 240])
# sigma = tvera.Sigma
# plotSVD(sigma, time_steps, 5)











## Prediction
# Time spans for training and prediction
total_time_training = 5
total_time_prediction = 10
number_steps_training = int(total_time_training * frequency) + 1
number_steps_prediction = int(total_time_prediction * frequency) + 1
tspan_training = np.round(np.linspace(0, total_time_training , number_steps_training), decimals=2)
tspan_prediction = np.round(np.linspace(0, total_time_prediction, number_steps_prediction), decimals=2)

# Nominals
nominal_output_signal_prediction = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal', tspan=tspan_prediction)
nominal_input_signal_prediction = DiscreteSignal(dynamics.input_dimension, 'Nominal u', total_time_prediction, frequency)
nominal_output_signal_training = DiscreteSignal(dynamics.output_dimension, 'Nominal x', total_time_training, frequency, signal_shape='External', data=nominal_output_signal.data[:, 0:number_steps_training])
nominal_input_signal_training = DiscreteSignal(dynamics.input_dimension, 'Nominal u', total_time_training, frequency)
nominal_reference = DiscreteSignal(dynamics.input_dimension + dynamics.output_dimension, 'Nominal Reference', total_time_training, frequency, signal_shape='External', data=np.concatenate((nominal_input_signal_training.data, nominal_output_signal_training.data), axis=0))
nominal = DiscreteSignal(dynamics.input_dimension + dynamics.output_dimension, 'Nominal', total_time_prediction, frequency, signal_shape='External', data=np.concatenate((nominal_input_signal_prediction.data, nominal_output_signal_prediction.data), axis=0))

# Input signal
prediction_deviation_input_signal = DiscreteSignal(dynamics.input_dimension, 'Prediction Deviation Input Signal', total_time_prediction, frequency)
prediction_input_signal = ContinuousSignal(dynamics.input_dimension, 'Prediction Input Signal')

# Prediction
window_size = 20
starting_step = int(frequency * total_time_training)
selected_for_propagation, output_signal_predicted = prediction(nominal_reference, identified_system, nominal, identified_system, prediction_deviation_input_signal, starting_step, window_size=window_size)

# Construction of predicted signal and systems
true_output_signal_prediction = OutputSignal(prediction_input_signal, test_system, 'True Output Signal', tspan=tspan_prediction)
def A_chosen_f(t):
    return selected_for_propagation['A'][round(t * frequency)]
def B_chosen_f(t):
    return selected_for_propagation['B'][round(t * frequency)]
def C_chosen_f(t):
    return selected_for_propagation['C'][round(t * frequency)]
def D_chosen_f(t):
    return selected_for_propagation['D'][round(t * frequency)]
dumb_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(tvera.x0, 0)], 'System ID', A_chosen_f, B_chosen_f, C_chosen_f, D_chosen_f)
identified_output_signal_prediction = add2Signals(nominal_output_signal_prediction, output_signal_predicted)

# Plotting
plotSignals([[nominal_output_signal_prediction, true_output_signal_prediction, identified_output_signal_prediction], [subtract2Signals(true_output_signal_prediction, identified_output_signal_prediction)]], 21, percentage=0.98)
#plotHistoryEigenValues1System(dumb_system, number_steps_training + number_steps_prediction, 2)


print('RMSE q =', np.sqrt(((true_output_signal_prediction.data[0:2, :] - identified_output_signal_prediction.data[0:2, :]) ** 2).mean()))
print('RMSE q_d =', np.sqrt(((true_output_signal_prediction.data[2:4, :] - identified_output_signal_prediction.data[2:4, :]) ** 2).mean()))








