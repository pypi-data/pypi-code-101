#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 09:51:00 2021

@author: ydor9e
"""
from numpy import radians, array

class doublet(object):
    def __init__(self):
        self.t = 0.0
        self.Xe = None
        self.X = None
        self.Ue = None
        self.command = 'elevator'
        self.amplitude = 1
        self.T = 1
        self.t_init = 1
    
    @property
    def U(self):
        if self.command == 'thrust':
            if self.t >= self.t_init and self.t <= (self.T/2 + self.t_init):
                delta_p = self.Ue[0] + self.amplitude
            elif self.t >= (self.T/2 + self.t_init) and self.t <= (self.T + self.t_init):
                delta_p = self.Ue[0] - self.amplitude
            else:
                delta_p = self.Ue[0]
                
            delta_e = self.Ue[1]
            delta_a = self.Ue[2]
            delta_r = self.Ue[3]
       
        elif self.command == 'elevator':

            if self.t >= self.t_init and self.t <= (self.T/2 + self.t_init):
                delta_e = self.Ue[1] + radians(self.amplitude)
                
            elif self.t >= (self.T/2 + self.t_init) and self.t <= (self.T + self.t_init):
                delta_e = self.Ue[1] - radians(self.amplitude)
            else:
                delta_e = self.Ue[1]
                
            delta_p = self.Ue[0]
            delta_a = self.Ue[2]
            delta_r = self.Ue[3]
            
        elif self.command == 'aileron':
            if self.t >= self.t_init and self.t <= (self.T/2 + self.t_init):
                delta_a = self.Ue[2] + radians(self.amplitude)
                
            elif self.t >= (self.T/2 + self.t_init) and self.t <= (self.T + self.t_init):
                delta_a = self.Ue[2] - radians(self.amplitude)
                
            else:
                delta_a = self.Ue[2]

            delta_p = self.Ue[0]    
            delta_e = self.Ue[1]
            delta_r = self.Ue[3]
            
        elif self.command == 'rudder':
            if self.t >= self.t_init and self.t <= (self.T/2 + self.t_init):
                delta_r = self.Ue[3] + radians(self.amplitude)
            elif self.t >= (self.T/2 + self.t_init) and self.t <= (self.T + self.t_init):
                delta_r = self.Ue[3] - radians(self.amplitude)
            else:
                delta_r = self.Ue[3]
                
            delta_p = self.Ue[0]                
            delta_e = self.Ue[1]
            delta_a = self.Ue[2]
            
        else:
            delta_p = self.Ue[0]                
            delta_e = self.Ue[1]
            delta_a = self.Ue[2]
            delta_r = self.Ue[3]
        return array([delta_p, delta_e, delta_a, delta_r])

class equilibrium(object):
    def __init__(self):
        self.t = 0.0
        self.Xe = None
        self.X = None
        self.Ue = None
        
    @property
    def U(self):            
        return array([self.Ue[0], self.Ue[1], self.Ue[2], self.Ue[3]])
    
class step(object):
    def __init__(self):
        self.t = 0.0
        self.Xe = None
        self.X = None
        self.Ue = None
        self.command = 'elevator'
        self.amplitude = 1
        self.t_init = 1
    
    @property
    def U(self):
        if self.command == 'thrust':
            if self.t >= self.t_init:
                delta_p = self.Ue[0] + self.amplitude
            else:
                delta_p = self.Ue[0]
                
            delta_e = self.Ue[1]
            delta_a = self.Ue[2]
            delta_r = self.Ue[3]
       
        elif self.command == 'elevator':

            if self.t >= self.t_init:
                delta_e = self.Ue[1] + radians(self.amplitude)
            else:
                delta_e = self.Ue[1]
                
            delta_p = self.Ue[0]
            delta_a = self.Ue[2]
            delta_r = self.Ue[3]
            
        elif self.command == 'aileron':
            if self.t >= self.t_init:
                delta_a = self.Ue[2] + radians(self.amplitude)                
            else:
                delta_a = self.Ue[2]

            delta_p = self.Ue[0]    
            delta_e = self.Ue[1]
            delta_r = self.Ue[3]
            
        elif self.command == 'rudder':
            if self.t >= self.t_init:
                delta_r = self.Ue[3] + radians(self.amplitude)
            else:
                delta_r = self.Ue[3]
                
            delta_p = self.Ue[0]                
            delta_e = self.Ue[1]
            delta_a = self.Ue[2]
            
        else:
            delta_p = self.Ue[0]                
            delta_e = self.Ue[1]
            delta_a = self.Ue[2]
            delta_r = self.Ue[3]
            
        return array([delta_p, delta_e, delta_a, delta_r])
    
class loop(object):
    def __init__(self, controls, var):
        if type(controls)==list:
            self.loopList = controls
        else:
            self.loopList = [controls]
        self.var = var
        self.u = None
    
    def computeComand(self, X, Xe):
        
        if self.var == 'x':
            self.u = X[0] - Xe[0]
        
        elif self.var == 'y':
            self.u = X[1] -Xe[1]
        
        elif self.var == 'z':
            self.u = X[2] -Xe[2]
        
        elif self.var == 'u':
            self.u = X[3] -Xe[3]

        elif self.var == 'v':
            self.u = X[4] - Xe[4]

        elif self.var == 'w':
            self.u = X[5] - Xe[5]

        elif self.var == 'phi':
            self.u = X[6] - Xe[6]

        elif self.var == 'theta':
            self.u = X[7] - Xe[7]

        elif self.var == 'psi':
            self.u = X[8] - Xe[8]

        elif self.var == 'p':
            self.u = X[9] - Xe[9]

        elif self.var == 'q':
            self.u = X[10] - Xe[10]

        elif self.var == 'r':
            self.u = X[11] - Xe[11]

        elif self.var == 'uf':
            self.u = X[12]

        elif self.var == 'vf':
            self.u = X[13]

        elif self.var == 'wf':
            self.u = X[14]
        
        for cont in self.loopList:
            self.u = cont.computeControl(self.u)
    
    @property
    def nbStates(self):
        nbState = 0
        for i in self.loops:
            nbState  = nbState + i.nbState
        return nbState

class P():
    def __init__(self, gain):
        self.nbState = 0
        self.gain = gain
    
    def computeControl(self, deltaX):
        return self.gain*deltaX

            
        
        
        