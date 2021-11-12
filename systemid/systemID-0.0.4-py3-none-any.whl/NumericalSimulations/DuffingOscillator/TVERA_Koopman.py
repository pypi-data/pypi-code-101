"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np
import scipy.special
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from numpy import linalg as LA
from scipy import signal

from ClassesDynamics.ClassDuffingOscillatorDynamics import DuffingOscillatorDynamics
from SystemIDAlgorithms.DepartureDynamics import departureDynamics
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, addSignals, subtract2Signals, stackSignals
from Plotting.PlotSignals import plotSignals
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassMarkovParameters import TVOKIDObserver
from ClassesSystemID.ClassERA import TVERA
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck
from SystemIDAlgorithms.CreateAugmentedSignal import createAugmentedSignalPolynomialBasisFunctions, createAugmentedSignalWithGivenFunctions



## Parameters for Dynamics
def delta(t):
    return  0.2 + 0.2*np.sin(2*np.pi*2*t)
def alpha(t):
    return  1 + 0.1*np.sin(2*np.pi*3*t + np.pi/2)
def beta(t):
    return  -1 + 0.1*np.sin(2*np.pi*4*t + np.pi)



## Import Dynamics
dynamics = DuffingOscillatorDynamics(delta, alpha, beta)



## Parameters for identification
total_time = 11
frequency = 10
number_steps = int(total_time * frequency) + 1
tspan = np.round(np.linspace(0, total_time, number_steps), decimals=2)
# order = 5
# max_order = order
# augmented_state_dimension = 0
# augmented_output_dimension = 0
# augmented_input_dimension = 0
# for i in range(1, max_order + 1):
#     augmented_state_dimension += int(scipy.special.binom(dynamics.state_dimension + i - 1, i))
#     augmented_output_dimension += int(scipy.special.binom(dynamics.output_dimension + i - 1, i))
#     augmented_input_dimension += int(scipy.special.binom(dynamics.input_dimension + i - 1, i))
augmented_state_dimension = 2
augmented_output_dimension = 2
augmented_input_dimension = 1
p, q = getOptimizedHankelMatrixSize(augmented_state_dimension, augmented_output_dimension, augmented_input_dimension)
deadbeat_order = max(augmented_state_dimension, 10)

# p = max(p, 10)
# q = max(q, 10)



## Number Experiments
number_free_decay_experiments = q * augmented_input_dimension + 10
number_forced_response_experiments = round(augmented_input_dimension + max(p + 1 + q - 1, deadbeat_order) * (augmented_input_dimension + augmented_output_dimension)) + 10



## Create System
initial_states = [([0.1, -0.2], 0)]
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)



## Nominal Input Signal
def u_nom(t):
    return  0.1 * signal.square(2 * np.pi * t)
nominal_input_signal = ContinuousSignal(dynamics.input_dimension, signal_shape='External', u=u_nom)



## Nominal Output Signal
nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan)
# plotSignals([[nominal_output_signal]], num=1)



## Update dynamics with nominal trajectory
r = 1
total_time_test = total_time - r / frequency
number_steps_test = number_steps - r
tspan_test = tspan[:-r]
tspan_test = np.round(tspan_test, decimals=2)
#dynamics = DuffingOscillatorDynamics(delta, alpha, beta, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, 'Nominal Trajectory', total_time, frequency, signal_shape='External', data=nominal_output_signal.state), nominal_u=DiscreteSignal(dynamics.input_dimension, 'Nominal Input Signal', total_time, frequency, signal_shape='External', data=nominal_input_signal.u(tspan)), dt=1/frequency)
nominal_output_signal_test = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan_test)



## Deviations dx0
deviations_dx0 = []
for i in range(number_free_decay_experiments):
    deviations_dx0.append(0.05 * np.random.randn(dynamics.state_dimension))



