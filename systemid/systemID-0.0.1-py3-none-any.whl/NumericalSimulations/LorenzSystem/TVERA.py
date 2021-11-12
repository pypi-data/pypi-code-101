"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np

from ClassesDynamics.ClassLorenzSystemDynamics import LorenzSystemDynamics
from SystemIDAlgorithms.DepartureDynamics import departureDynamics
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, add2Signals, subtract2Signals
from Plotting.PlotSignals import plotSignals
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassMarkovParameters import TVOKIDObserver
from ClassesSystemID.ClassERA import TVERA
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck


# Parameters for Dynamics
sigma = 10
rho = 28
beta = 8/3


# Import Dynamics
dynamics = LorenzSystemDynamics(sigma, rho, beta)


# Parameters for identification
total_time = 5
frequency = 10
number_steps = int(total_time * frequency) + 1
assumed_order = 3
p, q = getOptimizedHankelMatrixSize(assumed_order, dynamics.output_dimension, dynamics.input_dimension)
deadbeat_order = 5


# Number Experiments
number_free_decay_experiments = q * dynamics.input_dimension
number_forced_response_experiments = round(dynamics.input_dimension + max(p + 1 + q - 1, deadbeat_order) * (dynamics.input_dimension + dynamics.output_dimension))


# Create System
initial_states = [(np.array([-8, 7, 27]), 0)]
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)
nominal_system_d = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System Discrete', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


# tspan
tspan = np.linspace(0, total_time, number_steps)


# Nominal Input Signal
gamma = np.array([0.01, 0.02, -0.01])
omega = 2 * np.pi * np.array([1, 2, 3])
phi = np.zeros(dynamics.input_dimension)
nominal_input_signal = ContinuousSignal(dynamics.input_dimension, 'Nominal Input Signal', signal_shape='Sinusoid', magnitude_sinusoid=gamma, frequency_sinusoid=omega / (2 * np.pi), phase_sinusoid=phi)


# Nominal Output Signal
nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal', tspan=tspan)


# Plot
plotSignals([[nominal_output_signal]], 1)


# Update dynamics with nominal trajectory
r = q
total_time_test = total_time - r / frequency
number_steps_test = number_steps - r
tspan_test = np.linspace(0, total_time_test, number_steps_test)
dynamics = LorenzSystemDynamics(sigma, rho, beta, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, 'Nominal Trajectory', total_time, frequency, signal_shape='External', data=nominal_output_signal.state), nominal_u=DiscreteSignal(dynamics.input_dimension, 'Nominal Input Signal', total_time, frequency, signal_shape='External', data=nominal_input_signal.u(tspan)), dt=1/frequency)
nominal_output_signal_test = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal Test', tspan=tspan_test)



# Deviations dx0
deviations_dx0 = []
for i in range(number_free_decay_experiments):
    deviations_dx0.append(0.01 * np.random.randn(dynamics.state_dimension))


# Deviations du
deviations_input_signal = []
N = 30
a0 = 0.01 * np.random.randn(number_forced_response_experiments, dynamics.input_dimension) / 2
ak = 0.01 * np.random.randn(N, number_forced_response_experiments, dynamics.input_dimension)
bk = 0.01 * np.random.randn(N, number_forced_response_experiments, dynamics.input_dimension)
for i in range(number_forced_response_experiments):
    def make_du(i):
        def du(t):
            S = a0[i, :].reshape((dynamics.input_dimension, 1))
            for j in range(1, N):
                 S = S + np.outer(ak[j, i, :], np.cos(j * t)) + np.outer(bk[j, i, :], np.sin(j * t))
            if S.shape[1] == 1:
                return S[:, 0]
            else:
                return S
        return du
    deviations_input_signal.append(ContinuousSignal(dynamics.input_dimension, 'Deviation Input Signal ' + str(i), signal_shape='External', u=make_du(i)))



# Full experiment
full_deviation_dx0 = 0.01 * np.random.randn(dynamics.state_dimension)
full_amplitude = np.array([0.01, -0.005, 0.02])
full_omega = 2 * np.pi * np.array([2.32, 1.58, 6.14])
full_phase = np.zeros(dynamics.input_dimension)
full_deviation_input_signal = ContinuousSignal(dynamics.input_dimension, 'Full Deviation Input Signal', signal_shape='Sinusoid', magnitude_sinusoid=full_amplitude, frequency_sinusoid=(omega + full_omega) / (2 * np.pi), phase_sinusoid=full_phase)
full_deviation_input_signal_d = DiscreteSignal(dynamics.input_dimension, 'Full Deviation Input Signal', total_time_test, frequency, signal_shape='Sinusoid', magnitude_sinusoid=full_amplitude, frequency_sinusoid=(omega + full_omega) / (2 * np.pi), phase_sinusoid=full_phase)


