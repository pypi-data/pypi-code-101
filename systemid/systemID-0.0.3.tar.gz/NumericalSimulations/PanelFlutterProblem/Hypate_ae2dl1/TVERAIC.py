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
from scipy.fft import fft

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from ClassesDynamics.ClassPanelFlutterDynamics import PanelFlutterDynamics
from SystemIDAlgorithms.DepartureDynamics import departureDynamicsFromInitialConditionResponse


from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, add2Signals, subtract2Signals
from ClassesGeneral.ClassExperiments import Experiments
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassERA import TVERAFromInitialConditionResponse
from NumericalSimulations.PanelFlutterProblem.Hypate_ae2dl1.PlotFormating import plotModeShapes, plotMidPoint, plotSVD, plotSurface



# Load data
ae2d_l1_S_m_100 = pickle.load(open("data/ae2d_l1_S=-10.pkl", "rb"))
ae2d_l1_S_m_098 = pickle.load(open("data/ae2d_l1_S=-9,8.pkl", "rb"))
ae2d_l1_S_m_096 = pickle.load(open("data/ae2d_l1_S=-9,6.pkl", "rb"))
ae2d_l1_S_m_095 = pickle.load(open("data/ae2d_l1_S=-9,5.pkl", "rb"))
ae2d_l1_S_m_094 = pickle.load(open("data/ae2d_l1_S=-9,4.pkl", "rb"))
ae2d_l1_S_m_092 = pickle.load(open("data/ae2d_l1_S=-9,2.pkl", "rb"))
ae2d_l1_S_m_090 = pickle.load(open("data/ae2d_l1_S=-9.pkl", "rb"))
ae2d_l1_S_m_088 = pickle.load(open("data/ae2d_l1_S=-8,8.pkl", "rb"))
ae2d_l1_S_m_086 = pickle.load(open("data/ae2d_l1_S=-8,6.pkl", "rb"))
ae2d_l1_S_m_085 = pickle.load(open("data/ae2d_l1_S=-8,5.pkl", "rb"))
ae2d_l1_S_m_084 = pickle.load(open("data/ae2d_l1_S=-8,4.pkl", "rb"))
ae2d_l1_S_m_082 = pickle.load(open("data/ae2d_l1_S=-8,2.pkl", "rb"))
ae2d_l1_S_m_080 = pickle.load(open("data/ae2d_l1_S=-8.pkl", "rb"))
# ae2d_l1_S_m_075 = pickle.load(open("data/ae2d_l1_S=-7,5.pkl", "rb"))
# ae2d_l1_S_m_070 = pickle.load(open("data/ae2d_l1_S=-7.pkl", "rb"))
# ae2d_l1_S_m_065 = pickle.load(open("data/ae2d_l1_S=-6,5.pkl", "rb"))
# ae2d_l1_S_m_060 = pickle.load(open("data/ae2d_l1_S=-6.pkl", "rb"))
# ae2d_l1_S_m_055 = pickle.load(open("data/ae2d_l1_S=-5,5.pkl", "rb"))
# ae2d_l1_S_m_050 = pickle.load(open("data/ae2d_l1_S=-5.pkl", "rb"))
# ae2d_l1_S_m_045 = pickle.load(open("data/ae2d_l1_S=-4,5.pkl", "rb"))
# ae2d_l1_S_m_040 = pickle.load(open("data/ae2d_l1_S=-4.pkl", "rb"))
# ae2d_l1_S_m_035 = pickle.load(open("data/ae2d_l1_S=-3,5.pkl", "rb"))
# ae2d_l1_S_m_030 = pickle.load(open("data/ae2d_l1_S=-3.pkl", "rb"))
# ae2d_l1_S_m_025 = pickle.load(open("data/ae2d_l1_S=-2,5.pkl", "rb"))
# ae2d_l1_S_m_020 = pickle.load(open("data/ae2d_l1_S=-2.pkl", "rb"))
# ae2d_l1_S_m_018 = pickle.load(open("data/ae2d_l1_S=-1,8.pkl", "rb"))
# ae2d_l1_S_m_016 = pickle.load(open("data/ae2d_l1_S=-1,6.pkl", "rb"))
# ae2d_l1_S_m_015 = pickle.load(open("data/ae2d_l1_S=-1,5.pkl", "rb"))
# ae2d_l1_S_m_014 = pickle.load(open("data/ae2d_l1_S=-1,4.pkl", "rb"))
# ae2d_l1_S_m_012 = pickle.load(open("data/ae2d_l1_S=-1,2.pkl", "rb"))
# ae2d_l1_S_m_010 = pickle.load(open("data/ae2d_l1_S=-1.pkl", "rb"))
# ae2d_l1_S_m_008 = pickle.load(open("data/ae2d_l1_S=-0,8.pkl", "rb"))
# ae2d_l1_S_m_006 = pickle.load(open("data/ae2d_l1_S=-0,6.pkl", "rb"))
# ae2d_l1_S_m_005 = pickle.load(open("data/ae2d_l1_S=-0,5.pkl", "rb"))
# ae2d_l1_S_m_004 = pickle.load(open("data/ae2d_l1_S=-0,4.pkl", "rb"))
# ae2d_l1_S_m_002 = pickle.load(open("data/ae2d_l1_S=-0,2.pkl", "rb"))
# ae2d_l1_S_000 = pickle.load(open("data/ae2d_l1_S=0.pkl", "rb"))
# ae2d_l1_S_p_002 = pickle.load(open("data/ae2d_l1_S=0,2.pkl", "rb"))
# ae2d_l1_S_p_004 = pickle.load(open("data/ae2d_l1_S=0,4.pkl", "rb"))
# ae2d_l1_S_p_005 = pickle.load(open("data/ae2d_l1_S=0,5.pkl", "rb"))
# ae2d_l1_S_p_006 = pickle.load(open("data/ae2d_l1_S=0,6.pkl", "rb"))
# ae2d_l1_S_p_008 = pickle.load(open("data/ae2d_l1_S=0,8.pkl", "rb"))
# ae2d_l1_S_p_010 = pickle.load(open("data/ae2d_l1_S=1.pkl", "rb"))
# ae2d_l1_S_p_012 = pickle.load(open("data/ae2d_l1_S=1,2.pkl", "rb"))
# ae2d_l1_S_p_014 = pickle.load(open("data/ae2d_l1_S=1,4.pkl", "rb"))
# ae2d_l1_S_p_015 = pickle.load(open("data/ae2d_l1_S=1,5.pkl", "rb"))
# ae2d_l1_S_p_016 = pickle.load(open("data/ae2d_l1_S=1,6.pkl", "rb"))
# ae2d_l1_S_p_018 = pickle.load(open("data/ae2d_l1_S=1,8.pkl", "rb"))
# ae2d_l1_S_p_020 = pickle.load(open("data/ae2d_l1_S=2.pkl", "rb"))
# ae2d_l1_S_p_021 = pickle.load(open("data/ae2d_l1_S=2,1.pkl", "rb"))
# ae2d_l1_S_p_022 = pickle.load(open("data/ae2d_l1_S=2,2.pkl", "rb"))
# ae2d_l1_S_p_023 = pickle.load(open("data/ae2d_l1_S=2,3.pkl", "rb"))
# ae2d_l1_S_p_024 = pickle.load(open("data/ae2d_l1_S=2,4.pkl", "rb"))
# ae2d_l1_S_p_025 = pickle.load(open("data/ae2d_l1_S=2,5.pkl", "rb"))
# ae2d_l1_S_p_026 = pickle.load(open("data/ae2d_l1_S=2,6.pkl", "rb"))
# ae2d_l1_S_p_027 = pickle.load(open("data/ae2d_l1_S=2,7.pkl", "rb"))
# ae2d_l1_S_p_028 = pickle.load(open("data/ae2d_l1_S=2,8.pkl", "rb"))
# ae2d_l1_S_p_029 = pickle.load(open("data/ae2d_l1_S=2,9.pkl", "rb"))
# ae2d_l1_S_p_030 = pickle.load(open("data/ae2d_l1_S=3.pkl", "rb"))
# ae2d_l1_S_p_035 = pickle.load(open("data/ae2d_l1_S=3,5.pkl", "rb"))
# ae2d_l1_S_p_040 = pickle.load(open("data/ae2d_l1_S=4.pkl", "rb"))
# ae2d_l1_S_p_045 = pickle.load(open("data/ae2d_l1_S=4,5.pkl", "rb"))
# ae2d_l1_S_p_050 = pickle.load(open("data/ae2d_l1_S=5.pkl", "rb"))
# ae2d_l1_S_p_055 = pickle.load(open("data/ae2d_l1_S=5,5.pkl", "rb"))
# ae2d_l1_S_p_060 = pickle.load(open("data/ae2d_l1_S=6.pkl", "rb"))
# ae2d_l1_S_p_065 = pickle.load(open("data/ae2d_l1_S=6,5.pkl", "rb"))
# ae2d_l1_S_p_070 = pickle.load(open("data/ae2d_l1_S=7.pkl", "rb"))
# ae2d_l1_S_p_075 = pickle.load(open("data/ae2d_l1_S=7,5.pkl", "rb"))
ae2d_l1_S_p_080 = pickle.load(open("data/ae2d_l1_S=8.pkl", "rb"))
ae2d_l1_S_p_082 = pickle.load(open("data/ae2d_l1_S=8,2.pkl", "rb"))
ae2d_l1_S_p_084 = pickle.load(open("data/ae2d_l1_S=8,4.pkl", "rb"))
ae2d_l1_S_p_085 = pickle.load(open("data/ae2d_l1_S=8,5.pkl", "rb"))
ae2d_l1_S_p_086 = pickle.load(open("data/ae2d_l1_S=8,6.pkl", "rb"))
ae2d_l1_S_p_088 = pickle.load(open("data/ae2d_l1_S=8,8.pkl", "rb"))
ae2d_l1_S_p_090 = pickle.load(open("data/ae2d_l1_S=9.pkl", "rb"))
ae2d_l1_S_p_092 = pickle.load(open("data/ae2d_l1_S=9,2.pkl", "rb"))
ae2d_l1_S_p_094 = pickle.load(open("data/ae2d_l1_S=9,4.pkl", "rb"))
ae2d_l1_S_p_095 = pickle.load(open("data/ae2d_l1_S=9,5.pkl", "rb"))
ae2d_l1_S_p_096 = pickle.load(open("data/ae2d_l1_S=9,6.pkl", "rb"))
ae2d_l1_S_p_098 = pickle.load(open("data/ae2d_l1_S=9,8.pkl", "rb"))
ae2d_l1_S_p_100 = pickle.load(open("data/ae2d_l1_S=10.pkl", "rb"))

