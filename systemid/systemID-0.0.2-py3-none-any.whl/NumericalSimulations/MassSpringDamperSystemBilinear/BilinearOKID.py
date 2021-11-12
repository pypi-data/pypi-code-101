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
import matplotlib.pyplot as plt

from ClassesDynamics.ClassMassSpringDamperDynamics import MassSpringDamperDynamicsBilinear
from ClassesGeneral.ClassSystem import ContinuousBilinearSystem
from ClassesGeneral.ClassSignal import ContinuousSignal, OutputSignal, DiscreteSignal, subtract2Signals
from Plotting.PlotSignals import plotSignals
from ClassesGeneral.ClassExperiments import Experiments



## Parameters
mass = 1
damping_coefficient = 0.5
measurements = ['position']
dynamics = MassSpringDamperDynamicsBilinear(mass, damping_coefficient, measurements)


# def A(t):
#     return np.array([[0, 1], [0, 0]])
# def N(t):
#     return np.array([[0, 0], [-1, 0]])
# def B(t):
#     return np.array([[0], [-3]])
#     # return np.eye(2)
# def C(t):
#     # return np.array([[0, 1]])
#     return np.eye(2)
# def D(t):
#     return np.array([[0], [0]])
#
#
# def A(t):
#     return np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 3]])
# def N(t):
#     return np.array([[1, -1, 0, 0, 0, 1], [0, 2, 1, 1, 0, 1], [1, 3, 4, 4, 2, 1]])
# def B(t):
#     return np.array([[1, 0], [0, 2], [1, 1]])
# def C(t):
#     return np.array([[1, 0, 1], [-1, 1, 2]])
# def D(t):
#     return np.array([[0, 0], [0, 0]])



def A(t):
    return np.array([[-1, 0], [1, -2]])
def N(t):
    return np.array([[0, 0, 1, 1], [1, 1, 0, 0]])
def B(t):
    return np.array([[1, 0], [0, 1]])
    # return np.eye(2)
def C(t):
    return np.array([[0, 1]])
def D(t):
    return np.array([[0, 0]])



## Identification parameters
input_dimension = 2
output_dimension = 1
state_dimension = 2
p = 10



## Signal parameters
total_time = 5
frequency = 20
dt = 1 /frequency
number_steps = total_time * frequency + 1
tspan = np.linspace(0, total_time, number_steps)



## Create System
x0 = np.zeros(state_dimension)
# x0 = 0.1 * np.random.randn(state_dimension)
system = ContinuousBilinearSystem(state_dimension, input_dimension, output_dimension, [(x0, 0)], 'Nominal system', dynamics.A, dynamics.N, dynamics.B, dynamics.C, dynamics.D)
def u(t):
    # return np.array([0.1 * np.sin(7*t)])
    return np.array([0.1 * np.sin(7*t), 0.1 * np.cos(10*t)])
test_signal = ContinuousSignal(input_dimension, signal_shape='External', u=u)
true_output = OutputSignal(test_signal, system, tspan=tspan)




## Experiments
N1 = 10
N2 = 5
random_inputs_1 = 0.1*np.zeros([input_dimension, number_steps + 500, N1])
random_inputs_2 = 0.1*np.zeros([input_dimension, number_steps + 500, N2, N2])
random_inputs_1[:, 0, :] = np.random.randn(input_dimension, N1)
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
    systems.append(system)

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
print('Error A:', LA.norm(LA.eig(Ac)[0] - LA.eig(dynamics.A(0))[0]))



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
for i in range(input_dimension):
    print('Error N' + str(i+1) + ':', LA.norm(LA.eig(Nc[:, i*state_dimension:(i+1)*state_dimension])[0] - LA.eig(dynamics.N(0)[:, i*state_dimension:(i+1)*state_dimension])[0]))



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

x0_id = x0
identified_system = ContinuousBilinearSystem(state_dimension, input_dimension, output_dimension, [(x0_id, 0)], 'Identified system', A_id, N_id, B_id, C_id, D_id)

## Test
identified_output = OutputSignal(test_signal, identified_system, tspan=tspan)

plotSignals([[true_output, identified_output], [subtract2Signals(true_output, identified_output)]], 1)



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

# plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
# rc('text', usetex=True)

## Plot input and output Training
fig = plt.figure(num=1, figsize=[12, 9])
ax = fig.add_subplot(3, 1, 1)
ax.plot(tspan, u(tspan)[0, :], color=colors[0], label='u1')
ax.plot(tspan, u(tspan)[1, :], color=colors[1], label='u2')
plt.xlabel('Time [sec]')
plt.ylabel('Input')
ax = fig.add_subplot(3, 1, 2)
ax.plot(tspan, true_output.data[0, :], color=colors[5], label='True')
ax.plot(tspan, identified_output.data[0, :], '--', color=colors[7], label='Identified')
plt.xlabel('Time [sec]')
plt.ylabel('Output')
plt.legend(loc='upper right')
ax = fig.add_subplot(3, 1, 3)
ax.plot(tspan, subtract2Signals(true_output, identified_output).data[0, :], color=colors[9])
plt.xlabel('Time [sec]')
plt.ylabel('Error')
plt.show()


# Plot SVD
plt.figure(num=2, figsize=[4, 4])
plt.semilogy(np.linspace(1, 10, 10), np.diag(Sigma1), '.', color=colors[7])
plt.xlabel('Number of singular values')
plt.ylabel('Magnitude of singular values')
plt.title('Singular value plot')
plt.show()