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


from ClassesDynamics.ClassPointMassInRotatingTubeDynamics import PointMassInRotatingTubeDynamics
from ClassesGeneral.ClassSystem import DiscreteLinearSystem
from SystemIDAlgorithms.IdentificationInitialCondition import identificationInitialCondition
from ClassesSystemID.ClassMarkovParameters import OKIDObserver, OKIDObserverWithInitialCondition
from ClassesGeneral.ClassSignal import DiscreteSignal, OutputSignal, subtract2Signals, add2Signals
from ClassesSystemID.ClassERA import ERA
from SystemIDAlgorithms.GetObserverGainMatrix import getObserverGainMatrix



## Dynamics
dt = 0.1
mass = 1
spring_constant = 10
def theta_dot(t):
    return 0.5
dynamics = PointMassInRotatingTubeDynamics(dt, mass, spring_constant, theta_dot)


## Initial Condition
x0 = np.zeros(dynamics.state_dimension)
# x0 = np.random.randn(dynamics.state_dimension)


## Frequency and total time
frequency = 10
total_time = 50
total_time_training = 20
number_steps = round(total_time * frequency + 1)
number_steps_training = round(total_time_training * frequency + 1)
tspan = np.linspace(0, total_time, number_steps)
tspan_training = np.linspace(0, total_time_training, number_steps_training)


## System
nominal_system = DiscreteLinearSystem(frequency, dynamics.state_dimension, dynamics.input_dimension, dynamics.output_dimension, [(x0, 0)], 'Nominal System', lambda t: dynamics.A(0), lambda t: dynamics.B(0), lambda t: dynamics.C(0), lambda t: dynamics.D(0))


## Input Signals
gaussian_input_signal = DiscreteSignal(dynamics.input_dimension, 'Gaussian Input Signal', total_time, frequency, signal_shape='White Noise', covariance=np.array([[0.1**2]]))
square_wave_input_signal = DiscreteSignal(dynamics.input_dimension, 'Square Wave Input Signal', total_time, frequency, signal_shape='External', data=signal.square(2 * np.pi * 5 * tspan))
cosine_wave_input_signal = DiscreteSignal(dynamics.input_dimension, 'Cosine Wave Input Signal', total_time, frequency, signal_shape='External', data=np.cos(2 * np.pi * 2 * tspan))


## Output Signals
gaussian_output_signal = OutputSignal(gaussian_input_signal, nominal_system, 'Gaussian Output Signal')
square_wave_output_signal = OutputSignal(square_wave_input_signal, nominal_system, 'Square Output Signal')
cosine_wave_output_signal = OutputSignal(cosine_wave_input_signal, nominal_system, 'Cosine Output Signal')



## Parameters for identification
assumed_order = 2
p = 20
q = p
deadbeat_order = 10
number_system_markov_parameters = 500


## Noise
# sigma = 0.001
# noise = DiscreteSignal(dynamics.input_dimension, 'Noise', total_time, frequency, signal_shape='White Noise', covariance=np.array([[sigma**2]]))
# gaussian_output_signal = add2Signals(gaussian_output_signal, noise)


## Input Signal for training
gaussian_input_signal_training = DiscreteSignal(dynamics.input_dimension, 'Gaussian Input Signal Training', total_time_training, frequency, signal_shape='External', data=gaussian_input_signal.data[:, 0:number_steps_training])


## Output Signal for training
gaussian_output_signal_training = DiscreteSignal(dynamics.output_dimension, 'Gaussian Output Signal Training', total_time_training, frequency, signal_shape='External', data=gaussian_output_signal.data[:, 0:number_steps_training])


## OKID
okid = OKIDObserver(gaussian_input_signal_training, gaussian_output_signal_training, deadbeat_order, number_system_markov_parameters)
# okid = OKIDObserverWithInitialCondition(gaussian_input_signal_training, gaussian_output_signal_training, deadbeat_order, number_system_markov_parameters)


## ERA
era = ERA(okid.markov_parameters, assumed_order, p=p)


