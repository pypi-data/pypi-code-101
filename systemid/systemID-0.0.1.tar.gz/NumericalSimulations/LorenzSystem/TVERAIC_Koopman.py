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
from matplotlib import rc
import scipy.linalg as LA

from ClassesDynamics.ClassLorenzSystemDynamics import LorenzSystemDynamics
from SystemIDAlgorithms.DepartureDynamics import departureDynamicsFromInitialConditionResponse
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem, ContinuousNonlinearSystemHigherOrderExpansion
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
from SparseIDAlgorithms.GeneratePolynomialBasisFunctions import generatePolynomialBasisFunctions



def main_Koopman(order, full_deviation_dx0, x0):
    print('order =', order)
    print('full_deviation_dx0 =', full_deviation_dx0)


    ## Parameters for Dynamics
    print('> Parameters for Dynamics')
    def sigma(t):
        return 10
    def rho(t):
        return 28
    def beta(t):
        return 8/3


    ## Parameters for identification
    print('> Parameters for Identification')
    total_time = 6
    frequency = 100
    dt = 1 / frequency
    number_steps = int(total_time * frequency) + 1
    tspan = np.linspace(0, total_time, number_steps)
    total_time_interp = 5
    number_steps_interp = int(total_time_interp * frequency) + 1
    tspan_interp = np.linspace(0, total_time_interp, number_steps_interp)


    ## Import Dynamics
    print('> Import Dynamics')
    dynamics = LorenzSystemDynamics(sigma, rho, beta)


    ## Orders and Sizes
    print('> Orders and Sizes')
    index = generatePolynomialIndex(dynamics.state_dimension, order, True, max_order=order)
    assumed_order = len(index) - 1
    p, q = getOptimizedHankelMatrixSize(assumed_order, assumed_order, dynamics.input_dimension)
    q = 100
    print('p =', p)
    print('q =', q)
    number_free_decay_experiments = 120


    ## Create Nominal System
    print('> Create Nominal System')
    initial_states = [(x0, 0)]
    nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)


    ## Create Nominal Input Signal
    print('> Create Nominal Input Signal')
    nominal_input_signal = ContinuousSignal(dynamics.input_dimension)
    nominal_input_signal_d = DiscreteSignal(dynamics.input_dimension, total_time_interp, frequency)


    ## CreateNominal Output Signal
    print('> Create Nominal Output Signal')
    nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan_interp)


    ## Update dynamics with nominal trajectory
    print('> Update dynamics with nominal trajectory')
    dynamics = LorenzSystemDynamics(sigma, rho, beta, nominal=True, initial_states=initial_states, nominal_u=nominal_input_signal, dt=dt, tspan=tspan)


    ## Deviations dx0
    print('> Deviations dx0')
    deviations_dx0 = []
    for i in range(number_free_decay_experiments):
        deviations_dx0.append(0.02 * np.random.randn(dynamics.state_dimension))


    ## Full experiment
    print('> Full experiment')
    full_deviation_input_signal = ContinuousSignal(dynamics.input_dimension)
    full_deviation_input_signal_d = DiscreteSignal(dynamics.input_dimension, total_time_interp, frequency)


    ## Departure Dynamics From Initial Condition Response
    print('> Departure Dynamics From Initial Condition Response')
    free_decay_experiments, free_decay_experiments_deviated, full_experiment, full_experiment_deviated = departureDynamicsFromInitialConditionResponse(nominal_system, nominal_input_signal, tspan_interp, deviations_dx0, full_deviation_dx0[0])


    ## Koopman
    print('> Koopman')
    max_order = order
    for i in range(free_decay_experiments_deviated.number_experiments):
        free_decay_experiments_deviated.output_signals[i] = createAugmentedSignalPolynomialBasisFunctions(free_decay_experiments_deviated.output_signals[i], order, True, max_order)
    for i in range(full_experiment_deviated.number_experiments):
        full_experiment_deviated.output_signals[i] = createAugmentedSignalPolynomialBasisFunctions(full_experiment_deviated.output_signals[i], order, True, max_order)
    free_decay_experiments_deviated.output_dimension = free_decay_experiments_deviated.output_signals[0].dimension
    full_experiment_deviated.output_dimension = full_experiment_deviated.output_signals[0].dimension
    augmented_dimension = full_experiment_deviated.output_signals[0].dimension


    ## TVERAIC
    print('> TVERAIC')
    tvera = TVERAFromInitialConditionResponse(free_decay_experiments_deviated, augmented_dimension, p=10)
    era = ERAFromInitialConditionResponse(free_decay_experiments_deviated.output_signals, augmented_dimension, dynamics.input_dimension, p=10, q=10)


    true_output_signals = []
    identified_output_signals_tvera = []
    identified_output_signals_era = []


    for i in range(len(full_deviation_dx0)):

        ## True Output Signal
        print('> True Output Signal')
        true_output_signals.append(OutputSignal(full_deviation_input_signal, ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(x0 + full_deviation_dx0[i], 0)], 'Nominal System', dynamics.F, dynamics.G), tspan=tspan_interp))


        ## Full Experiment deviated
        print('> Full Experiment deviated')
        full_output_signal_deviated = subtract2Signals(true_output_signals[-1], nominal_output_signal)
        full_output_signal_deviated = createAugmentedSignalPolynomialBasisFunctions(full_output_signal_deviated, order, True, max_order)


        ## Identify Initial Condition
        print('> Identify Initial Condition')
        x0_id_tvera = identificationInitialCondition(full_deviation_input_signal_d, full_output_signal_deviated, tvera.A, tvera.B, tvera.C, tvera.D, 0, p)
        x0_id_era = identificationInitialCondition(full_deviation_input_signal_d, full_output_signal_deviated, era.A, era.B, era.C, era.D, 0, p)


        ## Identified System TVERA
        print('> Identified System TVERA')
        identified_system_tvera = DiscreteLinearSystem(frequency, augmented_dimension, dynamics.input_dimension, augmented_dimension, [(x0_id_tvera, 0)], 'System ID', tvera.A, tvera.B, tvera.C, tvera.D)


        ## Identified System ERA
        print('> Identified System ERA')
        identified_system_era = DiscreteLinearSystem(frequency, augmented_dimension, dynamics.input_dimension, augmented_dimension, [(x0_id_era, 0)], 'System ID ERA', era.A, era.B, era.C, era.D)


        ## Identified Output Signals (Full Operator propagation)
        print('> Identified Output Signals (Full Operator propagation)')
        identified_deviated_output_signal_augmented_tvera = OutputSignal(full_deviation_input_signal_d, identified_system_tvera)
        identified_deviated_output_signal_augmented_era = OutputSignal(full_deviation_input_signal_d, identified_system_era)

        identified_deviated_signal_tvera = DiscreteSignal(dynamics.output_dimension, total_time_interp, frequency, signal_shape='External', data=identified_deviated_output_signal_augmented_tvera.data[0:dynamics.state_dimension, :])
        identified_deviated_signal_era = DiscreteSignal(dynamics.output_dimension, total_time_interp, frequency, signal_shape='External', data=identified_deviated_output_signal_augmented_era.data[0:dynamics.state_dimension, :])

        identified_output_signals_tvera.append(addSignals([nominal_output_signal, identified_deviated_signal_tvera]))
        identified_output_signals_era.append(addSignals([nominal_output_signal, identified_deviated_signal_era]))


    # # Partial operator propagation
    # index = generatePolynomialIndex(dynamics.state_dimension, order, True, max_order=order)
    # basis_functions = generatePolynomialBasisFunctions(dynamics.state_dimension, index)
    # y = np.zeros([dynamics.output_dimension, full_deviation_input_signal_d.number_steps])
    # x = np.zeros([dynamics.state_dimension, full_deviation_input_signal_d.number_steps + 1])
    # x[:, 0] = tvera.x0[0:dynamics.state_dimension]
    # for i in range(full_deviation_input_signal_d.number_steps):
    #     x_red = x[:, i]
    #     for jj in range(3, len(index)):
    #         x_red = np.concatenate((x_red, np.array([basis_functions[jj](x[:, i])])))
    #     y[:, i] = np.matmul(tvera.C(i * dt)[0:dynamics.output_dimension, :], x_red)
    #     x[:, i+1] = np.matmul(tvera.A(i * dt)[0:dynamics.state_dimension, :], x_red)
    # identified_deviated_signal_augmented_partial = DiscreteSignal(dynamics.output_dimension, total_time_test, frequency, signal_shape='External', data=y)
    # identified_output_signal_partial = addSignals([nominal_output_signal_test, identified_deviated_signal_augmented_partial])





    ##Plotting
    # plotSignals([[true_output_signal, identified_output_signal_era, identified_output_signal_tvera, true_output_signal_order1],
    #              [subtract2Signals(true_output_signal, identified_output_signal_era), subtract2Signals(true_output_signal, identified_output_signal_tvera),
    #               subtract2Signals(true_output_signal, true_output_signal_order1)]], 1, percentage=0.9)


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


    return true_output_signals, identified_output_signals_tvera, identified_output_signals_era, free_decay_experiments, nominal_output_signal





