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

from ClassesGeneral.ClassSystem import DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, addSignals, subtract2Signals
from ClassesGeneral.ClassExperiments import Experiments
from ClassesSystemID.ClassERA import TVERAFromInitialConditionResponse
from SystemIDAlgorithms.IdentificationInitialCondition import identificationInitialCondition



ate2d_l3_Tw260_Pinf04000_F = pickle.load(open("Data/ate2d_l3_Tw260_Pinf4000_F.pkl", "rb"))
ate2d_l3_Tw260_Pinf08000_F = pickle.load(open("Data/ate2d_l3_Tw260_Pinf8000_F.pkl", "rb"))
ate2d_l3_Tw260_Pinf10000_F = pickle.load(open("Data/ate2d_l3_Tw260_Pinf10000_F.pkl", "rb"))
ate2d_l3_Tw260_Pinf12000_F = pickle.load(open("Data/ate2d_l3_Tw260_Pinf12000_F.pkl", "rb"))
ate2d_l3_Tw260_Pinf15000_F = pickle.load(open("Data/ate2d_l3_Tw260_Pinf15000_F.pkl", "rb"))
ate2d_l3_Tw260_Pinf16000_F = pickle.load(open("Data/ate2d_l3_Tw260_Pinf16000_F.pkl", "rb"))
ate2d_l3_Tw260_Pinf20000_F = pickle.load(open("Data/ate2d_l3_Tw260_Pinf20000_F.pkl", "rb"))
ate2d_l3_Tw260_Pinf25000_F = pickle.load(open("Data/ate2d_l3_Tw260_Pinf25000_F.pkl", "rb"))
ate2d_l3_Tw260_Pinf30000_F = pickle.load(open("Data/ate2d_l3_Tw260_Pinf30000_F.pkl", "rb"))
ate2d_l3_Tw260_Pinf35000_F = pickle.load(open("Data/ate2d_l3_Tw260_Pinf35000_F.pkl", "rb"))
ate2d_l3_Tw260_Pinf40000_F = pickle.load(open("Data/ate2d_l3_Tw260_Pinf40000_F.pkl", "rb"))
ate2d_l3_Tw265_Pinf10000_F = pickle.load(open("Data/ate2d_l3_Tw265_Pinf10000_F.pkl", "rb"))
ate2d_l3_Tw265_Pinf15000_F = pickle.load(open("Data/ate2d_l3_Tw265_Pinf15000_F.pkl", "rb"))
ate2d_l3_Tw265_Pinf20000_F = pickle.load(open("Data/ate2d_l3_Tw265_Pinf20000_F.pkl", "rb"))
ate2d_l3_Tw265_Pinf25000_F = pickle.load(open("Data/ate2d_l3_Tw265_Pinf25000_F.pkl", "rb"))
ate2d_l3_Tw265_Pinf30000_F = pickle.load(open("Data/ate2d_l3_Tw265_Pinf30000_F.pkl", "rb"))
ate2d_l3_Tw265_Pinf35000_F = pickle.load(open("Data/ate2d_l3_Tw265_Pinf35000_F.pkl", "rb"))
ate2d_l3_Tw265_Pinf40000_F = pickle.load(open("Data/ate2d_l3_Tw265_Pinf40000_F.pkl", "rb"))
ate2d_l3_Tw270_Pinf04000_F = pickle.load(open("Data/ate2d_l3_Tw270_Pinf4000_F.pkl", "rb"))
ate2d_l3_Tw270_Pinf08000_F = pickle.load(open("Data/ate2d_l3_Tw270_Pinf8000_F.pkl", "rb"))
ate2d_l3_Tw270_Pinf12000_F = pickle.load(open("Data/ate2d_l3_Tw270_Pinf12000_F.pkl", "rb"))
ate2d_l3_Tw270_Pinf16000_F = pickle.load(open("Data/ate2d_l3_Tw270_Pinf16000_F.pkl", "rb"))
ate2d_l3_Tw270_Pinf20000_F = pickle.load(open("Data/ate2d_l3_Tw270_Pinf20000_F.pkl", "rb"))
ate2d_l3_Tw270_Pinf25000_F = pickle.load(open("Data/ate2d_l3_Tw270_Pinf25000_F.pkl", "rb"))
ate2d_l3_Tw270_Pinf30000_F = pickle.load(open("Data/ate2d_l3_Tw270_Pinf30000_F.pkl", "rb"))
ate2d_l3_Tw270_Pinf35000_F = pickle.load(open("Data/ate2d_l3_Tw270_Pinf35000_F.pkl", "rb"))
ate2d_l3_Tw270_Pinf40000_F = pickle.load(open("Data/ate2d_l3_Tw270_Pinf40000_F.pkl", "rb"))
ate2d_l3_Tw280_Pinf04000_F = pickle.load(open("Data/ate2d_l3_Tw280_Pinf4000_F.pkl", "rb"))
ate2d_l3_Tw280_Pinf08000_F = pickle.load(open("Data/ate2d_l3_Tw280_Pinf8000_F.pkl", "rb"))
ate2d_l3_Tw280_Pinf12000_F = pickle.load(open("Data/ate2d_l3_Tw280_Pinf12000_F.pkl", "rb"))
ate2d_l3_Tw280_Pinf16000_F = pickle.load(open("Data/ate2d_l3_Tw280_Pinf16000_F.pkl", "rb"))
ate2d_l3_Tw280_Pinf20000_F = pickle.load(open("Data/ate2d_l3_Tw280_Pinf20000_F.pkl", "rb"))
ate2d_l3_Tw290_Pinf04000_F = pickle.load(open("Data/ate2d_l3_Tw290_Pinf4000_F.pkl", "rb"))
ate2d_l3_Tw290_Pinf08000_F = pickle.load(open("Data/ate2d_l3_Tw290_Pinf8000_F.pkl", "rb"))
ate2d_l3_Tw290_Pinf12000_F = pickle.load(open("Data/ate2d_l3_Tw290_Pinf12000_F.pkl", "rb"))
ate2d_l3_Tw290_Pinf16000_F = pickle.load(open("Data/ate2d_l3_Tw290_Pinf16000_F.pkl", "rb"))
ate2d_l3_Tw290_Pinf20000_F = pickle.load(open("Data/ate2d_l3_Tw290_Pinf20000_F.pkl", "rb"))
ate2d_l3_Tw300_Pinf04000_F = pickle.load(open("Data/ate2d_l3_Tw300_Pinf4000_F.pkl", "rb"))
ate2d_l3_Tw300_Pinf08000_F = pickle.load(open("Data/ate2d_l3_Tw300_Pinf8000_F.pkl", "rb"))
ate2d_l3_Tw300_Pinf12000_F = pickle.load(open("Data/ate2d_l3_Tw300_Pinf12000_F.pkl", "rb"))
ate2d_l3_Tw300_Pinf16000_F = pickle.load(open("Data/ate2d_l3_Tw300_Pinf16000_F.pkl", "rb"))
ate2d_l3_Tw300_Pinf20000_F = pickle.load(open("Data/ate2d_l3_Tw300_Pinf20000_F.pkl", "rb"))
ate2d_l3_Tw310_Pinf04000_F = pickle.load(open("Data/ate2d_l3_Tw310_Pinf4000_F.pkl", "rb"))
ate2d_l3_Tw310_Pinf08000_F = pickle.load(open("Data/ate2d_l3_Tw310_Pinf8000_F.pkl", "rb"))
ate2d_l3_Tw310_Pinf12000_F = pickle.load(open("Data/ate2d_l3_Tw310_Pinf12000_F.pkl", "rb"))
ate2d_l3_Tw310_Pinf16000_F = pickle.load(open("Data/ate2d_l3_Tw310_Pinf16000_F.pkl", "rb"))
ate2d_l3_Tw310_Pinf20000_F = pickle.load(open("Data/ate2d_l3_Tw310_Pinf20000_F.pkl", "rb"))
ate2d_l3_Tw320_Pinf04000_F = pickle.load(open("Data/ate2d_l3_Tw320_Pinf4000_F.pkl", "rb"))
ate2d_l3_Tw320_Pinf08000_F = pickle.load(open("Data/ate2d_l3_Tw320_Pinf8000_F.pkl", "rb"))
ate2d_l3_Tw320_Pinf12000_F = pickle.load(open("Data/ate2d_l3_Tw320_Pinf12000_F.pkl", "rb"))
ate2d_l3_Tw320_Pinf16000_F = pickle.load(open("Data/ate2d_l3_Tw320_Pinf16000_F.pkl", "rb"))
ate2d_l3_Tw320_Pinf20000_F = pickle.load(open("Data/ate2d_l3_Tw320_Pinf20000_F.pkl", "rb"))



