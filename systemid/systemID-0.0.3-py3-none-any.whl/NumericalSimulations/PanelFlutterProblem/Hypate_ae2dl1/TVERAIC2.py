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
from NumericalSimulations.PanelFlutterProblem.Hypate_ae2dl1.PlotFormating import plotModeShapes, plotMidPoint



# Load data
ae2d_l1_S_m_100 = pickle.load(open("data/ae2d_l1_S=-10.pkl", "rb"))
ae2d_l1_S_m_095 = pickle.load(open("data/ae2d_l1_S=-9,5.pkl", "rb"))
ae2d_l1_S_m_090 = pickle.load(open("data/ae2d_l1_S=-9.pkl", "rb"))
ae2d_l1_S_m_085 = pickle.load(open("data/ae2d_l1_S=-8,5.pkl", "rb"))
ae2d_l1_S_m_080 = pickle.load(open("data/ae2d_l1_S=-8.pkl", "rb"))
ae2d_l1_S_m_075 = pickle.load(open("data/ae2d_l1_S=-7,5.pkl", "rb"))
ae2d_l1_S_m_070 = pickle.load(open("data/ae2d_l1_S=-7.pkl", "rb"))
ae2d_l1_S_m_065 = pickle.load(open("data/ae2d_l1_S=-6,5.pkl", "rb"))
ae2d_l1_S_m_060 = pickle.load(open("data/ae2d_l1_S=-6.pkl", "rb"))
ae2d_l1_S_m_055 = pickle.load(open("data/ae2d_l1_S=-5,5.pkl", "rb"))
ae2d_l1_S_m_050 = pickle.load(open("data/ae2d_l1_S=-5.pkl", "rb"))
ae2d_l1_S_m_045 = pickle.load(open("data/ae2d_l1_S=-4,5.pkl", "rb"))
ae2d_l1_S_m_040 = pickle.load(open("data/ae2d_l1_S=-4.pkl", "rb"))
ae2d_l1_S_m_035 = pickle.load(open("data/ae2d_l1_S=-3,5.pkl", "rb"))
ae2d_l1_S_m_030 = pickle.load(open("data/ae2d_l1_S=-3.pkl", "rb"))
ae2d_l1_S_m_025 = pickle.load(open("data/ae2d_l1_S=-2,5.pkl", "rb"))
ae2d_l1_S_m_020 = pickle.load(open("data/ae2d_l1_S=-2.pkl", "rb"))
ae2d_l1_S_m_015 = pickle.load(open("data/ae2d_l1_S=-1,5.pkl", "rb"))
ae2d_l1_S_m_010 = pickle.load(open("data/ae2d_l1_S=-1.pkl", "rb"))
ae2d_l1_S_m_005 = pickle.load(open("data/ae2d_l1_S=-0,5.pkl", "rb"))
ae2d_l1_S_000 = pickle.load(open("data/ae2d_l1_S=0.pkl", "rb"))
ae2d_l1_S_p_005 = pickle.load(open("data/ae2d_l1_S=0,5.pkl", "rb"))
ae2d_l1_S_p_010 = pickle.load(open("data/ae2d_l1_S=1.pkl", "rb"))
ae2d_l1_S_p_015 = pickle.load(open("data/ae2d_l1_S=1,5.pkl", "rb"))
ae2d_l1_S_p_020 = pickle.load(open("data/ae2d_l1_S=2.pkl", "rb"))
ae2d_l1_S_p_025 = pickle.load(open("data/ae2d_l1_S=2,5.pkl", "rb"))
ae2d_l1_S_p_030 = pickle.load(open("data/ae2d_l1_S=3.pkl", "rb"))
ae2d_l1_S_p_035 = pickle.load(open("data/ae2d_l1_S=3,5.pkl", "rb"))
ae2d_l1_S_p_040 = pickle.load(open("data/ae2d_l1_S=4.pkl", "rb"))
ae2d_l1_S_p_045 = pickle.load(open("data/ae2d_l1_S=4,5.pkl", "rb"))
ae2d_l1_S_p_050 = pickle.load(open("data/ae2d_l1_S=5.pkl", "rb"))
ae2d_l1_S_p_055 = pickle.load(open("data/ae2d_l1_S=5,5.pkl", "rb"))
ae2d_l1_S_p_060 = pickle.load(open("data/ae2d_l1_S=6.pkl", "rb"))
ae2d_l1_S_p_065 = pickle.load(open("data/ae2d_l1_S=6,5.pkl", "rb"))
ae2d_l1_S_p_070 = pickle.load(open("data/ae2d_l1_S=7.pkl", "rb"))
ae2d_l1_S_p_075 = pickle.load(open("data/ae2d_l1_S=7,5.pkl", "rb"))
ae2d_l1_S_p_080 = pickle.load(open("data/ae2d_l1_S=8.pkl", "rb"))
ae2d_l1_S_p_085 = pickle.load(open("data/ae2d_l1_S=8,5.pkl", "rb"))
ae2d_l1_S_p_090 = pickle.load(open("data/ae2d_l1_S=9.pkl", "rb"))
ae2d_l1_S_p_095 = pickle.load(open("data/ae2d_l1_S=9,5.pkl", "rb"))
ae2d_l1_S_p_100 = pickle.load(open("data/ae2d_l1_S=10.pkl", "rb"))
ae2d_l1_S_p_021 = pickle.load(open("data/ae2d_l1_S=2,1.pkl", "rb"))
ae2d_l1_S_p_022 = pickle.load(open("data/ae2d_l1_S=2,2.pkl", "rb"))
ae2d_l1_S_p_023 = pickle.load(open("data/ae2d_l1_S=2,3.pkl", "rb"))
ae2d_l1_S_p_024 = pickle.load(open("data/ae2d_l1_S=2,4.pkl", "rb"))
ae2d_l1_S_p_026 = pickle.load(open("data/ae2d_l1_S=2,6.pkl", "rb"))
ae2d_l1_S_p_027 = pickle.load(open("data/ae2d_l1_S=2,7.pkl", "rb"))
ae2d_l1_S_p_028 = pickle.load(open("data/ae2d_l1_S=2,8.pkl", "rb"))
ae2d_l1_S_p_029 = pickle.load(open("data/ae2d_l1_S=2,9.pkl", "rb"))


