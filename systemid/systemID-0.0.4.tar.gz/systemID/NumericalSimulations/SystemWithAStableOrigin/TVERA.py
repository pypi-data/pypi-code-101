"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np


from ClassesDynamics.ClassSystemWithAStableOriginDynamics import SystemWithAStableOriginDynamics
from ClassesDynamics.ClassPointMassInRotatingTubeDynamics import PointMassInRotatingTubeDynamics
from ClassesGeneral.ClassSystem import DiscreteLinearSystem
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from ClassesGeneral.ClassSignal import DiscreteSignal, OutputSignal, subtract2Signals, addSignals
from ClassesGeneral.ClassExperiments import Experiments
from Plotting.PlotSignals import plotSignals
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassMarkovParameters import TVOKIDWithObserver
from ClassesSystemID.ClassERA import TVERA, TVERADC
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck
from SystemIDAlgorithms.GetTimeVaryingObserverGainMatrix import getTimeVaryingObserverGainMatrix



# Dynamics
dt = 0.1
mass = 1
spring_constant = 10
damping_coefficient = 0.1
def theta_dot(t):
    return 3 * np.sin(t / 2)
# dynamics = MassSpringDamperDynamics(dt, mass, spring_constant, damping_coefficient, ['mass'], ['position', 'velocity'])
dynamics = PointMassInRotatingTubeDynamics(dt, mass, spring_constant, theta_dot)


# Initial Condition
x0 = np.random.randn(dynamics.state_dimension)*0.1
# x0 = np.zeros(dynamics.state_dimension)


# Frequency and total time
frequency = 10
total_time = 50
number_steps = total_time * frequency + 1
tspan = np.linspace(0, total_time, number_steps)

# System
nominal_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(x0, 0)], 'Nominal System', dynamics.A, dynamics.B, dynamics.C, dynamics.D)


# Parameters for identification
assumed_order = 3
p, q = getOptimizedHankelMatrixSize(assumed_order, dynamics.output_dimension, dynamics.input_dimension)
p=4
q=10
deadbeat_order = 5


# Free Decay Experiments
number_batches = 5
number_free_decay_experiments = q * dynamics.input_dimension * 2
number_free_decay_experiments_total = number_free_decay_experiments * number_batches
free_decay_systems = []
free_decay_input_signals = []
free_decay_experiments_batch = []
for l in range(number_batches):
    free_decay_systems_batch = []
    free_decay_input_signals_batch = []
    for i in range(number_free_decay_experiments):
        initial_state = np.random.randn(dynamics.state_dimension) * 0.1
        free_decay_systems.append(DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_state, 0)], 'Free Decay Experiments System ' + str(i), dynamics.A, dynamics.B, dynamics.C, dynamics.D))
        free_decay_systems_batch.append(DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(initial_state, 0)], 'Free Decay Experiments System ' + str(i), dynamics.A, dynamics.B, dynamics.C, dynamics.D))
        free_decay_input_signals.append(DiscreteSignal(dynamics.input_dimension, total_time, frequency))
        free_decay_input_signals_batch.append(DiscreteSignal(dynamics.input_dimension, total_time, frequency))
    free_decay_experiments_batch.append(Experiments(free_decay_systems_batch, free_decay_input_signals_batch))
free_decay_experiments = Experiments(free_decay_systems, free_decay_input_signals)


## Add noise
for i in range(number_free_decay_experiments_total):
    noise = DiscreteSignal(dynamics.output_dimension, total_time, frequency, signal_shape='White Noise', covariance=0.02 * np.eye(dynamics.output_dimension))
    free_decay_experiments.output_signals[i] = addSignals([free_decay_experiments.output_signals[i], noise])
    free_decay_experiments_batch[int(np.floor(i / number_free_decay_experiments))].output_signals[i % number_free_decay_experiments] = addSignals([free_decay_experiments_batch[int(np.floor(i / number_free_decay_experiments))].output_signals[i % number_free_decay_experiments], noise])


# Forced Experiments
number_forced_experiments = round(dynamics.input_dimension + max(p + 1 + q - 1, deadbeat_order) * (dynamics.input_dimension + dynamics.output_dimension)) + 10
forced_response_systems = []
forced_response_input_signals = []
for i in range(number_forced_experiments):
    forced_response_systems.append(DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.zeros(dynamics.state_dimension), 0)], 'Forced Experiments System ' + str(i), dynamics.A, dynamics.B, dynamics.C, dynamics.D))
    forced_response_input_signals.append(DiscreteSignal(dynamics.input_dimension, total_time, frequency, signal_shape='White Noise'))
forced_experiments = Experiments(forced_response_systems, forced_response_input_signals)


## Add noise
for i in range(number_forced_experiments):
    noise = DiscreteSignal(dynamics.output_dimension, total_time, frequency, signal_shape='White Noise', covariance=0.02 * np.eye(dynamics.output_dimension))
    forced_experiments.output_signals[i] = addSignals([forced_experiments.output_signals[i], noise])


# Full Experiment
full_system = [nominal_system]
full_input_signal = [DiscreteSignal(dynamics.input_dimension, total_time, frequency, signal_shape='White Noise', covariance=0.01 * np.eye(dynamics.input_dimension))]
full_experiment = Experiments(full_system, full_input_signal)


# Plotting Experiments
plotSignals([free_decay_experiments.output_signals, forced_experiments.output_signals, full_experiment.output_signals], 1)


# TVOKID
okid = TVOKIDWithObserver(forced_experiments, observer_order=deadbeat_order)


