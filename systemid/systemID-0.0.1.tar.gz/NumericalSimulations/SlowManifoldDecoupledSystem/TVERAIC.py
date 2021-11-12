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
from scipy import signal

from ClassesDynamics.ClassSlowManifoldDecoupledSystemDynamics import SlowManifoldDecoupledSystemDynamics
from ClassesGeneral.ClassSystem import DiscreteLinearSystem, ContinuousNonlinearSystem, ContinuousLinearSystem
from ClassesGeneral.ClassSignal import OutputSignal, subtract2Signals, add2Signals, ContinuousSignal, DiscreteSignal
from ClassesGeneral.ClassExperiments import Experiments
from ClassesSystemID.ClassMarkovParameters import *
from ClassesSystemID.ClassERA import ERAFromInitialConditionResponse, ERA
from SystemIDAlgorithms.IdentificationInitialCondition import identificationInitialCondition
from SystemIDAlgorithms.GetMarkovParameters import getMarkovParameters
from SystemIDAlgorithms.GetInitialConditionResponseMarkovParameters import getInitialConditionResponseMarkovParameters
from Plotting.PlotEigenValues import plotEigenValues
from Plotting.PlotSignals import plotSignals
from Plotting.PlotSingularValues import plotSingularValues
from Plotting.PlotMarkovParameters2 import plotMarkovParameters2


## Parameters for Dynamics
def mu(t):
    return  -0.5 + 1.5*np.sin(2*np.pi*2*t)
def l(t):
    return  -0.2 + 0.5*np.cos(2*np.pi*3*t)
dt = 0.1



## Parameters
frequency = 50
total_time = 10
number_steps = int(total_time * frequency) + 1
tspan = np.linspace(0, total_time, number_steps)



## Import Dynamics
dynamics = SlowManifoldDecoupledSystemDynamics(mu, l)



## Nominal System
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.array([0, 0, 0]), 0)], 'Nominal System', dynamics.F, dynamics.G)
nominal_input_signal = ContinuousSignal(dynamics.input_dimension, 'Nominal Input Signal')
nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal', tspan=tspan)



## Input signal
number_experiments = 1
systems = []
initial_states = []
input_signals = []
for i in range(number_experiments):
    init_state = [(np.array([0.5, 0.75, 0.25]), 0)]
    initial_states.append(init_state)
    systems.append(ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, init_state, 'Nominal System', dynamics.F, dynamics.G))
    input_signals.append(nominal_input_signal)



## Output signal
Exp = Experiments(systems, input_signals, tspan=tspan)



# Update dynamics with nominal trajectory
r = 4
total_time_test = total_time - r / frequency
number_steps_test = number_steps - r
tspan_test = np.linspace(0, total_time_test, number_steps_test)
dynamics = SlowManifoldDecoupledSystemDynamics(mu, l, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, 'Nominal Trajectory', total_time, frequency, signal_shape='External', data=nominal_output_signal.state), nominal_u=DiscreteSignal(dynamics.input_dimension, 'Nominal Input Signal', total_time, frequency, signal_shape='External', data=nominal_input_signal.u(tspan)), dt=1/frequency)
nominal_output_signal_test = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal Test', tspan=tspan_test)
nominal_input_signal_d = DiscreteSignal(dynamics.input_dimension, 'Nominal Input Signal', total_time_test, frequency)
Sys = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.array([0, 0, 0]), 0)], 'Nominal System', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


## Plotting
plotSignals([Exp.output_signals], 1)


## Calculate Markov Parameters and Identified system
ERA1 = ERAFromInitialConditionResponse(Exp.output_signals, dynamics.state_dimension, dynamics.input_dimension)




## Define Identified System
SysID = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(ERA1.x0[:, 0], 0)], 'Identified System', ERA1.A, ERA1.B, ERA1.C, ERA1.D)


## Define the Identified Output Signal
S2ID = OutputSignal(DiscreteSignal(3, 'Zero Input', total_time, frequency), SysID, 'Identified Output Signal')



# ## Plotting
plotSignals([[Exp.output_signals[0], S2ID], [subtract2Signals(Exp.output_signals[0], S2ID)]], 2)
plotEigenValues([Sys, SysID], 2)
plotSingularValues([ERA1], ['IdentifiedSystem'], 3)
# plotMarkovParameters2(markov_parameters, markov_parameters_true, 'OKID', 'True', 4)















































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
import numpy.linalg as LA

