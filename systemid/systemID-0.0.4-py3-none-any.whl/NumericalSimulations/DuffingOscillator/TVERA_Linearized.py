"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np
from scipy.signal import chirp

from ClassesDynamics.ClassDuffingOscillatorDynamics import DuffingOscillatorDynamics
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassExperiments import Experiments
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
alpha = 1
beta = -1


# Import Dynamics
dynamics = DuffingOscillatorDynamics(delta, alpha, beta)


# Parameters for identification
total_time = 4
frequency = 10
number_steps = int(total_time * frequency) + 1
assumed_order = 2
p, q = getOptimizedHankelMatrixSize(assumed_order, dynamics.output_dimension, dynamics.input_dimension)
deadbeat_order = 4


# Number Experiments
number_free_decay_experiments = q * dynamics.input_dimension
number_forced_response_experiments = round(dynamics.input_dimension + max(p + 1 + q - 1, deadbeat_order) * (dynamics.input_dimension + dynamics.output_dimension))


# Create System
initial_states = [(np.array([0.1, -0.2]), 0)]
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)


# tspan
tspan = np.linspace(0, total_time, number_steps)


# Nominal Input Signal
gamma = 0.3
omega = 1
phi = 0
nominal_input_signal = ContinuousSignal(dynamics.input_dimension, 'Nominal Input Signal', signal_shape='Sinusoid', magnitude_sinusoid=gamma, frequency_sinusoid=omega / (2 * np.pi), phase_sinusoid=phi)



# Nominal Output Signal
nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal', tspan=tspan)


# Update dynamics with nominal trajectory
r = q
total_time_test = total_time - r / frequency
number_steps_test = number_steps - r
tspan_test = np.linspace(0, total_time_test, number_steps_test)
dynamics = DuffingOscillatorDynamics(delta, alpha, beta, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, 'Nominal Trajectory', total_time, frequency, signal_shape='External', data=nominal_output_signal.state), nominal_u=DiscreteSignal(dynamics.input_dimension, 'Nominal Input Signal', total_time, frequency, signal_shape='External', data=nominal_input_signal.u(tspan)), dt=1/frequency)


# Create System
initial_states = [(np.array([0.1, -0.2]), 0)]
nominal_system_d = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System Discrete', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


# Output Signal
nominal_input_signal_d = DiscreteSignal(dynamics.input_dimension, 'Nominal Input Signal', total_time_test, frequency, signal_shape='Sinusoid', magnitude_sinusoid=[gamma], frequency_sinusoid=[omega / (2 * np.pi)], phase_sinusoid=[phi])
nominal_output_signal_test = OutputSignal(nominal_input_signal_d, nominal_system_d, 'Nominal Output Signal Test')


# Free Decay Experiments
number_free_decay_experiments = q * dynamics.input_dimension
free_decay_systems = []
free_decay_input_signals = []
for i in range(number_free_decay_experiments):
    initial_state = np.random.randn(dynamics.state_dimension)
    free_decay_systems.append(DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_state , 0)], 'Free Decay Experiments System ' + str(i), dynamics.A, dynamics.B, dynamics.C, dynamics.D))
    free_decay_input_signals.append(DiscreteSignal(dynamics.input_dimension, 'Free Decay Experiments Input Signal ' + str(i), total_time_test, frequency))
free_decay_experiments = Experiments(free_decay_systems, free_decay_input_signals)


# Forced Experiments
number_forced_experiments = round(dynamics.input_dimension + max(p + 1 + q - 1, deadbeat_order) * (dynamics.input_dimension + dynamics.output_dimension)) + 1
forced_response_systems = []
forced_response_input_signals = []
mag = 0.1 * np.random.randn(number_forced_experiments)
for i in range(number_forced_experiments):
    data = mag[i] * chirp(tspan_test, f0=0.1 + i, f1=500 + 100*i, t1=4, method='linear')
    forced_response_systems.append(DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.zeros(dynamics.state_dimension), 0)], 'Forced Experiments System ' + str(i), dynamics.A, dynamics.B, dynamics.C, dynamics.D))
    forced_response_input_signals.append(DiscreteSignal(dynamics.input_dimension, 'Forced Experiments Input Signal ' + str(i), total_time_test, frequency, signal_shape='External', data=data))
    #forced_response_input_signals.append(DiscreteSignal(dynamics.input_dimension, 'Forced Experiments Input Signal ' + str(i), total_time_test, frequency, signal_shape='White Noise'))
forced_experiments = Experiments(forced_response_systems, forced_response_input_signals)


# Full Experiment
full_system = [nominal_system_d]
full_input_signal = [DiscreteSignal(dynamics.input_dimension, 'Input Signal', total_time_test, frequency, signal_shape='White Noise')]
full_experiment = Experiments(full_system, full_input_signal)


# Plotting Experiments
plotSignals([free_decay_experiments.output_signals, forced_experiments.output_signals, full_experiment.output_signals], 1)


# TVOKID
okid = TVOKIDObserver(forced_experiments, free_decay_experiments, p, q, deadbeat_order)


# TVERA
tvera = TVERA(okid.Y, okid.hki, okid.D, full_experiment, dynamics.state_dimension, p, q, apply_transformation=True)


# Identified System
system_id = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(tvera.x0, 0)], 'System ID', tvera.A, tvera.B, tvera.C, tvera.D)


# Test Signal
test_signal = DiscreteSignal(dynamics.input_dimension, 'Test Signal', total_time_test, frequency, signal_shape='White Noise')


# True Output
output_signal = OutputSignal(test_signal, nominal_system_d, 'True Output')


# Identified Output
output_signal_id = OutputSignal(test_signal, system_id, 'Identified Output')


# Plotting Output Signals
plotSignals([[output_signal, output_signal_id], [subtract2Signals(output_signal, output_signal_id)]], 2, percentage=0.9)


# True Corrected System
corrected_system = correctSystemForEigenvaluesCheck(nominal_system_d, full_input_signal[0].number_steps - q, p)


# Identified Corrected System
corrected_system_id = correctSystemForEigenvaluesCheck(system_id, full_input_signal[0].number_steps - q, p)


# Plot Eigenvalues
plotHistoryEigenValues2Systems([corrected_system, corrected_system_id], full_input_signal[0].number_steps - q, 3)