training_data_large_perturbation = [ae2d_l1_S_m_100, ae2d_l1_S_m_096, ae2d_l1_S_m_092, ae2d_l1_S_m_088, ae2d_l1_S_m_084,
                                    ae2d_l1_S_m_080, ae2d_l1_S_p_080, ae2d_l1_S_p_084, ae2d_l1_S_p_088, ae2d_l1_S_p_092,
                                    ae2d_l1_S_p_096, ae2d_l1_S_p_100]

# training_data_small_perturbation = [ae2d_l1_S_m_030, ae2d_l1_S_m_025, ae2d_l1_S_m_020, ae2d_l1_S_m_016, ae2d_l1_S_m_012,
#                                     ae2d_l1_S_m_008, ae2d_l1_S_m_004, ae2d_l1_S_p_004, ae2d_l1_S_p_008, ae2d_l1_S_p_012,
#                                     ae2d_l1_S_p_016, ae2d_l1_S_p_020, ae2d_l1_S_p_021, ae2d_l1_S_p_022, ae2d_l1_S_p_023,
#                                     ae2d_l1_S_p_024, ae2d_l1_S_p_025, ae2d_l1_S_p_026, ae2d_l1_S_p_027, ae2d_l1_S_p_028,
#                                     ae2d_l1_S_p_029, ae2d_l1_S_p_030]