training_data = [ae2d_l1_S_m_100, ae2d_l1_S_m_090, ae2d_l1_S_m_080, ae2d_l1_S_m_070, ae2d_l1_S_m_060, ae2d_l1_S_m_050,
                 ae2d_l1_S_m_040, ae2d_l1_S_m_030, ae2d_l1_S_m_020, ae2d_l1_S_m_010, ae2d_l1_S_p_010, ae2d_l1_S_p_020,
                 ae2d_l1_S_p_030, ae2d_l1_S_p_040, ae2d_l1_S_p_050, ae2d_l1_S_p_060, ae2d_l1_S_p_070, ae2d_l1_S_p_080,
                 ae2d_l1_S_p_090, ae2d_l1_S_p_100]

test_data_large = [ae2d_l1_S_m_095, ae2d_l1_S_m_085, ae2d_l1_S_m_075, ae2d_l1_S_m_065, ae2d_l1_S_m_055, ae2d_l1_S_m_045,
                 ae2d_l1_S_m_035, ae2d_l1_S_m_025, ae2d_l1_S_m_015, ae2d_l1_S_m_005, ae2d_l1_S_p_005, ae2d_l1_S_p_015,
                 ae2d_l1_S_p_025, ae2d_l1_S_p_035, ae2d_l1_S_p_045, ae2d_l1_S_p_055, ae2d_l1_S_p_065, ae2d_l1_S_p_075,
                 ae2d_l1_S_p_085, ae2d_l1_S_p_095]

test_data_narrow = [ae2d_l1_S_p_021, ae2d_l1_S_p_022, ae2d_l1_S_p_023, ae2d_l1_S_p_024, ae2d_l1_S_p_025,
                    ae2d_l1_S_p_026, ae2d_l1_S_p_027, ae2d_l1_S_p_028, ae2d_l1_S_p_029]


