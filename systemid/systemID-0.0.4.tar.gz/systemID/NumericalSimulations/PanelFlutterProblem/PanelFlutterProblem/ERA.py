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
from ClassesGeneral.ClassExperiments import Experiments
from SystemIDAlgorithms.DepartureDynamics import departureDynamicsFromInitialConditionResponse
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, addSignals, subtract2Signals
from Plotting.PlotSignals import plotSignals
from ClassesSystemID.ClassERA import ERAFromInitialConditionResponse
from Plotting.PlotSingularValues import plotSingularValues
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassERA import TVERAFromInitialConditionResponse
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck
from NumericalSimulations.PanelFlutterProblem.PanelFlutterProblem.PlotFormating import plotResponse3, plotEigenValues, plotSVD
from SystemIDAlgorithms.CreateAugmentedSignal import createAugmentedSignalPolynomialBasisFunctions, createAugmentedSignalWithGivenFunctions


## Parameters for Dynamics
print('Define Parameters')
def RT(t):
    return 0
def mu(t):
    return 0.01
def M(t):
    return 5
def l(t):
    return 300


# Import Dynamics
print('Import Dynamics')
dynamics = PanelFlutterDynamics(RT, mu, M, l)


# Parameters for identification
total_time = 10
frequency = 50
dt = 1 / frequency
number_steps = int(total_time * frequency) + 1
tspan = np.linspace(0, total_time, number_steps)



# ## Nominal System
# nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.array([0.001, 0, 0, 0]), 0)], 'Nominal System', dynamics.F, dynamics.G)
# nominal_input_signal = ContinuousSignal(dynamics.input_dimension)
# nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan)
#
#
#
# ## Input signal
# number_experiments = 1
# systems = []
# initial_states = []
# input_signals = []
# for i in range(number_experiments):
#     init_state = [(np.array([0.001, 0, 0, 0]), 0)]
#     initial_states.append(init_state)
#     systems.append(ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, init_state, 'Nominal System', dynamics.F, dynamics.G))
#     input_signals.append(nominal_input_signal)
#
#
#
# ## Output signal
# Exp = Experiments(systems, input_signals, tspan=tspan)
#
#
#
# # Update dynamics with nominal trajectory
# r = 4
# total_time_test = total_time - r / frequency
# number_steps_test = number_steps - r
# tspan_test = np.linspace(0, total_time_test, number_steps_test)
# dynamics = PanelFlutterDynamics(RT, mu, M, l, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, total_time, frequency, signal_shape='External', data=nominal_output_signal.state), nominal_u=DiscreteSignal(dynamics.input_dimension, total_time, frequency, signal_shape='External', data=nominal_input_signal.u(tspan)), dt=1/frequency)
# nominal_output_signal_test = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan_test)
# nominal_input_signal_d = DiscreteSignal(dynamics.input_dimension, total_time_test, frequency)
# Sys = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.array([0.001, 0, 0, 0]), 0)], 'Nominal System', dynamics.A, dynamics.B, dynamics.C, dynamics.D)
#
#
# ## Plotting
# # plotSignals([Exp.output_signals], 1)
#
#
#
# ## Koopman
# order = 3
# max_order = order
# for i in range(Exp.number_experiments):
#     Exp.output_signals[i] = createAugmentedSignalPolynomialBasisFunctions(Exp.output_signals[i], order, True, max_order)
#     # Exp.output_signals[i] = createAugmentedSignalWithGivenFunctions(Exp.output_signals[i], [lambda x: x[0] ** 2])
#
# Exp.output_dimension = Exp.output_signals[0].dimension
# #
# ## Calculate Markov Parameters and Identified system
# assumed_order = Exp.output_dimension
# ERA1 = ERAFromInitialConditionResponse(Exp.output_signals, assumed_order, dynamics.input_dimension)
#
#
#
#
# ## Define Identified System
# SysID = DiscreteLinearSystem(frequency, assumed_order, dynamics.input_dimension, Exp.output_dimension, [(ERA1.x0[:, 0], 0)], 'Identified System', ERA1.A, ERA1.B, ERA1.C, ERA1.D)
#
#
# ## Define the Identified Output Signal
# S2ID = OutputSignal(DiscreteSignal(dynamics.input_dimension, total_time, frequency), SysID)
#
#
#
# # ## Plotting
# # plotSignals([[Exp.output_signals[0], S2ID], [subtract2Signals(Exp.output_signals[0], S2ID)]], 2)
# # plotEigenValues([Sys, SysID], 500, 2)
# # plotSingularValues([ERA1], ['IdentifiedSystem'], 3)
# # plotMarkovParameters2(markov_parameters, markov_parameters_true, 'OKID', 'True', 4)
#
#
#
# np.save('S2_300_3', Exp.output_signals[0].data, allow_pickle=True)
# np.save('S2ID_300_3', S2ID.data, allow_pickle=True)







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