# training_data_small_perturbation = [ae2d_l1_S_p_020, ae2d_l1_S_p_022, ae2d_l1_S_p_023,
#                                     ae2d_l1_S_p_024, ae2d_l1_S_p_026, ae2d_l1_S_p_027, ae2d_l1_S_p_028, ae2d_l1_S_p_030]

test_data_large_perturbation = [ae2d_l1_S_m_098, ae2d_l1_S_m_095, ae2d_l1_S_m_094, ae2d_l1_S_m_090, ae2d_l1_S_m_086,
                                ae2d_l1_S_m_085, ae2d_l1_S_m_082, ae2d_l1_S_p_082, ae2d_l1_S_p_085, ae2d_l1_S_p_086,
                                ae2d_l1_S_p_090, ae2d_l1_S_p_094, ae2d_l1_S_p_095, ae2d_l1_S_p_098]

# test_data_small_perturbation = [ae2d_l1_S_m_018, ae2d_l1_S_m_015, ae2d_l1_S_m_014, ae2d_l1_S_m_010, ae2d_l1_S_m_016,
#                                 ae2d_l1_S_m_015, ae2d_l1_S_m_012, ae2d_l1_S_p_012, ae2d_l1_S_p_015, ae2d_l1_S_p_016,
#                                 ae2d_l1_S_p_010, ae2d_l1_S_p_014, ae2d_l1_S_p_015, ae2d_l1_S_p_018]

# test_data_small_perturbation = [ae2d_l1_S_p_021, ae2d_l1_S_p_025, ae2d_l1_S_p_029]