# Parameters for identification
tspan = ae2d_l1_S_m_100['time']
total_time = tspan[-1]
frequency = int(1 / (tspan[1] - tspan[0]))
number_steps = int(total_time * frequency) + 1
assumed_state_dimension = 10
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
input_signal_nominal = DiscreteSignal(input_dimension, 'Zero Input', 1 - 1 / frequency, frequency)


# Free Decay Experiments
number_free_decay_experiments = len(training_data)
free_decay_output_signals_deviated = []
free_decay_experiments_systems = []
free_decay_experiments_input_signals = []
for i in range(number_free_decay_experiments):
    free_decay_output_signals_deviated.append(DiscreteSignal(output_dimension, 'Output Signal Deviated ' + str(i) + ' 1', 1 - 1 / frequency, frequency, signal_shape='External', data=training_data[i]['data'][0::3, 0, 0:1000]))
    free_decay_experiments_systems.append(system)
    free_decay_experiments_input_signals.append(input_signal_nominal)
    free_decay_output_signals_deviated.append(DiscreteSignal(output_dimension, 'Output Signal Deviated ' + str(i) + ' 2', 1 - 1 / frequency, frequency, signal_shape='External', data=training_data[i]['data'][0::3, 0, 1000:2000]))
    free_decay_experiments_systems.append(system)
    free_decay_experiments_input_signals.append(input_signal_nominal)
free_decay_experiments_deviated = Experiments(free_decay_experiments_systems, free_decay_experiments_input_signals)
for i in range(number_free_decay_experiments):
    free_decay_experiments_deviated.output_signals[i] = free_decay_output_signals_deviated[i]


# Full Experiments
number_full_experiments_training = len(training_data)
number_full_experiments_large = len(test_data_large)
number_full_experiments_narrow = len(test_data_narrow)
full_output_signals_deviated = []
full_experiments = []
for i in range(number_full_experiments_training):
    exp = Experiments([system], [input_signal_nominal])
    exp.output_signals[0] = DiscreteSignal(output_dimension, 'Output Signal Deviated ' + str(i) + ' 1', 1 - 1 / frequency, frequency, signal_shape='External', data=training_data[i]['data'][0::3, 0, 0:1000])
    full_experiments.append(exp)
    exp = Experiments([system], [input_signal_nominal])
    exp.output_signals[0] = DiscreteSignal(output_dimension, 'Output Signal Deviated ' + str(i) + ' 2', 1 - 1 / frequency, frequency, signal_shape='External', data=training_data[i]['data'][0::3, 0, 1000:2000])
    full_experiments.append(exp)
for i in range(number_full_experiments_large):
    exp = Experiments([system], [input_signal_nominal])
    exp.output_signals[0] = DiscreteSignal(output_dimension, 'Output Signal Deviated ' + str(i) + ' 1', 1 - 1 / frequency, frequency, signal_shape='External', data=test_data_large[i]['data'][0::3, 0, 0:1000])
    full_experiments.append(exp)
    exp = Experiments([system], [input_signal_nominal])
    exp.output_signals[0] = DiscreteSignal(output_dimension, 'Output Signal Deviated ' + str(i) + ' 2', 1 - 1 / frequency, frequency, signal_shape='External', data=test_data_large[i]['data'][0::3, 0, 1000:2000])
    full_experiments.append(exp)
for i in range(number_full_experiments_narrow):
    exp = Experiments([system], [input_signal_nominal])
    exp.output_signals[0] = DiscreteSignal(output_dimension, 'Output Signal Deviated ' + str(i) + ' 1', 1 - 1 / frequency, frequency, signal_shape='External', data=test_data_narrow[i]['data'][0::3, 0, 0:1000])
    full_experiments.append(exp)
    exp = Experiments([system], [input_signal_nominal])
    exp.output_signals[0] = DiscreteSignal(output_dimension, 'Output Signal Deviated ' + str(i) + ' 2', 1 - 1 / frequency, frequency, signal_shape='External', data=test_data_narrow[i]['data'][0::3, 0, 1000:2000])
    full_experiments.append(exp)



