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


from ClassesGeneral.ClassSystem import DiscreteLinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal
from ClassesGeneral.ClassExperiments import Experiments
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from ClassesSystemID.ClassERA import ERAFromInitialConditionResponse



# Load data
ae2d_l1_S_1 = pickle.load(open("data/ae2d_l1_S_1.pkl", "rb"))
ae2d_l1_S_2 = pickle.load(open("data/ae2d_l1_S_2.pkl", "rb"))
ae2d_l1_S_3 = pickle.load(open("data/ae2d_l1_S_3.pkl", "rb"))
ae2d_l1_S_4 = pickle.load(open("data/ae2d_l1_S_4.pkl", "rb"))
ae2d_l1_S_5 = pickle.load(open("data/ae2d_l1_S_5.pkl", "rb"))
ae2d_l1_S_6 = pickle.load(open("data/ae2d_l1_S_6.pkl", "rb"))
ae2d_l1_S_7 = pickle.load(open("data/ae2d_l1_S_7.pkl", "rb"))
ae2d_l1_S_8 = pickle.load(open("data/ae2d_l1_S_8.pkl", "rb"))
ae2d_l1_S_9 = pickle.load(open("data/ae2d_l1_S_9.pkl", "rb"))
ae2d_l1_S_10 = pickle.load(open("data/ae2d_l1_S_10.pkl", "rb"))
ae2d_l1_S_11 = pickle.load(open("data/ae2d_l1_S_11.pkl", "rb"))
ae2d_l1_S_12 = pickle.load(open("data/ae2d_l1_S_12.pkl", "rb"))
ae2d_l1_S_13 = pickle.load(open("data/ae2d_l1_S_13.pkl", "rb"))
ae2d_l1_S_14 = pickle.load(open("data/ae2d_l1_S_14.pkl", "rb"))
ae2d_l1_S_15 = pickle.load(open("data/ae2d_l1_S_15.pkl", "rb"))
ae2d_l1_S_16 = pickle.load(open("data/ae2d_l1_S_16.pkl", "rb"))
ae2d_l1_S_17 = pickle.load(open("data/ae2d_l1_S_17.pkl", "rb"))
ae2d_l1_S_18 = pickle.load(open("data/ae2d_l1_S_18.pkl", "rb"))
ae2d_l1_S_19 = pickle.load(open("data/ae2d_l1_S_19.pkl", "rb"))
ae2d_l1_S_20 = pickle.load(open("data/ae2d_l1_S_20.pkl", "rb"))
ae2d_l1_S_21 = pickle.load(open("data/ae2d_l1_S_21.pkl", "rb"))
ae2d_l1_S_test1 = pickle.load(open("data/ae2d_l1_S_test1.pkl", "rb"))
ae2d_l1_S_test2 = pickle.load(open("data/ae2d_l1_S_test2.pkl", "rb"))
raw_data = [ae2d_l1_S_1, ae2d_l1_S_2, ae2d_l1_S_3, ae2d_l1_S_4, ae2d_l1_S_5, ae2d_l1_S_6, ae2d_l1_S_7, ae2d_l1_S_8,
            ae2d_l1_S_9, ae2d_l1_S_10, ae2d_l1_S_12, ae2d_l1_S_13, ae2d_l1_S_14, ae2d_l1_S_15,
            ae2d_l1_S_16, ae2d_l1_S_17, ae2d_l1_S_18, ae2d_l1_S_19, ae2d_l1_S_20, ae2d_l1_S_21]


# Parameters for identification
tspan = ae2d_l1_S_1['time']
total_time = tspan[-1]
frequency = int(1 / (tspan[1] - tspan[0]))
number_steps = int(total_time * frequency) + 1
assumed_state_dimension = 4
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
number_signals = len(raw_data)
output_signals_deviated = []
free_decay_experiments_systems = []
free_decay_experiments_input_signals = []
for i in range(number_signals):
    output_signals_deviated.append(DiscreteSignal(output_dimension, 'Output Signal Deviated ' + str(i), total_time, frequency, signal_shape='External', data=raw_data[i]['data'][0::3, 0, :]))
    free_decay_experiments_systems.append(system)
    free_decay_experiments_input_signals.append(input_signal_nominal)
free_decay_experiments_deviated = Experiments(free_decay_experiments_systems, free_decay_experiments_input_signals)
for i in range(number_signals):
    free_decay_experiments_deviated.output_signals[i] = output_signals_deviated[i]