## Identified System
identified_x0 = np.zeros(assumed_order)
# identified_x0 = identificationInitialCondition(gaussian_input_signal, gaussian_output_signal, era.A, era.B, era.C, era.D, 0, 10)
identified_system = DiscreteLinearSystem(frequency, assumed_order, dynamics.input_dimension, dynamics.output_dimension, [(identified_x0, 0)], 'Nominal System', era.A, era.B, era.C, era.D)


## Identified Signals
gaussian_output_signal_identified = OutputSignal(gaussian_input_signal, identified_system, 'Gaussian Output Signal Identified')
square_wave_output_signal_identified = OutputSignal(square_wave_input_signal, identified_system, 'Square Output Signal Identified')
cosine_wave_output_signal_identified = OutputSignal(cosine_wave_input_signal, identified_system, 'Cosine Output Signal Identified')


## Observer Gain Matrix
G, O, Yo = getObserverGainMatrix(era.A, era.C, okid.observer_gain_markov_parameters, 0, dt, 20)


## State Estimation
x_gaussian_estimated = np.zeros([assumed_order, number_steps + 1])
y_gaussian_estimated = np.zeros([dynamics.output_dimension, number_steps])
x_square_wave_estimated = np.zeros([assumed_order, number_steps + 1])
y_square_wave_estimated = np.zeros([dynamics.output_dimension, number_steps])
x_cosine_wave_estimated = np.zeros([assumed_order, number_steps + 1])
y_cosine_wave_estimated = np.zeros([dynamics.output_dimension, number_steps])
x_gaussian_estimated[:, 0] = np.random.randn(assumed_order)
x_square_wave_estimated[:, 0] = np.random.randn(assumed_order)
x_cosine_wave_estimated[:, 0] = np.random.randn(assumed_order)
for i in range(0, number_steps):
    y_gaussian_estimated[:, i] = np.matmul(era.C(0), x_gaussian_estimated[:, i]) + np.matmul(era.D(0), gaussian_input_signal.data[:, i])
    x_gaussian_estimated[:, i + 1] = np.matmul(era.A(0), x_gaussian_estimated[:, i]) + np.matmul(era.B(0), gaussian_input_signal.data[:, i]) - np.matmul(G, gaussian_output_signal_identified.data[:, i] - y_gaussian_estimated[:, i])
    y_square_wave_estimated[:, i] = np.matmul(era.C(0), x_square_wave_estimated[:, i]) + np.matmul(era.D(0), square_wave_input_signal.data[:, i])
    x_square_wave_estimated[:, i + 1] = np.matmul(era.A(0), x_square_wave_estimated[:, i]) + np.matmul(era.B(0), square_wave_input_signal.data[:, i]) - np.matmul(G, square_wave_output_signal_identified.data[:, i] - y_square_wave_estimated[:, i])
    y_cosine_wave_estimated[:, i] = np.matmul(era.C(0), x_cosine_wave_estimated[:, i]) + np.matmul(era.D(0), cosine_wave_input_signal.data[:, i])
    x_cosine_wave_estimated[:, i + 1] = np.matmul(era.A(0), x_cosine_wave_estimated[:, i]) + np.matmul(era.B(0), cosine_wave_input_signal.data[:, i]) - np.matmul(G, cosine_wave_output_signal_identified.data[:, i] - y_cosine_wave_estimated[:, i])




## Plotting

# Plot input and output Training
fig = plt.figure(num=1, figsize=[12, 6])
ax = fig.add_subplot(2, 2, 1)
ax.plot(tspan_training, gaussian_input_signal_training.data[0, :], color=colors[0])
plt.xlabel('Time [sec]')
plt.ylabel('Input')
plt.title('Training')
ax = fig.add_subplot(2, 2, 3)
ax.plot(tspan_training, gaussian_output_signal_training.data[0, :], color=colors[1])
plt.xlabel('Time [sec]')
plt.ylabel('Position')
plt.title('Training')
ax = fig.add_subplot(2, 2, 4)
ax.plot(tspan_training, gaussian_output_signal_training.data[1, :], color=colors[1])
plt.xlabel('Time [sec]')
plt.ylabel('Velocity')
plt.title('Training')
plt.show()