# TVERA
tvera = []
for i in range(2 * (number_full_experiments_training + number_free_decay_experiments + number_full_experiments_narrow)):
    tvera.append(TVERAFromInitialConditionResponse(free_decay_experiments_deviated, full_experiments[i], assumed_state_dimension, p))


# Identified Systems
identified_systems = []
for i in range(2 * (number_full_experiments_training + number_free_decay_experiments + number_full_experiments_narrow)):
    identified_systems.append(DiscreteLinearSystem(frequency, assumed_state_dimension, input_dimension, output_dimension, [(tvera[i].x0, 0)], 'System ID ' + str(i), tvera[i].A, tvera[i].B, tvera[i].C, tvera[i].D))


# True Signals
true_output_signals = []
for i in range(2 * (number_full_experiments_training + number_free_decay_experiments + number_full_experiments_narrow)):
    true_output_signals.append(full_experiments[i].output_signals[0])


# Identified Output Signals
identified_output_signals = []
for i in range(2 * (number_full_experiments_training + number_free_decay_experiments + number_full_experiments_narrow)):
    identified_output_signals.append(OutputSignal(input_signal_nominal, identified_systems[i], 'Identified Output Signal Test ' + str(i)))


# Plotting
plotModeShapes(true_output_signals[0:10], identified_output_signals[0:10], np.array([0, 2, 5, 10, 20, 50, 100, 200, 500, 950]), 1)
plotModeShapes(true_output_signals[10:20], identified_output_signals[10:20], np.array([0, 2, 5, 10, 20, 50, 100, 200, 500, 950]), 2)
# plotModeShapes(true_output_signals[20:30], identified_output_signals[20:30], np.array([0, 2, 5, 10, 20, 50, 100, 200, 500, 950]), 3)
# plotModeShapes(true_output_signals[30:40], identified_output_signals[30:40], np.array([0, 2, 5, 10, 20, 50, 100, 200, 500, 950]), 4)
# plotModeShapes(true_output_signals[40:49], identified_output_signals[40:49], np.array([0, 2, 5, 10, 20, 50, 100, 200, 500, 950]), 5)
plotMidPoint(true_output_signals[0:10], identified_output_signals[0:10], 50, np.linspace(0, 1 - 1 / frequency, frequency), 11)
plotMidPoint(true_output_signals[10:20], identified_output_signals[10:20], 50, np.linspace(1, 2 - 1 / frequency, frequency), 12)
plotMidPoint(true_output_signals[20:30], identified_output_signals[20:30], 50, np.linspace(0, 1 - 1 / frequency, frequency), 13)
plotMidPoint(true_output_signals[30:40], identified_output_signals[30:40], 50, np.linspace(0, 1 - 1 / frequency, frequency), 14)
plotMidPoint(true_output_signals[40:50], identified_output_signals[40:50], 50, np.linspace(0, 1 - 1 / frequency, frequency), 15)
plotMidPoint(true_output_signals[50:60], identified_output_signals[50:60], 50, np.linspace(1, 2 - 1 / frequency, frequency), 16)
plotMidPoint(true_output_signals[60:70], identified_output_signals[60:70], 50, np.linspace(0, 1 - 1 / frequency, frequency), 17)
plotMidPoint(true_output_signals[70:80], identified_output_signals[70:80], 50, np.linspace(0, 1 - 1 / frequency, frequency), 18)
plotMidPoint(true_output_signals[80:89], identified_output_signals[80:89], 50, np.linspace(0, 1 - 1 / frequency, frequency), 19)
plotMidPoint(true_output_signals[89:98], identified_output_signals[89:98], 50, np.linspace(0, 1 - 1 / frequency, frequency), 20)