## Load Data
S2_260_1 = np.load('S2_260_1.npy')
S2_260_2 = np.load('S2_260_2.npy')
S2_260_3 = np.load('S2_260_3.npy')
S2_270_1 = np.load('S2_270_1.npy')
S2_270_2 = np.load('S2_270_2.npy')
S2_270_3 = np.load('S2_270_3.npy')
S2_280_1 = np.load('S2_280_1.npy')
S2_280_2 = np.load('S2_280_2.npy')
S2_280_3 = np.load('S2_280_3.npy')
S2_290_1 = np.load('S2_290_1.npy')
S2_290_2 = np.load('S2_290_2.npy')
S2_290_3 = np.load('S2_290_3.npy')
S2_300_1 = np.load('S2_300_1.npy')
S2_300_2 = np.load('S2_300_2.npy')
S2_300_3 = np.load('S2_300_3.npy')
S2ID_260_1 = np.load('S2ID_260_1.npy')
S2ID_260_2 = np.load('S2ID_260_2.npy')
S2ID_260_3 = np.load('S2ID_260_3.npy')
S2ID_270_1 = np.load('S2ID_270_1.npy')
S2ID_270_2 = np.load('S2ID_270_2.npy')
S2ID_270_3 = np.load('S2ID_270_3.npy')
S2ID_280_1 = np.load('S2ID_280_1.npy')
S2ID_280_2 = np.load('S2ID_280_2.npy')
S2ID_280_3 = np.load('S2ID_280_3.npy')
S2ID_290_1 = np.load('S2ID_290_1.npy')
S2ID_290_2 = np.load('S2ID_290_2.npy')
S2ID_290_3 = np.load('S2ID_290_3.npy')
S2ID_300_1 = np.load('S2ID_300_1.npy')
S2ID_300_2 = np.load('S2ID_300_2.npy')
S2ID_300_3 = np.load('S2ID_300_3.npy')




fig = plt.figure(10, figsize=(5, 3))
ax = plt.subplot(111)
ax.plot(tspan, S2ID_260_1[0, :], '-', color=colors[6], label='TI Koopman order 1')
ax.plot(tspan, S2ID_260_2[0, :], '-', color=colors[7], label='TI Koopman order 2')
ax.plot(tspan, S2ID_260_3[0, :], '-', color=colors[8], label='TI Koopman order 3')
ax.plot(tspan, S2_260_1[0, :], color=colors[0], label='True')
plt.xlabel('Time [s]')
plt.ylabel(r'$q_1$')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('q1_L260_TIK1.eps', format='eps')
plt.show()

fig = plt.figure(11, figsize=(5, 3))
ax = plt.subplot(111)
ax.plot(tspan, S2ID_260_1[1, :], '-', color=colors[6], label='TI Koopman order 1')
ax.plot(tspan, S2ID_260_2[1, :], '-', color=colors[7], label='TI Koopman order 2')
ax.plot(tspan, S2ID_260_3[1, :], '-', color=colors[8], label='TI Koopman order 3')
ax.plot(tspan, S2_260_1[1, :], color=colors[0], label='True')
plt.xlabel('Time [s]')
plt.ylabel(r'$q_2$')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('q2_L260_TIK1.eps', format='eps')
plt.show()

fig = plt.figure(12, figsize=(5, 3))
ax = plt.subplot(111)
ax.plot(tspan, S2ID_280_1[0, :], '-', color=colors[6], label='TI Koopman order 1')
ax.plot(tspan, S2ID_280_2[0, :], '-', color=colors[7], label='TI Koopman order 2')
ax.plot(tspan, S2ID_280_3[0, :], '-', color=colors[8], label='TI Koopman order 3')
ax.plot(tspan, S2_280_1[0, :], color=colors[0], label='True')
plt.xlabel('Time [s]')
plt.ylabel(r'$q_1$')
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('q1_L280_TIK1.eps', format='eps')
plt.show()