# Parameters for identification
perturbation = 'Large'
if perturbation == 'Small':
    training_set = training_data_small_perturbation
    test_set = test_data_small_perturbation
else:
    training_set = training_data_large_perturbation
    test_set = test_data_large_perturbation
tspan = ae2d_l1_S_m_100['time']
total_time = tspan[-1]
frequency = int(1 / (tspan[1] - tspan[0]))
number_steps = int(total_time * frequency) + 1
assumed_state_dimension = 6
output_dimension = 101
input_dimension = 1
p, q = getOptimizedHankelMatrixSize(assumed_state_dimension, output_dimension, input_dimension)


# Number Experiments
number_free_decay_experiments = q * input_dimension


# Fake system
def A(tk):
    return np.zeros([assumed_state_dimension, assumed_state_dimension])
def B(tk):
    return np.zeros([assumed_state_dimension, input_dimension])
def C(tk):
    return np.zeros([output_dimension, assumed_state_dimension])
def D(tk):
    return np.zeros([output_dimension, input_dimension])
system = DiscreteLinearSystem(frequency, assumed_state_dimension, input_dimension, output_dimension, [(np.zeros(assumed_state_dimension), 0)], 'Fake System', A, B, C, D)


# Fake Input Signal
input_signal_nominal = DiscreteSignal(input_dimension, 'Zero Input', total_time, frequency)


# Free Decay Experiments
number_free_decay_experiments = len(training_set)
free_decay_output_signals_deviated = []
free_decay_experiments_systems = []
free_decay_experiments_input_signals = []
for i in range(number_free_decay_experiments):
    free_decay_output_signals_deviated.append(DiscreteSignal(output_dimension, 'Output Signal Deviated ' + str(i), total_time, frequency, signal_shape='External', data=training_set[i]['data'][0::3, 0, :]))
    free_decay_experiments_systems.append(system)
    free_decay_experiments_input_signals.append(input_signal_nominal)
free_decay_experiments_deviated = Experiments(free_decay_experiments_systems, free_decay_experiments_input_signals)
for i in range(number_free_decay_experiments):
    free_decay_experiments_deviated.output_signals[i] = free_decay_output_signals_deviated[i]


# Full Experiments
number_full_experiments_training = len(training_set)
number_full_experiments_test = len(test_set)
full_output_signals_deviated = []
full_experiments = []
for i in range(number_full_experiments_training):
    exp = Experiments([system], [input_signal_nominal])
    exp.output_signals[0] = DiscreteSignal(output_dimension, 'Output Signal Deviated ' + str(i), total_time, frequency, signal_shape='External', data=training_set[i]['data'][0::3, 0, :])
    full_experiments.append(exp)
for i in range(number_full_experiments_test):
    exp = Experiments([system], [input_signal_nominal])
    exp.output_signals[0] = DiscreteSignal(output_dimension, 'Output Signal Deviated ' + str(i), total_time, frequency, signal_shape='External', data=test_set[i]['data'][0::3, 0, :])
    full_experiments.append(exp)


# TVERA
tvera = []
for i in range(number_full_experiments_training + number_full_experiments_test):
    tvera.append(TVERAFromInitialConditionResponse(free_decay_experiments_deviated, full_experiments[i], assumed_state_dimension, p))


# Identified Systems
identified_systems = []
for i in range(number_full_experiments_training + number_full_experiments_test):
    identified_systems.append(DiscreteLinearSystem(frequency, assumed_state_dimension, input_dimension, output_dimension, [(tvera[i].x0, 0)], 'System ID ' + str(i), tvera[i].A, tvera[i].B, tvera[i].C, tvera[i].D))


# True Signals
true_output_signals = []
for i in range(number_full_experiments_training + number_full_experiments_test):
    true_output_signals.append(full_experiments[i].output_signals[0])


# Identified Output Signals
identified_output_signals = []
for i in range(number_full_experiments_training + number_full_experiments_test):
    identified_output_signals.append(OutputSignal(input_signal_nominal, identified_systems[i], 'Identified Output Signal Test ' + str(i), state_propagation=False, signal_input_history=full_experiments[i].output_signals[0].data, signal_output_history=full_experiments[i].output_signals[0].data))








# Plotting
time_steps = np.array([0, 1, 5, 10, 50, 100, 500, 1000, 1500, 1999])
perturbP = np.array([-0.0001, -0.000092, -0.000084, +0.000084, +0.000092, +0.0001])
plotModeShapes([true_output_signals[0], true_output_signals[2],true_output_signals[5], true_output_signals[6], true_output_signals[9], true_output_signals[11]],
               [identified_output_signals[0], identified_output_signals[2], identified_output_signals[5], identified_output_signals[6], identified_output_signals[9], identified_output_signals[11]],
                time_steps, perturbP, 1)