def main_STT(full_deviation_dx0, x0):


    ## Parameters for Dynamics
    print('> Parameters for Dynamics')
    def sigma(t):
        return 10
    def rho(t):
        return 28
    def beta(t):
        return 8/3


    ## Parameters for identification
    print('> Parameters for Identification')
    total_time = 6
    frequency = 100
    dt = 1 / frequency
    number_steps = int(total_time * frequency) + 1
    tspan = np.linspace(0, total_time, number_steps)
    total_time_interp = 5
    number_steps_interp = int(total_time_interp * frequency) + 1
    tspan_interp = np.linspace(0, total_time_interp, number_steps_interp)


    ## Import Dynamics
    print('> Import Dynamics')
    dynamics = LorenzSystemDynamics(sigma, rho, beta)


    ## Create Nominal System
    print('> Create Nominal System')
    initial_states = [(x0, 0)]
    nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)


    ## Create Nominal Input Signal
    print('> Create Nominal Input Signal')
    nominal_input_signal = ContinuousSignal(dynamics.input_dimension)
    nominal_input_signal_d = DiscreteSignal(dynamics.input_dimension, total_time_interp, frequency)


    ## CreateNominal Output Signal
    print('> Create Nominal Output Signal')
    nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan_interp)


    ## Update dynamics with nominal trajectory
    print('> Update dynamics with nominal trajectory')
    dynamics = LorenzSystemDynamics(sigma, rho, beta, nominal=True, initial_states=initial_states, nominal_u=nominal_input_signal, dt=dt, tspan=tspan)


    ## Full experiment
    print('> Full experiment')
    full_deviation_input_signal = ContinuousSignal(dynamics.input_dimension)
    full_deviation_input_signal_d = DiscreteSignal(dynamics.input_dimension, total_time_interp, frequency)


    ## Linearized Solutions
    print('> Linearized Solutions')
    linearized_system_order1 = ContinuousNonlinearSystemHigherOrderExpansion(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(full_deviation_dx0[0], 0)], 'Nominal System', dynamics.F, dynamics.G, [dynamics.Ac1], x0, nominal_input_signal, tspan)
    linearized_system_order2 = ContinuousNonlinearSystemHigherOrderExpansion(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(full_deviation_dx0[0], 0)], 'Nominal System', dynamics.F, dynamics.G, [dynamics.Ac1, dynamics.Ac2], x0, nominal_input_signal, tspan)
    linearized_system_order3 = ContinuousNonlinearSystemHigherOrderExpansion(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(full_deviation_dx0[0], 0)], 'Nominal System', dynamics.F, dynamics.G, [dynamics.Ac1, dynamics.Ac2, dynamics.Ac3], x0, nominal_input_signal, tspan)
    linearized_system_order4 = ContinuousNonlinearSystemHigherOrderExpansion(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(full_deviation_dx0[0], 0)], 'Nominal System', dynamics.F, dynamics.G, [dynamics.Ac1, dynamics.Ac2, dynamics.Ac3, dynamics.Ac4], x0, nominal_input_signal, tspan)


    true_output_signals = []
    true_output_signals_order1 = []
    true_output_signals_order2 = []
    true_output_signals_order3 = []
    # true_output_signals_order4 = []

    for i in range(len(full_deviation_dx0)):
        ## True Output Signal
        print('> True Output Signal')
        true_output_signals.append(OutputSignal(full_deviation_input_signal, ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(x0 + full_deviation_dx0[i], 0)], 'Nominal System', dynamics.F, dynamics.G), tspan=tspan_interp))

        linearized_system_order1.initial_states = [(full_deviation_dx0[i], 0)]
        linearized_system_order1.x0 = full_deviation_dx0[i]
        linearized_system_order2.initial_states = [(full_deviation_dx0[i], 0)]
        linearized_system_order2.x0 = full_deviation_dx0[i]
        linearized_system_order3.initial_states = [(full_deviation_dx0[i], 0)]
        linearized_system_order3.x0 = full_deviation_dx0[i]
        linearized_system_order4.initial_states = [(full_deviation_dx0[i], 0)]
        linearized_system_order4.x0 = full_deviation_dx0[i]



        ## Output Signals from Linearized Solutions
        print('> Output Signals from Linearized Solutions')
        true_output_signals_order1.append(addSignals([nominal_output_signal, OutputSignal(full_deviation_input_signal, linearized_system_order1, tspan=tspan_interp)]))
        true_output_signals_order2.append(addSignals([nominal_output_signal, OutputSignal(full_deviation_input_signal, linearized_system_order2, tspan=tspan_interp)]))
        true_output_signals_order3.append(addSignals([nominal_output_signal, OutputSignal(full_deviation_input_signal, linearized_system_order3, tspan=tspan_interp)]))
        true_output_signals_order4.append(addSignals([nominal_output_signal, OutputSignal(full_deviation_input_signal, linearized_system_order4, tspan=tspan_interp)]))


    return true_output_signals, nominal_output_signal, true_output_signals_order1, true_output_signals_order2, true_output_signals_order3, true_output_signals_order4, dynamics, linearized_system_order1, linearized_system_order2, linearized_system_order3, linearized_system_order4




    # return true_output_signal, identified_output_signal_era, identified_output_signal_tvera, free_decay_experiments, full_experiment, nominal_output_signal
    # return true_output_signal, free_decay_experiments, full_experiment, nominal_output_signal, true_output_signal_order1, true_output_signal_order2


