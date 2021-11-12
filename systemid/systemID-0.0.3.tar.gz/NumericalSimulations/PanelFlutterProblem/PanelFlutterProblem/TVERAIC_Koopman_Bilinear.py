"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Date: November 2021
Python: 3.7.7
"""



import numpy as np
import scipy.linalg as LA

from SystemIDAlgorithms.GetObservabilityMatrix import getObservabilityMatrix
from ClassesDynamics.ClassPanelFlutterDynamics import PanelFlutterDynamics3
from SystemIDAlgorithms.DepartureDynamics import departureDynamicsFromInitialConditionResponse
from ClassesGeneral.ClassSystem import ContinuousNonlinearSystem, DiscreteLinearSystem, ContinuousLinearSystem, ContinuousBilinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, DiscreteSignal, OutputSignal, addSignals, subtract2Signals
from Plotting.PlotSignals import plotSignals
from ClassesGeneral.ClassExperiments import Experiments
from Plotting.PlotEigenValues import plotHistoryEigenValues1System
from SystemIDAlgorithms.GetOptimizedHankelMatrixSize import getOptimizedHankelMatrixSize
from Plotting.PlotEigenValues import plotHistoryEigenValues2Systems
from ClassesSystemID.ClassERA import TVERAFromInitialConditionResponse
from SystemIDAlgorithms.CorrectSystemForEigenvaluesCheck import correctSystemForEigenvaluesCheck
from NumericalSimulations.PanelFlutterProblem.PanelFlutterProblem.PlotFormating import plotResponse3, plotEigenValues, plotSVD
from SystemIDAlgorithms.CreateAugmentedSignal import createAugmentedSignalPolynomialBasisFunctions, createAugmentedSignalWithGivenFunctions




## Parameters for Dynamics
print('Define Parameters')
def RT(t):
    return 0 + 0 * t
def mu(t):
    return 0.01 + 0 * t
def M(t):
    return 5 + 0 * t
def l(t):
    return 280 + 0 * t
#  + 20 * np.sin(2 * np.pi * 2 * t)


## Import Dynamics
print('Import Dynamics')
dynamics = PanelFlutterDynamics3(RT)
input_dimension = dynamics.input_dimension
output_dimension = dynamics.output_dimension
state_dimension = dynamics.state_dimension



## Parameters for identification
total_time = 2
frequency = 20
dt = 1 / frequency
number_steps = int(total_time * frequency) + 1
tspan = np.linspace(0, total_time, number_steps)
assumed_order = 4
p = 4




## Create System
print('Create Nominal System')
initial_states = [(np.array([0, 0.001, 0, 0]), 0)]
nominal_system = ContinuousNonlinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System', dynamics.F, dynamics.G)



## Nominal Input Signal
print('Create Nominal Input Signal')
def u_nominal(t):
    return np.array([l(t), np.sqrt(l(t) * mu(t) / M(t))])
nominal_input_signal = ContinuousSignal(dynamics.input_dimension, signal_shape='External', u=u_nominal)
nominal_input_signal_d = DiscreteSignal(dynamics.input_dimension, total_time, frequency, signal_shape='External', data=u_nominal(tspan))
true_output = OutputSignal(nominal_input_signal, nominal_system, tspan=tspan)




## Experiments
N1 = 20
N2 = 10
mean = np.array([280, 0.75])
covariance = np.array([[20, 0], [0, 0.01]])
random_inputs_1 = np.zeros([input_dimension, number_steps + 500, N1])
random_inputs_2 = np.zeros([input_dimension, number_steps + 500, N2, N2])
random_inputs_1[:, 0, :] = mean[:, np.newaxis] + np.matmul(LA.sqrtm(covariance), np.random.randn(input_dimension, N1))
for i in range(N2):
    random_input = random_inputs_1[:, 0, i]
    random_inputs_2[:, 0, :, i] = random_inputs_1[:, 0, 0:N2]
    random_inputs_2[:, 1, :, i] = np.outer(random_input, np.ones(N2))
inputs_1 = []
inputs_2 = []
systems = []

for i in range(N1):
    def make_u1(i):
        def u(t):
            if type(t) == np.ndarray:
                return random_inputs_1[:, :-500, i]
            else:
                return random_inputs_1[:, int(t * frequency), i]
        return u
    inputs_1.append(ContinuousSignal(input_dimension, signal_shape='External', u=make_u1(i)))
    systems.append(nominal_system)

for i in range(N2):
    inputs_2.append([])
    for j in range(N2):
        def make_u2(i, j):
            def u(t):
                if type(t) == np.ndarray:
                    return random_inputs_2[:, :-500, j, i]
                else:
                    return random_inputs_2[:, int(t * frequency), j, i]
            return u
        inputs_2[-1].append(ContinuousSignal(input_dimension, signal_shape='External', u=make_u2(i, j)))

experiments_1 = Experiments(systems, inputs_1, tspan=tspan)
experiments_2 = []
for i in range(N2):
    experiments_2.append(Experiments(systems, inputs_2[i], tspan=tspan))

for i in range(experiments_1.number_experiments):
    experiments_1.input_signals[i] = DiscreteSignal(input_dimension, total_time, frequency, signal_shape='External', data=experiments_1.input_signals[i].u(tspan))
for i in range(N2):
    for j in range(experiments_2[i].number_experiments):
        experiments_2[i].input_signals[j] = DiscreteSignal(input_dimension, total_time, frequency, signal_shape='External', data=experiments_2[i].input_signals[j].u(tspan))



# ## Departure Dynamics
# for i in range(experiments_1.number_experiments):
#     experiments_1.output_signals[i] = subtract2Signals(experiments_1.output_signals[i], true_output)
#     experiments_1.input_signals[i] = subtract2Signals(experiments_1.input_signals[i], nominal_input_signal_d)
# for i in range(N2):
#     for j in range(experiments_2[i].number_experiments):
#         experiments_2[i].output_signals[j] = subtract2Signals(experiments_2[i].output_signals[j], true_output)
#         experiments_2[i].input_signals[j] = subtract2Signals(experiments_2[i].input_signals[j], nominal_input_signal_d)


## Departure Dynamics
cst = DiscreteSignal(output_dimension, total_time, frequency, signal_shape='External', data=np.outer(np.array([0, 0.001, 0, 0]), np.ones(number_steps)))
for i in range(experiments_1.number_experiments):
    experiments_1.output_signals[i] = subtract2Signals(experiments_1.output_signals[i], cst)
for i in range(N2):
    for j in range(experiments_2[i].number_experiments):
        experiments_2[i].output_signals[j] = subtract2Signals(experiments_2[i].output_signals[j], cst)





## Identification of D
Y0_N1 = np.zeros([output_dimension, N1])
V0_N1 = np.zeros([input_dimension, N1])

for i in range(N1):
    Y0_N1[:, i] = experiments_1.output_signals[i].data[:, 0]
    V0_N1[:, i] = experiments_1.input_signals[i].data[:, 0]
D1 = np.matmul(Y0_N1, LA.pinv(V0_N1))



## Identification of C and A
Y11 = np.zeros([(p) * output_dimension, N1])
Y12 = np.zeros([(p) * output_dimension, N1])
Y21 = np.zeros([(p) * output_dimension, N2])
for i in range(p):
    for j in range(N1):
        Y11[i * output_dimension:(i + 1) * output_dimension, j] = experiments_1.output_signals[j].data[:, i + 1]
    for j in range(N1):
        Y12[i * output_dimension:(i + 1) * output_dimension, j] = experiments_1.output_signals[j].data[:, i + 2]
(R1, sigma1, St1) = LA.svd(Y11)
Sigma1 = np.diag(sigma1)
Rn1 = R1[:, 0:state_dimension]
Snt1 = St1[0:state_dimension, :]
Sigman1 = Sigma1[0:state_dimension, 0:state_dimension]
O1 = np.matmul(Rn1, LA.sqrtm(Sigman1))
X1 = np.matmul(LA.sqrtm(Sigman1), Snt1)
C = O1[0:output_dimension, :]
def C_id(tk):
    return C
AA = np.matmul(LA.pinv(O1), np.matmul(Y12, LA.pinv(X1)))
Ac = LA.logm(AA) / dt




## Identification of Nc

LAA = np.zeros([state_dimension, N2 * state_dimension])

for i in range(N2):
    Y22 = np.zeros([(p) * output_dimension, N2])
    for j in range(N2):
        for k in range(p):
            Y22[k * output_dimension:(k + 1) * output_dimension, j] = experiments_2[i].output_signals[j].data[:, k + 2]

    P = Y22 - np.matmul(O1, np.outer(X1[:, i:i+1], np.ones(N2)))

    LAA[:, i*state_dimension:(i + 1)*state_dimension] = LA.logm(np.matmul(LA.pinv(O1), np.matmul(P, LA.pinv(X1[:, 0:N2])))) / dt - Ac

CR = np.kron(V0_N1[:, 0:N2], np.eye(state_dimension))
CR_inv = LA.pinv(CR)
Nc = np.matmul(LAA, CR_inv)


## Identification of Bc

Z = np.zeros([2*state_dimension, 2*state_dimension])
Coeff = np.zeros([state_dimension * N1, input_dimension * state_dimension])
ytil = np.zeros([state_dimension * N1])

for i in range(N1):
    Z[0:state_dimension, 0:state_dimension] = Ac
    for j in range(input_dimension):
        Z[0:state_dimension, 0:state_dimension] += Nc[:, j*state_dimension:(j+1)*state_dimension] * V0_N1[j, i]
    Z[0:state_dimension, state_dimension:2*state_dimension] = np.eye(state_dimension)
    eZ = LA.expm(Z * dt)
    G = eZ[0:state_dimension, state_dimension:2*state_dimension]
    Coeff[i*state_dimension:(i+1)*state_dimension, :] = np.kron(V0_N1[:, i:i+1].T, G)
    ytil[i*state_dimension:(i+1)*state_dimension] = X1[:, i]

VecBchat = np.matmul(LA.pinv(Coeff), ytil)
Bchat = np.reshape(VecBchat, [input_dimension, state_dimension]).T


## Identified system
def A_id(t):
    return Ac
def N_id(t):
    return Nc
def B_id(t):
    return Bchat
def C_id(t):
    return C
def D_id(t):
    return D1



x0 = np.zeros(state_dimension)
x0_id = x0
identified_system = ContinuousBilinearSystem(state_dimension, input_dimension, output_dimension, [(x0_id, 0)], 'Identified system', A_id, N_id, B_id, C_id, D_id)



identified_output = addSignals([OutputSignal(nominal_input_signal, identified_system, tspan=tspan), cst])

plotSignals([[true_output, identified_output], [subtract2Signals(true_output, identified_output)]], 1, percentage=0.8)




# ## Linearization
# print('Create Linearized System')
# dynamics = PanelFlutterDynamics3(RT, tspan=tspan, nominal_x=DiscreteSignal(dynamics.state_dimension, total_time, frequency, signal_shape='External', data=nominal_output_signal.state), nominal_u=nominal_input_signal_d, dt=1/frequency)
# initial_states = [(np.array([0, 0.0001, 0, 0]), 0)]
# linearized_system = ContinuousLinearSystem(dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, initial_states, 'Nominal System Discrete', dynamics.Ac, dynamics.Bc, dynamics.C, dynamics.D)


# ## Deviated Input Signal
# print('Create Deviated Input Signal')
# def u_deviated(t):
#     return 0.01 * np.array([l(t), np.sqrt(l(t) * mu(t) / M(t))])
# deviated_input_signal = ContinuousSignal(dynamics.input_dimension, signal_shape='External', u=u_deviated)
#
#
# ## Output Signal from Linearized System
# print('Create Deviated Output Signal from Linearization')
# deviated_output_signal = OutputSignal(deviated_input_signal, linearized_system, tspan=tspan)
# true_output_from_linearization = addSignals([nominal_output_signal, deviated_output_signal])
#
#
# ## True Input
# print('Create True Input Signal')
# def u(t):
#     return u_nominal(t) + u_deviated(t)
# true_input_signal = ContinuousSignal(dynamics.input_dimension, signal_shape='External', u=u)
#
#
# ## True Output Signal
# print('Create True Output Signal')
# true_output_signal = OutputSignal(true_input_signal, nominal_system, tspan=tspan)
#
#
# ## PLot Signals
# plotSignals([[nominal_output_signal, true_output_signal, true_output_from_linearization]], 1)









