"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np
import pickle
from scipy import linalg as LA

from ClassesDynamics.ClassPanelFlutterDynamics import PanelFlutterDynamics
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, add2Signals, subtract2Signals
from ClassesGeneral.ClassExperiments import Experiments
from SparseIDAlgorithms.NormalizeSignals import normalizeSignals
from SparseIDAlgorithms.SparseApproximation2ndOrder import sparseApproximation2ndOrder
from ClassesSparseID.ClassSparseApproximation import SparseApproximation1stOrder
from Plotting.PlotSignals import plotSignals
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassERA import TVERAFromInitialConditionResponse
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck
from NumericalSimulations.PanelFlutterProblem.PanelFlutterProblem.PlotFormating import plotResponse3



# Parameters for Dynamics
RT = 10
mu = 0.01
M = 5
l = 290
frequency = 500
total_time = 2
number_steps = int(frequency * total_time) + 1


# Import Dynamics
dynamics = PanelFlutterDynamics(RT, mu, M, l)


# Create System
initial_state = [(np.array([0.001, 0, 0, 0]), 0)]
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_state, 'Nominal System', dynamics.F, dynamics.G)
nominal_system_d = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_state, 'Nominal System Discrete', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


# tspan
tspan = np.linspace(0, total_time, number_steps)


# Nominal Input Signal
nominal_input_signal = ContinuousSignal(dynamics.input_dimension, 'Nominal Input Signal')


# Nominal Output Signal
nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal', tspan=tspan)

plotSignals([[nominal_output_signal]], 3)
plotSignals([normalizeSignals([nominal_output_signal])], 1)

# Create Experiments
number_trajectories = 4
systems = []
input_signals = []
for i in range(number_trajectories):
    init_state = 0.001 * np.random.randn()
    system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.array([init_state, 0, 0, 0]), 0)], 'System ' + str(i), dynamics.F, dynamics.G)
    systems.append(system)
    input_signal = ContinuousSignal(dynamics.input_dimension, 'Zero')
    input_signals.append(input_signal)
experiments = Experiments(systems, input_signals, tspan=tspan)
for i in range(number_trajectories):
    experiments.input_signals[i] = DiscreteSignal(4, 'Prime term ' + str(i), total_time, frequency)
    #experiments.output_signals[i] = DiscreteSignal(5, 'Output ' + str(i), total_time, frequency, signal_shape='External', data=experiments.output_signals[i].data)


# Normalize Signals
#experiments.output_signals = normalizeSignals(experiments.output_signals)


## Sparse Approximation
order = 4
max_order = 4
post_treatment = 'true'
l1 = 1e-8
l2 = l1
alpha = 1.5
delta = [0.5, 0.5, 200, 200]
epsilon = 1e-20
max_iterations = 5
shift = 1
x0s_testing = [np.array([0.0000562, 0, 0, 0]), np.array([0.0000148, 0, 0, 0])]
SA = SparseApproximation1stOrder(experiments.output_signals, experiments.input_signals, x0s_testing, [experiments.input_signals[0], experiments.input_signals[1]], order, max_order, post_treatment, l1, alpha, delta, epsilon, max_iterations, shift)


















## Ploting
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


