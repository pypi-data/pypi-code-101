"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy import signal

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

from ClassesDynamics.ClassDuffingOscillatorDynamics import DuffingOscillatorDynamics
from ClassesGeneral.ClassSystem import DiscreteLinearSystem, ContinuousNonlinearSystem, ContinuousLinearSystem
from ClassesGeneral.ClassSignal import OutputSignal, subtract2Signals, addSignals, ContinuousSignal, DiscreteSignal
from ClassesGeneral.ClassExperiments import Experiments
from ClassesSystemID.ClassMarkovParameters import *
from ClassesSystemID.ClassERA import ERAFromInitialConditionResponse, ERA
from ClassesSystemID.ClassMarkovParameters import OKIDObserverWithInitialCondition
from SystemIDAlgorithms.IdentificationInitialCondition import identificationInitialCondition
from SystemIDAlgorithms.GetMarkovParameters import getMarkovParameters
from SystemIDAlgorithms.GetInitialConditionResponseMarkovParameters import getInitialConditionResponseMarkovParameters
from Plotting.PlotEigenValues import plotEigenValues
from Plotting.PlotSignals import plotSignals
from Plotting.PlotSingularValues import plotSingularValues
from Plotting.PlotMarkovParameters2 import plotMarkovParameters2
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck


## Parameters for Dynamics
def delta(t):
    return 0.2 + 0.2*np.sin(2*np.pi*2*t)
    # return 0.2
def alpha(t):
    return  1 + 0.5*np.sin(2*np.pi*3*t + np.pi/2)
    # return 1
def beta(t):
    return  -1 + 0.5*np.sin(2*np.pi*4*t + np.pi)
    # return 0
dt = 0.1



## Parameters
frequency = 10
total_time = 20
number_steps = int(total_time * frequency) + 1
tspan = np.linspace(0, total_time, number_steps)


## Test
r = 2
total_time_test = total_time - r / frequency
number_steps_test = number_steps - r
tspan_test = np.linspace(0, total_time_test, number_steps_test)



## Import Dynamics
dynamics = DuffingOscillatorDynamics(delta, alpha, beta)



## Nominal System
system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.array([0.1, -0.2]), 0)], 'Nominal System', dynamics.F, dynamics.G)
dynamics2 = DuffingOscillatorDynamics(delta, alpha, beta, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, total_time, frequency), nominal_u=DiscreteSignal(dynamics.input_dimension, total_time, frequency), dt=1/frequency)
# system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.array([0.1, -0.2]), 0)], 'Nominal System', lambda t: dynamics2.A(0), lambda t: dynamics2.B(0), lambda t: dynamics2.C(0), lambda t: dynamics2.D(0))
# system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.array([0.1, -0.2]), 0)], 'Nominal System', dynamics2.A, dynamics2.B, dynamics2.C, dynamics2.D)


## Input
zoh = 0.1*np.random.randn(number_steps)
def u(t):
    if type(t) == np.ndarray:
        return zoh
    else:
        return zoh[int(t * frequency)]
input_signal_d = DiscreteSignal(dynamics.input_dimension, total_time_test, frequency, signal_shape='External', data=zoh)
input_signal = ContinuousSignal(dynamics.input_dimension, signal_shape='External', u=u)
output_signal = OutputSignal(input_signal_d, system, tspan=tspan_test)
# output_signal = OutputSignal(input_signal_d, system2, tspan=tspan_test)


#
# # Update dynamics with nominal trajectory
# dynamics = DuffingOscillatorDynamics(delta, alpha, beta, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, total_time, frequency, signal_shape='External', data=output_signal.state), nominal_u=DiscreteSignal(dynamics.input_dimension, total_time, frequency, signal_shape='External', data=input_signal.u(tspan)), dt=1/frequency)
# output_signal_test = OutputSignal(input_signal, system, tspan=tspan_test)
# input_signal_test = DiscreteSignal(dynamics.input_dimension, total_time, frequency, signal_shape='External', data=u(tspan_test))
# Sys = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.array([0.1, -0.2]), 0)], 'Nominal System', dynamics.A, dynamics.B, dynamics.C, dynamics.D)
# output_signal2 = OutputSignal(input_signal_test, Sys, tspan=tspan_test)

## OKID
deadbeat_order = 4
number_to_calculate = 500
okid = OKIDObserverWithInitialCondition(input_signal_d, output_signal, deadbeat_order, number_to_calculate)


## Calculate Markov Parameters and Identified system
era = ERA(okid.markov_parameters, dynamics.state_dimension, p=20)


## Define Identified System
x0 = identificationInitialCondition(input_signal_d, output_signal, era.A, era.B, era.C, era.D, 0, 20)
SysID = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(x0, 0)], 'Identified System', era.A, era.B, era.C, era.D)

## Input test
def u_testf(t):
    return signal.square(0.2 * np.pi * t)
u_test = ContinuousSignal(dynamics.input_dimension, signal_shape='External', u=u_testf)
u_test_d = DiscreteSignal(dynamics.input_dimension, total_time_test, frequency, signal_shape='External', data=signal.square(0.2 * np.pi * tspan_test))


## Define the Identified Output Signal
S2 = OutputSignal(u_test_d, system)
# S2 = OutputSignal(u_test, system, tspan=tspan_test)
S2ID = OutputSignal(u_test_d, SysID)



# ## Plotting
# plotSignals([[S2, S2ID], [subtract2Signals(S2, S2ID)]], 2)
# # plotEigenValues([system, SysID], 2)
# plotSingularValues([era], ['IdentifiedSystem'], 3)
# # plotMarkovParameters2(markov_parameters, markov_parameters_true, 'OKID', 'True', 4)



system_corrected = correctSystemForEigenvaluesCheck(system, number_steps_test, r)
systemID_corrected = correctSystemForEigenvaluesCheck(SysID, number_steps_test, r)







plt.figure(num=2, figsize=[5, 5])
plt.plot(S2.data[0, :], S2.data[1, :], color=colors[0])
plt.plot(S2ID.data[0, :], S2ID.data[1, :], color=colors[6], linestyle='-.')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['True', 'Identified'])
plt.tight_layout()
# plt.savefig('Phase_plot_case_2.eps', format='eps')
plt.show()

plt.figure(num=3, figsize=[5, 2])
plt.plot(tspan_test, np.linalg.norm(S2.data - S2ID.data, axis=0), color=colors[7])
plt.xlabel('Time [sec]')
plt.ylabel('Error')
plt.tight_layout()
# plt.savefig('Error_case_2.eps', format='eps')
plt.show()




plt.figure(num=3, figsize=[3, 3])
plt.scatter(np.real(np.linalg.eig(system_corrected.A(0))[0]), np.imag(np.linalg.eig(system_corrected.A(0))[0]), color=colors[0])
plt.scatter(np.real(np.linalg.eig(systemID_corrected.A(0))[0]), np.imag(np.linalg.eig(systemID_corrected.A(0))[0]), color=colors[6], facecolors='none')
plt.legend(['True', 'Identified'], loc='best')
plt.xlabel('Real part of eigenvalues')
plt.ylabel('Imaginary part of eigenvalues')
plt.tight_layout()
plt.savefig('Eigenvalues_case_1.eps', format='eps')
plt.show()