## Run
x0 = np.array([-8, 7, 27])
end = 100

full_deviation_dx0 = []
number_test_trajectories = 10
number_increments = 20
r = np.linspace(0.005, 0.05, number_increments)
t1 = np.linspace(1, number_test_trajectories, number_test_trajectories) * 2 * np.pi / number_test_trajectories
t2 = np.linspace(1, number_test_trajectories, number_test_trajectories) * 2 * np.pi / number_test_trajectories

for i in range(number_increments):
    for j in range(number_test_trajectories):
        for k in range(number_test_trajectories):
            full_deviation_dx0.append(np.array([r[i] * np.cos(t1[j]) * np.sin(t2[k]), r[i] * np.sin(t1[j]) * np.sin(t2[k]), r[i] * np.cos(t2[k])]))


true_output_signals_stt, nominal_output_signal_stt, true_output_signals_order1, true_output_signals_order2, true_output_signals_order3, true_output_signals_order4, dynamics, linearized_system_order1, linearized_system_order2, linearized_system_order3, linearized_system_order4 = main_STT(full_deviation_dx0, x0)
RMSE_STT = np.zeros([4, number_increments, number_test_trajectories])

for i in range(number_increments):
    for j in range(number_test_trajectories):
        RMSE_STT[0, i, j] = np.sqrt(np.mean(subtract2Signals(true_output_signals_stt[i * number_test_trajectories + j], true_output_signals_order1[i * number_test_trajectories + j]).data[:, :-end] ** 2))
        RMSE_STT[1, i, j] = np.sqrt(np.mean(subtract2Signals(true_output_signals_stt[i * number_test_trajectories + j], true_output_signals_order2[i * number_test_trajectories + j]).data[:, :-end] ** 2))
        RMSE_STT[2, i, j] = np.sqrt(np.mean(subtract2Signals(true_output_signals_stt[i * number_test_trajectories + j], true_output_signals_order3[i * number_test_trajectories + j]).data[:, :-end] ** 2))
        RMSE_STT[3, i, j] = np.sqrt(np.mean(subtract2Signals(true_output_signals_stt[i * number_test_trajectories + j], true_output_signals_order4[i * number_test_trajectories + j]).data[:, :-end] ** 2))


