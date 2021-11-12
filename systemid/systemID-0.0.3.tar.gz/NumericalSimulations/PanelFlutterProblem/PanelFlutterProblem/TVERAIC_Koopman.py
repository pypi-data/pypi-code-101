"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np
import cmath
import scipy.linalg as LA

from SystemIDAlgorithms.GetObservabilityMatrix import getObservabilityMatrix
from ClassesDynamics.ClassPanelFlutterDynamics import PanelFlutterDynamics
from SystemIDAlgorithms.DepartureDynamics import departureDynamicsFromInitialConditionResponse
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, addSignals, subtract2Signals
from Plotting.PlotSignals import plotSignals
from Plotting.PlotEigenValues import plotHistoryEigenValues1System
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassERA import TVERAFromInitialConditionResponse
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck
from NumericalSimulations.PanelFlutterProblem.PanelFlutterProblem.PlotFormating import plotResponse3, plotEigenValues, plotSVD
from SystemIDAlgorithms.CreateAugmentedSignal import createAugmentedSignalPolynomialBasisFunctions, createAugmentedSignalWithGivenFunctions



# lambdaa = np.linspace(260, 300, 41)
#
# for l_val in lambdaa:
#
#     print('Lambda =', l_val)
#
#
#
#
#
#     # Parameters for Dynamics
#     print('Define Parameters')
#     def RT(t):
#         return 0
#     def mu(t):
#         return 0.01
#     def M(t):
#         return 5
#     def l(t):
#         return l_val
#
#
#     # Import Dynamics
#     print('Import Dynamics')
#     dynamics = PanelFlutterDynamics(RT, mu, M, l)
#
#
#     # Parameters for identification
total_time = 120
frequency = 100
dt = 1 / frequency
number_steps = int(total_time * frequency) + 1
tspan = np.linspace(0, total_time, number_steps)
assumed_order = 4
p = 4
#
#
#     # Number Experiments
#     print('Set Number of Experiments')
#     number_free_decay_experiments = 20 + 20
#
#
#     # Create System
#     print('Create Nominal System')
#     initial_states = [(np.array([0, 0, 0, 0]), 0)]
#     nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)
#     nominal_system_d = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System Discrete', dynamics.A, dynamics.B, dynamics.C, dynamics.D)
#
#
#     # Nominal Input Signal
#     print('Create Nominal Input Signal')
#     nominal_input_signal = ContinuousSignal(dynamics.input_dimension)
#
#
#     # Nominal Output Signal
#     print('Create Nominal Output Signal')
#     nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan)
#
#
#     # Plot Output Signal
#     # plotSignals([[nominal_output_signal]], 2, percentage=0.9)
#
#
#
#
#     # Update dynamics with nominal trajectory
#     print('Update Linearized Dynamics with Nominal Trajectory')
r = p
total_time_test = total_time - r / frequency
number_steps_test = number_steps - r
tspan_test = np.linspace(0, total_time_test, number_steps_test)
#     dynamics = PanelFlutterDynamics(RT, mu, M, l, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, total_time, frequency, signal_shape='External', data=nominal_output_signal.state), nominal_u=DiscreteSignal(dynamics.input_dimension, total_time, frequency), dt=1/frequency)
#     nominal_output_signal_test = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan_test)
#
#
#     # Deviations dx0
#     print('Generate dx0')
#     deviations_dx0 = []
#     for i in range(number_free_decay_experiments):
#         deviations_dx0.append(np.array([0.000805 + 0.00001 * i, 0, 0, 0]))
#         # deviations_dx0.append(np.array([0.001 + 0.0002 * np.random.randn(), 0, 0, 0]))
#
#
#     # Full experiment
#     print('Full Experiment')
#     full_deviation_dx0 = np.array([0.001, 0, 0, 0])
#     # full_deviation_dx0 = 0.00001 * np.random.randn(dynamics.state_dimension)
#     full_deviation_input_signal = ContinuousSignal(dynamics.input_dimension)
#     full_deviation_input_signal_d = DiscreteSignal(dynamics.input_dimension, total_time_test, frequency)
#
#
#     # Departure Dynamics
#     print('Departure Dynamics')
#     free_decay_experiments, free_decay_experiments_deviated, full_experiment, full_experiment_deviated = departureDynamicsFromInitialConditionResponse(nominal_system, nominal_input_signal, tspan_test, deviations_dx0, full_deviation_dx0)
#
#
#     # Koopman with given basis functions
#     print('Koopman')
#     order = 1
#     max_order = order
#     for i in range(free_decay_experiments_deviated.number_experiments):
#         # print(i)
#         # free_decay_experiments_deviated.output_signals[i] = createAugmentedSignalWithGivenFunctions(free_decay_experiments_deviated.output_signals[i], given_functions)
#         free_decay_experiments_deviated.output_signals[i] = createAugmentedSignalPolynomialBasisFunctions(free_decay_experiments_deviated.output_signals[i], order, True, max_order)
#     for i in range(full_experiment_deviated.number_experiments):
#         # full_experiment_deviated.output_signals[i] = createAugmentedSignalWithGivenFunctions(full_experiment_deviated.output_signals[i], given_functions)
#         full_experiment_deviated.output_signals[i] = createAugmentedSignalPolynomialBasisFunctions(full_experiment_deviated.output_signals[i], order, True, max_order)
#     free_decay_experiments_deviated.output_dimension = free_decay_experiments_deviated.output_signals[0].dimension
#     full_experiment_deviated.output_dimension = full_experiment_deviated.output_signals[0].dimension
#     augmented_dimension = full_experiment_deviated.output_signals[0].dimension
#
#
#     # TVERAIC
#     print('TVERAIC')
#     tvera = TVERAFromInitialConditionResponse(free_decay_experiments_deviated, full_experiment_deviated, augmented_dimension, p)
#
#
#     # Test System
#     print('Test System')
#     test_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_states[0][0] + full_deviation_dx0, 0)], 'Test System', dynamics.F, dynamics.G)
#
#
#     # True Output Signal
#     print('True Output Signal')
#     true_output_signal = full_experiment.output_signals[0]
#
#
#     # Identified System
#     print('Identified System')
#     identified_system = DiscreteLinearSystem(frequency, augmented_dimension, dynamics.input_dimension, augmented_dimension, [(tvera.x0, 0)], 'System ID', tvera.A, tvera.B, tvera.C, tvera.D)
#
#
#     # Identified Output Signal
#     print('Identified Output Signal')
#     identified_deviated_signal_augmented = OutputSignal(full_deviation_input_signal_d, identified_system)
#     identified_deviated_signal = DiscreteSignal(dynamics.output_dimension, total_time_test, frequency, signal_shape='External', data=identified_deviated_signal_augmented.data[0:4, :])
#     identified_output_signal = addSignals([nominal_output_signal_test, identified_deviated_signal])
#
#
#     # # Linearized System
#     # linearized_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(full_deviation_dx0, 0)], 'System Linearized', dynamics.A, dynamics.B, dynamics.C, dynamics.D)
#     #
#     #
#     # # Linearized Output Signal
#     # linearized_output_signal = addSignals([nominal_output_signal_test, OutputSignal(full_deviation_input_signal_d, linearized_system)])
#     #
#     #
#     # # Plotting
#     # # plotSignals([[true_output_signal, identified_output_signal], [subtract2Signals(true_output_signal, identified_output_signal)]], 1, percentage=0.9)
#     #
#     #
#     # # True Corrected System
#     # corrected_system = correctSystemForEigenvaluesCheck(nominal_system_d, number_steps_test - p, p)
#     #
#     # # Identified Corrected System
#     # corrected_system_id = correctSystemForEigenvaluesCheck(identified_system, number_steps_test - p, p)
#     #
#     # # Linearized Corrected System
#     # corrected_system_linearized = correctSystemForEigenvaluesCheck(linearized_system, number_steps_test - p, p)
#
#
#     # plotHistoryEigenValues2Systems([corrected_system_linearized, corrected_system_id], number_steps_test - p, 2)
#     # plotResponse3([true_output_signal, identified_output_signal], [subtract2Signals(true_output_signal, identified_output_signal)], tspan, 244, ['$q_1$', '$q_2$', '$q_1\'$', '$q_2\'$'], 1)
#     # plotEigenValues([corrected_system_id, corrected_system_linearized], number_steps_test - p, 2)
#
#     # time_steps = np.array([0, 1, 2, 5, 10, 20, 50, 100, 200, 240])
#     # sigma = tvera.Sigma
#     # plotSVD(sigma, time_steps, 5)
#
#     print('RMSE =', np.sqrt(((true_output_signal.data[0:2, 0:490] - identified_output_signal.data[0:2, 0:490]) ** 2).mean()))
#
#
#     np.save('S2_TVKO_order3_L' + str(l_val), true_output_signal.data[:, 0:number_steps_test - p], allow_pickle=True)
#     np.save('S2ID_TVKO_order3_L' + str(l_val), identified_output_signal.data[:, 0:number_steps_test - p], allow_pickle=True)
#
#
#     np.save('A_id_TVKO_order3_L' + str(l_val), tvera.A_id, allow_pickle=True)
#     np.save('B_id_TVKO_order3_L' + str(l_val), tvera.B_id, allow_pickle=True)
#     np.save('C_id_TVKO_order3_L' + str(l_val), tvera.C_id, allow_pickle=True)
#     np.save('D_id_TVKO_order3_L' + str(l_val), tvera.D_id, allow_pickle=True)
#     np.save('x0_id_TVKO_order3_L' + str(l_val), tvera.x0, allow_pickle=True)
#
#
#
#
#
#