# Departure Dynamics
free_decay_experiments, free_decay_experiments_deviated, forced_response_experiments, forced_response_experiments_deviated, full_experiment, full_experiment_deviated = departureDynamics(nominal_system, nominal_input_signal, tspan_test, deviations_dx0, deviations_input_signal, full_deviation_dx0, full_deviation_input_signal)


# TVOKID
okid = TVOKIDObserver(forced_response_experiments_deviated, free_decay_experiments_deviated, p, q, deadbeat_order)
print(okid)

# TVERA
tvera = TVERA(okid.Y, okid.hki, okid.D, full_experiment_deviated, dynamics.state_dimension, p, q, apply_transformation=True)


# Test Signal
test_amplitude = 0.01 * np.random.randn(dynamics.input_dimension)
test_omega = 2 * np.pi * np.random.randn(dynamics.input_dimension)
test_phase = np.random.randn(dynamics.input_dimension)
def test_du(t):
    data = test_amplitude.reshape((dynamics.input_dimension, 1)) * np.sin(np.outer(test_omega, t) + test_phase.reshape((dynamics.input_dimension, 1)))
    if data.shape[1] == 1:
        return data[:, 0]
    else:
        return data
def test_u(t):
    return nominal_input_signal.u(t) + test_du(t)
data = test_du(tspan_test)
test_deviation_input_signal = DiscreteSignal(dynamics.input_dimension, 'Test Deviation Input Signal', total_time_test, frequency, signal_shape='External', data=data)
test_input_signal = ContinuousSignal(dynamics.input_dimension, 'Test Input Signal', signal_shape='External', u=test_u)


# Test System
test_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_states[0][0] + full_deviation_dx0, 0)], 'Test System', dynamics.F, dynamics.G)


# True Output Signal
#true_output_signal = OutputSignal(test_input_signal, test_system, 'True Output Signal', tspan=tspan_test)
true_output_signal = full_experiment.output_signals[0]


# Identified System
identified_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(tvera.x0, 0)], 'System ID', tvera.A, tvera.B, tvera.C, tvera.D)


# Identified Output Signal
identified_output_signal = add2Signals(nominal_output_signal_test, OutputSignal(full_deviation_input_signal_d, identified_system, 'Identified Deviation Output Signal'))


# # Linearized System
# #linearized_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(full_deviation_dx0, 0)], 'System Linearized', dynamics.A, dynamics.B, dynamics.C, dynamics.D)
#
#
# # Linearized Output Signal
# #linearized_output_signal = add2Signals(nominal_output_signal_test, OutputSignal(full_deviation_input_signal_d, linearized_system, 'Linearized Deviation Output Signal'))
#
#
# Plotting
plotSignals([[true_output_signal, identified_output_signal], [subtract2Signals(true_output_signal, identified_output_signal)]], 5, percentage=0.06)
#plotSignals([[true_output_signal, identified_output_signal, linearized_output_signal], [subtract2Signals(true_output_signal, identified_output_signal), subtract2Signals(true_output_signal, linearized_output_signal)]], 5, percentage=0.2)


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
# # plotSignals([[nominal_output_signal] + free_decay_experiments.output_signals, [nominal_output_signal] + forced_response_experiments.output_signals, [nominal_output_signal] + full_experiment.output_signals], 11)
# # plotSignals([free_decay_experiments_deviated.input_signals, forced_response_experiments_deviated.input_signals, full_experiment_deviated.input_signals], 12)
# # plotSignals([free_decay_experiments_deviated.output_signals, forced_response_experiments_deviated.output_signals, full_experiment_deviated.output_signals], 13)
#
#
# #Mk = timeVaryingObserverKalmanIdentificationAlgorithmObserver(forced_response_experiments_deviated, p, q, deadbeat_order, 2)
#
#
#
# #plotHistoryEigenValues2Systems([corrected_system_linearized, corrected_system_id], number_steps_test - p, 23)
#
#