# max_order = 8
# RMSE_Koopman = np.zeros([2, max_order, number_increments, number_test_trajectories])
#
#
# for o in range(1, max_order + 1):
#     true_output_signals, identified_output_signals_tvera, identified_output_signals_era, free_decay_experiments, nominal_output_signal = main_Koopman(o, full_deviation_dx0, x0)
#     for i in range(number_increments):
#         for j in range(number_test_trajectories):
#             RMSE_Koopman[0, o - 1, i, j] = np.sqrt(np.mean(subtract2Signals(true_output_signals[i * number_test_trajectories + j], identified_output_signals_tvera[i * number_test_trajectories + j]).data[:, :-end] ** 2))
#             RMSE_Koopman[1, o - 1, i, j] = np.sqrt(np.mean(subtract2Signals(true_output_signals[i * number_test_trajectories + j], identified_output_signals_era[i * number_test_trajectories + j]).data[:, :-end] ** 2))
#

# for i in range(3, 4):
#     for j in range(6, 7):
#         print('Case', i * 10 + j)
#
#         true_output_signal, identified_output_signal_era, identified_output_signal_tvera, free_decay_experiments, full_experiment, nominal_output_signal = main_Koopman(i+1, np.array([dev[j], dev[j]]))
#         # true_output_signal, identified_output_signal_era, identified_output_signal_tvera, free_decay_experiments, full_experiment, nominal_output_signal = main(i + 1, np.array([dev[j], dev[j]]))
#
#         RMSE_TIKO = np.sqrt(np.mean(subtract2Signals(true_output_signal, identified_output_signal_era).data[:, :-end] ** 2))
#         RMSE_TVKO = np.sqrt(np.mean(subtract2Signals(true_output_signal, identified_output_signal_tvera).data[:, :-end] ** 2))
#         # RMSE_Phi1 = np.sqrt(np.mean(subtract2Signals(true_output_signal, true_output_signal_order1).data[:, :-end] ** 2))
#         # RMSE_Phi2 = np.sqrt(np.mean(subtract2Signals(true_output_signal, true_output_signal_order2).data[:, :-end] ** 2))
#         # RMSE_Phi3 = np.sqrt(np.mean(subtract2Signals(true_output_signal, true_output_signal_order3).data[:, :-10] ** 2))
#         # RMSE_Phi4 = np.sqrt(np.mean(subtract2Signals(true_output_signal, true_output_signal_order4).data[:, :-10] ** 2))
#         RMSE_Koopman[0, j, i] = RMSE_TIKO
#         RMSE_Koopman[1, j, i] = RMSE_TVKO

