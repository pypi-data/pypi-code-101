"""
Python Aerospace Analysis Toolbox - PyAAT
Copyright (c) 2021 Kenedy Matiasso Portella
Distributed under MIT License

This is the user file.
"""
### NUMPY IMPORTS ###
from numpy import array

### MATPLOTLIB IMPORTS ###
import matplotlib.pyplot as plt

### PYTHON-CONTROL IMPORTS ###

### LOCAL IMPORTS ###
# Build-in plotter
from pyaat.tools import plotter
pltr = plotter()

# printer
from pyaat.tools import printInfo

# Cria objeto aeronave e atribui valores
from pyaat.aircraft import Aircraft
from pyaat.constants import RHO_SEA
airc = Aircraft()

# Cria objeto atmosfera
from pyaat.atmosphere import atmosCOESA
atm = atmosCOESA()

# Cria modelo gravitacional
from pyaat.gravity import NewtonGravity
grav = NewtonGravity()

#Cria modelo propulsivo
from pyaat.propulsion import SimpleModel
prop = SimpleModel()

#Cria sistema
from system import system
System = system(atmosphere = atm, propulsion = prop, aircraft = airc, gravity = grav)

#Printa as informações do sistema
Xe, Ue = System.trimmer(condition='cruize', HE = 10000., VE = 200)
printInfo(Xe, Ue, frame ='aero')
printInfo(Xe,Ue, frame='controls')

#Propaga os estados para uma dada condição inicial
solution, controls = System.propagate(Xe, Ue, TF = 180)

# Preparando os plots no objeto plotter
pltr.states = solution
pltr.time = System.time
pltr.control = controls

# Printa resultados
pltr.LinVel(frame = 'aero') # Velocidade aerodinâmica
pltr.LinPos()               # Posição linear
pltr.Attitude()             # Atitude
pltr.AngVel()               # Velocidade angular
pltr.Controls()             # Controles

### Perturbação nos controles ###
from pyaat.pyaatcontrol import doublet, step

# Criação de uma entrada doublet
doub = doublet()
doub.command = 'elevator' #Superfície de controle
doub.amplitude = 3 #amplitude (graus para deflexões angulares, % para variáveis propulsivas)
doub.T = 2 # Período de aplicação (T/2 positivo e T/2 negativo)
doub.t_init = 2 # Instante de aplicação

#Criação de uma entrada degrau
st =step()
st.command = 'aileron' #Variável de controle
st.amplitude = 0.5 # Amplitude (graus)
st.t_init = 20 #Instante de aplicação

#solution, controls = System.propagate(Xe, Ue, TF = 80, perturbation=True, control = [doub, st])
solution, controls = System.simulateAugmented(Xe, Ue, TF = 30, perturbation=True, control = [doub, st])

pltr.states = solution
pltr.time = System.time
pltr.control = controls

# plota resultados
pltr.Controls()             # Controles
pltr.LinVel(frame = 'aero') # Velocidade aerodinâmica
pltr.LinPos()               # Posição linear
pltr.Attitude()             # Atitude
pltr.AngVel()               # Velocidade angular

plt.figure()
plt.plot(System.time, System.states[3] - System.Xe[3])
plt.plot(System.time, System.states[12])
plt.title("velocidade aerodinâmica u")

plt.figure()
plt.plot(System.time, System.states[4] - System.Xe[4])
plt.plot(System.time, System.states[13])
plt.title("velocidade aerodinâmica v")

plt.figure()
plt.plot(System.time, System.states[5] - System.Xe[5])
plt.plot(System.time, System.states[14])
plt.title("velocidade aerodinâmica w")

plt.figure()
plt.plot(System.time, System.controlAction[0] - System.Ue[0])
plt.plot(System.time, System.states[15])
plt.title("Variação na manete de potência")

plt.figure()
plt.plot(System.time, System.controlAction[1] - System.Ue[1])
plt.plot(System.time, System.states[16])
plt.title("Deflexão do profundor")

plt.figure()
plt.plot(System.time, System.controlAction[2] - System.Ue[2])
plt.plot(System.time, System.states[17])
plt.title("deflexão dos ailerons")

plt.figure()
plt.plot(System.time, System.controlAction[3] - System.Ue[3])
plt.plot(System.time, System.states[18])
plt.title("deflexão do leme")