from ClassesDynamics.ClassSlowManifoldDecoupledSystemDynamics import SlowManifoldDecoupledSystemDynamics
from SystemIDAlgorithms.DepartureDynamics import departureDynamicsFromInitialConditionResponse
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, add2Signals, subtract2Signals
from Plotting.PlotSignals import plotSignals
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassERA import TVERAFromInitialConditionResponse
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck


# Parameters for Dynamics
def mu(t):
    return  -0.5 + 1.5*np.sin(2*np.pi*2*t)
def l(t):
    return  -0.2 + 0.5*np.cos(2*np.pi*3*t)


# Import Dynamics
dynamics = SlowManifoldDecoupledSystemDynamics(mu, l)


# Parameters for identification
total_time = 10
frequency = 50
number_steps = int(total_time * frequency) + 1
assumed_order = 3
p, q = getOptimizedHankelMatrixSize(assumed_order, dynamics.output_dimension, dynamics.input_dimension)
deadbeat_order = 4


# Number Experiments
number_free_decay_experiments = q * dynamics.input_dimension


# Create System
initial_states = [(np.array([0, 0, 0]), 0)]
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)
nominal_system_d = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System Discrete', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


# tspan
tspan = np.linspace(0, total_time, number_steps)


# Nominal Input Signal
nominal_input_signal = ContinuousSignal(dynamics.input_dimension, 'Nominal Input Signal')


# Nominal Output Signal
nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal', tspan=tspan)


# Update dynamics with nominal trajectory
r = 2
total_time_test = total_time - r / frequency
number_steps_test = number_steps - r
tspan_test = tspan[:-r]
dynamics = SlowManifoldDecoupledSystemDynamics(mu, l, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, 'Nominal Trajectory', total_time, frequency, signal_shape='External', data=nominal_output_signal.state), nominal_u=DiscreteSignal(dynamics.input_dimension, 'Nominal Input Signal', total_time, frequency), dt=1/frequency)
nominal_output_signal_test = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal Test', tspan=tspan_test)


plotSignals([[nominal_output_signal]], 1)


# Deviations dx0
deviations_dx0 = []
for i in range(number_free_decay_experiments):
    x0 = 0.1 * np.random.randn()
    y0 = 0.1 * np.random.randn()
    deviations_dx0.append(np.array([x0, y0, x0**2]))


# Full experiment
full_deviation_dx0 = np.array([0.5, 0.75, 0.25])
#full_deviation_dx0 = 0.1 * np.random.randn(dynamics.state_dimension)
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


# Plotting
plotSignals([[true_output_signal, identified_output_signal, linearized_output_signal], [subtract2Signals(true_output_signal, identified_output_signal), subtract2Signals(true_output_signal, linearized_output_signal)]], 1, percentage=0.9)


# True Corrected System
corrected_system = correctSystemForEigenvaluesCheck(nominal_system_d, number_steps_test - r, r)

# Identified Corrected System
corrected_system_id = correctSystemForEigenvaluesCheck(identified_system, number_steps_test - r, r)

# Linearized Corrected System
corrected_system_linearized = correctSystemForEigenvaluesCheck(linearized_system, number_steps_test - r, r)


plotHistoryEigenValues2Systems([corrected_system_linearized, corrected_system_id], number_steps_test - r, 2)






########################################################################################################################
#####################################################  PLOTTING  #######################################################
########################################################################################################################


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


plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
rc('text', usetex=True)


# Phase plots
fig = plt.figure(num=1, figsize=[4, 4])
plt.plot(true_output_signal.data[0, :], true_output_signal.data[1, :], color=colors[5])
plt.plot(identified_output_signal.data[0, :], identified_output_signal.data[1, :], color=colors[7], linestyle='-.')
plt.plot(S2ID.data[0, :], S2ID.data[1, :], linestyle=':', color=colors[0])
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['True', 'Time-varying Koopman', 'Time-invariant Koopman'], loc='lower right')
plt.show()


# Error plots
fig = plt.figure(num=2, figsize=[4, 2.5])
ax = fig.add_subplot(2, 1, 1)
ax.plot(tspan_test[:-1], true_output_signal.data[0, :-1] - identified_output_signal.data[0, :-1], color=colors[7])
plt.legend(['Time-varying Koopman'], loc='upper right')
plt.ylabel('Error')
ax = fig.add_subplot(2, 1, 2)
ax.plot(tspan_test[:-1], true_output_signal.data[0, :-1] -S2ID.data[0, :-3], color=colors[0])
plt.legend(['Time-invariant Koopman'], loc='upper right')
plt.xlabel('Time [sec]')
plt.ylabel('Error')
plt.show()