## Deviations du
deviations_input_signal = []
random_inputs_numbers = 0.2 * np.random.randn(number_forced_response_experiments, number_steps - 1)
for i in range(number_forced_response_experiments):
    def make_du(i):
        def du(t):
            if type(t) == float:
                return random_inputs_numbers[i, int(t * frequency)]
            else:
                return random_inputs_numbers[i, :]
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



# ## Append state to input
# for i in range(forced_response_experiments_deviated.number_experiments):
#     forced_response_experiments_deviated.input_signals[i] = stackSignals([forced_response_experiments_deviated.input_signals[i], forced_response_experiments_deviated.output_signals[i]])
# for i in range(full_experiment_deviated.number_experiments):
#     full_experiment_deviated.input_signals[i] = stackSignals([full_experiment_deviated.input_signals[i], full_experiment_deviated.output_signals[i]])




## Koopman with given basis functions
# functions = [lambda x: x[1] - x[0]]
# for i in range(free_decay_experiments_deviated.number_experiments):
#     # free_decay_experiments_deviated.output_signals[i] = createAugmentedSignalPolynomialBasisFunctions(free_decay_experiments_deviated.output_signals[i], order, True, max_order)
#     free_decay_experiments_deviated.output_signals[i] = createAugmentedSignalWithGivenFunctions(free_decay_experiments_deviated.output_signals[i], functions)
# for i in range(forced_response_experiments_deviated.number_experiments):
#     # forced_response_experiments_deviated.output_signals[i] = createAugmentedSignalPolynomialBasisFunctions(forced_response_experiments_deviated.output_signals[i], order, True, max_order)
#     forced_response_experiments_deviated.output_signals[i] = createAugmentedSignalWithGivenFunctions(forced_response_experiments_deviated.output_signals[i], functions)
#     # forced_response_experiments_deviated.input_signals[i] = createAugmentedSignalPolynomialBasisFunctions(forced_response_experiments_deviated.input_signals[i], order, True, max_order)
# for i in range(full_experiment_deviated.number_experiments):
#     # full_experiment_deviated.output_signals[i] = createAugmentedSignalPolynomialBasisFunctions(full_experiment_deviated.output_signals[i], order, True, max_order)
#     full_experiment_deviated.output_signals[i] = createAugmentedSignalWithGivenFunctions(full_experiment_deviated.output_signals[i], functions)
#     # full_experiment_deviated.input_signals[i] = createAugmentedSignalPolynomialBasisFunctions(full_experiment_deviated.input_signals[i], order, True, max_order)
# free_decay_experiments_deviated.output_dimension = free_decay_experiments_deviated.output_signals[0].dimension
# forced_response_experiments_deviated.output_dimension = forced_response_experiments_deviated.output_signals[0].dimension
# # forced_response_experiments_deviated.input_dimension = forced_response_experiments_deviated.input_signals[0].dimension
# full_experiment_deviated.output_dimension = full_experiment_deviated.output_signals[0].dimension
# # full_experiment_deviated.input_dimension = full_experiment_deviated.input_signals[0].dimension



# TVOKID
okid = TVOKIDObserver(forced_response_experiments_deviated, free_decay_experiments_deviated, p, q, deadbeat_order)


# TVERA
tvera = TVERA(okid.Y, okid.hki, okid.D, full_experiment_deviated, augmented_state_dimension, p, q, apply_transformation=True)


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


# Test System
test_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_states[0][0] + full_deviation_dx0, 0)], 'Test System', dynamics.F, dynamics.G)


# True Output Signal
true_output_signal = OutputSignal(test_input_signal, test_system, tspan=tspan_test)


# Identified System
identified_system = DiscreteLinearSystem(frequency, augmented_state_dimension, augmented_input_dimension, augmented_output_dimension, [(tvera.x0, 0)], 'System ID', tvera.A, tvera.B, tvera.C, tvera.D)