# true_output_signal, identified_output_signal_era, identified_output_signal_tvera, free_decay_experiments, full_experiment, nominal_output_signal, true_output_signal_order1, true_output_signal_order2 = main(1, np.array([dev[7], dev[7]]))
#
# RMSE_Phi1 = np.sqrt(np.mean(subtract2Signals(true_output_signal, true_output_signal_order1).data[:, :-end] ** 2))
# RMSE_Phi2 = np.sqrt(np.mean(subtract2Signals(true_output_signal, true_output_signal_order2).data[:, :-end] ** 2))

########################################################################################################################
#####################################################  PLOTTING  #######################################################
########################################################################################################################

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


plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
rc('text', usetex=True)



# fig = plt.figure(1, figsize=(8, 5))
# ax = plt.subplot(111)
# for i in range(free_decay_experiments.number_experiments):
#     ax.plot(free_decay_experiments.output_signals[i].data[0, :-end], free_decay_experiments.output_signals[i].data[1, :-end], color=colors[9])
# for i in range(free_decay_experiments.number_experiments):
#     ax.plot(free_decay_experiments.output_signals[i].data[0, 0], free_decay_experiments.output_signals[i].data[1, 0], '.', color=colors[10])
# ax.plot(nominal_output_signal.data[0, :-end], nominal_output_signal.data[1, :-end], color=colors[0], label='Nominal')
# ax.plot(true_output_signal.data[0, :-end], true_output_signal.data[1, :-end], color=colors[5], label='True')
# ax.plot(identified_output_signal_era.data[0, :-850], identified_output_signal_era.data[1, :-850], '--', color=colors[6], label='ERA')
# ax.plot(identified_output_signal_tvera.data[0, :-end], identified_output_signal_tvera.data[1, :-end], '--', color=colors[7], label='TVERA')
# # ax.plot(true_output_signal_order1.data[0, :-end], true_output_signal_order1.data[1, :-end], '--', color=colors[9], label='Linearized order 1')
# # ax.plot(true_output_signal_order2.data[0, :-450], true_output_signal_order2.data[1, :-450], '--', color=colors[8], label='Linearized order 2')
# plt.xlabel(r'$x_1$')
# plt.ylabel(r'$x_2$')
# ax.legend(loc='upper left')
# plt.tight_layout()
# # plt.savefig('limit_cycle.eps', format='eps')
# plt.show()