# Plot SVD
plt.figure(num=2, figsize=[4, 4])
plt.semilogy(np.linspace(1, np.min((p * dynamics.output_dimension, q * dynamics.input_dimension)), np.min((p * dynamics.output_dimension, q * dynamics.input_dimension))), np.diag(era.Sigma), '.', color=colors[7])
plt.xlabel('Number of singular values')
plt.ylabel('Magnitude of singular values')
plt.title('SVD Plot')
plt.show()


# Check Eigenvalues
plt.figure(num=3, figsize=[4, 4])
plt.scatter(np.real(LA.eig(dynamics.A(0))[0]), np.imag(LA.eig(dynamics.A(0))[0]), color=colors[1])
plt.scatter(np.real(LA.eig(era.A(0))[0]), np.imag(LA.eig(era.A(0))[0]), color=colors[4], facecolors='none')
plt.legend(['True', 'Identified'], loc='best')
plt.xlabel('Real part of eigenvalues')
plt.ylabel('Imaginary part of eigenvalues')
plt.title('Eigenvalues Plot')
plt.show()


# Plot input and output Training
fig = plt.figure(num=4, figsize=[12, 18])

ax = fig.add_subplot(6, 2, 1)
ax.plot(tspan, gaussian_output_signal.data[0, :], color=colors[1])
ax.plot(tspan, gaussian_output_signal_identified.data[0, :], color=colors[4], linestyle='-.')
plt.ylabel('Position')
plt.legend(['True', 'Identified'])
plt.title('Gaussian Input')
ax = fig.add_subplot(6, 2, 2)
ax.plot(tspan, gaussian_output_signal.data[1, :], color=colors[1])
ax.plot(tspan, gaussian_output_signal_identified.data[1, :], color=colors[4], linestyle='-.')
plt.ylabel('Velocity')
plt.legend(['True', 'Identified'])
plt.title('Gaussian Input')
ax = fig.add_subplot(6, 2, 3)
ax.plot(tspan, gaussian_output_signal.data[0, :] - gaussian_output_signal_identified.data[0, :], color=colors[7])
plt.ylabel('Error Position')
ax = fig.add_subplot(6, 2, 4)
ax.plot(tspan, gaussian_output_signal.data[1, :] - gaussian_output_signal_identified.data[1, :], color=colors[7])
plt.ylabel('Error Velocity')

ax = fig.add_subplot(6, 2, 5)
ax.plot(tspan, square_wave_output_signal.data[0, :], color=colors[1])
ax.plot(tspan, square_wave_output_signal_identified.data[0, :], color=colors[4], linestyle='-.')
plt.ylabel('Position')
plt.legend(['True', 'Identified'])
plt.title('Square Wave Input')
ax = fig.add_subplot(6, 2, 6)
ax.plot(tspan, square_wave_output_signal.data[1, :], color=colors[1])
ax.plot(tspan, square_wave_output_signal_identified.data[1, :], color=colors[4], linestyle='-.')
plt.ylabel('Velocity')
plt.legend(['True', 'Identified'])
plt.title('Square Wave Input')
ax = fig.add_subplot(6, 2, 7)
ax.plot(tspan, square_wave_output_signal.data[0, :] - square_wave_output_signal_identified.data[0, :], color=colors[7])
plt.ylabel('Error Position')
ax = fig.add_subplot(6, 2, 8)
ax.plot(tspan, square_wave_output_signal.data[1, :] - square_wave_output_signal_identified.data[1, :], color=colors[7])
plt.ylabel('Error Velocity')

