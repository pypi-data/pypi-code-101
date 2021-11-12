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
from ClassesGeneral.ClassSignal import OutputSignal, subtract2Signals, addSignals, ContinuousSignal, DiscreteSignal
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

from SystemIDAlgorithms.CreateAugmentedSignal import createAugmentedSignalPolynomialBasisFunctions, createAugmentedSignalWithGivenFunctions


## Parameters for Dynamics
def mu(t):
    # return -0.5 + 1.5*np.sin(2*np.pi*2*t)
    return -0.5
def l(t):
    # return -0.2 + 0.5*np.cos(2*np.pi*3*t)
    return -0.2



## Parameters
frequency = 20
dt = 1 / frequency
total_time = 5
number_steps = int(total_time * frequency) + 1
tspan = np.linspace(0, total_time, number_steps)



## Import Dynamics
dynamics = SlowManifoldDecoupledSystemDynamics(mu, l)



## Nominal System
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(np.array([0, 0]), 0)], 'Nominal System', dynamics.F, dynamics.G)
nominal_input_signal = ContinuousSignal(dynamics.input_dimension, 'Nominal Input Signal')
nominal_output_signal = OutputSignal(nominal_input_signal, nominal_system, 'Nominal Output Signal', tspan=tspan)



## Input signal
number_experiments = 1
systems = []
initial_states = []
input_signals = []
for i in range(number_experiments):
    init_state = [(np.array([0.5, 0.75]), 0)]
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



## Koopman
order = 2
max_order = 2
for i in range(Exp.number_experiments):
    #Exp.output_signals[i] = createAugmentedSignalPolynomialBasisFunctions(Exp.output_signals[i], order, True, max_order)
    Exp.output_signals[i] = createAugmentedSignalWithGivenFunctions(Exp.output_signals[i], [lambda x: x[0] ** 2])

Exp.output_dimension = Exp.output_signals[0].dimension

## Calculate Markov Parameters and Identified system
ERA1 = ERAFromInitialConditionResponse(Exp.output_signals, 3, dynamics.input_dimension)




## Define Identified System
SysID = DiscreteLinearSystem(frequency, Exp.output_dimension, dynamics.input_dimension, Exp.output_dimension, [(ERA1.x0[:, 0], 0)], 'Identified System', ERA1.A, ERA1.B, ERA1.C, ERA1.D)


## Define the Identified Output Signal
S2ID = OutputSignal(DiscreteSignal(dynamics.input_dimension, 'Zero Input', total_time, frequency), SysID, 'Identified Output Signal')



# ## Plotting
plotSignals([[Exp.output_signals[0], S2ID], [subtract2Signals(Exp.output_signals[0], S2ID)]], 2)
plotEigenValues([Sys, SysID], 2)
plotSingularValues([ERA1], ['IdentifiedSystem'], 3)
# plotMarkovParameters2(markov_parameters, markov_parameters_true, 'OKID', 'True', 4)