########################################################################################################################
#############                                     PLOTTING                                                 #############
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

plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"], "font.size":11})
rc('text', usetex=True)
#
# tspan_plot = np.linspace(0, total_time_test - p * dt, number_steps_test - p)
#
# ## Load Data
# S2_260_1 = np.load('S2_260_1.npy')
# S2_260_2 = np.load('S2_260_2.npy')
# S2_260_3 = np.load('S2_260_3.npy')
# S2_270_1 = np.load('S2_270_1.npy')
# S2_270_2 = np.load('S2_270_2.npy')
# S2_270_3 = np.load('S2_270_3.npy')
# S2_280_1 = np.load('S2_280_1.npy')
# S2_280_2 = np.load('S2_280_2.npy')
# S2_280_3 = np.load('S2_280_3.npy')
# S2_290_1 = np.load('S2_290_1.npy')
# S2_290_2 = np.load('S2_290_2.npy')
# S2_290_3 = np.load('S2_290_3.npy')
# S2_300_1 = np.load('S2_300_1.npy')
# S2_300_2 = np.load('S2_300_2.npy')
# S2_300_3 = np.load('S2_300_3.npy')
# S2ID_260_1 = np.load('S2ID_260_1.npy')
# S2ID_260_2 = np.load('S2ID_260_2.npy')
# S2ID_260_3 = np.load('S2ID_260_3.npy')
# S2ID_270_1 = np.load('S2ID_270_1.npy')
# S2ID_270_2 = np.load('S2ID_270_2.npy')
# S2ID_270_3 = np.load('S2ID_270_3.npy')
# S2ID_280_1 = np.load('S2ID_280_1.npy')
# S2ID_280_2 = np.load('S2ID_280_2.npy')
# S2ID_280_3 = np.load('S2ID_280_3.npy')
# S2ID_290_1 = np.load('S2ID_290_1.npy')
# S2ID_290_2 = np.load('S2ID_290_2.npy')
# S2ID_290_3 = np.load('S2ID_290_3.npy')
# S2ID_300_1 = np.load('S2ID_300_1.npy')
# S2ID_300_2 = np.load('S2ID_300_2.npy')
# S2ID_300_3 = np.load('S2ID_300_3.npy')
#
# TV_S2_260_1 = np.load('TV_S2_260_1.npy')
# TV_S2_260_2 = np.load('TV_S2_260_2.npy')
# TV_S2_260_3 = np.load('TV_S2_260_3.npy')
# TV_S2_270_1 = np.load('TV_S2_270_1.npy')
# TV_S2_270_2 = np.load('TV_S2_270_2.npy')
# TV_S2_270_3 = np.load('TV_S2_270_3.npy')
# TV_S2_280_1 = np.load('TV_S2_280_1.npy')
# TV_S2_280_2 = np.load('TV_S2_280_2.npy')
# TV_S2_280_3 = np.load('TV_S2_280_3.npy')
# TV_S2_290_1 = np.load('TV_S2_290_1.npy')
# TV_S2_290_2 = np.load('TV_S2_290_2.npy')
# TV_S2_290_3 = np.load('TV_S2_290_3.npy')
# TV_S2_300_1 = np.load('TV_S2_300_1.npy')
# TV_S2_300_2 = np.load('TV_S2_300_2.npy')
# TV_S2_300_3 = np.load('TV_S2_300_3.npy')
# TV_S2ID_260_1 = np.load('TV_S2ID_260_1.npy')
# TV_S2ID_260_2 = np.load('TV_S2ID_260_2.npy')
# TV_S2ID_260_3 = np.load('TV_S2ID_260_3.npy')
# TV_S2ID_270_1 = np.load('TV_S2ID_270_1.npy')
# TV_S2ID_270_2 = np.load('TV_S2ID_270_2.npy')
# TV_S2ID_270_3 = np.load('TV_S2ID_270_3.npy')
# TV_S2ID_280_1 = np.load('TV_S2ID_280_1.npy')
# TV_S2ID_280_2 = np.load('TV_S2ID_280_2.npy')
# TV_S2ID_280_3 = np.load('TV_S2ID_280_3.npy')
# TV_S2ID_290_1 = np.load('TV_S2ID_290_1.npy')
# TV_S2ID_290_2 = np.load('TV_S2ID_290_2.npy')
# TV_S2ID_290_3 = np.load('TV_S2ID_290_3.npy')
# TV_S2ID_300_1 = np.load('TV_S2ID_300_1.npy')
# TV_S2ID_300_2 = np.load('TV_S2ID_300_2.npy')
# TV_S2ID_300_3 = np.load('TV_S2ID_300_3.npy')
#
#
#
#
# fig = plt.figure(10, figsize=(5, 3))
# ax = plt.subplot(111)
# ax.plot(tspan_plot, TV_S2ID_260_3[0, :], '-', color=colors[6], label='TV Koopman order 1')
# ax.plot(tspan_plot, TV_S2ID_260_3[0, :], '-', color=colors[7], label='TV Koopman order 2')
# ax.plot(tspan_plot, TV_S2ID_260_3[0, :], '-', color=colors[8], label='TV Koopman order 3')
# ax.plot(tspan_plot, TV_S2_260_3[0, :], color=colors[0], label='True')
# plt.xlabel('Time [s]')
# plt.ylabel(r'$q_1$')
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fancybox=True, shadow=True)
# # plt.tight_layout()
# # plt.savefig('q1_L260_TVK.eps', format='eps')
# plt.show()
#
#
# fig = plt.figure(11, figsize=(5, 3))
# ax = plt.subplot(111)
# ax.plot(tspan_plot, TV_S2ID_260_1[1, :], '-', color=colors[6], label='TV Koopman order 1')
# ax.plot(tspan_plot, TV_S2ID_260_2[1, :], '-', color=colors[7], label='TV Koopman order 2')
# ax.plot(tspan_plot, TV_S2ID_260_3[1, :], '-', color=colors[8], label='TV Koopman order 3')
# ax.plot(tspan_plot, TV_S2_260_1[1, :], color=colors[0], label='True')
# plt.xlabel('Time [s]')
# plt.ylabel(r'$q_2$')
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fancybox=True, shadow=True)
# # plt.tight_layout()
# # plt.savefig('q2_L260_TVK.eps', format='eps')
# plt.show()
#
# fig = plt.figure(12, figsize=(5, 3))
# ax = plt.subplot(111)
# ax.plot(tspan_plot, TV_S2ID_280_1[0, :], '-', color=colors[6], label='TV Koopman order 1')
# ax.plot(tspan_plot, TV_S2ID_280_2[0, :], '-', color=colors[7], label='TV Koopman order 2')
# ax.plot(tspan_plot, TV_S2ID_280_3[0, :], '-', color=colors[8], label='TV Koopman order 3')
# ax.plot(tspan_plot, TV_S2_280_1[0, :], color=colors[0], label='True')
# plt.xlabel('Time [s]')
# plt.ylabel(r'$q_1$')
# # ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fancybox=True, shadow=True)
# # plt.tight_layout()
# # plt.savefig('q1_L280_TVK.eps', format='eps')
# plt.show()
#
# fig = plt.figure(13, figsize=(5, 3))
# ax = plt.subplot(111)
# ax.plot(tspan_plot, TV_S2ID_280_1[1, :], '-', color=colors[6], label='TV Koopman order 1')
# ax.plot(tspan_plot, TV_S2ID_280_2[1, :], '-', color=colors[7], label='TV Koopman order 2')
# ax.plot(tspan_plot, TV_S2ID_280_3[1, :], '-', color=colors[8], label='TV Koopman order 3')
# ax.plot(tspan_plot, TV_S2_280_1[1, :], color=colors[0], label='True')
# plt.xlabel('Time [s]')
# plt.ylabel(r'$q_2$')
# # ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fancybox=True, shadow=True)
# # plt.tight_layout()
# # plt.savefig('q2_L280_TVK.eps', format='eps')
# plt.show()
#
# fig = plt.figure(14, figsize=(5, 3))
# ax = plt.subplot(111)
# ax.plot(tspan_plot, TV_S2ID_300_1[0, :], '-', color=colors[6], label='TV Koopman order 1')
# ax.plot(tspan_plot, TV_S2ID_300_2[0, :], '-', color=colors[7], label='TV Koopman order 2')
# ax.plot(tspan_plot, TV_S2ID_300_3[0, :], '-', color=colors[8], label='TV Koopman order 3')
# ax.plot(tspan_plot, TV_S2_300_1[0, :], color=colors[0], label='True')
# plt.xlabel('Time [s]')
# plt.ylabel(r'$q_1$')
# # ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fancybox=True, shadow=True)
# # plt.tight_layout()
# # plt.savefig('q1_L300_TVK.eps', format='eps')
# plt.show()
#
# fig = plt.figure(15, figsize=(5, 3))
# ax = plt.subplot(111)
# ax.plot(tspan_plot, TV_S2ID_300_1[1, :], '-', color=colors[6], label='TV Koopman order 1')
# ax.plot(tspan_plot, TV_S2ID_300_2[1, :], '-', color=colors[7], label='TV Koopman order 2')
# ax.plot(tspan_plot, TV_S2ID_300_3[1, :], '-', color=colors[8], label='TV Koopman order 3')
# ax.plot(tspan_plot, TV_S2_300_1[1, :], color=colors[0], label='True')
# plt.xlabel('Time [s]')
# plt.ylabel(r'$q_2$')
# # ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fancybox=True, shadow=True)
# # plt.tight_layout()
# # plt.savefig('q2_L300_TVK.eps', format='eps')
# plt.show()
#
#
#
#
# fig = plt.figure(16, figsize=(11, 3))
# ax = plt.subplot(111)
#
# labels = ['260', '270', '280', '290', '300']
#
# TIK1 = [np.sqrt(((S2_260_1[0:2, :] - S2ID_260_1[0:2, :]) ** 2).mean()),
#         np.sqrt(((S2_270_1[0:2, :] - S2ID_270_1[0:2, :]) ** 2).mean()),
#         np.sqrt(((S2_280_1[0:2, :] - S2ID_280_1[0:2, :]) ** 2).mean()),
#         np.sqrt(((S2_290_1[0:2, :] - S2ID_290_1[0:2, :]) ** 2).mean()),
#         np.sqrt(((S2_300_1[0:2, :] - S2ID_300_1[0:2, :]) ** 2).mean())]
# TIK2 = [np.sqrt(((S2_260_2[0:2, :] - S2ID_260_2[0:2, :]) ** 2).mean()),
#         np.sqrt(((S2_270_2[0:2, :] - S2ID_270_2[0:2, :]) ** 2).mean()),
#         np.sqrt(((S2_280_2[0:2, :] - S2ID_280_2[0:2, :]) ** 2).mean()),
#         np.sqrt(((S2_290_2[0:2, :] - S2ID_290_2[0:2, :]) ** 2).mean()),
#         np.sqrt(((S2_300_2[0:2, :] - S2ID_300_2[0:2, :]) ** 2).mean())]
# TIK3 = [np.sqrt(((S2_260_3[0:2, :] - S2ID_260_3[0:2, :]) ** 2).mean()),
#         np.sqrt(((S2_270_3[0:2, :] - S2ID_270_3[0:2, :]) ** 2).mean()),
#         np.sqrt(((S2_280_3[0:2, :] - S2ID_280_3[0:2, :]) ** 2).mean()),
#         np.sqrt(((S2_290_3[0:2, :] - S2ID_290_3[0:2, :]) ** 2).mean()),
#         np.sqrt(((S2_300_3[0:2, :] - S2ID_300_3[0:2, :]) ** 2).mean())]
#
# TVK1 = [np.sqrt(((TV_S2_260_1[0:2, :] - TV_S2ID_260_1[0:2, :]) ** 2).mean()),
#         np.sqrt(((TV_S2_270_1[0:2, :] - TV_S2ID_270_1[0:2, :]) ** 2).mean()),
#         np.sqrt(((TV_S2_280_1[0:2, :] - TV_S2ID_280_1[0:2, :]) ** 2).mean()),
#         np.sqrt(((TV_S2_290_1[0:2, :] - TV_S2ID_290_1[0:2, :]) ** 2).mean()),
#         np.sqrt(((TV_S2_300_1[0:2, :] - TV_S2ID_300_1[0:2, :]) ** 2).mean())]
# TVK2 = [np.sqrt(((TV_S2_260_2[0:2, :] - TV_S2ID_260_2[0:2, :]) ** 2).mean()),
#         np.sqrt(((TV_S2_270_2[0:2, :] - TV_S2ID_270_2[0:2, :]) ** 2).mean()),
#         np.sqrt(((TV_S2_280_2[0:2, :] - TV_S2ID_280_2[0:2, :]) ** 2).mean()),
#         np.sqrt(((TV_S2_290_2[0:2, :] - TV_S2ID_290_2[0:2, :]) ** 2).mean()),
#         np.sqrt(((TV_S2_300_2[0:2, :] - TV_S2ID_300_2[0:2, :]) ** 2).mean())]
# TVK3 = [np.sqrt(((TV_S2_260_3[0:2, :] - TV_S2ID_260_3[0:2, :]) ** 2).mean()),
#         np.sqrt(((TV_S2_270_3[0:2, :] - TV_S2ID_270_3[0:2, :]) ** 2).mean()),
#         np.sqrt(((TV_S2_280_3[0:2, :] - TV_S2ID_280_3[0:2, :]) ** 2).mean()),
#         np.sqrt(((TV_S2_290_3[0:2, :] - TV_S2ID_290_3[0:2, :]) ** 2).mean()),
#         np.sqrt(((TV_S2_300_3[0:2, :] - TV_S2ID_300_3[0:2, :]) ** 2).mean())]
#
# x = np.arange(len(labels))  # the label locations
# width = 0.2  # the width of the bars
#
# rects1_TI = ax.bar(x - width, TIK1, width, label='TI Koopman order 1', color='white', edgecolor=colors[6])
# rects2_TI = ax.bar(x, TIK2, width, label='TI Koopman order 2', color='white', edgecolor=colors[7])
# rects3_TI = ax.bar(x + width, TIK3, width, label='TI Koopman order 3', color='white', edgecolor=colors[8])
#
# rects1_TV = ax.bar(x - width, TVK1, width, label='TV Koopman order 1', color=colors[6])
# rects2_TV = ax.bar(x, TVK2, width, label='TV Koopman order 2', color=colors[7])
# rects3_TV = ax.bar(x + width, TVK3, width, label='TV Koopman order 3', color=colors[8])
#
# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('RMS Error')
# ax.set_xlabel(r'$\lambda$')
# ax.set_xticks(x)
# ax.set_yscale('log')
# ax.set_xticklabels(labels)
# ax.legend(ncol=2)
#
# # ax.bar_label(rects1, padding=3)
# # ax.bar_label(rects2, padding=3)
# # ax.bar_label(rects3, padding=3)
#
# # plt.tight_layout()
# # plt.savefig('RMSE_L_TVIK.eps', format='eps')
#
# plt.show()