# Full Experiments
full_experiment_deviated0 = Experiments([system], [input_signal_nominal])
full_experiment_deviated0.output_signals[0] = DiscreteSignal(output_dimension, 'Output Signal Deviated Test 0', total_time, frequency, signal_shape='External', data=raw_data[5]['data'][0::3, 0, :])
full_experiment_deviated1 = Experiments([system], [input_signal_nominal])
full_experiment_deviated1.output_signals[0] = DiscreteSignal(output_dimension, 'Output Signal Deviated Test 1', total_time, frequency, signal_shape='External', data=ae2d_l1_S_test1['data'][0::3, 0, :])
full_experiment_deviated2 = Experiments([system], [input_signal_nominal])
full_experiment_deviated2.output_signals[0] = DiscreteSignal(output_dimension, 'Output Signal Deviated Test 2', total_time, frequency, signal_shape='External', data=ae2d_l1_S_test2['data'][0::3, 0, :])


# TVERA
eraic0 = ERAFromInitialConditionResponse(free_decay_experiments_deviated.output_signals, assumed_state_dimension, input_dimension, p=4)


# True Output Signals
true_output_signal0 = DiscreteSignal(output_dimension, 'Output Signal Deviated Test 0', total_time, frequency, signal_shape='External', data=raw_data[5]['data'][0::3, 0, :])
# true_output_signal1 = DiscreteSignal(output_dimension, 'Output Signal Deviated Test 1', total_time, frequency, signal_shape='External', data=ae2d_l1_S_test1['data'][0::3, 0, :])
# true_output_signal2 = DiscreteSignal(output_dimension, 'Output Signal Deviated Test 2', total_time, frequency, signal_shape='External', data=ae2d_l1_S_test2['data'][0::3, 0, :])


# Identified System
identified_system0 = DiscreteLinearSystem(frequency, assumed_state_dimension, input_dimension, output_dimension, [(eraic0.x0[:, 5], 0)], 'System ID 0', eraic0.A, eraic0.B, eraic0.C, eraic0.D)
# identified_system1 = DiscreteLinearSystem(frequency, assumed_state_dimension, input_dimension, output_dimension, [(tvera1.x0, 0)], 'System ID 1', tvera1.A, tvera1.B, tvera1.C, tvera1.D)
# identified_system2 = DiscreteLinearSystem(frequency, assumed_state_dimension, input_dimension, output_dimension, [(tvera2.x0, 0)], 'System ID 2', tvera2.A, tvera2.B, tvera2.C, tvera2.D)


# Identified Output Signal
identified_output_signal0 = OutputSignal(input_signal_nominal, identified_system0, 'Identified Output Signal Test 0')
# identified_output_signal1 = OutputSignal(input_signal_nominal, identified_system1, 'Identified Output Signal Test 1')
# identified_output_signal2 = OutputSignal(input_signal_nominal, identified_system2, 'Identified Output Signal Test 2')



# Plotting prediction + extrapolation
plt.figure(num=1, figsize=[30, 18])

