"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np


from ClassesDynamics.ClassOscillatorySystemZeroDampingDynamics import OscillatorySystemZeroDampingDynamics
from ClassesGeneral.ClassSystem import DiscreteLinearSystem
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from ClassesGeneral.ClassSignal import DiscreteSignal, OutputSignal, subtract2Signals
from ClassesGeneral.ClassExperiments import Experiments
from Plotting.PlotSignals import plotSignals
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassMarkovParameters import TVOKIDObserver
from ClassesSystemID.ClassERA import TVERA
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck



# Dynamics
dt = 0.01
dynamics = OscillatorySystemZeroDampingDynamics(dt)


# Initial Condition
x0 = np.random.randn(dynamics.state_dimension)


# Frequency and total time
frequency = 10
total_time = 10


# System
nominal_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(x0, 0)], 'Nominal System', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


# Parameters for identification
assumed_order = 4
p, q = getOptimizedHankelMatrixSize(assumed_order, dynamics.output_dimension, dynamics.input_dimension)
deadbeat_order = 5


# Free Decay Experiments
number_free_decay_experiments = q * dynamics.input_dimension
free_decay_systems = []
free_decay_input_signals = []
for i in range(number_free_decay_experiments):
    initial_state = np.random.randn(dynamics.state_dimension)
    free_decay_systems.append(DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_state , 0)], 'Free Decay Experiments System ' + str(i), dynamics.A, dynamics.B, dynamics.C, dynamics.D))
    free_decay_input_signals.append(DiscreteSignal(dynamics.input_dimension, 'Free Decay Experiments Input Signal ' + str(i), total_time, frequency))
free_decay_experiments = Experiments(free_decay_systems, free_decay_input_signals)


# Forced Experiments
number_forced_experiments = round(dynamics.input_dimension + max(p + 1 + q - 1, deadbeat_order) * (dynamics.input_dimension + dynamics.output_dimension)) + 1
forced_response_systems = []
forced_response_input_signals = []
for i in range(number_forced_experiments):
    forced_response_systems.append(DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.zeros(dynamics.state_dimension), 0)], 'Forced Experiments System ' + str(i), dynamics.A, dynamics.B, dynamics.C, dynamics.D))
    forced_response_input_signals.append(DiscreteSignal(dynamics.input_dimension, 'Forced Experiments Input Signal ' + str(i), total_time, frequency, signal_shape='White Noise'))
forced_experiments = Experiments(forced_response_systems, forced_response_input_signals)


# Full Experiment
full_system = [nominal_system]
full_input_signal = [DiscreteSignal(dynamics.input_dimension, 'Input Signal', total_time, frequency, signal_shape='White Noise')]
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
test_signal = DiscreteSignal(dynamics.input_dimension, 'Test Signal', total_time, frequency, signal_shape='White Noise')


# True Output
output_signal = OutputSignal(test_signal, nominal_system, 'True Output')


# Identified Output
output_signal_id = OutputSignal(test_signal, system_id, 'Identified Output')


# Plotting Output Signals
plotSignals([[output_signal, output_signal_id], [subtract2Signals(output_signal, output_signal_id)]], 2, percentage=0.9)


# True Corrected System
corrected_system = correctSystemForEigenvaluesCheck(nominal_system, full_input_signal[0].number_steps - q, p)


# Identified Corrected System
corrected_system_id = correctSystemForEigenvaluesCheck(system_id, full_input_signal[0].number_steps - q, p)


# Plot Eigenvalues
plotHistoryEigenValues2Systems([corrected_system, corrected_system_id], full_input_signal[0].number_steps - q, 3)