id = 1500
end_point = 10

fig = plt.figure(1, figsize=(12, 7))
# ax = plt.subplot(111)
ax = plt.axes(projection='3d')
ax.plot3D(nominal_output_signal_stt.data[0, :], nominal_output_signal_stt.data[1, :], nominal_output_signal_stt.data[2, :], color=colors[0], label='Nominal')
ax.plot3D(true_output_signals_stt[id].data[0, :], true_output_signals_stt[id].data[1, :], true_output_signals_stt[id].data[2, :], color=colors[5], label='True')
# ax.plot3D(identified_output_signals_tvera[id].data[0, :], identified_output_signals_tvera[id].data[1, :], identified_output_signals_tvera[id].data[2, :], color=colors[2], label='TVKO order 2')
ax.plot(true_output_signals_order1[id].data[0, :-end_point], true_output_signals_order1[id].data[1, :-end_point], true_output_signals_order1[id].data[2, :-end_point], '--', color=colors[1], label='Taylor order 1')
ax.plot(true_output_signals_order2[id].data[0, :-end_point], true_output_signals_order2[id].data[1, :-end_point], true_output_signals_order2[id].data[2, :-end_point], '--', color=colors[2], label='Taylor order 2')
ax.plot(true_output_signals_order3[id].data[0, :-end_point], true_output_signals_order3[id].data[1, :-end_point], true_output_signals_order3[id].data[2, :-end_point], '--', color=colors[3], label='Taylor order 3')
ax.plot(true_output_signals_order3[id].data[0, :-end_point], true_output_signals_order3[id].data[1, :-end_point], true_output_signals_order3[id].data[2, :-end_point], '--', color=colors[3], label='Taylor order 4')
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
ax.legend(loc='upper left')
plt.tight_layout()
# plt.savefig('limit_cycle.eps', format='eps')
plt.show()