plt.subplot(10, 6, 1)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 0])
plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal0.data[:, 0])
plt.xlabel('x')
plt.ylabel('Displacement')
plt.legend(['True', 'Identified'])
plt.title('TEST 0 - Time step: 0')
plt.subplot(10, 6, 2)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 0] - identified_output_signal0.data[:, 0])
plt.xlabel('x')
plt.ylabel('Error')
plt.legend(['Error'])
plt.title('TEST 0 - Time step: 0')
# plt.subplot(10, 6, 3)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 0])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal1.data[:, 0])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 1 - Time step: 0')
# plt.subplot(10, 6, 4)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 0] - identified_output_signal1.data[:, 0])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 1 - Time step: 0')
# plt.subplot(10, 6, 5)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 0])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal2.data[:, 0])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 2 - Time step: 0')
# plt.subplot(10, 6, 6)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 0] - identified_output_signal2.data[:, 0])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 2 - Time step: 0')
#
plt.subplot(10, 6, 7)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 2])
plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal0.data[:, 2])
plt.xlabel('x')
plt.ylabel('Displacement')
plt.legend(['True', 'Identified'])
plt.title('TEST 0 - Time step: 2')
plt.subplot(10, 6, 8)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 2] - identified_output_signal0.data[:, 2])
plt.xlabel('x')
plt.ylabel('Error')
plt.legend(['Error'])
plt.title('TEST 0 - Time step: 2')
# plt.subplot(10, 6, 9)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 10])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal1.data[:, 10])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 1 - Time step: 10')
# plt.subplot(10, 6, 10)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 10] - identified_output_signal1.data[:, 10])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 1 - Time step: 10')
# plt.subplot(10, 6, 11)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 10])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal2.data[:, 10])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 2 - Time step: 10')
# plt.subplot(10, 6, 12)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 10] - identified_output_signal2.data[:, 10])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 2 - Time step: 10')
#
plt.subplot(10, 6, 13)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 4])
plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal0.data[:, 4])
plt.xlabel('x')
plt.ylabel('Displacement')
plt.legend(['True', 'Identified'])
plt.title('TEST 0 - Time step: 4')
plt.subplot(10, 6, 14)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 4] - identified_output_signal0.data[:, 4])
plt.xlabel('x')
plt.ylabel('Error')
plt.legend(['Error'])
plt.title('TEST 0 - Time step: 4')
# plt.subplot(10, 6, 15)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 20])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal1.data[:, 20])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 1 - Time step: 20')
# plt.subplot(10, 6, 16)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 20] - identified_output_signal1.data[:, 20])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 1 - Time step: 20')
# plt.subplot(10, 6, 17)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 20])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal2.data[:, 20])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 2 - Time step: 20')
# plt.subplot(10, 6, 18)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 20] - identified_output_signal2.data[:, 20])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 2 - Time step: 20')
#
plt.subplot(10, 6, 19)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 6])
plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal0.data[:, 6])
plt.xlabel('x')
plt.ylabel('Displacement')
plt.legend(['True', 'Identified'])
plt.title('TEST 0 - Time step: 6')
plt.subplot(10, 6, 20)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 6] - identified_output_signal0.data[:, 6])
plt.xlabel('x')
plt.ylabel('Error')
plt.legend(['Error'])
plt.title('TEST 0 - Time step: 6')
# plt.subplot(10, 6, 21)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 50])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal1.data[:, 50])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 1 - Time step: 50')
# plt.subplot(10, 6, 22)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 50] - identified_output_signal1.data[:, 50])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 1 - Time step: 50')
# plt.subplot(10, 6, 23)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 50])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal2.data[:, 50])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 2 - Time step: 50')
# plt.subplot(10, 6, 24)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 50] - identified_output_signal2.data[:, 50])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 2 - Time step: 50')
#
plt.subplot(10, 6, 25)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 8])
plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal0.data[:, 8])
plt.xlabel('x')
plt.ylabel('Displacement')
plt.legend(['True', 'Identified'])
plt.title('TEST 0 - Time step: 8')
plt.subplot(10, 6, 26)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 8] - identified_output_signal0.data[:, 8])
plt.xlabel('x')
plt.ylabel('Error')
plt.legend(['Error'])
plt.title('TEST 0 - Time step: 8')
# plt.subplot(10, 6, 27)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 100])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal1.data[:, 100])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 1 - Time step: 100')
# plt.subplot(10, 6, 28)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 100] - identified_output_signal1.data[:, 100])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 1 - Time step: 100')
# plt.subplot(10, 6, 29)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 100])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal2.data[:, 100])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 2 - Time step: 100')
# plt.subplot(10, 6, 30)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 100] - identified_output_signal2.data[:, 100])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 2 - Time step: 100')
#
plt.subplot(10, 6, 31)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 10])
plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal0.data[:, 10])
plt.xlabel('x')
plt.ylabel('Displacement')
plt.legend(['True', 'Identified'])
plt.title('TEST 0 - Time step: 10')
plt.subplot(10, 6, 32)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 10] - identified_output_signal0.data[:, 10])
plt.xlabel('x')
plt.ylabel('Error')
plt.legend(['Error'])
plt.title('TEST 0 - Time step: 10')
# plt.subplot(10, 6, 33)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 200])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal1.data[:, 200])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 1 - Time step: 200')
# plt.subplot(10, 6, 34)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 200] - identified_output_signal1.data[:, 200])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 1 - Time step: 200')
# plt.subplot(10, 6, 35)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 200])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal2.data[:, 200])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 2 - Time step: 200')
# plt.subplot(10, 6, 36)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 200] - identified_output_signal2.data[:, 200])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 2 - Time step: 200')
#
plt.subplot(10, 6, 37)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 20])
plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal0.data[:, 20])
plt.xlabel('x')
plt.ylabel('Displacement')
plt.legend(['True', 'Identified'])
plt.title('TEST 0 - Time step: 20')
plt.subplot(10, 6, 38)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 20] - identified_output_signal0.data[:, 20])
plt.xlabel('x')
plt.ylabel('Error')
plt.legend(['Error'])
plt.title('TEST 0 - Time step: 20')
# plt.subplot(10, 6, 39)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 500])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal1.data[:, 500])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 1 - Time step: 500')
# plt.subplot(10, 6, 40)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 500] - identified_output_signal1.data[:, 500])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 1 - Time step: 500')
# plt.subplot(10, 6, 41)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 500])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal2.data[:, 500])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 2 - Time step: 500')
# plt.subplot(10, 6, 42)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 500] - identified_output_signal2.data[:, 500])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 2 - Time step: 500')
#
plt.subplot(10, 6, 43)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 30])
plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal0.data[:, 30])
plt.xlabel('x')
plt.ylabel('Displacement')
plt.legend(['True', 'Identified'])
plt.title('TEST 0 - Time step: 30')
plt.subplot(10, 6, 44)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 30] - identified_output_signal0.data[:, 30])
plt.xlabel('x')
plt.ylabel('Error')
plt.legend(['Error'])
plt.title('TEST 0 - Time step: 30')
# plt.subplot(10, 6, 45)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 1000])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal1.data[:, 1000])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 1 - Time step: 1000')
# plt.subplot(10, 6, 46)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 1000] - identified_output_signal1.data[:, 1000])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 1 - Time step: 1000')
# plt.subplot(10, 6, 47)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 1000])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal2.data[:, 1000])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 2 - Time step: 1000')
# plt.subplot(10, 6, 48)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 1000] - identified_output_signal2.data[:, 1000])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 2 - Time step: 1000')
#
plt.subplot(10, 6, 49)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 40])
plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal0.data[:, 40])
plt.xlabel('x')
plt.ylabel('Displacement')
plt.legend(['True', 'Identified'])
plt.title('TEST 0 - Time step: 40')
plt.subplot(10, 6, 50)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 40] - identified_output_signal0.data[:, 40])
plt.xlabel('x')
plt.ylabel('Error')
plt.legend(['Error'])
plt.title('TEST 0 - Time step: 40')
# plt.subplot(10, 6, 51)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 1500])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal1.data[:, 1500])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 1 - Time step: 1500')
# plt.subplot(10, 6, 52)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 1500] - identified_output_signal1.data[:, 1500])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 1 - Time step: 1500')
# plt.subplot(10, 6, 53)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 1500])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal2.data[:, 1500])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 2 - Time step: 1500')
# plt.subplot(10, 6, 54)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 1500] - identified_output_signal2.data[:, 1500])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 2 - Time step: 1500')
#
plt.subplot(10, 6, 55)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 50])
plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal0.data[:, 50])
plt.xlabel('x')
plt.ylabel('Displacement')
plt.legend(['True', 'Identified'])
plt.title('TEST 0 - Time step: 50')
plt.subplot(10, 6, 56)
plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal0.data[:, 50] - identified_output_signal0.data[:, 50])
plt.xlabel('x')
plt.ylabel('Error')
plt.legend(['Error'])
plt.title('TEST 0 - Time step: 50')
# plt.subplot(10, 6, 57)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 2000])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal1.data[:, 2000])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 1 - Time step: 2000')
# plt.subplot(10, 6, 58)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal1.data[:, 2000] - identified_output_signal1.data[:, 2000])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 1 - Time step: 2000')
# plt.subplot(10, 6, 59)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 2000])
# plt.plot(np.linspace(-0.5, 0.5, 101), identified_output_signal2.data[:, 2000])
# plt.xlabel('x')
# plt.ylabel('Displacement')
# plt.legend(['True', 'Identified'])
# plt.title('TEST 2 - Time step: 2000')
# plt.subplot(10, 6, 60)
# plt.plot(np.linspace(-0.5, 0.5, 101), true_output_signal2.data[:, 2000] - identified_output_signal2.data[:, 2000])
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.legend(['Error'])
# plt.title('TEST 2 - Time step: 2000')
#
plt.show()
#
#
#
plt.figure(num=2, figsize=[20, 6])

plt.subplot(3, 2, 1)
plt.plot(tspan, true_output_signal0.data[50, :])
plt.plot(tspan, identified_output_signal0.data[50, :])
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.legend(['True', 'Identified'], loc='lower right')
plt.title('TEST 0')
plt.subplot(3, 2, 2)
plt.plot(tspan, true_output_signal0.data[50, :] - identified_output_signal0.data[50, :])
plt.xlabel('Time')
plt.ylabel('Error')
plt.title('TEST 0')
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
plt.show()
#
#
#
#
plt.figure(num=3, figsize=[10, 8])

plt.semilogy(np.linspace(1, len(eraic0.Sigma[0]), len(eraic0.Sigma[0])), np.diag(eraic0.Sigma), '*')
plt.xlabel('# Singular Values')
plt.ylabel('Magnitude')
plt.title('TEST 0')

plt.show()








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