fig = plt.figure(13, figsize=(5, 3))
ax = plt.subplot(111)
ax.plot(tspan, S2ID_280_1[1, :], '-', color=colors[6], label='TI Koopman order 1')
ax.plot(tspan, S2ID_280_2[1, :], '-', color=colors[7], label='TI Koopman order 2')
ax.plot(tspan, S2ID_280_3[1, :], '-', color=colors[8], label='TI Koopman order 3')
ax.plot(tspan, S2_280_1[1, :], color=colors[0], label='True')
plt.xlabel('Time [s]')
plt.ylabel(r'$q_2$')
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('q2_L280_TIK1.eps', format='eps')
plt.show()

fig = plt.figure(14, figsize=(5, 3))
ax = plt.subplot(111)
ax.plot(tspan, S2ID_300_1[0, :], '-', color=colors[6], label='TI Koopman order 1')
ax.plot(tspan, S2ID_300_2[0, :], '-', color=colors[7], label='TI Koopman order 2')
ax.plot(tspan, S2ID_300_3[0, :], '-', color=colors[8], label='TI Koopman order 3')
ax.plot(tspan, S2_300_1[0, :], color=colors[0], label='True')
plt.xlabel('Time [s]')
plt.ylabel(r'$q_1$')
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('q1_L300_TIK1.eps', format='eps')
plt.show()

fig = plt.figure(15, figsize=(5, 3))
ax = plt.subplot(111)
ax.plot(tspan, S2ID_300_1[1, :], '-', color=colors[6], label='TI Koopman order 1')
ax.plot(tspan, S2ID_300_2[1, :], '-', color=colors[7], label='TI Koopman order 2')
ax.plot(tspan, S2ID_300_3[1, :], '-', color=colors[8], label='TI Koopman order 3')
ax.plot(tspan, S2_300_1[1, :], color=colors[0], label='True')
plt.xlabel('Time [s]')
plt.ylabel(r'$q_2$')
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('q2_L300_TIK1.eps', format='eps')
plt.show()




fig = plt.figure(16, figsize=(10, 3))
ax = plt.subplot(111)

labels = ['260', '270', '280', '290', '300']
TIK1 = [np.sqrt(((S2_260_1[0:2, :] - S2ID_260_1[0:2, :]) ** 2).mean()),
        np.sqrt(((S2_270_1[0:2, :] - S2ID_270_1[0:2, :]) ** 2).mean()),
        np.sqrt(((S2_280_1[0:2, :] - S2ID_280_1[0:2, :]) ** 2).mean()),
        np.sqrt(((S2_290_1[0:2, :] - S2ID_290_1[0:2, :]) ** 2).mean()),
        np.sqrt(((S2_300_1[0:2, :] - S2ID_300_1[0:2, :]) ** 2).mean())]
TIK2 = [np.sqrt(((S2_260_2[0:2, :] - S2ID_260_2[0:2, :]) ** 2).mean()),
        np.sqrt(((S2_270_2[0:2, :] - S2ID_270_2[0:2, :]) ** 2).mean()),
        np.sqrt(((S2_280_2[0:2, :] - S2ID_280_2[0:2, :]) ** 2).mean()),
        np.sqrt(((S2_290_2[0:2, :] - S2ID_290_2[0:2, :]) ** 2).mean()),
        np.sqrt(((S2_300_2[0:2, :] - S2ID_300_2[0:2, :]) ** 2).mean())]
TIK3 = [np.sqrt(((S2_260_3[0:2, :] - S2ID_260_3[0:2, :]) ** 2).mean()),
        np.sqrt(((S2_270_3[0:2, :] - S2ID_270_3[0:2, :]) ** 2).mean()),
        np.sqrt(((S2_280_3[0:2, :] - S2ID_280_3[0:2, :]) ** 2).mean()),
        np.sqrt(((S2_290_3[0:2, :] - S2ID_290_3[0:2, :]) ** 2).mean()),
        np.sqrt(((S2_300_3[0:2, :] - S2ID_300_3[0:2, :]) ** 2).mean())]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

rects1 = ax.bar(x - width, TIK1, width, label='TI Koopman order 1', color=colors[6])
rects2 = ax.bar(x, TIK2, width, label='TI Koopman order 2', color=colors[7])
rects3 = ax.bar(x + width, TIK3, width, label='TI Koopman order 3', color=colors[8])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('RMS Error')
ax.set_xlabel(r'$\lambda$')
ax.set_xticks(x)
ax.set_yscale('log')
ax.set_xticklabels(labels)
ax.legend()

# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)

plt.tight_layout()
plt.savefig('RMSE_L_TIK.eps', format='eps')

plt.show()

