# plt.figure(num=2, figsize=[20, 6])
#
# plt.subplot(3, 2, 1)
# plt.plot(tspan, true_output_signal0.data[50, :])
# plt.plot(tspan, identified_output_signal0.data[50, :])
# plt.xlabel('Time')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'], loc='lower right')
# plt.title('TEST 0')
# plt.subplot(3, 2, 2)
# plt.plot(tspan, true_output_signal0.data[50, :] - identified_output_signal0.data[50, :])
# plt.xlabel('Time')
# plt.ylabel('Error')
# plt.title('TEST 0')
#
# plt.subplot(3, 2, 3)
# plt.plot(tspan, true_output_signal1.data[50, :])
# plt.plot(tspan, identified_output_signal1.data[50, :])
# plt.xlabel('Time')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'], loc='lower right')
# plt.title('TEST 1')
# plt.subplot(3, 2, 4)
# plt.plot(tspan, true_output_signal1.data[50, :] - identified_output_signal1.data[50, :])
# plt.xlabel('Time')
# plt.ylabel('Error')
# plt.title('TEST 1')
#
# plt.subplot(3, 2, 5)
# plt.plot(tspan, true_output_signal2.data[50, :])
# plt.plot(tspan, identified_output_signal2.data[50, :])
# plt.xlabel('Time')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'], loc='lower right')
# plt.title('TEST 2')
# plt.subplot(3, 2, 6)
# plt.plot(tspan, true_output_signal2.data[50, :] - identified_output_signal2.data[50, :])
# plt.xlabel('Time')
# plt.ylabel('Error')
# plt.title('TEST 2')
#
# plt.show()
#
#
#
#
# plt.figure(num=3, figsize=[15, 10])
#
# plt.subplot(2, 3, 1)
# plt.semilogy(np.linspace(1, len(tvera0.Sigma[0]), len(tvera0.Sigma[0])), tvera0.Sigma[0], '*')
# plt.semilogy(np.linspace(1, len(tvera0.Sigma[10]), len(tvera0.Sigma[10])), tvera0.Sigma[10], '*')
# plt.semilogy(np.linspace(1, len(tvera0.Sigma[20]), len(tvera0.Sigma[20])), tvera0.Sigma[20], '*')
# plt.semilogy(np.linspace(1, len(tvera0.Sigma[50]), len(tvera0.Sigma[50])), tvera0.Sigma[50], '*')
# plt.semilogy(np.linspace(1, len(tvera0.Sigma[100]), len(tvera0.Sigma[100])), tvera0.Sigma[100], '*')
# plt.xlabel('# Singular Values')
# plt.ylabel('Magnitude')
# plt.legend(['time = 0', 'time = 10', 'time = 20', 'time = 50', 'time = 100'], loc='upper right')
# plt.title('TEST 0')
# plt.subplot(2, 3, 2)
# plt.semilogy(np.linspace(1, len(tvera1.Sigma[0]), len(tvera1.Sigma[0])), tvera1.Sigma[0], '*')
# plt.semilogy(np.linspace(1, len(tvera1.Sigma[10]), len(tvera1.Sigma[10])), tvera1.Sigma[10], '*')
# plt.semilogy(np.linspace(1, len(tvera1.Sigma[20]), len(tvera1.Sigma[20])), tvera1.Sigma[20], '*')
# plt.semilogy(np.linspace(1, len(tvera1.Sigma[50]), len(tvera1.Sigma[50])), tvera1.Sigma[50], '*')
# plt.semilogy(np.linspace(1, len(tvera1.Sigma[100]), len(tvera1.Sigma[100])), tvera1.Sigma[100], '*')
# plt.xlabel('# Singular Values')
# plt.ylabel('Magnitude')
# plt.legend(['time = 0', 'time = 10', 'time = 20', 'time = 50', 'time = 100'], loc='upper right')
# plt.title('TEST 1')
# plt.subplot(2, 3, 3)
# plt.semilogy(np.linspace(1, len(tvera2.Sigma[0]), len(tvera2.Sigma[0])), tvera2.Sigma[0], '*')
# plt.semilogy(np.linspace(1, len(tvera2.Sigma[10]), len(tvera2.Sigma[10])), tvera2.Sigma[10], '*')
# plt.semilogy(np.linspace(1, len(tvera2.Sigma[20]), len(tvera2.Sigma[20])), tvera2.Sigma[20], '*')
# plt.semilogy(np.linspace(1, len(tvera2.Sigma[50]), len(tvera2.Sigma[50])), tvera2.Sigma[50], '*')
# plt.semilogy(np.linspace(1, len(tvera2.Sigma[100]), len(tvera2.Sigma[100])), tvera2.Sigma[100], '*')
# plt.xlabel('# Singular Values')
# plt.ylabel('Magnitude')
# plt.legend(['time = 0', 'time = 10', 'time = 20', 'time = 50', 'time = 100'], loc='upper right')
# plt.title('TEST 2')
#
# plt.subplot(2, 3, 4)
# plt.semilogy(np.linspace(1, len(tvera0.Sigma[200]), len(tvera0.Sigma[200])), tvera0.Sigma[200], '*')
# plt.semilogy(np.linspace(1, len(tvera0.Sigma[500]), len(tvera0.Sigma[500])), tvera0.Sigma[500], '*')
# plt.semilogy(np.linspace(1, len(tvera0.Sigma[100]), len(tvera0.Sigma[1000])), tvera0.Sigma[1000], '*')
# plt.semilogy(np.linspace(1, len(tvera0.Sigma[1500]), len(tvera0.Sigma[1500])), tvera0.Sigma[1500], '*')
# plt.semilogy(np.linspace(1, len(tvera0.Sigma[1900]), len(tvera0.Sigma[1900])), tvera0.Sigma[1900], '*')
# plt.xlabel('# Singular Values')
# plt.ylabel('Magnitude')
# plt.legend(['time = 200', 'time = 500', 'time = 1000', 'time = 1500', 'time = 1900'], loc='upper right')
# plt.title('TEST 0')
# plt.subplot(2, 3, 5)
# plt.semilogy(np.linspace(1, len(tvera1.Sigma[200]), len(tvera1.Sigma[200])), tvera1.Sigma[200], '*')
# plt.semilogy(np.linspace(1, len(tvera1.Sigma[500]), len(tvera1.Sigma[500])), tvera1.Sigma[500], '*')
# plt.semilogy(np.linspace(1, len(tvera1.Sigma[1000]), len(tvera1.Sigma[1000])), tvera1.Sigma[1000], '*')
# plt.semilogy(np.linspace(1, len(tvera1.Sigma[1500]), len(tvera1.Sigma[1500])), tvera1.Sigma[1500], '*')
# plt.semilogy(np.linspace(1, len(tvera1.Sigma[1900]), len(tvera1.Sigma[1900])), tvera1.Sigma[1900], '*')
# plt.xlabel('# Singular Values')
# plt.ylabel('Magnitude')
# plt.legend(['time = 200', 'time = 500', 'time = 1000', 'time = 1500', 'time = 1900'], loc='upper right')
# plt.title('TEST 1')
# plt.subplot(2, 3, 6)
# plt.semilogy(np.linspace(1, len(tvera2.Sigma[200]), len(tvera2.Sigma[200])), tvera2.Sigma[200], '*')
# plt.semilogy(np.linspace(1, len(tvera2.Sigma[500]), len(tvera2.Sigma[500])), tvera2.Sigma[500], '*')
# plt.semilogy(np.linspace(1, len(tvera2.Sigma[1000]), len(tvera2.Sigma[1000])), tvera2.Sigma[1000], '*')
# plt.semilogy(np.linspace(1, len(tvera2.Sigma[1500]), len(tvera2.Sigma[1500])), tvera2.Sigma[1500], '*')
# plt.semilogy(np.linspace(1, len(tvera2.Sigma[1900]), len(tvera2.Sigma[1900])), tvera2.Sigma[1900], '*')
# plt.xlabel('# Singular Values')
# plt.ylabel('Magnitude')
# plt.legend(['time = 200', 'time = 500', 'time = 1000', 'time = 1500', 'time = 1900'], loc='upper right')
# plt.title('TEST 2')
#
# plt.show()




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
# # plotSignals([[nominal_output_signal] + free_decay_experiments.output_signals, [nominal_output_signal] + forced_response_experiments.output_signals, [nominal_output_signal] + full_experiment.output_signals], 1)
# # plotSignals([free_decay_experiments_deviated.input_signals, forced_response_experiments_deviated.input_signals, full_experiment_deviated.input_signals], 2)
# # plotSignals([free_decay_experiments_deviated.output_signals, forced_response_experiments_deviated.output_signals, full_experiment_deviated.output_signals], 3)