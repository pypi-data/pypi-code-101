"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np
import random
from scipy import linalg as LA
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import rc
from numpy.linalg import matrix_power
import scipy.io

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
from ClassesGeneral.ClassSignal import DiscreteSignal, OutputSignal, subtract2Signals
from ClassesSystemID.ClassERA import ERAFromInitialConditionResponse
from SystemIDAlgorithms.GetObserverGainMatrix import getObserverGainMatrix
from Plotting.PlotSingularValues import plotSingularValues



## Import Data
data_file = scipy.io.loadmat('data.mat')
tspan = data_file['t'].T[0]



## Dimension
output_dimension = 1



## Frequency and total time
frequency = 1
total_time = 2047
number_steps = round(total_time * frequency + 1)



## Zero input
input_signal = DiscreteSignal(1, total_time, frequency)



## Output Signals
output_signal1 = DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=data_file['y'].T[0, :])
output_signal2 = DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=data_file['y'].T[1, :])
output_signal3 = DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=data_file['y'].T[2, :])
output_signal4 = DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=data_file['y'].T[3, :])
output_signal5 = DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=data_file['y'].T[4, :])
output_signals = [output_signal1, output_signal2]



## Parameters for identification
assumed_order = 20
p = 500
q = p



## ERA
era = ERAFromInitialConditionResponse(output_signals, assumed_order, 1, p=p)



## Identified System
identified_system = DiscreteLinearSystem(frequency, assumed_order, 1, output_dimension, [(era.x0[:, 0], 0)], 'Nominal System Experiment', era.A, era.B, era.C, era.D)



## Identified Signals
output_signal_identified1 = OutputSignal(input_signal, identified_system)


## Plotting
#plotSignals([[output_signal1, output_signal_identified1]], 1)
plt.plot(tspan, output_signal1.data[0, :] - output_signal_identified1.data[0, :])
plt.show()


plotSingularValues([era], 'f', 2)