ax = fig.add_subplot(6, 2, 9)
ax.plot(tspan, cosine_wave_output_signal.data[0, :], color=colors[1])
ax.plot(tspan, cosine_wave_output_signal_identified.data[0, :], color=colors[4], linestyle='-.')
plt.ylabel('Position')
plt.legend(['True', 'Identified'])
plt.title('Cosine Wave Input')
ax = fig.add_subplot(6, 2, 10)
ax.plot(tspan, cosine_wave_output_signal.data[1, :], color=colors[1])
ax.plot(tspan, cosine_wave_output_signal_identified.data[1, :], color=colors[4], linestyle='-.')
plt.ylabel('Velocity')
plt.legend(['True', 'Identified'])
plt.title('Cosine Wave Input')
ax = fig.add_subplot(6, 2, 11)
ax.plot(tspan, cosine_wave_output_signal.data[0, :] - cosine_wave_output_signal_identified.data[0, :], color=colors[7])
plt.ylabel('Error Position')
ax = fig.add_subplot(6, 2, 12)
ax.plot(tspan, cosine_wave_output_signal.data[1, :] - cosine_wave_output_signal_identified.data[1, :], color=colors[7])
plt.ylabel('Error Velocity')
plt.xlabel('Time [sec]')

plt.show()


# Plot state estimate
fig = plt.figure(num=5, figsize=[12, 18])

ax = fig.add_subplot(6, 2, 1)
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), gaussian_output_signal_identified.state[0, :], color=colors[1])
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), x_gaussian_estimated[0, :], color=colors[4], linestyle='-.')
plt.ylabel('Position')
plt.legend(['Identified', 'Estimated'])
plt.title('Gaussian Input')
ax = fig.add_subplot(6, 2, 2)
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), gaussian_output_signal_identified.state[1, :], color=colors[1])
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), x_gaussian_estimated[1, :], color=colors[4], linestyle='-.')
plt.ylabel('Velocity')
plt.legend(['Identified', 'Estimated'])
plt.title('Gaussian Input')
ax = fig.add_subplot(6, 2, 3)
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), gaussian_output_signal_identified.state[0, :] - x_gaussian_estimated[0, :], color=colors[7])
plt.ylabel('Error Position')
ax = fig.add_subplot(6, 2, 4)
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), gaussian_output_signal_identified.state[1, :] - x_gaussian_estimated[1, :], color=colors[7])
plt.ylabel('Error Velocity')

ax = fig.add_subplot(6, 2, 5)
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), square_wave_output_signal_identified.state[0, :], color=colors[1])
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), x_square_wave_estimated[0, :], color=colors[4], linestyle='-.')
plt.ylabel('Position')
plt.legend(['Identified', 'Estimated'])
plt.title('Square Wave Input')
ax = fig.add_subplot(6, 2, 6)
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), square_wave_output_signal_identified.state[1, :], color=colors[1])
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), x_square_wave_estimated[1, :], color=colors[4], linestyle='-.')
plt.ylabel('Velocity')
plt.legend(['Identified', 'Estimated'])
plt.title('Square Wave Input')
ax = fig.add_subplot(6, 2, 7)
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), square_wave_output_signal_identified.state[0, :] - x_square_wave_estimated[0, :], color=colors[7])
plt.ylabel('Error Position')
ax = fig.add_subplot(6, 2, 8)
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), square_wave_output_signal_identified.state[1, :] - x_square_wave_estimated[1, :], color=colors[7])
plt.ylabel('Error Velocity')

ax = fig.add_subplot(6, 2, 9)
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), cosine_wave_output_signal_identified.state[0, :], color=colors[1])
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), x_cosine_wave_estimated[0, :], color=colors[4], linestyle='-.')
plt.ylabel('Position')
plt.legend(['Identified', 'Estimated'])
plt.title('Cosine Input')
ax = fig.add_subplot(6, 2, 10)
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), cosine_wave_output_signal_identified.state[1, :], color=colors[1])
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), x_cosine_wave_estimated[1, :], color=colors[4], linestyle='-.')
plt.ylabel('Velocity')
plt.legend(['Identified', 'Estimated'])
plt.title('Cosine Input')
ax = fig.add_subplot(6, 2, 11)
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), cosine_wave_output_signal_identified.state[0, :] - x_cosine_wave_estimated[0, :], color=colors[7])
plt.ylabel('Error Position')
ax = fig.add_subplot(6, 2, 12)
ax.plot(np.linspace(0, total_time + 1 / frequency, number_steps + 1), cosine_wave_output_signal_identified.state[1, :] - x_cosine_wave_estimated[1, :], color=colors[7])
plt.ylabel('Error Velocity')
plt.xlabel('Time [sec]')

plt.show()