# ########################################################################################################################
# #############                                     TESTING BIFURCATION                                      #############
# ########################################################################################################################
#
# ## Parameters for Dynamics
# print('Define Parameters')
# def RT(t):
#     return 0
# def mu(t):
#     return 0.01
# def M(t):
#     return 5
# def l(t):
#     return 299
#
#
# # Import Dynamics
# print('Import Dynamics')
# dynamics = PanelFlutterDynamics(RT, mu, M, l)
#
#
# # Parameters for identification
# total_time = 10
# frequency = 50
# dt = 1 / frequency
# number_steps = int(total_time * frequency) + 1
# tspan = np.linspace(0, total_time, number_steps)
# assumed_order = 4
# p = 4
#
#
# # Number Experiments
# print('Set Number of Experiments')
# number_free_decay_experiments = 4 + 20
#
#
# # Create System
# print('Create Nominal System')
# initial_states = [(np.array([0, 0, 0, 0]), 0)]
# nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)
# nominal_system_d = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System Discrete', dynamics.A, dynamics.B, dynamics.C, dynamics.D)
#
#
# # Nominal Input Signal
# print('Create Nominal Input Signal')
# nominal_input_signal = ContinuousSignal(dynamics.input_dimension)
#
#
# # Nominal Output Signal
# print('Create Nominal Output Signal')
# nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan)
#
#
# # Plot Output Signal
# # plotSignals([[nominal_output_signal]], 2, percentage=0.9)
#
#
#
# # Update dynamics with nominal trajectory
# print('Update Linearized Dynamics with Nominal Trajectory')
# r = p
# total_time_test = total_time - r / frequency
# number_steps_test = number_steps - r
# tspan_test = np.linspace(0, total_time_test, number_steps_test)
# dynamics = PanelFlutterDynamics(RT, mu, M, l, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, total_time, frequency, signal_shape='External', data=nominal_output_signal.state), nominal_u=DiscreteSignal(dynamics.input_dimension, total_time, frequency), dt=1/frequency)
# nominal_output_signal_test = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan_test)
#
#
# # Deviations dx0
# print('Generate dx0')
# deviations_dx0 = []
# for i in range(number_free_decay_experiments):
#     deviations_dx0.append(np.array([0.001 + 0.0002 * np.random.randn(), 0, 0, 0]))
#
#
# # Full experiment
# print('Full Experiment')
# full_deviation_dx0 = np.array([0.001, 0, 0, 0])
# # full_deviation_dx0 = 0.00001 * np.random.randn(dynamics.state_dimension)
# full_deviation_input_signal = ContinuousSignal(dynamics.input_dimension)
# full_deviation_input_signal_d = DiscreteSignal(dynamics.input_dimension, total_time_test, frequency)
#
#
# # Departure Dynamics
# print('Departure Dynamics')
# free_decay_experiments, free_decay_experiments_deviated, full_experiment, full_experiment_deviated = departureDynamicsFromInitialConditionResponse(nominal_system, nominal_input_signal, tspan_test, deviations_dx0, full_deviation_dx0)
#
#
# # Koopman with given basis functions
# print('Koopman')
# order = 1
# max_order = order
# for i in range(free_decay_experiments_deviated.number_experiments):
#     print(i)
#     # free_decay_experiments_deviated.output_signals[i] = createAugmentedSignalWithGivenFunctions(free_decay_experiments_deviated.output_signals[i], given_functions)
#     free_decay_experiments_deviated.output_signals[i] = createAugmentedSignalPolynomialBasisFunctions(free_decay_experiments_deviated.output_signals[i], order, True, max_order)
# for i in range(full_experiment_deviated.number_experiments):
#     # full_experiment_deviated.output_signals[i] = createAugmentedSignalWithGivenFunctions(full_experiment_deviated.output_signals[i], given_functions)
#     full_experiment_deviated.output_signals[i] = createAugmentedSignalPolynomialBasisFunctions(full_experiment_deviated.output_signals[i], order, True, max_order)
# free_decay_experiments_deviated.output_dimension = free_decay_experiments_deviated.output_signals[0].dimension
# full_experiment_deviated.output_dimension = full_experiment_deviated.output_signals[0].dimension
# augmented_dimension = full_experiment_deviated.output_signals[0].dimension
#
#
# # TVERAIC
# print('TVERAIC')
# tvera = TVERAFromInitialConditionResponse(free_decay_experiments_deviated, full_experiment_deviated, augmented_dimension, p)
#
#
# # Test System
# print('Test System')
# test_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_states[0][0] + full_deviation_dx0, 0)], 'Test System', dynamics.F, dynamics.G)
#
#
# # True Output Signal
# print('True Output Signal')
# true_output_signal = full_experiment.output_signals[0]
#
#
# # A_id_TVK1_L298 = np.load('A_id_TVKO_order1_L298.0.npy')
# # B_id_TVK1_L298 = np.load('B_id_TVKO_order1_L298.0.npy')
# # C_id_TVK1_L298 = np.load('C_id_TVKO_order1_L298.0.npy')
# # D_id_TVK1_L298 = np.load('D_id_TVKO_order1_L298.0.npy')
# # A_id_TVK1_L300 = np.load('A_id_TVKO_order1_L300.0.npy')
# # B_id_TVK1_L300 = np.load('B_id_TVKO_order1_L300.0.npy')
# # C_id_TVK1_L300 = np.load('C_id_TVKO_order1_L300.0.npy')
# # D_id_TVK1_L300 = np.load('D_id_TVKO_order1_L300.0.npy')
# A_id_TVK1_L298 = np.load('A_id_TVK1_L298.npy')
# B_id_TVK1_L298 = np.load('B_id_TVK1_L298.npy')
# C_id_TVK1_L298 = np.load('C_id_TVK1_L298.npy')
# D_id_TVK1_L298 = np.load('D_id_TVK1_L298.npy')
# A_id_TVK1_L300 = np.load('A_id_TVK1_L300.npy')
# B_id_TVK1_L300 = np.load('B_id_TVK1_L300.npy')
# C_id_TVK1_L300 = np.load('C_id_TVK1_L300.npy')
# D_id_TVK1_L300 = np.load('D_id_TVK1_L300.npy')
#
# def A_id_TVK1_L299(t):
#     return (A_id_TVK1_L298[:, :, int(round(t * frequency))] + A_id_TVK1_L300[:, :, int(round(t * frequency))]) / 2
#
# def B_id_TVK1_L299(t):
#     return (B_id_TVK1_L298[:, :, int(round(t * frequency))] + B_id_TVK1_L300[:, :, int(round(t * frequency))]) / 2
#
# def C_id_TVK1_L299(t):
#     return (C_id_TVK1_L298[:, :, int(round(t * frequency))] + C_id_TVK1_L300[:, :, int(round(t * frequency))]) / 2
#
# def D_id_TVK1_L299(t):
#     return (D_id_TVK1_L298[:, :, int(round(t * frequency))] + D_id_TVK1_L300[:, :, int(round(t * frequency))]) / 2
#
# identified_system = DiscreteLinearSystem(frequency, augmented_dimension, dynamics.input_dimension, augmented_dimension, [(tvera.x0, 0)], 'System ID', A_id_TVK1_L299, B_id_TVK1_L299, C_id_TVK1_L299, D_id_TVK1_L299)
#
#
# # Identified Output Signal
# print('Identified Output Signal')
# identified_deviated_signal_augmented = OutputSignal(full_deviation_input_signal_d, identified_system)
# identified_deviated_signal = DiscreteSignal(dynamics.output_dimension, total_time_test, frequency, signal_shape='External', data=identified_deviated_signal_augmented.data[0:4, :])
# identified_output_signal = addSignals([nominal_output_signal_test, identified_deviated_signal])
#
#
#
#
# # Plotting
# plotSignals([[true_output_signal, identified_output_signal], [subtract2Signals(true_output_signal, identified_output_signal)]], 1, percentage=0.9)
#
# plotSignals([[identified_output_signal]], 1, percentage=0.95)









