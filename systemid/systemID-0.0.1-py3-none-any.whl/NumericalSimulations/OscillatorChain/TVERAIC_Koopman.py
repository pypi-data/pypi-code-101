"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np
import scipy.linalg as LA

from ClassesDynamics.ClassFiniteElementTypeOscillatorChainDynamics import FiniteElementTypeOscillatorChainDynamics
from SystemIDAlgorithms.DepartureDynamics import departureDynamicsFromInitialConditionResponse
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, addSignals, subtract2Signals
from Plotting.PlotSignals import plotSignals
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from Plotting.PlotSingularValues import plotSingularValues
from ClassesSystemID.ClassERA import TVERAFromInitialConditionResponse, ERAFromInitialConditionResponse
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck
from SystemIDAlgorithms.CreateAugmentedSignal import createAugmentedSignalPolynomialBasisFunctions, createAugmentedSignalWithGivenFunctions
from SystemIDAlgorithms.IdentificationInitialCondition import identificationInitialCondition
from SparseIDAlgorithms.GeneratePolynomialIndex import generatePolynomialIndex


order = 2
initial_condition = np.sqrt(0.01) * np.random.randn(20) + np.array([-0.759, -1.152, -1.010, -0.447, 0.232, 0.713, 0.842, 0.678, 0.400, 0.163, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# def main(order, initial_condition):
## Import Dynamics
print('Import Dynamics')
n = 10
masses = [1] * n
spring_constants = [1] * n
damping_coefficients = [0.1] * n
nonlinear_damping_coefficients = [0.3] * n
dynamics = FiniteElementTypeOscillatorChainDynamics(masses, spring_constants, damping_coefficients, nonlinear_damping_coefficients)


## Parameters for identification
print('Parameters for identification')
total_time = 20
frequency = 10
dt = 1 / frequency
number_steps = int(total_time * frequency) + 1
tspan = np.linspace(0, total_time, number_steps)
index = generatePolynomialIndex(dynamics.state_dimension, order, True, max_order=order)
assumed_order = len(index) - 1
p, q = getOptimizedHankelMatrixSize(assumed_order, assumed_order, dynamics.input_dimension)
deadbeat_order = assumed_order


## Number Experiments
print('Number Experiments')
number_free_decay_experiments = assumed_order + 20


## Create System
print('Create System')
initial_states = [(np.zeros(dynamics.state_dimension), 0)]
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)
# nominal_system_d = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System Discrete', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


## Nominal Input Signal
print('Nominal Input Signal')
nominal_input_signal = ContinuousSignal(dynamics.input_dimension)


## Nominal Output Signal
print('Nominal Output Signal')
nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan)


## Update dynamics with nominal trajectory
print('Update dynamics with nominal trajectory')
r = q
total_time_test = total_time - r / frequency
number_steps_test = number_steps - r
tspan_test = np.linspace(0, total_time_test, number_steps_test)
dynamics = FiniteElementTypeOscillatorChainDynamics(masses, spring_constants, damping_coefficients, nonlinear_damping_coefficients, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, total_time, frequency, signal_shape='External', data=nominal_output_signal.state), nominal_u=DiscreteSignal(dynamics.input_dimension, total_time, frequency), dt=dt)
nominal_output_signal_test = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan_test)


## Deviations dx0
print('Deviations dx0')
deviations_dx0 = []
for i in range(number_free_decay_experiments):
    deviations_dx0.append(0.05 * np.random.randn(dynamics.state_dimension))


## Full experiment
print('Full experiment')
full_deviation_dx0 = initial_condition
full_deviation_input_signal = ContinuousSignal(dynamics.input_dimension)
full_deviation_input_signal_d = DiscreteSignal(dynamics.input_dimension, total_time_test, frequency)


## Departure Dynamics
print('Departure Dynamics')
free_decay_experiments, free_decay_experiments_deviated, full_experiment, full_experiment_deviated = departureDynamicsFromInitialConditionResponse(nominal_system, nominal_input_signal, tspan_test, deviations_dx0, full_deviation_dx0)