## Plotting results
output_signal_training_1 = DiscreteSignal(4, 'S2_nom', total_time - shift, frequency, signal_shape='External', data=experiments.output_signals[0].data[:, 0:int(number_steps-frequency*shift)])
output_signal_training_2 = DiscreteSignal(4, 'S2_nom', total_time - shift, frequency, signal_shape='External', data=experiments.output_signals[1].data[:, 0:int(number_steps-frequency*shift)])
nominal_output_signal_testing_1 = OutputSignal(nominal_input_signal, ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(x0s_testing[0], 0)], 'Nominal System', dynamics.F, dynamics.G), 'Nominal Output Signal', tspan=tspan)
nominal_output_signal_testing_2 = OutputSignal(nominal_input_signal, ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(x0s_testing[1], 0)], 'Nominal System', dynamics.F, dynamics.G), 'Nominal Output Signal', tspan=tspan)
output_signal_testing_1 = DiscreteSignal(4, 'S2_nom', total_time - shift, frequency, signal_shape='External', data=nominal_output_signal_testing_1.data[:, 0:int(number_steps-frequency*shift)])
output_signal_testing_2 = DiscreteSignal(4, 'S2_nom', total_time - shift, frequency, signal_shape='External', data=nominal_output_signal_testing_2.data[:, 0:int(number_steps-frequency*shift)])
output_signal_training_1_LS = DiscreteSignal(4, 'S2_nom', total_time - shift, frequency, signal_shape='External', data=SA.LS_signals[0].data[:, 0:int(number_steps-frequency*shift)])
output_signal_training_2_LS = DiscreteSignal(4, 'S2_nom', total_time - shift, frequency, signal_shape='External', data=SA.LS_signals[1].data[:, 0:int(number_steps-frequency*shift)])
output_signal_testing_1_LS = DiscreteSignal(4, 'S2_nom', total_time - shift, frequency, signal_shape='External', data=SA.LS_signals_testing[0].data[:, 0:int(number_steps-frequency*shift)])
output_signal_testing_2_LS = DiscreteSignal(4, 'S2_nom', total_time - shift, frequency, signal_shape='External', data=SA.LS_signals_testing[1].data[:, 0:int(number_steps-frequency*shift)])
output_signal_training_1_SP = DiscreteSignal(4, 'S2_nom', total_time - shift, frequency, signal_shape='External', data=SA.Sparse_signals[0].data[:, 0:int(number_steps-frequency*shift)])
output_signal_training_2_SP = DiscreteSignal(4, 'S2_nom', total_time - shift, frequency, signal_shape='External', data=SA.Sparse_signals[1].data[:, 0:int(number_steps-frequency*shift)])
output_signal_testing_1_SP = DiscreteSignal(4, 'S2_nom', total_time - shift, frequency, signal_shape='External', data=SA.Sparse_signals_testing[0].data[:, 0:int(number_steps-frequency*shift)])
output_signal_testing_2_SP = DiscreteSignal(4, 'S2_nom', total_time - shift, frequency, signal_shape='External', data=SA.Sparse_signals_testing[1].data[:, 0:int(number_steps-frequency*shift)])


## Plotting Coefficients
plt.figure(1, figsize=(8, 6))

plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
rc('text', usetex=True)

plt.subplot(221)
plt.semilogy(np.abs(SA.THETA_LS[:, 0]), '*', color=colors[7])
plt.semilogy(np.abs(SA.THETA_SPARSE[:, 0]), '.', color=colors[5])
plt.xlabel('\# in the dictionnary')
plt.ylabel('Absolute value of coefficients')
plt.legend(['LS Solution', 'Sparse Solution'], loc='upper right')
plt.title(r"Coefficients for $q_1$")
plt.subplot(222)
plt.semilogy(np.abs(SA.THETA_LS[:, 2]), '*', color=colors[7])
plt.semilogy(np.abs(SA.THETA_SPARSE[:, 2]), '.', color=colors[5])
plt.xlabel('\# in the dictionnary')
plt.ylabel('Absolute value of coefficients')
plt.legend(['LS Solution', 'Sparse Solution'], loc='upper right')
plt.title(r"Coefficients for $q_1'$")
plt.subplot(223)
plt.semilogy(np.abs(SA.THETA_LS[:, 1]), '*', color=colors[7])
plt.semilogy(np.abs(SA.THETA_SPARSE[:, 1]), '.', color=colors[5])
plt.xlabel('\# in the dictionnary')
plt.ylabel('Absolute value of coefficients')
plt.legend(['LS Solution', 'Sparse Solution'], loc='upper right')
plt.title(r"Coefficients for $q_2$")
plt.subplot(224)
plt.semilogy(np.abs(SA.THETA_LS[:, 3]), '*', color=colors[7])
plt.semilogy(np.abs(SA.THETA_SPARSE[:, 3]), '.', color=colors[5])
plt.xlabel('\# in the dictionnary')
plt.ylabel('Absolute value of coefficients')
plt.legend(['LS Solution', 'Sparse Solution'], loc='upper right')
plt.title(r"Coefficients for $q_2'$")