# ########################################################################################################################
# #############                                     BIFURCATION PLOT                                         #############
# ########################################################################################################################


# amp = np.zeros(41)
#
# for i in range(41):
#
#
#     ## Parameters for Dynamics
#     print('Define Parameters')
#
#
#     def RT(t):
#         return 0
#
#     def mu(t):
#         return 0.01
#
#     def M(t):
#         return 5
#
#     def l(t):
#         return 260 + i
#
#
#     # Import Dynamics
#     print('Import Dynamics')
#     dynamics = PanelFlutterDynamics(RT, mu, M, l)
#
#     # Parameters for identification
#     total_time = 10
#     frequency = 50
#     dt = 1 / frequency
#     number_steps = int(total_time * frequency) + 1
#     tspan = np.linspace(0, total_time, number_steps)
#     assumed_order = 4
#     p = 4
#
#     # Number Experiments
#     print('Set Number of Experiments')
#     number_free_decay_experiments = 4 + 20
#
#     # Create System
#     print('Create Nominal System')
#     initial_states = [(np.array([0.001, 0, 0, 0]), 0)]
#     nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)
#     nominal_system_d = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System Discrete', dynamics.A, dynamics.B, dynamics.C, dynamics.D)
#
#     # Nominal Input Signal
#     print('Create Nominal Input Signal')
#     nominal_input_signal = ContinuousSignal(dynamics.input_dimension)
#
#     # Nominal Output Signal
#     print('Create Nominal Output Signal')
#     nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan)
#
#     amp[i] = np.max(nominal_output_signal.data[0, 250:])


# fig = plt.figure(20, figsize=(5, 5))
# ax = plt.subplot(111)
# ax.plot(np.linspace(260, 300, 41), amp, '-o', color=colors[0], label='True')
# ax.plot(np.linspace(261, 299, 20), amp[1::2], 'o', mfc='none', color=colors[6], label='Identified')
# plt.xlabel(r'$\lambda$')
# plt.ylabel(r'Amplitude of oscillations for limite cycle')
# ax.legend(loc='upper left')
# plt.tight_layout()
# plt.savefig('limit_cycle.eps', format='eps')
# plt.show()

























# #######################################################################################################################
# ############                                     INTERPOLATION                                            #############
# #######################################################################################################################
#
#
#
#
# frequency = 50
#
# ## Load matrices and build true systems
# A_id_TVKO_order3 = []
# B_id_TVKO_order3 = []
# C_id_TVKO_order3 = []
# D_id_TVKO_order3 = []
# x0_id_TVKO_order3 = []
# S2ID_TVKO_order3 = []
# S2_TVKO_order3 = []
#
# systems = []
#
# for i in range(260, 301):
#     A = np.load('A_id_TVKO_order1_L' + str(i) + '.0.npy')
#     B = np.load('B_id_TVKO_order1_L' + str(i) + '.0.npy')
#     C = np.load('C_id_TVKO_order1_L' + str(i) + '.0.npy')
#     D = np.load('D_id_TVKO_order1_L' + str(i) + '.0.npy')
#     x0 = np.load('x0_id_TVKO_order1_L' + str(i) + '.0.npy')
#     S2ID = np.load('S2ID_TVKO_order1_L' + str(i) + '.0.npy')
#     S2 = np.load('S2_TVKO_order1_L' + str(i) + '.0.npy')
#     A_id_TVKO_order3.append(A)
#     B_id_TVKO_order3.append(B)
#     C_id_TVKO_order3.append(C)
#     D_id_TVKO_order3.append(D)
#     x0_id_TVKO_order3.append(x0)
#     S2ID_TVKO_order3.append(S2ID)
#     S2_TVKO_order3.append(S2)
#
#     def A_id(tk):
#         return A[:, :, int(round(tk * frequency))]
#     def B_id(tk):
#         return B[:, :, int(round(tk * frequency))]
#     def C_id(tk):
#         return C[:, :, int(round(tk * frequency))]
#     def D_id(tk):
#         return D[:, :, int(round(tk * frequency))]
#
#     systems.append(DiscreteLinearSystem(frequency, 4, 2, 4, [(x0, 0)], 'Nominal System Discrete', A_id, B_id, C_id, D_id))
#
#
#
#
#
#
#