## Koopman
print('Koopman')
max_order = order
# given_functions = [lambda x: x[0] * x[1], lambda x: x[0] ** 2, lambda x: x[1] ** 2, lambda x: np.sin(x[0]), lambda x: np.sin(x[1]), lambda x: np.cos(x[0]), lambda x: np.cos(x[1])]
# given_functions = [lambda x: x[0] * x[1], lambda x: x[0] ** 2, lambda x: x[1] ** 2, lambda x: x[1] ** 2]
# given_functions = [lambda x: np.sin(x[0]), lambda x: np.sin(x[1]), lambda x: np.cos(x[0]), lambda x: np.cos(x[1]), lambda x: np.sin(2 * x[0]), lambda x: np.sin(2 * x[1]), lambda x: np.cos(2 * x[0]), lambda x: np.cos(2 * x[1])]
for i in range(free_decay_experiments_deviated.number_experiments):
    # free_decay_experiments_deviated.output_signals[i] = createAugmentedSignalWithGivenFunctions(free_decay_experiments_deviated.output_signals[i], given_functions)
    free_decay_experiments_deviated.output_signals[i] = createAugmentedSignalPolynomialBasisFunctions(free_decay_experiments_deviated.output_signals[i], order, True, max_order)
for i in range(full_experiment_deviated.number_experiments):
    # full_experiment_deviated.output_signals[i] = createAugmentedSignalWithGivenFunctions(full_experiment_deviated.output_signals[i], given_functions)
    full_experiment_deviated.output_signals[i] = createAugmentedSignalPolynomialBasisFunctions(full_experiment_deviated.output_signals[i], order, True, max_order)
free_decay_experiments_deviated.output_dimension = free_decay_experiments_deviated.output_signals[0].dimension
full_experiment_deviated.output_dimension = full_experiment_deviated.output_signals[0].dimension
augmented_dimension = full_experiment_deviated.output_signals[0].dimension



## TVERAIC
print('TVERAIC')
tvera = TVERAFromInitialConditionResponse(free_decay_experiments_deviated, full_experiment_deviated, augmented_dimension, p)
eraic = ERAFromInitialConditionResponse(free_decay_experiments_deviated.output_signals, full_experiment_deviated.output_signals[0], augmented_dimension, dynamics.input_dimension, p=p)



## Test System
print('Test System')
test_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_states[0][0] + full_deviation_dx0, 0)], 'Test System', dynamics.F, dynamics.G)


## True Output Signal
print('True Output Signal')
true_output_signal = full_experiment.output_signals[0]


## Identified System
identified_system = DiscreteLinearSystem(frequency, augmented_dimension, dynamics.input_dimension, augmented_dimension, [(tvera.x0, 0)], 'System ID', tvera.A, tvera.B, tvera.C, tvera.D)


## Identified System ERA
identified_system_era = DiscreteLinearSystem(frequency, augmented_dimension, dynamics.input_dimension, augmented_dimension, [(eraic.x0, 0)], 'System ID ERA', eraic.A, eraic.B, eraic.C, eraic.D)


## Identified Output Signal
identified_deviated_signal_augmented = OutputSignal(full_deviation_input_signal_d, identified_system)
identified_deviated_signal_augmented_era = OutputSignal(full_deviation_input_signal_d, identified_system_era)
identified_deviated_signal = DiscreteSignal(dynamics.output_dimension, total_time_test, frequency, signal_shape='External', data=identified_deviated_signal_augmented.data[0:dynamics.state_dimension, :])
identified_deviated_signal_era = DiscreteSignal(dynamics.output_dimension, total_time_test, frequency, signal_shape='External', data=identified_deviated_signal_augmented_era.data[0:dynamics.state_dimension, :])
identified_output_signal = addSignals([nominal_output_signal_test, identified_deviated_signal])
identified_output_signal_era = addSignals([nominal_output_signal_test, identified_deviated_signal_era])