plt.tight_layout()
plt.savefig('coeff_pf_n=4.eps', format='eps')

plt.show()



## Plotting Iterations
plt.figure(2, figsize=(15, 12))

plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
rc('text', usetex=True)

plt.subplot(4, 5, 1)
plt.semilogy(np.abs(SA.C[0, :, 0]), '.', color=colors[5])
plt.ylabel(r"Abs. value of coefficients - $q_1$")
plt.title(r"\textbf{Iteration 1}")
plt.subplot(4, 5, 2)
plt.semilogy(np.abs(SA.C[0, :, 1]), '.', color=colors[5])
plt.title(r"\textbf{Iteration 2}")
plt.subplot(4, 5, 3)
plt.semilogy(np.abs(SA.C[0, :, 2]), '.', color=colors[5])
plt.title(r"\textbf{Iteration 3}")
plt.subplot(4, 5, 4)
plt.semilogy(np.abs(SA.C[0, :, 3]), '.', color=colors[5])
plt.title(r"\textbf{Iteration 4}")
plt.subplot(4, 5, 5)
plt.semilogy(np.abs(SA.C[0, :, 4]), '.', color=colors[5])
plt.title(r"\textbf{Iteration 5}")
plt.subplot(4, 5, 6)
plt.semilogy(np.abs(SA.C[1, :, 0]), '.', color=colors[5])
plt.ylabel(r"Abs. value of coefficients - $q_2$")
plt.subplot(4, 5, 7)
plt.semilogy(np.abs(SA.C[1, :, 1]), '.', color=colors[5])
plt.subplot(4, 5, 8)
plt.semilogy(np.abs(SA.C[1, :, 2]), '.', color=colors[5])
plt.subplot(4, 5, 9)
plt.semilogy(np.abs(SA.C[1, :, 3]), '.', color=colors[5])
plt.subplot(4, 5, 10)
plt.semilogy(np.abs(SA.C[1, :, 4]), '.', color=colors[5])
plt.subplot(4, 5, 11)
plt.semilogy(np.abs(SA.C[2, :, 0]), '.', color=colors[5])
plt.ylabel(r"Abs. value of coefficients - $q_1'$")
plt.subplot(4, 5, 12)
plt.semilogy(np.abs(SA.C[2, :, 1]), '.', color=colors[5])
plt.subplot(4, 5, 13)
plt.semilogy(np.abs(SA.C[2, :, 2]), '.', color=colors[5])
plt.subplot(4, 5, 14)
plt.semilogy(np.abs(SA.C[2, :, 3]), '.', color=colors[5])
plt.subplot(4, 5, 15)
plt.semilogy(np.abs(SA.C[2, :, 4]), '.', color=colors[5])
plt.subplot(4, 5, 16)
plt.semilogy(np.abs(SA.C[3, :, 0]), '.', color=colors[5])
plt.xlabel('\# in the dictionnary')
plt.ylabel(r"Abs. value of coefficients - $q_2'$")
plt.subplot(4, 5, 17)
plt.semilogy(np.abs(SA.C[3, :, 1]), '.', color=colors[5])
plt.xlabel('\# in the dictionnary')
plt.subplot(4, 5, 18)
plt.semilogy(np.abs(SA.C[3, :, 2]), '.', color=colors[5])
plt.xlabel('\# in the dictionnary')
plt.subplot(4, 5, 19)
plt.semilogy(np.abs(SA.C[3, :, 3]), '.', color=colors[5])
plt.xlabel('\# in the dictionnary')
plt.subplot(4, 5, 20)
plt.semilogy(np.abs(SA.C[3, :, 4]), '.', color=colors[5])
plt.xlabel('\# in the dictionnary')

plt.tight_layout()
plt.savefig('iterations_pf_n=4.eps', format='eps')

plt.show()


## Error Sparse Orbits
fig = plt.figure(3, figsize=(20, 12))

plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
rc('text', usetex=True)

gs = fig.add_gridspec(8, 4)

tspan_plot = np.linspace(0, total_time - shift, frequency * (total_time - shift) + 1)