# Identified Output Signal
# test_deviation_input_signal = createAugmentedSignalWithGivenFunctions(test_deviation_input_signal, [lambda x: x[0] ** 2])
identified_deviated_signal_augmented = OutputSignal(test_deviation_input_signal, identified_system)
identified_deviated_signal = DiscreteSignal(dynamics.output_dimension, total_time_test, frequency, signal_shape='External', data=identified_deviated_signal_augmented.data[0:2, :])
identified_output_signal = addSignals([nominal_output_signal_test, identified_deviated_signal])


# Linearized System
#linearized_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(full_deviation_dx0, 0)], 'System Linearized', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


# Linearized Output Signal
#linearized_output_signal = add2Signals(nominal_output_signal_test, OutputSignal(full_deviation_input_signal_d, linearized_system, 'Linearized Deviation Output Signal'))


# Plotting
plotSignals([[nominal_output_signal, true_output_signal, identified_output_signal], [subtract2Signals(true_output_signal, identified_output_signal)]], 5, percentage=0.2)
#plotSignals([[true_output_signal, identified_output_signal, linearized_output_signal], [subtract2Signals(true_output_signal, identified_output_signal), subtract2Signals(true_output_signal, linearized_output_signal)]], 5, percentage=0.2)


# # True Corrected System
# corrected_system = correctSystemForEigenvaluesCheck(nominal_system_d, number_steps_test - p, p)
#
# # Identified Corrected System
# corrected_system_id = correctSystemForEigenvaluesCheck(identified_system, number_steps_test - p, p)
#
# # Linearized Corrected System
# corrected_system_linearized = correctSystemForEigenvaluesCheck(linearized_system, number_steps_test - p, p)



# plotSignals([forced_response_experiments_deviated.input_signals[10:], [nominal_output_signal_test] + forced_response_experiments.output_signals[10:], forced_response_experiments_deviated.output_signals[10:]], 11)
# plotSignals([free_decay_experiments_deviated.input_signals[0:4], free_decay_experiments_deviated.output_signals[0:4], free_decay_experiments.output_signals[0:4]], 12)
# plotSignals([[true_output_signal]], 13)

# plotSignals([[nominal_output_signal] + free_decay_experiments.output_signals, [nominal_output_signal] + forced_response_experiments.output_signals, [nominal_output_signal] + full_experiment.output_signals], 11)
# plotSignals([free_decay_experiments_deviated.input_signals[0:1], forced_response_experiments_deviated.input_signals[0:1], full_experiment_deviated.input_signals], 12)
# plotSignals([free_decay_experiments_deviated.output_signals, forced_response_experiments_deviated.output_signals, full_experiment_deviated.output_signals], 13)


#Mk = timeVaryingObserverKalmanIdentificationAlgorithmObserver(forced_response_experiments_deviated, p, q, deadbeat_order, 2)



#plotHistoryEigenValues2Systems([corrected_system_linearized, corrected_system_id], number_steps_test - p, 23)














########################################################################################################################
#############                                     PLOTTING                                                 #############
########################################################################################################################


import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns

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

plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"], "font.size":11})
rc('text', usetex=True)


## Convex Shape training
fig = plt.figure(1, figsize=(5, 5))
ax = plt.subplot(111)
ax.plot(forced_response_experiments.output_signals[0].data[0, :], forced_response_experiments.output_signals[0].data[1, :], '-', color=colors[9], label='Training (forced resp. exp.)')
for i in range(1, number_forced_response_experiments):
    ax.plot(forced_response_experiments.output_signals[i].data[0, :], forced_response_experiments.output_signals[i].data[1, :], '-', color=colors[9])
ax.plot(nominal_output_signal.data[0, :], nominal_output_signal.data[1, :], '-', color=colors[0], label='Nominal')
ax.plot(true_output_signal.data[0, :], true_output_signal.data[1, :], '-', color=colors[6], label='True')
ax.plot(identified_output_signal.data[0, 0:90], identified_output_signal.data[1, 0:90], '--', color=colors[7], label='Identified')
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fancybox=True, shadow=True)
# plt.tight_layout()
# plt.savefig('q1_L260_TVK.eps', format='eps')
plt.show()





