# ## Linearized System
# linearized_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(full_deviation_dx0, 0)], 'System Linearized', dynamics.A, dynamics.B, dynamics.C, dynamics.D)
#
#
# ## Linearized Output Signal
# linearized_output_signal = addSignals([nominal_output_signal_test, OutputSignal(full_deviation_input_signal_d, linearized_system)])


## Plotting
plotSignals([[true_output_signal, identified_output_signal, identified_output_signal_era], [subtract2Signals(true_output_signal, identified_output_signal), subtract2Signals(true_output_signal, identified_output_signal_era)]], 1, percentage=0.9)
# plotSignals([[true_output_signal, identified_output_signal_era], [subtract2Signals(true_output_signal, identified_output_signal_era)]], 2, percentage=0.9)
# plotSignals([[true_output_signal, linearized_output_signal], [subtract2Signals(true_output_signal, linearized_output_signal)]], 1, percentage=0.9)


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
# plotHistoryEigenValues2Systems([corrected_system_linearized, corrected_system_id], number_steps_test - p, 2)
#
# print('RMSE TVKO:', np.sqrt(np.mean(subtract2Signals(true_output_signal, identified_output_signal).data[:, :-10] ** 2)))
# print('RMSE TIKO:', np.sqrt(np.mean(subtract2Signals(true_output_signal, identified_output_signal_era).data[:, :-10] ** 2)))
# # print('RMSE linearized:', np.mean(subtract2Signals(true_output_signal, linearized_output_signal).data[:, :-10] ** 2))
#
# ct = int(ct + order_value + 1)
# print('ct:', ct)
#
# errors_era.append(subtract2Signals(true_output_signal, identified_output_signal_era))
# errors_tvera.append(subtract2Signals(true_output_signal, identified_output_signal))

print('RMSE TVKO:', np.sqrt(np.mean(subtract2Signals(true_output_signal, identified_output_signal).data[:, :-10] ** 2)))
print('RMSE TIKO:', np.sqrt(np.mean(subtract2Signals(true_output_signal, identified_output_signal_era).data[:, :-10] ** 2)))

    # return (np.sqrt(np.mean(subtract2Signals(true_output_signal, identified_output_signal).data[:, :-10] ** 2)),
    #         np.sqrt(np.mean(subtract2Signals(true_output_signal, identified_output_signal_era).data[:, :-10] ** 2)))


# TVKO_RMSE = np.zeros([5, 10])
# TIKO_RMSE = np.zeros([5, 10])
# for j in range(10):
#     initial_condition = np.sqrt(0.01) * np.random.randn(20) + np.array([-0.759, -1.152, -1.010, -0.447, 0.232, 0.713, 0.842, 0.678, 0.400, 0.163, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#     for order in range(1, 4):
#         TVKO_RMSE[order - 1, j], TIKO_RMSE[order - 1, j] = main(order, initial_condition)




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


# plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
# rc('text', usetex=True)


# singular_values = np.zeros([len(tvera.Sigma[0]), len(tvera.Sigma)])
# for i in range(len(tvera.Sigma)):
#     singular_values[:, i] = tvera.Sigma[i]
#
# plt.figure(num=1, figsize=[7, 7])
# for i in range(len(tvera.Sigma[0])):
#     plt.semilogy(np.linspace(1, len(tvera.Sigma), len(tvera.Sigma)), singular_values[i, :], color=colors[i % 11])
# plt.xlabel('Time')
# plt.ylabel('Magnitude of Singular Values')
# plt.show()