# lambda_values = np.linspace(260, 300, 41)
# intervals = [np.linspace(0, 40, 2)]
#
# full_deviation_input_signal_d = DiscreteSignal(2, total_time_test, frequency)
# nominal_output_signal_test = DiscreteSignal(4, total_time_test, frequency)
#
# n = 4
#
#
# def calculate_error(interval):
#
#     nb_points = int(interval[1] - interval[0] + 1)
#     a = int(interval[0])
#     b = int(interval[1])
#
#     lambda_values = np.linspace(a, b, nb_points)
#     lambda_values_normalized_positive = np.linspace(0, 1, nb_points)
#     lambda_values_normalized_negative = np.linspace(-1, 0, nb_points)
#
#     w1 = 1 - np.abs(lambda_values_normalized_positive) ** 3 * (10 - 15 * np.abs(lambda_values_normalized_positive) + 6 * np.abs(lambda_values_normalized_positive) ** 2)
#     w2 = 1 - np.abs(lambda_values_normalized_negative) ** 3 * (10 - 15 * np.abs(lambda_values_normalized_negative) + 6 * np.abs(lambda_values_normalized_negative) ** 2)
#
#     coeffs_A = np.zeros([n, n, 497 - n, nb_points])
#     coeffs_B = np.zeros([n, 2, 497 - n, nb_points])
#     coeffs_C = np.zeros([n, n, 497 - n, nb_points])
#     coeffs_D = np.zeros([n, 2, 497 - n, nb_points])
#     # x0 = np.zeros([n, nb_points])
#
#
#     def A1(tk):
#         return A_id_TVKO_order3[a][:, :, int(round(tk * frequency))]
#     def A2(tk):
#         return A_id_TVKO_order3[b][:, :, int(round(tk * frequency))]
#     def C1(tk):
#         return C_id_TVKO_order3[a][:, :, int(round(tk * frequency))]
#     def C2(tk):
#         return C_id_TVKO_order3[b][:, :, int(round(tk * frequency))]
#
#
#
#     for i in range(0, 497 - n):
#
#         O1 = getObservabilityMatrix(A1, C, n, i * dt, dt)
#         O2 = getObservabilityMatrix(A2, C, n, (i + 1) * dt, dt)
#
#         Tkp1 = np.matmul(LA.pinv(O2), Ok1[:, :, k])
#         Tk = np.matmul(LA.pinv(O2), Ok[:, :, k])
#         A_id[:, :, k] = np.matmul(Tkp1, np.matmul(np.matmul(X2, LA.pinv(X1)), LA.pinv(Tk)))
#         C_id[:, :, k] = np.matmul(O1[0:output_dimension, :], LA.pinv(Tk))
#
#     for i in range(2):
#         coeffs_A[:, :, :, -i] = A_id_TVKO_order3[int(interval[i])]
#         coeffs_C[:, :, :, -i] = C_id_TVKO_order3[int(interval[i])]
#
#     for i in range(1, nb_points - 1):
#         # coeffs_A[:, :, :, i] = coeffs_A[:, :, :, 0] * w1[i] + coeffs_A[:, :, :, -1] * w2[i]
#         # coeffs_C[:, :, :, i] = coeffs_C[:, :, :, 0] * w1[i] + coeffs_C[:, :, :, -1] * w2[i]
#         coeffs_A[:, :, :, i] = (coeffs_A[:, :, :, 0] + coeffs_A[:, :, :, -1]) / 2
#         coeffs_C[:, :, :, i] = (coeffs_C[:, :, :, 0] + coeffs_C[:, :, :, -1]) / 2
#
#     errors = []
#     identified_output_signals = []
#
#     for i in range(0, nb_points):
#         def A_id(tk):
#             return coeffs_A[:, :, int(round(tk * frequency)), i]
#
#         def B_id(tk):
#             return coeffs_B[:, :, int(round(tk * frequency)), i]
#
#         def C_id(tk):
#             return coeffs_C[:, :, int(round(tk * frequency)), i]
#
#         def D_id(tk):
#             return coeffs_D[:, :, int(round(tk * frequency)), i]
#
#         interpolated_identified_system = DiscreteLinearSystem(frequency, n, 2, n, [(x0_id_TVKO_order3[i + a], 0)], 'ID', A_id, B_id, C_id, D_id)
#
#         identified_deviated_signal_augmented = OutputSignal(full_deviation_input_signal_d, interpolated_identified_system)
#         identified_deviated_signal = DiscreteSignal(34, total_time_test, frequency, signal_shape='External', data=identified_deviated_signal_augmented.data[0:4, :])
#         identified_output_signal = addSignals([nominal_output_signal_test, identified_deviated_signal])
#         identified_output_signals.append(identified_output_signal)
#
#
#         errors.append((LA.norm((np.max(identified_output_signal.data[0, 350:493]) - np.max(S2ID_TVKO_order3[i + a][0, 350:493])) / np.max(S2ID_TVKO_order3[i + a][0, 350:493])) +
#                        LA.norm((np.max(identified_output_signal.data[1, 350:493]) - np.max(S2ID_TVKO_order3[i + a][1, 350:493])) / np.max(S2ID_TVKO_order3[i + a][1, 350:493]))) / 2)
#         # errors.append(LA.norm(identified_output_signal.data[0:2, 350:493] - S2ID_TVKO_order3[i + a][0:2, 350:493]) / (2 * (493-350)))
#
#
#     return np.max(errors), identified_output_signals
#
#
#
#
# # plt.plot(np.linspace(0, 492, 493), S2_TVKO_order3[9][0, :])
# # plt.plot(np.linspace(0, 492, 493), S2ID_TVKO_order3[9][0, :])
# # plt.plot(np.linspace(0, 492, 493), identified_output_signal.data[0, 0:493])
# # plt.show()
#
#
#
#
#
#
#
#
# def test_error(intervals, threshold, bool_error):
#
#     intervals_copy = intervals.copy()
#
#     nb_intervals = len(intervals_copy)
#
#     ct_interval = 0
#     for interval in intervals_copy:
#         error, _ = calculate_error(interval)
#         print("Error", error)
#
#         if error > threshold:
#             del intervals_copy[ct_interval]
#             interval1 = np.linspace(interval[0], np.round((interval[0] + interval[1]) / 2), 2)
#             interval2 = np.linspace(np.round((interval[0] + interval[1]) / 2), interval[1], 2)
#             intervals_copy.insert(ct_interval, interval2)
#             intervals_copy.insert(ct_interval, interval1)
#             break
#
#         ct_interval += 1
#
#     if ct_interval == nb_intervals:
#         bool_error = False
#
#     return intervals_copy, bool_error
#
#
#
# def construct_intervals(intervals, threshold):
#
#     bool_error = True
#
#     updated_intervals = intervals
#
#     while bool_error:
#         updated_intervals, bool_error = test_error(updated_intervals, threshold, bool_error)
#         print('updated_intervals:', updated_intervals)
#         print('bool_error:', bool_error)
#
#     return updated_intervals
#
#
# updated_intervals = construct_intervals(intervals, 0.0005)
#
#
#
# all_signals = []
#
# for interval in updated_intervals:
#     _, identified_output_signals = calculate_error(interval)
#     all_signals = all_signals + identified_output_signals
#
#
#
# _, identified_output_signals = calculate_error(np.array([38, 40]))
#
#
# plt.plot(np.linspace(0, 492, 493), S2ID_TVKO_order3[39][0, 0:493])
# plt.plot(np.linspace(0, 492, 493), identified_output_signals[2].data[0, 0:493])
# plt.show()
#
#
#
#
#
# A298 = np.load('A_id_TVKO_order1_L298.0.npy')
# B298 = np.load('B_id_TVKO_order1_L298.0.npy')
# C298 = np.load('C_id_TVKO_order1_L298.0.npy')
# D298 = np.load('D_id_TVKO_order1_L298.0.npy')
# x0298 = np.load('x0_id_TVKO_order1_L298.0.npy')
# def A_id298(tk):
#     return A298[:, :, int(round(tk * frequency))]
# def B_id298(tk):
#     return B298[:, :, int(round(tk * frequency))]
# def C_id298(tk):
#     return C298[:, :, int(round(tk * frequency))]
# def D_id298(tk):
#     return D298[:, :, int(round(tk * frequency))]
# system298 = DiscreteLinearSystem(frequency, 4, 2, 4, [(x0298, 0)], 'Nominal System Discrete', A_id298, B_id298, C_id298, D_id298)
#
# A300 = np.load('A_id_TVKO_order1_L300.0.npy')
# B300 = np.load('B_id_TVKO_order1_L300.0.npy')
# C300 = np.load('C_id_TVKO_order1_L300.0.npy')
# D300 = np.load('D_id_TVKO_order1_L300.0.npy')
# x0300 = np.load('x0_id_TVKO_order1_L300.0.npy')
# def A_id300(tk):
#     return A298[:, :, int(round(tk * frequency))]
# def B_id300(tk):
#     return B298[:, :, int(round(tk * frequency))]
# def C_id300(tk):
#     return C298[:, :, int(round(tk * frequency))]
# def D_id300(tk):
#     return D298[:, :, int(round(tk * frequency))]
# system300 = DiscreteLinearSystem(frequency, 4, 2, 4, [(x0300, 0)], 'Nominal System Discrete', A_id300, B_id300, C_id300, D_id300)
#
# input = DiscreteSignal(2, 496/50, 50)
# S2_298 = OutputSignal(input, system298)
# S2_300 = OutputSignal(input, system300)
#
# plt.plot(S2_298.state[0, :])
# plt.plot(S2_300.state[0, :])
# plt.show()
#
# plt.plot(S2_298.data[0, :])
# plt.plot(S2_300.data[0, :])
# plt.show()
#
#
# from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
#
# plotHistoryEigenValues2Systems([system298, system300], 450, 1)


















#######################################################################################################################
############                               WAVELETS INTERPOLATION                                         #############
#######################################################################################################################


# import scaleogram as scg
import copy
# import pywt
from scipy.signal import find_peaks
# scg.set_default_wavelet('cmor1-1.5')
from scipy.fft import fft, fftfreq, ifft
from scipy.signal import blackman, hanning
# import imageio
import os