## Parameters
print('> Parameters')
output_dimension = 2 * 98
total_time = 0.159
frequency = 1000
dt = 1 / frequency
number_steps = round(frequency * total_time + 1)
tspan = np.linspace(0, total_time, number_steps)
p = 6
q = 6
total_time_test = total_time - (p + 1) * dt
number_steps_test = number_steps - (p + 1)
tspan_test = np.linspace(0, total_time_test, number_steps_test)
total_time_zoom = 0.02
number_steps_zoom = round(frequency * total_time_zoom + 1)
tspan_zoom = np.linspace(0, total_time_zoom, number_steps_zoom)
total_time_zoom2 = 0.03
number_steps_zoom2 = round(frequency * total_time_zoom + 1)
tspan_zoom2 = np.linspace(total_time_test - total_time_zoom2, total_time_test, number_steps_zoom2)
state_dimension = 2
augmented_dimension = 4
input_dimension = 1


## Fake
# Fake system
def A(tk):
    return np.zeros([augmented_dimension, augmented_dimension])
def B(tk):
    return np.zeros([augmented_dimension, input_dimension])
def C(tk):
    return np.zeros([output_dimension, augmented_dimension])
def D(tk):
    return np.zeros([output_dimension, input_dimension])
system = DiscreteLinearSystem(frequency, augmented_dimension, input_dimension, output_dimension, [(np.zeros(augmented_dimension), 0)], 'Fake System', A, B, C, D)
input_signal = DiscreteSignal(input_dimension, total_time, frequency)


## Data Pinf = 20000
print('> Organize Free decay Experiments')
cases_considered = [ate2d_l3_Tw260_Pinf20000_F, ate2d_l3_Tw265_Pinf20000_F, ate2d_l3_Tw270_Pinf20000_F, ate2d_l3_Tw280_Pinf20000_F,
                    ate2d_l3_Tw290_Pinf20000_F, ate2d_l3_Tw300_Pinf20000_F, ate2d_l3_Tw310_Pinf20000_F, ate2d_l3_Tw320_Pinf20000_F]