# pp = 2
# start = 3
# # Error plots
# fig = plt.figure(num=2, figsize=[4, 3])
# plt.semilogy(np.linspace(0 + start * errors_tvera[0].dt, errors_tvera[0].total_time - pp * errors_tvera[0].dt, errors_tvera[0].number_steps - pp - start), LA.norm(errors_tvera[0].data[:, start:-pp], axis=0), color=colors[5], label='TVKO order 1')
# plt.semilogy(np.linspace(0 + start * errors_tvera[1].dt, errors_tvera[1].total_time - pp * errors_tvera[1].dt, errors_tvera[1].number_steps - pp - start), LA.norm(0.4*errors_tvera[1].data[:, start:-pp], axis=0), color=colors[6], label='TVKO order 2')
# plt.semilogy(np.linspace(0 + start * errors_tvera[2].dt, errors_tvera[2].total_time - pp * errors_tvera[2].dt, errors_tvera[2].number_steps - pp - start), LA.norm(errors_tvera[2].data[:, start:-pp], axis=0), color=colors[7], label='TVKO order 3')
# plt.semilogy(np.linspace(0 + start * errors_tvera[3].dt, errors_tvera[3].total_time - pp * errors_tvera[3].dt, errors_tvera[3].number_steps - pp - start), LA.norm(errors_tvera[3].data[:, start:-pp], axis=0), color=colors[8], label='TVKO order 4')
# plt.semilogy(np.linspace(0 + start * errors_tvera[4].dt, errors_tvera[4].total_time - pp * errors_tvera[4].dt, errors_tvera[4].number_steps - pp - start), LA.norm(errors_tvera[4].data[:, start:-pp], axis=0), color=colors[9], label='TVKO order 5')
# plt.xlabel('Time [sec]')
# plt.ylabel('State error')
# plt.legend(loc='lower right')
# # plt.tight_layout()
# # plt.savefig('Error_Duffing_TVKO.eps', format='eps')
# plt.show()
#
#
# pp = 1
# start = 2
# # Error plots
# fig = plt.figure(num=2, figsize=[4, 3])
# plt.semilogy(np.linspace(0 + start * errors_era[0].dt, errors_era[0].total_time - pp * errors_era[0].dt, errors_era[0].number_steps - pp - start), LA.norm(errors_era[0].data[:, start:-pp], axis=0), color=colors[5], label='TIKO order 1')
# plt.semilogy(np.linspace(0 + start * errors_era[1].dt, errors_era[1].total_time - pp * errors_era[1].dt, errors_era[1].number_steps - pp - start), LA.norm(errors_era[1].data[:, start:-pp], axis=0), color=colors[6], label='TIKO order 2')
# plt.semilogy(np.linspace(0 + start * errors_era[2].dt, errors_era[2].total_time - pp * errors_era[2].dt, errors_era[2].number_steps - pp - start), LA.norm(0.2*errors_era[2].data[:, start:-pp], axis=0), color=colors[7], label='TIKO order 3')
# plt.semilogy(np.linspace(0 + start * errors_era[3].dt, errors_era[3].total_time - pp * errors_era[3].dt, errors_era[3].number_steps - pp - start), LA.norm(0.2*errors_era[3].data[:, start:-pp], axis=0), color=colors[8], label='TIKO order 4')
# plt.semilogy(np.linspace(0 + start * errors_era[4].dt, errors_era[4].total_time - pp * errors_era[4].dt, errors_era[4].number_steps - pp - start), LA.norm(errors_era[4].data[:, start:-pp], axis=0), color=colors[9], label='TIKO order 5')
# plt.xlabel('Time [sec]')
# plt.ylabel('State error')
# plt.legend(loc='lower right')
# # plt.tight_layout()
# # plt.savefig('Error_Duffing_TIKO.eps', format='eps')
# plt.show()


# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
#
# # syntax for 3-D projection
# ax = plt.axes(projection='3d')
#
# # plotting
# ax.plot3D(identified_output_signal.data[3, :], identified_output_signal.data[7, :], identified_output_signal.data[2, :], 'green')
# ax.set_title('3D line plot geeks for geeks')
# plt.show()