fig = plt.figure(num=3, figsize=[4, 2.5])
ax = fig.add_subplot(2, 1, 1)
ax.plot(tspan_test[:-1], true_output_signal.data[1, :-1] - identified_output_signal.data[1, :-1], color=colors[7])
plt.legend(['Time-varying Koopman'], loc='upper left')
plt.ylabel('Error')
ax = fig.add_subplot(2, 1, 2)
ax.plot(tspan_test[:-1], true_output_signal.data[1, :-1] -S2ID.data[1, :-3], color=colors[0])
plt.legend(['Time-invariant Koopman'], loc='lower right')
plt.xlabel('Time [sec]')
plt.ylabel('Error')
plt.show()


# Eigenvalues
dt = identified_system.dt
eig1 = np.zeros([number_steps - r-2, identified_system.state_dimension])
eig2 = np.zeros([number_steps - r-2, identified_system.state_dimension])
eig3 = np.zeros([number_steps - r-2, identified_system.state_dimension])

for i in range(number_steps - r-2):
    eig1[i, :] = np.real(LA.eig(corrected_system_id.A(i * dt))[0])
    eig2[i, :] = np.real(LA.eig(corrected_system_linearized.A(i * dt))[0])
    eig3[i, :] = np.real(LA.eig(SysID.A(i * dt))[0])

eig1.sort(axis=1)
eig2.sort(axis=1)
eig3.sort(axis=1)

fig = plt.figure(num=4, figsize=[4, 2.5])
plt.plot(tspan_test[:-r-1], np.transpose(eig2[:-1, 0]), color=colors[5])
plt.plot(tspan_test[:-r-1], np.transpose(eig1[:-1, 0]), color=colors[7], linestyle='-.')
plt.plot(tspan_test[:-r-1], np.transpose(eig3[:-1, 0]), color=colors[0], linestyle=':')
plt.plot()
plt.xlabel('Time [sec]')
plt.ylabel('First eigenvalue')
plt.legend(['True', 'Time-varying Koopman', 'Time-invariant Koopman'], loc='upper right')
plt.show()

fig = plt.figure(num=5, figsize=[4, 2])
plt.plot(tspan_test[:-r-1], np.transpose(eig2[:-1, 0]) - np.transpose(eig1[:-1, 0]), color=colors[7])
plt.xlabel('Time [sec]')
plt.ylabel('Error in magnitude')
plt.show()

fig = plt.figure(num=6, figsize=[4, 2.5])
plt.plot(tspan_test[:-r-1], np.transpose(eig2[:-1, 1]), color=colors[5])
plt.plot(tspan_test[:-r-1], np.transpose(eig1[:-1, 1]), color=colors[7], linestyle='-.')
plt.plot(tspan_test[:-r-1], np.transpose(eig3[:-1, 1]), color=colors[0], linestyle=':')
plt.plot()
plt.xlabel('Time [sec]')
plt.ylabel('Second eigenvalue')
plt.legend(['True', 'Time-varying Koopman', 'Time-invariant Koopman'], loc='upper right')
plt.show()

fig = plt.figure(num=7, figsize=[4, 2])
plt.plot(tspan_test[:-r-1], np.transpose(eig2[:-1, 1]) - np.transpose(eig1[:-1, 1]), color=colors[7])
plt.xlabel('Time [sec]')
plt.ylabel('Error in magnitude')
plt.show()

fig = plt.figure(num=8, figsize=[4, 2.5])
plt.plot(tspan_test[:-r-1], np.transpose(eig2[:-1, 2]), color=colors[5])
plt.plot(tspan_test[:-r-1], np.transpose(eig1[:-1, 2]), color=colors[7], linestyle='-.')
plt.plot(tspan_test[:-r-1], np.transpose(eig3[:-1, 2]), color=colors[0], linestyle=':')
plt.plot()
plt.xlabel('Time [sec]')
plt.ylabel('Third eigenvalue')
plt.legend(['True', 'Time-varying Koopman', 'Time-invariant Koopman'], loc='upper right')
plt.show()

fig = plt.figure(num=9, figsize=[4, 2])
plt.plot(tspan_test[:-r-1], np.transpose(eig2[:-1, 2]) - np.transpose(eig1[:-1, 2]), color=colors[7])
plt.xlabel('Time [sec]')
plt.ylabel('Error in magnitude')
plt.show()