plotMidPoint([true_output_signals[0], true_output_signals[2],true_output_signals[5], true_output_signals[6], true_output_signals[9], true_output_signals[11]],
             [identified_output_signals[0], identified_output_signals[2], identified_output_signals[5], identified_output_signals[6], identified_output_signals[9], identified_output_signals[11]],
             50, tspan[0:2000], perturbP, 2)



time_steps = np.array([0, 1, 5, 10, 50, 100, 500, 1000, 1500, 1999])
perturbP = np.array([-0.000094, -0.000086, -0.000082, +0.000082, +0.000086, +0.000094])
plotModeShapes([true_output_signals[14], true_output_signals[16],true_output_signals[18], true_output_signals[19], true_output_signals[21], true_output_signals[23]],
               [identified_output_signals[14], identified_output_signals[16], identified_output_signals[18], identified_output_signals[19], identified_output_signals[21], identified_output_signals[23]],
                time_steps, perturbP, 3)

plotMidPoint([true_output_signals[14], true_output_signals[16],true_output_signals[18], true_output_signals[19], true_output_signals[21], true_output_signals[23]],
             [identified_output_signals[14], identified_output_signals[16], identified_output_signals[18], identified_output_signals[19], identified_output_signals[21], identified_output_signals[23]],
             50, tspan[0:2000], perturbP, 4)


sigma = tvera[0].Sigma
plotSVD(sigma, time_steps, 5)






N = 512
# sample spacing
T = 1 / frequency
x = np.linspace(0.0, N*T, N)
y = identified_output_signals[0].data[50, 1400:1912]
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()




# plt.figure(num=4, figsize=[20, 6])
#
# plt.subplot(3, 1, 1)
# plt.plot(tspan, tvera0.A(tspan)[0, 0])
# plt.plot(tspan, identified_output_signal0.data[50, :])
# plt.xlabel('Time')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'], loc='lower right')
# plt.title('TEST 0')
# plt.subplot(3, 1, 2)
# plt.plot(tspan, true_output_signal0.data[50, :] - identified_output_signal0.data[50, :])
# plt.xlabel('Time')
# plt.ylabel('Error')
# plt.title('TEST 0')
#
# plt.subplot(3, 1, 3)
# plt.plot(tspan, true_output_signal1.data[50, :])
# plt.plot(tspan, identified_output_signal1.data[50, :])
# plt.xlabel('Time')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'], loc='lower right')
# plt.title('TEST 1')
#
# plt.show()






# # Linearized System
# linearized_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(deviations_dx0[0], 0)], 'System Linearized', dynamics.A, dynamics.B, dynamics.C, dynamics.D)
#
#
# # Linearized Output Signal
# linearized_output_signal = add2Signals(nominal_output_signal_test, OutputSignal(nominal_input_signal_test, linearized_system, 'Linearized Deviation Output Signal'))
#
#
# Plotting
#plotSignals([[true_output_signal, identified_output_signal], [subtract2Signals(true_output_signal, identified_output_signal)]], 1, percentage=0.6)


# # # True Corrected System
# # corrected_system = correctSystemForEigenvaluesCheck(nominal_system_d, true_output_signal.number_steps - q, p)
# #
# # # Identified Corrected System
# # corrected_system_id = correctSystemForEigenvaluesCheck(identified_system, true_output_signal.number_steps - q, p)
# #
# #
#
# # # plotSignals([[nominal_output_signal] + free_decay_experiments.output_signals, [nominal_output_signal] + forced_response_experiments.output_signals, [nominal_output_signal] + full_experiment.output_signals], 1)
# # # plotSignals([free_decay_experiments_deviated.input_signals, forced_response_experiments_deviated.input_signals, full_experiment_deviated.input_signals], 2)
# # # plotSignals([free_decay_experiments_deviated.output_signals, forced_response_experiments_deviated.output_signals, full_experiment_deviated.output_signals], 3)




#
#
#
#
#
#
#
#
# # Coordinates
# x = ae2d_l1_S_m_100['coor'][:, 0]
# y = ae2d_l1_S_m_100['coor'][:, 1]
# X, Y = np.meshgrid(x, y)
# Z = np.zeros([303, 303, 10])
# time_steps = np.array([0, 1, 5, 10, 50, 100, 500, 1000, 1500, 1999])
# for k in range(10):
#     for i in range(303):
#         Z[i, :, k] = ae2d_l1_S_m_100['data'][:, 0, time_steps[k]]
#
# plotSurface(X, Y, Z, time_steps, 1)