## Load matrices and build true systems
# A_id_TVKO_order3 = []
# B_id_TVKO_order3 = []
# C_id_TVKO_order3 = []
# D_id_TVKO_order3 = []
# x0_id_TVKO_order3 = []
S2ID_TVKO_order3 = []
S2_TVKO_order3 = []
cAsq1 = []
cAsq2 = []
cDsq1 = []
cDsq2 = []
cAsq1ID = []
cAsq2ID = []
cDsq1ID = []
cDsq2ID = []
yfq1_true = []
yfq2_true = []
yfq1 = []
yfq2 = []

systems = []

wavelet = 'db20'
type = 'per'

# Number of sample points
N = 8192
window = hanning(N)

for i in range(260, 301):
    # A = np.load('A_id_TVKO_order3_L' + str(i) + '.0.npy')
    # B = np.load('B_id_TVKO_order3_L' + str(i) + '.0.npy')
    # C = np.load('C_id_TVKO_order3_L' + str(i) + '.0.npy')
    # D = np.load('D_id_TVKO_order3_L' + str(i) + '.0.npy')
    # x0 = np.load('x0_id_TVKO_order3_L' + str(i) + '.0.npy')
    S2ID = np.load('S2ID_TVKO_order3_L' + str(i) + '.0.npy')
    S2 = np.load('S2_TVKO_order3_L' + str(i) + '.0.npy')
    # (cAq1, cDq1) = pywt.dwt(S2[0, :], wavelet, type)
    # (cAq2, cDq2) = pywt.dwt(S2[1, :], wavelet, type)
    # (cAq1ID, cDq1ID) = pywt.dwt(S2ID[0, :], wavelet, type)
    # (cAq2ID, cDq2ID) = pywt.dwt(S2ID[1, :], wavelet, type)
    # yfq1.append(fft(S2ID[0, -512:] * window))
    # yfq2.append(fft(S2ID[1, -512:] * window))
    yfq1_true.append(fft(S2[0, -8192:]))
    yfq2_true.append(fft(S2[1, -8192:]))
    yfq1.append(fft(S2ID[0, -8192:]))
    yfq2.append(fft(S2ID[1, -8192:]))
    # cAsq1.append(cAq1)
    # cAsq1ID.append(cAq1ID)
    # cAsq2.append(cAq2)
    # cAsq2ID.append(cAq2ID)
    # cDsq1.append(cDq1)
    # cDsq1ID.append(cDq1ID)
    # cDsq2.append(cDq2)
    # cDsq2ID.append(cDq2ID)
    # A_id_TVKO_order3.append(A)
    # B_id_TVKO_order3.append(B)
    # C_id_TVKO_order3.append(C)
    # D_id_TVKO_order3.append(D)
    # x0_id_TVKO_order3.append(x0)
    S2ID_TVKO_order3.append(S2ID)
    S2_TVKO_order3.append(S2)

    # def A_id(tk):
    #     return A[:, :, int(round(tk * frequency))]
    # def B_id(tk):
    #     return B[:, :, int(round(tk * frequency))]
    # def C_id(tk):
    #     return C[:, :, int(round(tk * frequency))]
    # def D_id(tk):
    #     return D[:, :, int(round(tk * frequency))]
    #
    # systems.append(DiscreteLinearSystem(frequency, 4, 2, 4, [(x0, 0)], 'Nominal System Discrete', A_id, B_id, C_id, D_id))


lower = np.linspace(0, 1, 21)
upper = np.linspace(-1, 0, 21)

w1 = 1 - np.abs(lower) ** 3 * (10 - 15 * np.abs(lower) + 6 * np.abs(lower) ** 2)
w2 = 1 - np.abs(upper) ** 3 * (10 - 15 * np.abs(upper) + 6 * np.abs(upper) ** 2)

amplitudes_q1 = np.zeros([5, 41])
amplitudes_q2 = np.zeros([5, 41])

filenames = []

for i in range(1, 40):
    print(i)

    jj = 10

    # S2IDq1_wav = pywt.idwt((cAsq1ID[i-1]*w1[jj] + cAsq1ID[i+1]*w2[jj]), (cDsq1ID[i-1]*w1[jj] + cDsq1ID[i+1]*w2[jj]), wavelet, type)[0:-1]
    # S2IDq1_time = (S2ID_TVKO_order3[i-1][0, :]*w1[jj] + S2ID_TVKO_order3[i+1][0, :]*w2[jj])
    # S2IDq2_wav = pywt.idwt((cAsq2ID[i-1]*w1[jj] + cAsq2ID[i+1]*w2[jj]), (cDsq2ID[i-1]*w1[jj] + cDsq2ID[i+1]*w2[jj]), wavelet, type)[0:-1]
    S2IDq2_time = (S2ID_TVKO_order3[i-1][1, :]*w1[jj] + S2ID_TVKO_order3[i+1][1, :]*w2[jj])
    S2IDq1_fourier = np.real(ifft((yfq1[i-1] + yfq1[i+1])/2))
    S2IDq2_fourier = np.real(ifft((yfq2[i-1] + yfq2[i+1])/2))

    peaksq1, _ = find_peaks(S2_TVKO_order3[i][0, 3801:], height=0)
    peaksq1ID, _ = find_peaks(S2ID_TVKO_order3[i][0, 3801:], height=0)
    # peaksq1ID_wav, _ = find_peaks(S2IDq1_wav[3801:], height=0)
    # peaksq1ID_time, _ = find_peaks(S2IDq1_time[3801:], height=0)
    peaksq1ID_fourier, _ = find_peaks(S2IDq1_fourier, height=0)
    peaksq2, _ = find_peaks(S2_TVKO_order3[i][1, 3801:], height=0)
    peaksq2ID, _ = find_peaks(S2ID_TVKO_order3[i][1, 3801:], height=0)
    # peaksq2ID_wav, _ = find_peaks(S2IDq2_wav[3801:], height=0)
    # peaksq2ID_time, _ = find_peaks(S2IDq2_time[3801:], height=0)
    peaksq2ID_fourier, _ = find_peaks(S2IDq2_fourier, height=0)

    if i == 29:
        # plt.plot(S2ID_TVKO_order3[i-1][0, 1481:], label='ID l=284')
        # plt.plot(S2ID_TVKO_order3[i][0, 1481:], label='ID l=285')
        # plt.plot(S2ID_TVKO_order3[i+1][0, 1481:], label='ID l=286')
        # plt.legend(loc="lower right")
        # plt.show()
        fig = plt.figure(10, figsize=(10, 5))
        plt.plot(np.linspace(0, 120 - 0.08, 11993), S2ID_TVKO_order3[i][0, :], label='ID', color=colors[0])
        plt.plot(38.01 + peaksq1ID/frequency, S2ID_TVKO_order3[i][0, 3801 + peaksq1ID], "x", color=colors[5])
        # plt.plot(np.linspace(0, 120 - 0.08, 11993), S2IDq1_wav, label='ID interpolated wavelets', color=colors[1])
        # plt.plot(38.01 + peaksq1ID_wav/frequency, S2IDq1_wav[3801 + peaksq1ID_wav], "x", color=colors[6])
        # plt.plot(np.linspace(0, 120 - 0.08, 11993), S2IDq1_time, label='ID interpolated time', color=colors[2])
        # plt.plot(38.01 + peaksq1ID_time/frequency, S2IDq1_time[3801 + peaksq1ID_time], "x", color=colors[7])
        plt.plot(np.linspace(38.01, 120 - 0.08, 8192), S2IDq1_fourier, label='ID interpolated fourier', color=colors[4])
        plt.plot(38.01 + peaksq1ID_fourier/frequency, S2IDq1_fourier[peaksq1ID_fourier], "x", color=colors[8])
        plt.legend(loc="lower right")
        plt.title(r'$\lambda = '+str(260+i)+'$')
        plt.ylim(-0.34, 0.34)
        plt.show()
        # filename = f'{i}.png'
        plt.tight_layout()
        # filenames.append(filename)
        # plt.savefig(filename)
        plt.close()

    amplitudes_q1[0, i] = np.mean(S2_TVKO_order3[i][0, 3801 + peaksq1])
    amplitudes_q1[1, i] = np.mean(S2ID_TVKO_order3[i][0, 3801 + peaksq1ID])
    # amplitudes_q1[2, i] = np.mean(S2IDq1_wav[3801 + peaksq1ID_wav])
    # amplitudes_q1[3, i] = np.mean(S2IDq1_time[3801 + peaksq1ID_time])
    amplitudes_q1[4, i] = np.mean(S2IDq1_fourier[peaksq1ID_fourier])

    amplitudes_q2[0, i] = np.mean(S2_TVKO_order3[i][1, 3801 + peaksq2])
    amplitudes_q2[1, i] = np.mean(S2ID_TVKO_order3[i][1, 3801 + peaksq2ID])
    # amplitudes_q2[2, i] = np.mean(S2IDq2_wav[3801 + peaksq2ID_wav])
    # amplitudes_q2[3, i] = np.mean(S2IDq2_time[3801 + peaksq2ID_time])
    amplitudes_q2[4, i] = np.mean(S2IDq2_fourier[peaksq2ID_fourier])