number_free_decay_experiments = len(cases_considered)
free_decay_experiments = Experiments([system] * number_free_decay_experiments, [input_signal] * number_free_decay_experiments)
free_decay_output_signals = []
free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[0]['data'][:, [2, 5], 0:number_steps].reshape(output_dimension, number_steps)))
free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[1]['data'][:, [2, 5], 0:number_steps].reshape(output_dimension, number_steps)))
free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[2]['data'][:, [2, 5], 0:number_steps * 2 - 1:2].reshape(output_dimension, number_steps)))
free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[3]['data'][:, [2, 5], 0:number_steps * 2 - 1:2].reshape(output_dimension, number_steps)))
free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[4]['data'][:, [2, 5], 0:number_steps * 2 - 1:2].reshape(output_dimension, number_steps)))
free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[5]['data'][:, [2, 5], 0:number_steps * 2 - 1:2].reshape(output_dimension, number_steps)))
free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[6]['data'][:, [2, 5], 0:number_steps * 2 - 1:2].reshape(output_dimension, number_steps)))
free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[7]['data'][:, [2, 5], 0:number_steps * 2 - 1:2].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[0]['data'][:, [2, 5], number_steps:number_steps * 2].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[1]['data'][:, [2, 5], number_steps:number_steps * 2].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[2]['data'][:, [2, 5], number_steps * 2:number_steps*4 - 1:2].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[3]['data'][:, [2, 5], number_steps * 2:number_steps*4 - 1:2].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[4]['data'][:, [2, 5], number_steps * 2:number_steps*4 - 1:2].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[5]['data'][:, [2, 5], number_steps * 2:number_steps*4 - 1:2].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[6]['data'][:, [2, 5], number_steps * 2:number_steps*4 - 1:2].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[7]['data'][:, [2, 5], number_steps * 2:number_steps*4 - 1:2].reshape(output_dimension, number_steps)))
for i in range(number_free_decay_experiments):
    free_decay_experiments.output_signals[i] = free_decay_output_signals[i]


## TVERAIC
print('> TVERAIC')
tveraic = TVERAFromInitialConditionResponse(free_decay_experiments, augmented_dimension, p=p)


## Identify Initial Condition
print('> Identify Initial Condition')
X0_id_tvera = tveraic.X0


## Identified System TVERA
print('> Identified System TVERA')
identified_systems_tveraic = []
for i in range(number_free_decay_experiments):
    identified_systems_tveraic.append(DiscreteLinearSystem(frequency, augmented_dimension, input_dimension, output_dimension, [(X0_id_tvera[:, i], 0)], 'System ID', tveraic.A, tveraic.B, tveraic.C, tveraic.D))


## Identified Output Signals (Full Operator propagation)
print('> Identified Output Signals (Full Operator propagation)')
identified_output_signals_tveraic = []
for i in range(number_free_decay_experiments):
    identified_output_signal_augmented_tvera = OutputSignal(input_signal, identified_systems_tveraic[i])
    identified_output_signals_tveraic.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=identified_output_signal_augmented_tvera.data[0:output_dimension, :]))



## Plotting
fig = plt.figure(1, figsize=(24, 16))
for i in range(number_free_decay_experiments):
    ax = plt.subplot(number_free_decay_experiments, 4, i * 4 + 1)
    ax.plot(tspan_test, free_decay_output_signals[i].data[0, 0:number_steps_test], color=colors[0], label='True')
    ax.plot(tspan_test, identified_output_signals_tveraic[i].data[0, 0:number_steps_test], color=colors[5], label='ID')
    plt.xlabel(r'Time [s]')
    plt.ylabel(r'disp')
    ax.legend(loc='upper left')
    plt.title('Exp ' + str(i + 1))
    ax = plt.subplot(number_free_decay_experiments, 4, i * 4 + 2)
    ax.plot(tspan_test, free_decay_output_signals[i].data[0, 0:number_steps_test] - identified_output_signals_tveraic[i].data[0, 0:number_steps_test], color=colors[7], label='Error')
    plt.xlabel(r'Time [s]')
    plt.ylabel(r'Error in disp')
    ax.legend(loc='upper left')
    ax = plt.subplot(number_free_decay_experiments, 4, i * 4 + 3)
    ax.plot(tspan_test, free_decay_output_signals[i].data[1, 0:number_steps_test], color=colors[0], label='True')
    ax.plot(tspan_test, identified_output_signals_tveraic[i].data[1, 0:number_steps_test], color=colors[5], label='ID')
    plt.xlabel(r'Time [s]')
    plt.ylabel(r'wtmp')
    ax.legend(loc='upper left')
    ax = plt.subplot(number_free_decay_experiments, 4, i * 4 + 4)
    ax.plot(tspan_test, free_decay_output_signals[i].data[1, 0:number_steps_test] - identified_output_signals_tveraic[i].data[1, 0:number_steps_test], color=colors[7], label='Error')
    plt.xlabel(r'Time [s]')
    plt.ylabel(r'Error in wtmp')
    ax.legend(loc='upper left')
plt.tight_layout()
# plt.savefig('limit_cycle.eps', format='eps')
plt.show()



