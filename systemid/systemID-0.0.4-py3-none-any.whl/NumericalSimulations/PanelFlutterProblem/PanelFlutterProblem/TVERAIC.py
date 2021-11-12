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


## Parameters for Dynamics
def RT(t):
    return 0
def mu(t):
    return 0.01
def M(t):
    return 5
def l(t):
    return 280 + 20 * np.sin(2 * np.pi * 5 * t)


# Import Dynamics
dynamics = PanelFlutterDynamics(RT, mu, M, l)


# Parameters for identification
total_time = 10
frequency = 50
number_steps = int(total_time * frequency) + 1
assumed_order = 4
p, q = getOptimizedHankelMatrixSize(assumed_order, dynamics.output_dimension, dynamics.input_dimension)
deadbeat_order = 4


# Number Experiments
number_free_decay_experiments = q * dynamics.input_dimension + 2
number_forced_response_experiments = round(dynamics.input_dimension + max(p + 1 + q - 1, deadbeat_order) * (dynamics.input_dimension + dynamics.output_dimension)) + 2


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
    deviations_dx0.append(0.00001 * np.random.randn(dynamics.state_dimension))


# Full experiment
full_deviation_dx0 = np.array([-3.28e-6, 1.16e-5, -3.38e-6, -6.73e-6])
# full_deviation_dx0 = 0.00001 * np.random.randn(dynamics.state_dimension)
#full_deviation_dx0 = deviations_dx0[0]
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
plotSignals([[true_output_signal, identified_output_signal], [subtract2Signals(true_output_signal, identified_output_signal)]], 1, percentage=0.9)
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

print('RMSE =', np.sqrt(((true_output_signal.data - identified_output_signal.data) ** 2).mean()))