# with imageio.get_writer('evolution_reconstructed_signals.gif', mode='I') as writer:
#     for filename in filenames:
#         image = imageio.imread(filename)
#         writer.append_data(image)
# # Remove files
# for filename in set(filenames):
#     os.remove(filename)



# # Refined between 290 and 292
# amplitudes_q1_refined = np.zeros([2, 21])
# amplitudes_q2_refined = np.zeros([2, 21])
#
# for i in range(21):
#     print(i)
#
#     S2IDq1_wav = pywt.idwt((cAsq1ID[30]*w1[i] + cAsq1ID[32]*w2[i]), (cDsq1ID[30]*w1[i] + cDsq1ID[32]*w2[i]), wavelet, 'smooth')[0:-1]
#     S2IDq1_time = S2ID_TVKO_order3[30][0, :]*w1[i] + S2ID_TVKO_order3[32][0, :]*w2[i]
#     S2IDq2_wav = pywt.idwt((cAsq2ID[30]*w1[i] + cAsq2ID[32]*w2[i]), (cDsq2ID[30]*w1[i] + cDsq2ID[32]*w2[i]), wavelet, 'smooth')[0:-1]
#     S2IDq2_time = S2ID_TVKO_order3[30][1, :]*w1[i] + S2ID_TVKO_order3[32][1, :]*w2[i]
#
#     peaksq1ID_wav, _ = find_peaks(S2IDq1_wav[1481:], height=0)
#     peaksq1ID_time, _ = find_peaks(S2IDq1_time[1481:], height=0)
#     peaksq2ID_wav, _ = find_peaks(S2IDq2_wav[1481:], height=0)
#     peaksq2ID_time, _ = find_peaks(S2IDq2_time[1481:], height=0)
#
#     amplitudes_q1_refined[0, i] = np.mean(S2IDq1_wav[1481 + peaksq1ID_wav])
#     amplitudes_q1_refined[1, i] = np.mean(S2IDq1_time[1481 + peaksq1ID_time])
#
#     amplitudes_q2_refined[0, i] = np.mean(S2IDq2_wav[1481 + peaksq2ID_wav])
#     amplitudes_q2_refined[1, i] = np.mean(S2IDq2_time[1481 + peaksq2ID_time])
#
#
# fig = plt.figure(201, figsize=(12, 12))
# ax = plt.subplot(411)
# ax.plot(cAsq1ID[30], color=colors[1], label=r'$\lambda = 290$')
# ax.plot(cAsq1ID[31], color=colors[4], label=r'$\lambda = 291$')
# ax.plot(cAsq1ID[32], color=colors[5], label=r'$\lambda = 292$')
# plt.ylabel(r'Amplitude of coefficients cA')
# ax.legend(loc='upper left')
# ax = plt.subplot(412)
# ax.plot(cAsq1ID[31], color=colors[6], label='Identified cA')
# ax.plot((cAsq1ID[30]*w1[j] + cAsq1ID[32]*w2[j]), color=colors[7], label='Interpolated cA')
# plt.ylabel(r'Amplitude of coefficients')
# ax.legend(loc='upper left')
# ax = plt.subplot(413)
# ax.plot(cDsq1ID[30], color=colors[1], label=r'$\lambda = 290$')
# ax.plot(cDsq1ID[31], color=colors[4], label=r'$\lambda = 291$')
# ax.plot(cDsq1ID[32], color=colors[5], label=r'$\lambda = 292$')
# plt.ylabel(r'Amplitude of coefficients cD')
# ax.legend(loc='upper left')
# ax = plt.subplot(414)
# ax.plot(cDsq1ID[31], color=colors[6], label='Identified cD')
# ax.plot((cDsq1ID[30]*w1[j] + cDsq1ID[32]*w2[j]), color=colors[7], label='Interpolated cD')
# plt.ylabel(r'Amplitude of coefficients')
# ax.legend(loc='upper left')
# plt.tight_layout()
# # plt.savefig('limit_cycle.eps', format='eps')
# plt.show()
#
#
#
#
#
#
fig = plt.figure(20, figsize=(5, 5))
ax = plt.subplot(111)
ax.plot(np.linspace(261, 299, 39), amplitudes_q1[0, 1:-1], '-o', color=colors[0], label='True')
ax.plot(np.linspace(261, 299, 39), amplitudes_q1[1, 1:-1], 'o', mfc='none', color=colors[6], label='Identified')
ax.plot(np.linspace(261, 299, 39), amplitudes_q1[2, 1:-1], 'x', mfc='none', color=colors[7], label='Interpolated wavelets')
ax.plot(np.linspace(261, 299, 39), amplitudes_q1[3, 1:-1], '.', mfc='none', color=colors[8], label='Interpolated time')
ax.plot(np.linspace(261, 299, 39), np.abs(amplitudes_q1[4, 1:-1]), '+', mfc='none', color=colors[9], label='Interpolated Fourier')
plt.xlabel(r'$\lambda$')
plt.ylabel(r'Amplitude of oscillations for limite cycle')
ax.legend(loc='upper left')
plt.tight_layout()
# plt.savefig('limit_cycle.eps', format='eps')
plt.show()
#
#
# fig = plt.figure(21, figsize=(5, 5))
# ax = plt.subplot(111)
# ax.plot(np.linspace(261, 299, 39), amplitudes_q2[0, 1:-1], '-o', color=colors[0], label='True')
# ax.plot(np.linspace(261, 299, 39), amplitudes_q2[1, 1:-1], 'o', mfc='none', color=colors[6], label='Identified')
# ax.plot(np.linspace(261, 299, 39), amplitudes_q2[2, 1:-1], 'x', mfc='none', color=colors[7], label='Interpolated wavelets')
# ax.plot(np.linspace(261, 299, 39), amplitudes_q2[3, 1:-1], '.', mfc='none', color=colors[8], label='Interpolated time')
# ax.plot(np.linspace(261, 299, 39), amplitudes_q2[4, 1:-1], '+', mfc='none', color=colors[9], label='Interpolated Fourier')
# plt.xlabel(r'$\lambda$')
# plt.ylabel(r'Amplitude of oscillations for limite cycle')
# ax.legend(loc='upper left')
# plt.tight_layout()
# # plt.savefig('limit_cycle.eps', format='eps')
# plt.show()
#
# fig = plt.figure(22, figsize=(5, 5))
# ax = plt.subplot(111)
# ax.plot(np.array([290, 291, 292]), amplitudes_q1[0, 30:33], '-o', color=colors[0], label='True')
# ax.plot(np.array([290, 291, 292]), amplitudes_q1[1, 30:33], 'o', mfc='none', color=colors[6], label='Identified')
# ax.plot(lower * 2 + 290, amplitudes_q1_refined[0, :], 'x', mfc='none', color=colors[7], label='Interpolated wavelets')
# ax.plot(lower * 2 + 290, amplitudes_q1_refined[1, :], '.', mfc='none', color=colors[8], label='Interpolated time')
# plt.xlabel(r'$\lambda$')
# plt.ylabel(r'Amplitude of oscillations for limite cycle')
# ax.legend(loc='best')
# plt.tight_layout()
# # plt.savefig('limit_cycle.eps', format='eps')
# plt.show()
#
#
#
# Fourier Analysis
# sample spacing
T = dt
x = np.linspace(0.0, N*T, N, endpoint=False)
xf = fftfreq(N, T)[:N//2]
#
# fig = plt.figure(23, figsize=(8, 6))
# ax = plt.subplot(2, 2, 1)
# ax.plot(xf,  2.0/N * np.abs(yfq1[5][0:N//2]), color=colors[1])
# peaks = find_peaks(2.0/N * np.abs(yfq1[5][0:N//2]), height=0)
# ax.plot(xf[peaks[0]], peaks[1]['peak_heights'], 'x', mfc='none', color=colors[4])
# for i in range(len(xf[peaks[0]])):
#     ax.annotate(r'f = ' + str(xf[peaks[0]][i]), (xf[peaks[0]][i] + 1, peaks[1]['peak_heights'][i] - 0.00001))
# plt.title(r'$\lambda = 265$')
# plt.xlabel(r'Frequency [Hz]')
# plt.ylabel(r'Amplitude')
# ax = plt.subplot(2, 2, 2)
# ax.plot(xf,  2.0/N * np.abs(yfq1[15][0:N//2]), color=colors[1])
# peaks = find_peaks(2.0/N * np.abs(yfq1[15][0:N//2]), height=0)
# ax.plot(xf[peaks[0]], peaks[1]['peak_heights'], 'x', mfc='none', color=colors[4])
# for i in range(len(xf[peaks[0]])):
#     ax.annotate(r'f = ' + str(xf[peaks[0]][i]), (xf[peaks[0]][i] + 1, peaks[1]['peak_heights'][i] - 0.001))
# plt.title(r'$\lambda = 275$')
# plt.xlabel(r'Frequency [Hz]')
# plt.ylabel(r'Amplitude')
# ax = plt.subplot(2, 2, 3)
# ax.plot(xf,  2.0/N * np.abs(yfq1[25][0:N//2]), color=colors[1])
# peaks = find_peaks(2.0/N * np.abs(yfq1[25][0:N//2]), height=0)
# ax.plot(xf[peaks[0][2]], peaks[1]['peak_heights'][2], 'x', mfc='none', color=colors[4])
# ax.annotate(r'f = ' + str(xf[peaks[0]][2]), (xf[peaks[0]][2] + 1, peaks[1]['peak_heights'][2] - 0.01))
# plt.title(r'$\lambda = 285$')
# plt.xlabel(r'Frequency [Hz]')
# plt.ylabel(r'Amplitude')
# ax = plt.subplot(2, 2, 4)
# ax.plot(xf,  2.0/N * np.abs(yfq1[35][0:N//2]), color=colors[1])
# peaks = find_peaks(2.0/N * np.abs(yfq1[35][0:N//2]), height=0)
# ax.plot(xf[peaks[0][0]], peaks[1]['peak_heights'][0], 'x', mfc='none', color=colors[4])
# ax.annotate(r'f = ' + str(xf[peaks[0]][0]), (xf[peaks[0]][0] + 1, peaks[1]['peak_heights'][0] - 0.01))
# plt.title(r'$\lambda = 295$')
# plt.xlabel(r'Frequency [Hz]')
# plt.ylabel(r'Amplitude')
# plt.tight_layout()
# # plt.savefig('fourier_analysis.eps', format='eps')
# plt.show()



# fig = plt.figure(24, figsize=(8, 6))
# ax = plt.subplot(2, 2, 1)
# ax.plot(xf[0:100],  2.0/N * np.abs(yfq1[4][0:N//2])[0:100], color=colors[1], label=r'$\lambda = 264$')
# ax.plot(xf[0:100],  2.0/N * np.abs(yfq1[5][0:N//2])[0:100], color=colors[4], label=r'$\lambda = 265$')
# ax.plot(xf[0:100],  2.0/N * np.abs(yfq1[6][0:N//2])[0:100], color=colors[5], label=r'$\lambda = 266$')
# plt.xlabel(r'Frequency [Hz]')
# plt.ylabel(r'Amplitude')
# ax.legend(loc='best')
# ax = plt.subplot(2, 2, 2)
# ax.plot(xf[0:100],  2.0/N * np.abs(yfq1[14][0:N//2])[0:100], color=colors[1], label=r'$\lambda = 274$')
# ax.plot(xf[0:100],  2.0/N * np.abs(yfq1[15][0:N//2])[0:100], color=colors[4], label=r'$\lambda = 275$')
# ax.plot(xf[0:100],  2.0/N * np.abs(yfq1[16][0:N//2])[0:100], color=colors[5], label=r'$\lambda = 276$')
# plt.xlabel(r'Frequency [Hz]')
# plt.ylabel(r'Amplitude')
# ax.legend(loc='best')
# ax = plt.subplot(2, 2, 3)
# ax.plot(xf[0:100],  2.0/N * np.abs(yfq1[24][0:N//2])[0:100], color=colors[1], label=r'$\lambda = 284$')
# ax.plot(xf[0:100],  2.0/N * np.abs(yfq1[25][0:N//2])[0:100], color=colors[4], label=r'$\lambda = 285$')
# ax.plot(xf[0:100],  2.0/N * np.abs(yfq1[26][0:N//2])[0:100], color=colors[5], label=r'$\lambda = 286$')
# plt.xlabel(r'Frequency [Hz]')
# plt.ylabel(r'Amplitude')
# ax.legend(loc='best')
# ax = plt.subplot(2, 2, 4)
# ax.plot(xf[0:100],  2.0/N * np.abs(yfq1[38][0:N//2])[0:100], color=colors[1], label=r'$\lambda = 298$')
# ax.plot(xf[0:100],  2.0/N * np.abs(yfq1[39][0:N//2])[0:100], color=colors[4], label=r'$\lambda = 299$')
# ax.plot(xf[0:100],  2.0/N * np.abs(yfq1[40][0:N//2])[0:100], color=colors[5], label=r'$\lambda = 300$')
# plt.xlabel(r'Frequency [Hz]')
# plt.ylabel(r'Amplitude')
# ax.legend(loc='best')
# plt.tight_layout()
# # plt.savefig('fourier_analysis.eps', format='eps')
# plt.show()
#
fig = plt.figure(26, figsize=(24, 5))
ax = plt.subplot(1, 4, 1)
ax.plot(xf[0:1000],  2.0/N * np.abs(yfq1[38][0:N//2])[0:1000], color=colors[4], label=r'True $\lambda = 298$')
plt.xlabel(r'Frequency [Hz]')
plt.ylabel(r'Amplitude')
ax.legend(loc='best')
ax = plt.subplot(1, 4, 2)
ax.plot(xf[0:1000],  2.0/N * np.abs(yfq1[39][0:N//2])[0:1000], color=colors[5], label=r'True $\lambda = 299$')
plt.xlabel(r'Frequency [Hz]')
plt.ylabel(r'Amplitude')
ax.legend(loc='best')
ax = plt.subplot(1, 4, 3)
ax.plot(xf[0:1000],  2.0/N * np.abs(yfq1[40][0:N//2])[0:1000], color=colors[6], label=r'True $\lambda = 300$')
plt.xlabel(r'Frequency [Hz]')
plt.ylabel(r'Amplitude')
ax.legend(loc='best')
ax = plt.subplot(1, 4, 4)
ax.plot(xf[0:1000],  2.0/N * np.abs(yfq1[39][0:N//2])[0:1000], color=colors[5], label=r'True $\lambda = 299$')
ax.plot(xf[0:1000],  2.0/N * (np.abs(yfq1[38][0:N//2]) * 0.5 + np.abs(yfq1[40][0:N//2]) * 0.5)[0:1000], color=colors[9], label=r'Interp. $\lambda = 299$')
plt.xlabel(r'Frequency [Hz]')
plt.ylabel(r'Amplitude')
ax.legend(loc='best')
plt.tight_layout()
plt.show()


# # Video
# filenames = []
# for i in range(41):
#     fig = plt.figure(25, figsize=(5, 5))
#     plt.plot(xf[0:1000],  2.0/N * np.abs(yfq1[i][0:N//2])[0:1000], color=colors[5], label=r'$\lambda = '+str(260+i)+'$')
#     plt.xlabel(r'Frequency [Hz]')
#     plt.ylabel(r'Amplitude')
#     plt.legend(loc='upper left')
#     plt.ylim(0, 0.25)
#     filename = f'{i}.png'
#     plt.tight_layout()
#     filenames.append(filename)
#     plt.savefig(filename)
#     plt.close()
#     # build gif
# with imageio.get_writer('fft_no_window.gif', mode='I') as writer:
#     for filename in filenames:
#         image = imageio.imread(filename)
#         writer.append_data(image)
# # Remove files
# for filename in set(filenames):
#     os.remove(filename)



## Build bifurcation graph with Fourier
j = 10
amplitudes_fourier_q1 = np.zeros([3, 39])
amplitudes_fourier_q2 = np.zeros([3, 39])
for i in range(1, 40):
    amplitudes_fourier_q1[0, i-1] = np.max(2.0/N * np.abs(yfq1_true[i][0:N//2])[0:1000])
    amplitudes_fourier_q1[1, i-1] = np.max(2.0/N * np.abs(yfq1[i][0:N // 2])[0:1000])
    amplitudes_fourier_q1[2, i-1] = np.max(2.0/N * np.abs(yfq1[i-1][0:N // 2])[0:1000]) * 0.5 + np.max(2.0/N * np.abs(yfq1[i+1][0:N // 2])[0:1000]) * 0.5
    amplitudes_fourier_q2[0, i-1] = np.max(2.0/N * np.abs(yfq2_true[i][0:N // 2])[0:1000])
    amplitudes_fourier_q2[1, i-1] = np.max(2.0/N * np.abs(yfq2[i][0:N // 2])[0:1000])
    amplitudes_fourier_q2[2, i-1] = np.max(2.0/N * (np.abs(yfq2[i-1]) * w1[j] + np.abs(yfq2[i+1])*w2[j])[0:1000])

fig = plt.figure(30, figsize=(5, 5))
ax = plt.subplot(111)
ax.plot(np.linspace(261, 299, 39), amplitudes_fourier_q1[0, :], '-o', color=colors[0], label='True')
ax.plot(np.linspace(261, 299, 39), amplitudes_fourier_q1[1, :], 'o', mfc='none', color=colors[6], label='Identified')
ax.plot(np.linspace(261, 299, 39), amplitudes_fourier_q1[2, :], 'x', mfc='none', color=colors[7], label='Interpolated')
plt.xlabel(r'$\lambda$')
plt.ylabel(r'Amplitude of oscillations for limite cycle')
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('limit_cycle.eps', format='eps')
plt.show()

fig = plt.figure(31, figsize=(5, 5))
ax = plt.subplot(111)
ax.plot(np.linspace(261, 299, 39), amplitudes_q1[0, 1:-1], '-o', color=colors[0], label='True')
ax.plot(np.linspace(261, 299, 39), amplitudes_q1[1, 1:-1], 'o', mfc='none', color=colors[6], label='Identified')
ax.plot(np.linspace(261, 299, 39), amplitudes_fourier_q1[2, :], 'x', mfc='none', color=colors[4], label='Interpolated Fourier')
ax.plot(np.linspace(261, 299, 39), amplitudes_q1[2, 1:-1], 'x', mfc='none', color=colors[7], label='Interpolated wavelets')
ax.plot(np.linspace(261, 299, 39), amplitudes_q1[3, 1:-1], '.', mfc='none', color=colors[8], label='Interpolated time')
plt.xlabel(r'$\lambda$')
plt.ylabel(r'Amplitude of oscillations for limite cycle')
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('limit_cycle.eps', format='eps')
plt.show()