fig = plt.figure(2, figsize=(24, 16))
for i in range(number_free_decay_experiments):
    ax = plt.subplot(number_free_decay_experiments, 4, i * 4 + 1)
    ax.plot(tspan_zoom, free_decay_output_signals[i].data[0, 0:number_steps_zoom], color=colors[0], label='True')
    ax.plot(tspan_zoom, identified_output_signals_tveraic[i].data[0, 0:number_steps_zoom], color=colors[5], label='ID')
    plt.xlabel(r'Time [s]')
    plt.ylabel(r'disp')
    ax.legend(loc='upper left')
    plt.title('Exp ' + str(i + 1))
    ax = plt.subplot(number_free_decay_experiments, 4, i * 4 + 2)
    ax.plot(tspan_zoom, free_decay_output_signals[i].data[0, 0:number_steps_zoom] - identified_output_signals_tveraic[i].data[0, 0:number_steps_zoom], color=colors[7], label='Error')
    plt.xlabel(r'Time [s]')
    plt.ylabel(r'Error in disp')
    ax.legend(loc='upper left')
    ax = plt.subplot(number_free_decay_experiments, 4, i * 4 + 3)
    ax.plot(tspan_zoom, free_decay_output_signals[i].data[1, 0:number_steps_zoom], color=colors[0], label='True')
    ax.plot(tspan_zoom, identified_output_signals_tveraic[i].data[1, 0:number_steps_zoom], color=colors[5], label='ID')
    plt.xlabel(r'Time [s]')
    plt.ylabel(r'wtmp')
    ax.legend(loc='upper left')
    ax = plt.subplot(number_free_decay_experiments, 4, i * 4 + 4)
    ax.plot(tspan_zoom, free_decay_output_signals[i].data[1, 0:number_steps_zoom] - identified_output_signals_tveraic[i].data[1, 0:number_steps_zoom], color=colors[7], label='Error')
    plt.xlabel(r'Time [s]')
    plt.ylabel(r'Error in wtmp')
    ax.legend(loc='upper left')
plt.tight_layout()
# plt.savefig('limit_cycle.eps', format='eps')
plt.show()