fig = plt.figure(1, figsize=(8, 5))
ax = plt.subplot(111)
# ax.semilogy(r, np.mean(RMSE_Koopman[0, 0, :, :], axis=1), color=colors[1], label='TVKO order 1')
# ax.semilogy(r, np.mean(RMSE_Koopman[0, 1, :, :], axis=1), color=colors[2], label='TVKO order 2')
# ax.semilogy(r, np.mean(RMSE_Koopman[0, 2, :, :], axis=1), color=colors[3], label='TVKO order 3')
# ax.semilogy(r, np.mean(RMSE_Koopman[0, 3, :, :], axis=1), color=colors[4], label='TVKO order 4')
# ax.semilogy(r, np.mean(RMSE_Koopman[0, 4, :, :], axis=1), color=colors[6], label='TVKO order 5')
# ax.semilogy(r, np.mean(RMSE_Koopman[0, 5, :, :], axis=1), color=colors[7], label='TVKO order 6')
# ax.semilogy(r, np.mean(RMSE_Koopman[0, 6, :, :], axis=1), color=colors[8], label='TVKO order 7')
# ax.semilogy(r, np.mean(RMSE_Koopman[0, 7, :, :], axis=1), color=colors[9], label='TVKO order 8')
# ax.semilogy(r, np.mean(RMSE_STT[0, :, :], axis=1), '--', color=colors[1], label='Taylor order 1')
# ax.semilogy(r, np.mean(RMSE_STT[1, :, :], axis=1), '--', color=colors[2], label='Taylor order 2')
# ax.semilogy(r, np.mean(RMSE_STT[2, :, :], axis=1), '--', color=colors[3], label='Taylor order 3')
# ax.semilogy(r, np.mean(RMSE_STT[3, :, :], axis=1), '--', color=colors[4], label='Fourth order')
plt.xlabel(r'$||\delta x_0||$')
plt.ylabel(r'RMSE')
ax.legend(loc='lower right')
plt.tight_layout()
# plt.savefig('limit_cycle.eps', format='eps')
plt.show()









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
# plt.semilogy(np.linspace(0 + start * errors_tvera[1].dt, errors_tvera[1].total_time - pp * errors_tvera[1].dt, errors_tvera[1].number_steps - pp - start), LA.norm(errors_tvera[1].data[:, start:-pp], axis=0), color=colors[6], label='TVKO order 2')
# plt.semilogy(np.linspace(0 + start * errors_tvera[2].dt, errors_tvera[2].total_time - pp * errors_tvera[2].dt, errors_tvera[2].number_steps - pp - start), LA.norm(errors_tvera[2].data[:, start:-pp], axis=0), color=colors[7], label='TVKO order 3')
# plt.semilogy(np.linspace(0 + start * errors_tvera[3].dt, errors_tvera[3].total_time - pp * errors_tvera[3].dt, errors_tvera[3].number_steps - pp - start), LA.norm(errors_tvera[3].data[:, start:-pp], axis=0), color=colors[8], label='TVKO order 4')
# plt.semilogy(np.linspace(0 + start * errors_tvera[4].dt, errors_tvera[4].total_time - pp * errors_tvera[4].dt, errors_tvera[4].number_steps - pp - start), LA.norm(errors_tvera[4].data[:, start:-pp], axis=0), color=colors[9], label='TVKO order 5')
# plt.xlabel('Time [sec]')
# plt.ylabel('State error')
# plt.legend(loc='lower right')
# plt.tight_layout()
# plt.savefig('Error_Duffing_TVKO_along_nonzero.eps', format='eps')
# plt.show()
#
#
# pp = 1
# start = 2
# # Error plots
# fig = plt.figure(num=2, figsize=[4, 3])
# plt.semilogy(np.linspace(0 + start * errors_era[0].dt, errors_era[0].total_time - pp * errors_era[0].dt, errors_era[0].number_steps - pp - start), LA.norm(errors_era[0].data[:, start:-pp], axis=0), color=colors[5], label='TIKO order 1')
# plt.semilogy(np.linspace(0 + start * errors_era[1].dt, errors_era[1].total_time - pp * errors_era[1].dt, errors_era[1].number_steps - pp - start), LA.norm(errors_era[1].data[:, start:-pp], axis=0), color=colors[6], label='TIKO order 2')
# plt.semilogy(np.linspace(0 + start * errors_era[2].dt, errors_era[2].total_time - pp * errors_era[2].dt, errors_era[2].number_steps - pp - start), LA.norm(errors_era[2].data[:, start:-pp], axis=0), color=colors[7], label='TIKO order 3')
# plt.semilogy(np.linspace(0 + start * errors_era[3].dt, errors_era[3].total_time - pp * errors_era[3].dt, errors_era[3].number_steps - pp - start), LA.norm(errors_era[3].data[:, start:-pp], axis=0), color=colors[8], label='TIKO order 4')
# plt.semilogy(np.linspace(0 + start * errors_era[4].dt, errors_era[4].total_time - pp * errors_era[4].dt, errors_era[4].number_steps - pp - start), LA.norm(errors_era[4].data[:, start:-pp], axis=0), color=colors[9], label='TIKO order 5')
# plt.xlabel('Time [sec]')
# plt.ylabel('State error')
# plt.legend(loc='lower right')
# plt.tight_layout()
# plt.savefig('Error_Duffing_TIKO_along_nonzero.eps', format='eps')
# plt.show()