# TVERA
tvera = TVERA(free_decay_experiments, okid.hki, okid.D, full_experiment, dynamics.state_dimension, p, q, apply_transformation=True)
tveradc = TVERADC(free_decay_experiments_batch, okid.hki, okid.D, full_experiment, dynamics.state_dimension, p=4, q=10, xi=5, zeta=5, tau=10, apply_transformation=True)


# Identified System
system_id_tvera = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(tvera.x0, 0)], 'System ID', tvera.A, tvera.B, tvera.C, tvera.D)
system_id_tveradc = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(tveradc.x0, 0)], 'System ID', tveradc.A, tveradc.B, tveradc.C, tveradc.D)
# G = getTimeVaryingObserverGainMatrix(tvera.A, tvera.C, okid.hkio, p + 2, 1 / frequency)
# system_id_observer = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.zeros(dynamics.state_dimension), 0)], 'System ID', tvera.A, tvera.B, tvera.C, tvera.D, observer_gain=G)
# system_id_no_observer = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.zeros(dynamics.state_dimension), 0)], 'System ID', tvera.A, tvera.B, tvera.C, tvera.D)



# Test Signal
def u_test(t):
    return np.sin(2 * t) / 2
test_signal = DiscreteSignal(dynamics.input_dimension, total_time, frequency, signal_shape='External', data=u_test(tspan))


# True Output
output_signal = OutputSignal(test_signal, nominal_system)


# Identified Output
output_signal_tvera = OutputSignal(test_signal, system_id_tvera)
output_signal_tveradc = OutputSignal(test_signal, system_id_tveradc)
# output_signal_id_no_observer = OutputSignal(test_signal, system_id_no_observer)
# output_signal_id_observer = OutputSignal(test_signal, system_id_observer, observer=True, reference_output_signal=output_signal_id)


# Plotting Output Signals
# plotSignals([[output_signal, output_signal_tveradc], [subtract2Signals(output_signal, output_signal_tveradc)]], 2, percentage=0.9)


# True Corrected System
# corrected_system = correctSystemForEigenvaluesCheck(nominal_system, full_input_signal[0].number_steps - q, p)


# Identified Corrected System
# corrected_system_tvera = correctSystemForEigenvaluesCheck(system_id_tvera, full_input_signal[0].number_steps - q, p)
# corrected_system_tveradc = correctSystemForEigenvaluesCheck(system_id_tveradc, full_input_signal[0].number_steps - q, p)


# Plot Eigenvalues
# plotHistoryEigenValues2Systems([corrected_system, corrected_system_tvera], full_input_signal[0].number_steps - q, 3)
# plotHistoryEigenValues2Systems([corrected_system, corrected_system_tveradc], full_input_signal[0].number_steps - q, 3)











## Plotting

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


plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
rc('text', usetex=True)

end = 10
tspan_test = np.linspace(0, total_time - end, number_steps - end * frequency)

fig = plt.figure(1, figsize=(12, 6))
ax = plt.subplot(2, 2, 1)
ax.plot(tspan_test, output_signal.data[0, :-end * frequency], color=colors[0], label='True')
ax.plot(tspan_test, output_signal_tvera.data[0, :-end * frequency], color=colors[5], label='TVERA')
ax.plot(tspan_test, output_signal_tveradc.data[0, :-end * frequency], color=colors[7], label='TVERA/DC')
plt.xlabel(r'Time')
plt.ylabel(r'$y_1$')
ax.legend(loc='lower left')

ax = plt.subplot(2, 2, 2)
ax.plot(tspan_test, output_signal.data[1, :-end * frequency], color=colors[0], label='True')
ax.plot(tspan_test, output_signal_tvera.data[1, :-end * frequency], color=colors[5], label='TVERA')
ax.plot(tspan_test, output_signal_tveradc.data[1, :-end * frequency], color=colors[7], label='TVERA/DC')
plt.xlabel(r'Time')
plt.ylabel(r'$y_2$')
ax.legend(loc='lower left')

ax = plt.subplot(2, 2, 3)
ax.semilogy(tspan_test, np.abs(output_signal.data[0, :-end * frequency] - output_signal_tvera.data[0, :-end * frequency]), color=colors[5], label='TVERA')
ax.semilogy(tspan_test, np.abs(output_signal.data[0, :-end * frequency] - output_signal_tveradc.data[0, :-end * frequency]), color=colors[7], label='TVERA/DC')
plt.xlabel(r'Time')
plt.ylabel(r'Error $y_1$')
ax.legend(loc='lower left')

ax = plt.subplot(2, 2, 4)
ax.semilogy(tspan_test, np.abs(output_signal.data[1, :-end * frequency] - output_signal_tvera.data[1, :-end * frequency]), color=colors[5], label='TVERA')
ax.semilogy(tspan_test, np.abs(output_signal.data[1, :-end * frequency] - output_signal_tveradc.data[1, :-end * frequency]), color=colors[7], label='TVERA/DC')
plt.xlabel(r'Time')
plt.ylabel(r'Error $y_2$')
ax.legend(loc='lower left')
plt.tight_layout()
plt.savefig('TVERADC_1.eps', format='eps')
plt.show()


## RMSE
print('RMSE TVERA =', np.sqrt(np.mean(subtract2Signals(output_signal, output_signal_tvera).data[:, :-100] ** 2)))
print('RMSE TVERA\DC =', np.sqrt(np.mean(subtract2Signals(output_signal, output_signal_tveradc).data[:, :-100] ** 2)))
print('Absolute error TVERA =', np.mean(np.abs(subtract2Signals(output_signal, output_signal_tvera).data[:, :-100])))
print('Absolute error TVERADC =', np.mean(np.abs(subtract2Signals(output_signal, output_signal_tveradc).data[:, :-100])))