fig = plt.figure(3, figsize=(24, 16))
for i in range(number_free_decay_experiments):
    ax = plt.subplot(number_free_decay_experiments, 4, i * 4 + 1)
    ax.plot(tspan_zoom2, free_decay_output_signals[i].data[0, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[0], label='True')
    ax.plot(tspan_zoom2, identified_output_signals_tveraic[i].data[0, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[5], label='ID')
    plt.xlabel(r'Time [s]')
    plt.ylabel(r'disp')
    ax.legend(loc='upper left')
    plt.title('Exp ' + str(i + 1))
    ax = plt.subplot(number_free_decay_experiments, 4, i * 4 + 2)
    ax.plot(tspan_zoom2, free_decay_output_signals[i].data[0, number_steps_test - number_steps_zoom2:number_steps_test] - identified_output_signals_tveraic[i].data[0, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[7], label='Error')
    plt.xlabel(r'Time [s]')
    plt.ylabel(r'Error in disp')
    ax.legend(loc='upper left')
    ax = plt.subplot(number_free_decay_experiments, 4, i * 4 + 3)
    ax.plot(tspan_zoom2, free_decay_output_signals[i].data[1, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[0], label='True')
    ax.plot(tspan_zoom2, identified_output_signals_tveraic[i].data[1, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[5], label='ID')
    plt.xlabel(r'Time [s]')
    plt.ylabel(r'wtmp')
    ax.legend(loc='upper left')
    ax = plt.subplot(number_free_decay_experiments, 4, i * 4 + 4)
    ax.plot(tspan_zoom2, free_decay_output_signals[i].data[1, number_steps_test - number_steps_zoom2:number_steps_test] - identified_output_signals_tveraic[i].data[1, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[7], label='Error')
    plt.xlabel(r'Time [s]')
    plt.ylabel(r'Error in wtmp')
    ax.legend(loc='upper left')
plt.tight_layout()
# plt.savefig('limit_cycle.eps', format='eps')
plt.show()


## Errors
RMSE_disp = 0
RMSE_wtmp = 0
AbsE_disp = 0
AbsE_wtmp = 0
for i in range(number_free_decay_experiments):
    RMSE_disp += np.sqrt(np.mean((free_decay_output_signals[i].data[0, 0:number_steps_test] - identified_output_signals_tveraic[i].data[0, 0:number_steps_test]) ** 2)) / number_free_decay_experiments
    RMSE_wtmp += np.sqrt(np.mean((free_decay_output_signals[i].data[1, 0:number_steps_test] - identified_output_signals_tveraic[i].data[1, 0:number_steps_test]) ** 2)) / number_free_decay_experiments
    AbsE_disp += np.mean((np.abs(free_decay_output_signals[i].data[0, 2:number_steps_test] - identified_output_signals_tveraic[i].data[0, 2:number_steps_test])) / np.abs(free_decay_output_signals[i].data[0, 2:number_steps_test])) * 100 / number_free_decay_experiments
    AbsE_wtmp += np.mean((np.abs(free_decay_output_signals[i].data[1, 2:number_steps_test] - identified_output_signals_tveraic[i].data[1, 2:number_steps_test])) / np.abs(free_decay_output_signals[i].data[1, 2:number_steps_test])) * 100 / number_free_decay_experiments





fig = plt.figure(4, figsize=(12, 8))
ax = plt.subplot(2, 2, 1)
ax.scatter(np.linspace(1, 8, 8), tveraic.Sigma[0], color=colors[4])
ax.set_yscale('log')
plt.xlabel(r'Number of singular values')
plt.ylabel(r'Magnitude of singular values')
plt.title(r't = 0')
ax = plt.subplot(2, 2, 2)
ax.scatter(np.linspace(1, 8, 8), tveraic.Sigma[50], color=colors[4])
ax.set_yscale('log')
plt.xlabel(r'Number of singular values')
plt.ylabel(r'Magnitude of singular values')
plt.title(r't = 50')
ax = plt.subplot(2, 2, 3)
ax.scatter(np.linspace(1, 8, 8), tveraic.Sigma[100], color=colors[4])
ax.set_yscale('log')
plt.xlabel(r'Number of singular values')
plt.ylabel(r'Magnitude of singular values')
plt.title(r't = 100')
ax = plt.subplot(2, 2, 4)
ax.scatter(np.linspace(1, 8, 8), tveraic.Sigma[150], color=colors[4])
ax.set_yscale('log')
plt.xlabel(r'Number of singular values')
plt.ylabel(r'Magnitude of singular values')
plt.title(r't = 150')
plt.tight_layout()
# plt.savefig('limit_cycle.eps', format='eps')
plt.show()










## CASE 4
#
#
#
#
# ## Parameters
# print('> Parameters')
# output_dimension = 2 * 98
# total_time = 0.159
# frequency = 1000
# dt = 1 / frequency
# number_steps = round(frequency * total_time + 1)
# tspan = np.linspace(0, total_time, number_steps)
# p = 6
# q = 6
# total_time_test = total_time - (p + 1) * dt
# number_steps_test = number_steps - (p + 1)
# tspan_test = np.linspace(0, total_time_test, number_steps_test)
# total_time_zoom = 0.02
# number_steps_zoom = round(frequency * total_time_zoom + 1)
# tspan_zoom = np.linspace(0, total_time_zoom, number_steps_zoom)
# total_time_zoom2 = 0.03
# number_steps_zoom2 = round(frequency * total_time_zoom + 1)
# tspan_zoom2 = np.linspace(total_time_test - total_time_zoom2, total_time_test, number_steps_zoom2)
# state_dimension = 2
# augmented_dimension = 4
# input_dimension = 1
#
#
# ## Fake
# # Fake system
# def A(tk):
#     return np.zeros([augmented_dimension, augmented_dimension])
# def B(tk):
#     return np.zeros([augmented_dimension, input_dimension])
# def C(tk):
#     return np.zeros([output_dimension, augmented_dimension])
# def D(tk):
#     return np.zeros([output_dimension, input_dimension])
# system = DiscreteLinearSystem(frequency, augmented_dimension, input_dimension, output_dimension, [(np.zeros(augmented_dimension), 0)], 'Fake System', A, B, C, D)
# input_signal = DiscreteSignal(input_dimension, total_time, frequency)
#
#
# ## Data Pinf = 20000
# print('> Organize Free decay Experiments')
# cases_considered = [ate2d_l3_Tw260_Pinf20000_F, ate2d_l3_Tw265_Pinf20000_F, ate2d_l3_Tw270_Pinf20000_F,
#                     ate2d_l3_Tw290_Pinf20000_F, ate2d_l3_Tw300_Pinf20000_F, ate2d_l3_Tw310_Pinf20000_F, ate2d_l3_Tw320_Pinf20000_F]
# number_free_decay_experiments = len(cases_considered)
# free_decay_experiments = Experiments([system] * number_free_decay_experiments, [input_signal] * number_free_decay_experiments)
# free_decay_output_signals = []
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[0]['data'][:, [2, 5], 0:number_steps].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[1]['data'][:, [2, 5], 0:number_steps].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[2]['data'][:, [2, 5], 0:number_steps * 2 - 1:2].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[3]['data'][:, [2, 5], 0:number_steps * 2 - 1:2].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[4]['data'][:, [2, 5], 0:number_steps * 2 - 1:2].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[5]['data'][:, [2, 5], 0:number_steps * 2 - 1:2].reshape(output_dimension, number_steps)))
# free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[6]['data'][:, [2, 5], 0:number_steps * 2 - 1:2].reshape(output_dimension, number_steps)))
# # free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[7]['data'][:, [2, 5], 0:number_steps * 2 - 1:2].reshape(output_dimension, number_steps)))
# # free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[0]['data'][:, [2, 5], number_steps:number_steps * 2].reshape(output_dimension, number_steps)))
# # free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[1]['data'][:, [2, 5], number_steps:number_steps * 2].reshape(output_dimension, number_steps)))
# # free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[2]['data'][:, [2, 5], number_steps * 2:number_steps*4 - 1:2].reshape(output_dimension, number_steps)))
# # free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[3]['data'][:, [2, 5], number_steps * 2:number_steps*4 - 1:2].reshape(output_dimension, number_steps)))
# # free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[4]['data'][:, [2, 5], number_steps * 2:number_steps*4 - 1:2].reshape(output_dimension, number_steps)))
# # free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[5]['data'][:, [2, 5], number_steps * 2:number_steps*4 - 1:2].reshape(output_dimension, number_steps)))
# # free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[6]['data'][:, [2, 5], number_steps * 2:number_steps*4 - 1:2].reshape(output_dimension, number_steps)))
# # free_decay_output_signals.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=cases_considered[7]['data'][:, [2, 5], number_steps * 2:number_steps*4 - 1:2].reshape(output_dimension, number_steps)))
# for i in range(number_free_decay_experiments):
#     free_decay_experiments.output_signals[i] = free_decay_output_signals[i]
#
#
# ## TVERAIC
# print('> TVERAIC')
# tveraic = TVERAFromInitialConditionResponse(free_decay_experiments, augmented_dimension, p=p)
#
#
# ## Identify Initial Condition
# print('> Identify Initial Condition')
# X0_id_tvera = tveraic.X0
# free_decay_output_signal_testing = DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=ate2d_l3_Tw280_Pinf20000_F['data'][:, [2, 5], 0:number_steps * 2 - 1:2].reshape(output_dimension, number_steps))
# x0_id_testing = identificationInitialCondition(input_signal, free_decay_output_signal_testing, tveraic.A, tveraic.B, tveraic.C, tveraic.D, 0, p)
#
#
#
# ## Identified System TVERA
# print('> Identified System TVERA')
# identified_systems_tveraic = []
# for i in range(number_free_decay_experiments):
#     identified_systems_tveraic.append(DiscreteLinearSystem(frequency, augmented_dimension, input_dimension, output_dimension, [(X0_id_tvera[:, i], 0)], 'System ID', tveraic.A, tveraic.B, tveraic.C, tveraic.D))
# identified_systems_tveraic.append(DiscreteLinearSystem(frequency, augmented_dimension, input_dimension, output_dimension, [(x0_id_testing, 0)], 'System ID', tveraic.A, tveraic.B, tveraic.C, tveraic.D))
#
#
# ## Identified Output Signals (Full Operator propagation)
# print('> Identified Output Signals (Full Operator propagation)')
# identified_output_signals_tveraic = []
# for i in range(number_free_decay_experiments):
#     identified_output_signal_augmented_tvera = OutputSignal(input_signal, identified_systems_tveraic[i])
#     identified_output_signals_tveraic.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=identified_output_signal_augmented_tvera.data[0:output_dimension, :]))
# identified_output_signal_augmented_testing = OutputSignal(input_signal, identified_systems_tveraic[-1])
# identified_output_signals_tveraic.append(DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=identified_output_signal_augmented_testing.data[0:output_dimension, :]))
#
#
#
# ## Plotting
# fig = plt.figure(1, figsize=(24, 16))
# for i in range(number_free_decay_experiments):
#     ax = plt.subplot(number_free_decay_experiments + 1, 4, i * 4 + 1)
#     ax.plot(tspan_test, free_decay_output_signals[i].data[0, 0:number_steps_test], color=colors[0], label='True')
#     ax.plot(tspan_test, identified_output_signals_tveraic[i].data[0, 0:number_steps_test], color=colors[5], label='ID')
#     plt.xlabel(r'Time [s]')
#     plt.ylabel(r'disp')
#     ax.legend(loc='upper left')
#     plt.title('Exp ' + str(i + 1))
#     ax = plt.subplot(number_free_decay_experiments + 1, 4, i * 4 + 2)
#     ax.plot(tspan_test, free_decay_output_signals[i].data[0, 0:number_steps_test] - identified_output_signals_tveraic[i].data[0, 0:number_steps_test], color=colors[7], label='Error')
#     plt.xlabel(r'Time [s]')
#     plt.ylabel(r'Error in disp')
#     ax.legend(loc='upper left')
#     ax = plt.subplot(number_free_decay_experiments + 1, 4, i * 4 + 3)
#     ax.plot(tspan_test, free_decay_output_signals[i].data[1, 0:number_steps_test], color=colors[0], label='True')
#     ax.plot(tspan_test, identified_output_signals_tveraic[i].data[1, 0:number_steps_test], color=colors[5], label='ID')
#     plt.xlabel(r'Time [s]')
#     plt.ylabel(r'wtmp')
#     ax.legend(loc='upper left')
#     ax = plt.subplot(number_free_decay_experiments + 1, 4, i * 4 + 4)
#     ax.plot(tspan_test, free_decay_output_signals[i].data[1, 0:number_steps_test] - identified_output_signals_tveraic[i].data[1, 0:number_steps_test], color=colors[7], label='Error')
#     plt.xlabel(r'Time [s]')
#     plt.ylabel(r'Error in wtmp')
#     ax.legend(loc='upper left')
# ax = plt.subplot(number_free_decay_experiments + 1, 4, 7 * 4 + 1)
# ax.plot(tspan_test, free_decay_output_signal_testing.data[0, 0:number_steps_test], color=colors[0], label='True')
# ax.plot(tspan_test, identified_output_signals_tveraic[-1].data[0, 0:number_steps_test], color=colors[5], label='ID')
# plt.xlabel(r'Time [s]')
# plt.ylabel(r'disp')
# ax.legend(loc='upper left')
# plt.title('Testing Exp')
# ax = plt.subplot(number_free_decay_experiments + 1, 4, 7 * 4 + 2)
# ax.plot(tspan_test, free_decay_output_signal_testing.data[0, 0:number_steps_test] - identified_output_signals_tveraic[-1].data[0, 0:number_steps_test], color=colors[7], label='Error')
# plt.xlabel(r'Time [s]')
# plt.ylabel(r'Error in disp')
# ax.legend(loc='upper left')
# ax = plt.subplot(number_free_decay_experiments + 1, 4, 7 * 4 + 3)
# ax.plot(tspan_test, free_decay_output_signal_testing.data[1, 0:number_steps_test], color=colors[0], label='True')
# ax.plot(tspan_test, identified_output_signals_tveraic[-1].data[1, 0:number_steps_test], color=colors[5], label='ID')
# plt.xlabel(r'Time [s]')
# plt.ylabel(r'wtmp')
# ax.legend(loc='upper left')
# ax = plt.subplot(number_free_decay_experiments + 1, 4, 7 * 4 + 4)
# ax.plot(tspan_test, free_decay_output_signal_testing.data[1, 0:number_steps_test] - identified_output_signals_tveraic[-1].data[1, 0:number_steps_test], color=colors[7], label='Error')
# plt.xlabel(r'Time [s]')
# plt.ylabel(r'Error in wtmp')
# ax.legend(loc='upper left')
# plt.tight_layout()
# # plt.savefig('limit_cycle.eps', format='eps')
# plt.show()
#
#
#
# fig = plt.figure(2, figsize=(24, 16))
# for i in range(number_free_decay_experiments):
#     ax = plt.subplot(number_free_decay_experiments + 1, 4, i * 4 + 1)
#     ax.plot(tspan_zoom, free_decay_output_signals[i].data[0, 0:number_steps_zoom], color=colors[0], label='True')
#     ax.plot(tspan_zoom, identified_output_signals_tveraic[i].data[0, 0:number_steps_zoom], color=colors[5], label='ID')
#     plt.xlabel(r'Time [s]')
#     plt.ylabel(r'disp')
#     ax.legend(loc='upper left')
#     plt.title('Exp ' + str(i + 1))
#     ax = plt.subplot(number_free_decay_experiments + 1, 4, i * 4 + 2)
#     ax.plot(tspan_zoom, free_decay_output_signals[i].data[0, 0:number_steps_zoom] - identified_output_signals_tveraic[i].data[0, 0:number_steps_zoom], color=colors[7], label='Error')
#     plt.xlabel(r'Time [s]')
#     plt.ylabel(r'Error in disp')
#     ax.legend(loc='upper left')
#     ax = plt.subplot(number_free_decay_experiments + 1, 4, i * 4 + 3)
#     ax.plot(tspan_zoom, free_decay_output_signals[i].data[1, 0:number_steps_zoom], color=colors[0], label='True')
#     ax.plot(tspan_zoom, identified_output_signals_tveraic[i].data[1, 0:number_steps_zoom], color=colors[5], label='ID')
#     plt.xlabel(r'Time [s]')
#     plt.ylabel(r'wtmp')
#     ax.legend(loc='upper left')
#     ax = plt.subplot(number_free_decay_experiments + 1, 4, i * 4 + 4)
#     ax.plot(tspan_zoom, free_decay_output_signals[i].data[1, 0:number_steps_zoom] - identified_output_signals_tveraic[i].data[1, 0:number_steps_zoom], color=colors[7], label='Error')
#     plt.xlabel(r'Time [s]')
#     plt.ylabel(r'Error in wtmp')
#     ax.legend(loc='upper left')
# ax = plt.subplot(number_free_decay_experiments + 1, 4, 7 * 4 + 1)
# ax.plot(tspan_zoom, free_decay_output_signal_testing.data[0, 0:number_steps_zoom], color=colors[0], label='True')
# ax.plot(tspan_zoom, identified_output_signals_tveraic[-1].data[0, 0:number_steps_zoom], color=colors[5], label='ID')
# plt.xlabel(r'Time [s]')
# plt.ylabel(r'disp')
# ax.legend(loc='upper left')
# plt.title('Testing Exp')
# ax = plt.subplot(number_free_decay_experiments + 1, 4, 7 * 4 + 2)
# ax.plot(tspan_zoom, free_decay_output_signal_testing.data[0, 0:number_steps_zoom] - identified_output_signals_tveraic[-1].data[0, 0:number_steps_zoom], color=colors[7], label='Error')
# plt.xlabel(r'Time [s]')
# plt.ylabel(r'Error in disp')
# ax.legend(loc='upper left')
# ax = plt.subplot(number_free_decay_experiments + 1, 4, 7 * 4 + 3)
# ax.plot(tspan_zoom, free_decay_output_signal_testing.data[1, 0:number_steps_zoom], color=colors[0], label='True')
# ax.plot(tspan_zoom, identified_output_signals_tveraic[-1].data[1, 0:number_steps_zoom], color=colors[5], label='ID')
# plt.xlabel(r'Time [s]')
# plt.ylabel(r'wtmp')
# ax.legend(loc='upper left')
# ax = plt.subplot(number_free_decay_experiments + 1, 4, 7 * 4 + 4)
# ax.plot(tspan_zoom, free_decay_output_signal_testing.data[1, 0:number_steps_zoom] - identified_output_signals_tveraic[-1].data[1, 0:number_steps_zoom], color=colors[7], label='Error')
# plt.xlabel(r'Time [s]')
# plt.ylabel(r'Error in wtmp')
# ax.legend(loc='upper left')
# plt.tight_layout()
# # plt.savefig('limit_cycle.eps', format='eps')
# plt.show()
#
#
#
# fig = plt.figure(3, figsize=(24, 16))
# for i in range(number_free_decay_experiments):
#     ax = plt.subplot(number_free_decay_experiments + 1, 4, i * 4 + 1)
#     ax.plot(tspan_zoom2, free_decay_output_signals[i].data[0, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[0], label='True')
#     ax.plot(tspan_zoom2, identified_output_signals_tveraic[i].data[0, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[5], label='ID')
#     plt.xlabel(r'Time [s]')
#     plt.ylabel(r'disp')
#     ax.legend(loc='upper left')
#     plt.title('Exp ' + str(i + 1))
#     ax = plt.subplot(number_free_decay_experiments + 1, 4, i * 4 + 2)
#     ax.plot(tspan_zoom2, free_decay_output_signals[i].data[0, number_steps_test - number_steps_zoom2:number_steps_test] - identified_output_signals_tveraic[i].data[0, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[7], label='Error')
#     plt.xlabel(r'Time [s]')
#     plt.ylabel(r'Error in disp')
#     ax.legend(loc='upper left')
#     ax = plt.subplot(number_free_decay_experiments + 1, 4, i * 4 + 3)
#     ax.plot(tspan_zoom2, free_decay_output_signals[i].data[1, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[0], label='True')
#     ax.plot(tspan_zoom2, identified_output_signals_tveraic[i].data[1, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[5], label='ID')
#     plt.xlabel(r'Time [s]')
#     plt.ylabel(r'wtmp')
#     ax.legend(loc='upper left')
#     ax = plt.subplot(number_free_decay_experiments + 1, 4, i * 4 + 4)
#     ax.plot(tspan_zoom2, free_decay_output_signals[i].data[1, number_steps_test - number_steps_zoom2:number_steps_test] - identified_output_signals_tveraic[i].data[1, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[7], label='Error')
#     plt.xlabel(r'Time [s]')
#     plt.ylabel(r'Error in wtmp')
#     ax.legend(loc='upper left')
# ax = plt.subplot(number_free_decay_experiments + 1, 4, 7 * 4 + 1)
# ax.plot(tspan_zoom2, free_decay_output_signal_testing.data[0, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[0], label='True')
# ax.plot(tspan_zoom2, identified_output_signals_tveraic[-1].data[0, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[5], label='ID')
# plt.xlabel(r'Time [s]')
# plt.ylabel(r'disp')
# ax.legend(loc='upper left')
# plt.title('Testing Exp')
# ax = plt.subplot(number_free_decay_experiments + 1, 4, 7 * 4 + 2)
# ax.plot(tspan_zoom2, free_decay_output_signal_testing.data[0, number_steps_test - number_steps_zoom2:number_steps_test] - identified_output_signals_tveraic[-1].data[0, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[7], label='Error')
# plt.xlabel(r'Time [s]')
# plt.ylabel(r'Error in disp')
# ax.legend(loc='upper left')
# ax = plt.subplot(number_free_decay_experiments + 1, 4, 7 * 4 + 3)
# ax.plot(tspan_zoom2, free_decay_output_signal_testing.data[1, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[0], label='True')
# ax.plot(tspan_zoom2, identified_output_signals_tveraic[-1].data[1, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[5], label='ID')
# plt.xlabel(r'Time [s]')
# plt.ylabel(r'wtmp')
# ax.legend(loc='upper left')
# ax = plt.subplot(number_free_decay_experiments + 1, 4, 7 * 4 + 4)
# ax.plot(tspan_zoom2, free_decay_output_signal_testing.data[1, number_steps_test - number_steps_zoom2:number_steps_test] - identified_output_signals_tveraic[-1].data[1, number_steps_test - number_steps_zoom2:number_steps_test], color=colors[7], label='Error')
# plt.xlabel(r'Time [s]')
# plt.ylabel(r'Error in wtmp')
# ax.legend(loc='upper left')
# plt.tight_layout()
# # plt.savefig('limit_cycle.eps', format='eps')
# plt.show()
#
#
# ## Errors
# RMSE_disp = 0
# RMSE_wtmp = 0
# RelE_disp = 0
# RelE_wtmp = 0
# for i in range(number_free_decay_experiments):
#     RMSE_disp += np.sqrt(np.mean((free_decay_output_signals[i].data[0, 0:number_steps_test] - identified_output_signals_tveraic[i].data[0, 0:number_steps_test]) ** 2)) / number_free_decay_experiments
#     RMSE_wtmp += np.sqrt(np.mean((free_decay_output_signals[i].data[1, 0:number_steps_test] - identified_output_signals_tveraic[i].data[1, 0:number_steps_test]) ** 2)) / number_free_decay_experiments
#     RelE_disp += np.mean((np.abs(free_decay_output_signals[i].data[0, 2:number_steps_test] - identified_output_signals_tveraic[i].data[0, 2:number_steps_test])) / np.abs(free_decay_output_signals[i].data[0, 2:number_steps_test])) * 100 / number_free_decay_experiments
#     RelE_wtmp += np.mean((np.abs(free_decay_output_signals[i].data[1, 2:number_steps_test] - identified_output_signals_tveraic[i].data[1, 2:number_steps_test])) / np.abs(free_decay_output_signals[i].data[1, 2:number_steps_test])) * 100 / number_free_decay_experiments
#
# RMSE_disp_testing = np.sqrt(np.mean((free_decay_output_signal_testing.data[0, 0:number_steps_test] - identified_output_signals_tveraic[-1].data[0, 0:number_steps_test]) ** 2))
# RMSE_wtmp_testing = np.sqrt(np.mean((free_decay_output_signal_testing.data[1, 0:number_steps_test] - identified_output_signals_tveraic[-1].data[1, 0:number_steps_test]) ** 2))
# RelE_disp_testing = np.mean((np.abs(free_decay_output_signal_testing.data[0, 2:number_steps_test] - identified_output_signals_tveraic[-1].data[0, 2:number_steps_test])) / np.abs(free_decay_output_signals[-1].data[0, 2:number_steps_test])) * 100
# RelE_wtmp_testing = np.mean((np.abs(free_decay_output_signal_testing.data[1, 2:number_steps_test] - identified_output_signals_tveraic[-1].data[1, 2:number_steps_test])) / np.abs(free_decay_output_signals[-1].data[1, 2:number_steps_test])) * 100