ax = fig.add_subplot(gs[0:2, 0])
ax.plot(tspan_plot, output_signal_training_1.data[0, :], color=colors[0])
ax.plot(tspan_plot, output_signal_training_1_LS.data[0, :], color=colors[7], linestyle='--')
ax.plot(tspan_plot, output_signal_training_1_SP.data[0, :], color=colors[5], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"$q_1$")
plt.legend(['True Signal', 'LS approx.', 'Sparse approx.'])
plt.title(r"\textbf{Signal from Training Set}")
ax = fig.add_subplot(gs[0, 1])
ax.plot(tspan_plot, output_signal_training_1.data[0, :] - output_signal_training_1_LS.data[0, :], color=colors[8], linestyle='--')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_1$")
plt.legend(['Error LS'])
plt.title(r"\textbf{Error}")
ax = fig.add_subplot(gs[1, 1])
ax.plot(tspan_plot, output_signal_training_1.data[0, :] - output_signal_training_1_SP.data[0, :], color=colors[6], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_1$")
plt.legend(['Error Sparse'])

ax = fig.add_subplot(gs[0:2, 2])
ax.plot(tspan_plot, output_signal_testing_1.data[0, :], color=colors[0])
ax.plot(tspan_plot, output_signal_testing_1_LS.data[0, :], color=colors[7], linestyle='--')
ax.plot(tspan_plot, output_signal_testing_1_SP.data[0, :], color=colors[5], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"$q_1$")
plt.legend(['True Signal', 'LS approx.', 'Sparse approx.'])
plt.title(r"\textbf{Signal from Testing Set}")
ax = fig.add_subplot(gs[0, 3])
ax.plot(tspan_plot, output_signal_testing_1.data[0, :] - output_signal_testing_1_LS.data[0, :], color=colors[8], linestyle='--')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_1$")
plt.legend(['Error LS'])
plt.title(r"\textbf{Error}")
ax = fig.add_subplot(gs[1, 3])
ax.plot(tspan_plot, output_signal_testing_1.data[0, :] - output_signal_testing_1_SP.data[0, :], color=colors[6], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_1$")
plt.legend(['Error Sparse'])


ax = fig.add_subplot(gs[2:4, 0])
ax.plot(tspan_plot, output_signal_training_1.data[1, :], color=colors[0])
ax.plot(tspan_plot, output_signal_training_1_LS.data[1, :], color=colors[7], linestyle='--')
ax.plot(tspan_plot, output_signal_training_1_SP.data[1, :], color=colors[5], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"$q_2$")
plt.legend(['True Signal', 'LS approx.', 'Sparse approx.'])
ax = fig.add_subplot(gs[2, 1])
ax.plot(tspan_plot, output_signal_training_1.data[1, :] - output_signal_training_1_LS.data[1, :], color=colors[8], linestyle='--')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_2$")
plt.legend(['Error LS'])
ax = fig.add_subplot(gs[3, 1])
ax.plot(tspan_plot, output_signal_training_1.data[1, :] - output_signal_training_1_SP.data[1, :], color=colors[6], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_2$")
plt.legend(['Error Sparse'])

ax = fig.add_subplot(gs[2:4, 2])
ax.plot(tspan_plot, output_signal_testing_1.data[1, :], color=colors[0])
ax.plot(tspan_plot, output_signal_testing_1_LS.data[1, :], color=colors[7], linestyle='--')
ax.plot(tspan_plot, output_signal_testing_1_SP.data[1, :], color=colors[5], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"$q_2$")
plt.legend(['True Signal', 'LS approx.', 'Sparse approx.'])
ax = fig.add_subplot(gs[2, 3])
ax.plot(tspan_plot, output_signal_testing_1.data[1, :] - output_signal_testing_1_LS.data[1, :], color=colors[8], linestyle='--')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_2$")
plt.legend(['Error LS'])
ax = fig.add_subplot(gs[3, 3])
ax.plot(tspan_plot, output_signal_testing_1.data[1, :] - output_signal_testing_1_SP.data[1, :], color=colors[6], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_2$")
plt.legend(['Error Sparse'])

ax = fig.add_subplot(gs[4:6, 0])
ax.plot(tspan_plot, output_signal_training_1.data[2, :], color=colors[0])
ax.plot(tspan_plot, output_signal_training_1_LS.data[2, :], color=colors[7], linestyle='--')
ax.plot(tspan_plot, output_signal_training_1_SP.data[2, :], color=colors[5], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"$q_1'$")
plt.legend(['True Signal', 'LS approx.', 'Sparse approx.'])
ax = fig.add_subplot(gs[4, 1])
ax.plot(tspan_plot, output_signal_training_1.data[2, :] - output_signal_training_1_LS.data[2, :], color=colors[8], linestyle='--')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_1'$")
plt.legend(['Error LS'])
ax = fig.add_subplot(gs[5, 1])
ax.plot(tspan_plot, output_signal_training_1.data[2, :] - output_signal_training_1_SP.data[2, :], color=colors[6], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_1'$")
plt.legend(['Error Sparse'])

ax = fig.add_subplot(gs[4:6, 2])
ax.plot(tspan_plot, output_signal_testing_1.data[2, :], color=colors[0])
ax.plot(tspan_plot, output_signal_testing_1_LS.data[2, :], color=colors[7], linestyle='--')
ax.plot(tspan_plot, output_signal_testing_1_SP.data[2, :], color=colors[5], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"$q_1'$")
plt.legend(['True Signal', 'LS approx.', 'Sparse approx.'])
ax = fig.add_subplot(gs[4, 3])
ax.plot(tspan_plot, output_signal_testing_1.data[2, :] - output_signal_testing_1_LS.data[2, :], color=colors[8], linestyle='--')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_1'$")
plt.legend(['Error LS'])
ax = fig.add_subplot(gs[5, 3])
ax.plot(tspan_plot, output_signal_testing_1.data[2, :] - output_signal_testing_1_SP.data[2, :], color=colors[6], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_1'$")
plt.legend(['Error Sparse'])

ax = fig.add_subplot(gs[6:8, 0])
ax.plot(tspan_plot, output_signal_training_1.data[3, :], color=colors[0])
ax.plot(tspan_plot, output_signal_training_1_LS.data[3, :], color=colors[7], linestyle='--')
ax.plot(tspan_plot, output_signal_training_1_SP.data[3, :], color=colors[5], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"$q_2'$")
plt.legend(['True Signal', 'LS approx.', 'Sparse approx.'])
ax = fig.add_subplot(gs[6, 1])
ax.plot(tspan_plot, output_signal_training_1.data[3, :] - output_signal_training_1_LS.data[3, :], color=colors[8], linestyle='--')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_2'$")
plt.legend(['Error LS'])
ax = fig.add_subplot(gs[7, 1])
ax.plot(tspan_plot, output_signal_training_1.data[3, :] - output_signal_training_1_SP.data[3, :], color=colors[6], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_2'$")
plt.legend(['Error Sparse'])

ax = fig.add_subplot(gs[6:8, 2])
ax.plot(tspan_plot, output_signal_testing_1.data[3, :], color=colors[0])
ax.plot(tspan_plot, output_signal_testing_1_LS.data[3, :], color=colors[7], linestyle='--')
ax.plot(tspan_plot, output_signal_testing_1_SP.data[3, :], color=colors[5], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"$q_2'$")
plt.legend(['True Signal', 'LS approx.', 'Sparse approx.'])
ax = fig.add_subplot(gs[6, 3])
ax.plot(tspan_plot, output_signal_testing_1.data[3, :] - output_signal_testing_1_LS.data[3, :], color=colors[8], linestyle='--')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_2'$")
plt.legend(['Error LS'])
ax = fig.add_subplot(gs[7, 3])
ax.plot(tspan_plot, output_signal_testing_1.data[3, :] - output_signal_testing_1_SP.data[3, :], color=colors[6], linestyle='-.')
plt.xlabel('Time [sec]')
plt.ylabel(r"Error in $q_2'$")
plt.legend(['Error Sparse'])

plt.tight_layout()

plt.savefig('prop_pf_n=4.eps', format='eps')

plt.show()



