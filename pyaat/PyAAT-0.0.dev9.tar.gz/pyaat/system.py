"""
Python Aerospace Analysis Toolbox - PyAAT
Copyright (c) 2021 Kenedy Matiasso Portella
Distributed under MIT License

This is the system file of PyAAT.
"""
#import sys 
#sys.setrecursionlimit(10**4)

from pyaat.tools import computeTAS, earth2body, aero2body, body2earth, body2euler
from pyaat.tools import trimmer, trimmerClimb, linearization
from pyaat.tools import trimmerPullUp, trimmerCurve

from pyaat.flightmechanics import lateroMatrix, modesMatrix, longMatrix
from pyaat.flightmechanics import shortPeriodMatrix, phugoidMatrix

from numpy import array, cross, arange, radians, tan, sqrt, sin, copy, transpose
from scipy.integrate import odeint
from pyaat.pyaatcontrol import equilibrium

class system(object):
    
    def __init__(self, aircraft = None, atmosphere = None, propulsion = None,
                 gravity = None, control = None):
        
        self.aircraft = aircraft
        self.atmosphere = atmosphere
        self.propulsion = propulsion
        self.gravity = gravity
        eq = equilibrium()
        self.control = [eq]
        self.Xe = None
        self.Ue = None
        self.U = None
        self.time = None
        self._flagError = 'VALID'       # flag error
        self._error = ''                # error description
        self.controlAction = None
        self.states = None
        self.feedback =None
        
        
    def dynamics(self, t, X, U):
        # State space
        z = X[2]
        
        u = X[3]
        v = X[4]
        w = X[5]
        uvw =array([u, v, w])
        
        phi = X[6]
        theta = X[7]
        psi = X[8]
        
        p = X[9]
        q = X[10]
        r = X[11]
        pqr =array([p, q, r])
        
        #Controls
        delta_p = U[0]
        delta_e = U[1]
        delta_a = U[2]
        delta_r = U[3]
        
        # Aircraft
        m = self.aircraft._mass
        Inertia = self.aircraft.inertia
        InvInertia = self.aircraft.invInertia
        
        #gravity model
        self.gravity._altitude = -z
        g = self.gravity._gravity
        F_gravity_earth = m*g
        F_gravity_body = earth2body(F_gravity_earth, psi, theta, phi)
        #Atmospheric model
        self.atmosphere._altitude = -z
        rho = self.atmosphere._rho

        #Aerodynamic model
        self.aircraft._rho = rho
        alpha, beta, TAS = computeTAS(uvw)
       
        self.aircraft.delta_r = delta_r
        self.aircraft.delta_e = delta_e
        self.aircraft.delta_a = delta_a
        
        self.aircraft.alpha = alpha
        self.aircraft.beta = beta
        self.aircraft.TAS = TAS
        
        self.aircraft.p = p
        self.aircraft.q = q
        self.aircraft.r = r
        
        F_aero_aero = self.aircraft.Forces
        M_aero_aero = self.aircraft.Moments
        F_aero_body = aero2body(F_aero_aero, alpha, beta)
        M_aero_body = aero2body(M_aero_aero, alpha, beta)
        
        #Propulsion model
        self.propulsion.delta_p = delta_p
        self.propulsion._rho = rho
        F_prop_body = self.propulsion.Forces
        M_prop_body = self.propulsion.Moments
        
        """
        Kinematics
        """
        # Linear Kinematics
        xyz_d = body2earth(uvw, psi, theta, phi)
        
        x_d = xyz_d[0]
        y_d = xyz_d[1]
        z_d = xyz_d[2]
        
        # Angular Kinematics
        phithetapsi_d = body2euler(pqr, theta, phi)
        phi_d = phithetapsi_d[0]
        theta_d = phithetapsi_d[1]
        psi_d = phithetapsi_d[2]
        
        """
        Dynamics
        """
        # Linear Dynamics
        uvw_d = 1/m*(F_prop_body + F_aero_body + F_gravity_body) - cross(pqr, uvw)
        u_d = uvw_d[0]
        v_d = uvw_d[1]
        w_d = uvw_d[2]
            
        # Angular Dynamics
        Moments = M_aero_body + M_prop_body
        pqr_d = InvInertia.dot(Moments + cross(pqr, Inertia.dot(pqr)))
        p_d = pqr_d[0]
        q_d = pqr_d[1]
        r_d = pqr_d[2]
        
        # Obtain alpha_d and beta_d to use on next iteration of the aeodynamic model
        # TODO: It slows down hugly the simulation. Solve it.
        
        """
        if t!=0:
            Valphabeta_d = array([1., 1./(TAS),1./(TAS*cos(beta))])*body2aero(uvw_d, alpha, beta)
            beta_d = Valphabeta_d[1]
            alpha_d = Valphabeta_d[2]
            # Send information to aerodynamic model
            self.aircraft.alpha_d = alpha_d
            self.aircraft.beta_d = beta_d
            
        """
        
        return array([
            x_d,
            y_d,
            z_d,
            u_d,
            v_d,
            w_d,
            phi_d,
            theta_d,
            psi_d,
            p_d,
            q_d,
            r_d
            ])


    def Dronedynamics(self, t, X, U):
        # State space
        z = X[2]
        
        u = X[3]
        v = X[4]
        w = X[5]
        uvw =array([u, v, w])
        
        phi = X[6]
        theta = X[7]
        psi = X[8]
        
        p = X[9]
        q = X[10]
        r = X[11]
        pqr =array([p, q, r])
        
        # Aircraft
        m = self.aircraft._mass
        Inertia = self.aircraft.inertia
        InvInertia = self.aircraft.invInertia
        
        #gravity model
        self.gravity._altitude = -z
        g = self.gravity._gravity
        F_gravity_earth = m*g
        F_gravity_body = earth2body(F_gravity_earth, psi, theta, phi)
        #Atmospheric model
        self.atmosphere._altitude = -z
        rho = self.atmosphere._rho

        #Aerodynamic model
        self.aircraft._rho = rho
        alpha, beta, TAS = computeTAS(uvw)
    
        
        self.aircraft.alpha = alpha
        self.aircraft.beta = beta
        self.aircraft.TAS = TAS
        
        self.aircraft.p = p
        self.aircraft.q = q
        self.aircraft.r = r
        
        F_aero_aero = self.aircraft.Forces
        M_aero_aero = self.aircraft.Moments
        F_aero_body = aero2body(F_aero_aero, alpha, beta)
        M_aero_body = aero2body(M_aero_aero, alpha, beta)
        
        #Propulsion model
        self.propulsion.delta_p = U
        self.propulsion._rho = rho
        F_prop_body = self.propulsion.Forces
        M_prop_body = self.propulsion.Moments
        
        """
        Kinematics
        """
        # Linear Kinematics
        xyz_d = body2earth(uvw, psi, theta, phi)
        
        x_d = xyz_d[0]
        y_d = xyz_d[1]
        z_d = xyz_d[2]
        
        # Angular Kinematics
        phithetapsi_d = body2euler(pqr, theta, phi)
        phi_d = phithetapsi_d[0]
        theta_d = phithetapsi_d[1]
        psi_d = phithetapsi_d[2]
        
        """
        Dynamics
        """
        # Linear Dynamics
        uvw_d = 1/m*(F_prop_body + F_aero_body + F_gravity_body) - cross(pqr, uvw)
        u_d = uvw_d[0]
        v_d = uvw_d[1]
        w_d = uvw_d[2]
            
        # Angular Dynamics
        Moments = M_aero_body + M_prop_body
        pqr_d = InvInertia.dot(Moments + cross(pqr, Inertia.dot(pqr)))
        p_d = pqr_d[0]
        q_d = pqr_d[1]
        r_d = pqr_d[2]
        
        return array([
            x_d,
            y_d,
            z_d,
            u_d,
            v_d,
            w_d,
            phi_d,
            theta_d,
            psi_d,
            p_d,
            q_d,
            r_d
            ])
    
    def AugmentedDynamics(self, t, X, U):
        
        #Estados da aeronave
        XAircraft = X[0:12]
        
        # Estados dos filtros aerodinâmicos
        duf = X[12]
        dvf = X[13]
        dwf = X[14]
        
        #Estados dos atuadores
        dx_p = X[15] #Variação da Potencia do sistema propusivo em relação ao equilíbrio
        dx_e = X[16] #Variação da deflexão real do profundor em relação ao equilíbrio
        dx_a = X[17] #Variação da deflexão real dos ailerons em relação ao equilíbrio
        dx_r = X[18] #Variação da deflexão real do leme em relação ao equilíbrio
        
        #Constante de tenpo dos atuadores
        tauP = self.aircraft.tauP
        tauE = self.aircraft.tauE
        tauA = self.aircraft.tauA
        tauR = self.aircraft.tauR
        
        #Erro dos controles
        ddelta_p = U[0] - self.Ue[0] 
        ddelta_e = U[1] - self.Ue[1]
        ddelta_a = U[2] - self.Ue[2] 
        ddelta_r = U[3] - self.Ue[3]
        
        #Derivada dos estados dos atuadores
        dx_pd = -1/tauP*dx_p + 1/tauP*ddelta_p
        dx_ed = -1/tauE*dx_e + 1/tauE*ddelta_e
        dx_ad = -1/tauA*dx_a + 1/tauA*ddelta_a
        dx_rd = -1/tauR*dx_r + 1/tauR*ddelta_r
        
        U[0] = self.Ue[0] + ddelta_p
        U[1] = self.Ue[1] + ddelta_e
        U[2] = self.Ue[2] + ddelta_a
        U[3] = self.Ue[3] + ddelta_r
        
        #Derivada dos estados da aeronave
        Xp =  list(self.dynamics(t, XAircraft, U))
        
        #Constante de tempo dos filtros
        tauFu = self.aircraft.tauFu
        tauFv = self.aircraft.tauFv
        tauFw = self.aircraft.tauFw
        
        #Erro dos estados
        dx = X[0] - self.Xe[0]
        dy = X[1] - self.Xe[1] 
        dz = X[2] - self.Xe[2] 
        
        du = X[3] - self.Xe[3] 
        dv = X[4] - self.Xe[4]
        dw = X[5] - self.Xe[5]
        
        dphi = X[6] - self.Xe[7]
        dtheta = X[7] - self.Xe[7]
        dpsi = X[8] - self.Xe[8]
        
        dp = X[9] - self.Xe[9] 
        dq = X[10] - self.Xe[10]
        dr = X[11] - self.Xe[11]
        
        #Derivada dos estados dos filtros
        dufd = -1/tauFu*duf + 1/tauFu*du #derivada do estado do filtro de u
        dvfd = -1/tauFv*dvf + 1/tauFv*dv #derivada do estado do filtro de v
        dwfd = -1/tauFw*dwf + 1/tauFw*dw #derivada do estado do filtro de w
        
        Xp.append(dufd)
        Xp.append(dvfd)
        Xp.append(dwfd)
        Xp.append(dx_pd)
        Xp.append(dx_ed)
        Xp.append(dx_ad)
        Xp.append(dx_rd)     
        return Xp
    
    
    def simularaviao(self, X, t):
        Ue = copy(self.Ue)
        
        for cont in self.control:
            cont.t = t
            cont.Xe = self.Xe
            cont.Ue = Ue
            cont.X = X
            self.U = cont.U
            Ue = copy(self.U)
        
        return self.dynamics(t, X, self.U)
    
    def simularDinamicaAumentada(self, X, t):
        Ue = copy(self.Ue)
        
        for cont in self.control:
            cont.t = t
            cont.Xe = self.Xe
            cont.Ue = Ue
            cont.X = X
            self.U = cont.U
            Ue = copy(self.U)
            
        return self.AugmentedDynamics(t, X, self.U)
    
    def trimmer(self, condition = 'cruize', HE = None, VE = None, dH = None,
                dTH = None, dPS = None, BTA = None):
        
        # Check if HE is valid
        if HE == None:
            self._flagError = 'INVALID'
            self._error = 'You shall define an equilibrium altitude HE'
            
        elif (type(HE) != int) and type(HE) != float:
            self._flagError = 'INVALID'
            self._error = 'The equilibrium altitude shall be an integer or a float'
                
        elif HE < 0:
            self._flagError = 'INVALID'
            self._error = 'The equilibrium altitude shall be positive'
        
        # Check if VE is valid
        if VE == None:
            self._flagError = 'INVALID'
            self._error = 'You shall define an equilibrium velocity VE'
            
        elif (type(VE) != int) and type(VE) != float:
            self._flagError = 'INVALID'
            self._error = 'The equilibrium velocity shall be an integer or a float'
                
        elif VE < 0:
            self._flagError = 'INVALID'
            self._error = 'The equilibrium velocity shall be positive'
        
        # If cruize condition
        if condition == 'cruize':
            if self._flagError == 'VALID':
                if self.aircraft.kind == 'Aircraft':
                    return trimmer(self.dynamics, HE, VE)
                elif self.aircraft.kind == 'Drone':
                    pass
            else:
                raise Exception(self._error)
        
        if condition == 'hover':
            if self._flagError == 'VALID':
                if self.aircraft.kind == 'Drone':
                    return trimmerDroneHover(self.Dronedynamics, HE, len(self.propulsion.props))
                else:
                    pass
            else:
                raise Exception(self._error)        
                
        # If climb condition
        elif condition == 'climb':
            # Check dH
            if dH == None:
                self._flagError = 'INVALID'
                self._error = 'You shall define a climb rate dH'
                    
            elif (type(dH) != int) and type(dH) != float:
                self._flagError = 'INVALID'
                self._error = 'The equilibrium altitude shall be an integer or a float'
                
            if self._flagError == 'VALID':
                return trimmerClimb(self.dynamics, HE, VE, dH)
            else:
                raise Exception(self._error)
            
        elif condition == 'pullUp':
            if dTH == None:
                self._flagError = 'INVALID'
                self._error = 'You shall define a value for theta rate dTH'
                
            elif (type(dTH) != int) and type(dTH) != float:
                self._flagError = 'INVALID'
                self._error = 'The theta rate dTH shall be an integer or a float'
                    
            elif dTH < 0:
                self._flagError = 'INVALID'
                self._error = 'The theta rate dTH shall be positive'       
            
            if self._flagError == 'VALID':

                dTH = radians(dTH)
                return trimmerPullUp(self.dynamics, HE, VE, dTH)
            else:
                raise Exception(self._error)
                
        elif condition == 'turn':
            if dPS == None:
                self._flagError = 'INVALID'
                self._error = 'You shall define a value for turn rate dPS'
                
            elif (type(dPS) != int) and type(dPS) != float:
                self._flagError = 'INVALID'
                self._error = 'The turn rate dPS shall be an integer or a float'
                
            if BTA == None:
                self._flagError = 'INVALID'
                self._error = 'You shall define the slidinside angle BTA'
                
            elif (type(BTA) != int) and type(BTA) != float:
                self._flagError = 'INVALID'
                self._error = 'The slidinside angle BTA shall be an integer or a float'
                
            if self._flagError == 'VALID':
                BTA = radians(BTA)
                dPS = radians(dPS)
                return trimmerCurve(self.dynamics, HE, VE, dPS, BTA)
            else:
                raise Exception(self._error)
                
    def propagate(self, Xe, Ue, T0 = 0.0, TF = 10.0, dt = 0.01,
                  perturbation = False, state = {'beta':0., 'alpha':0.},
                  control = None):
        self.Xe = Xe
        tcritL = []
        if perturbation == False:
            self.Ue = Ue

        elif perturbation ==True:
            for value in state:
                if value == 'x':
                    Xe[0] = Xe[0] + state['x']
                    
                if value == 'y':
                    Xe[1] = Xe[1] + state['y']
                    
                if value == 'z':
                    Xe[2] = Xe[2] + state['z']
                    
                if value == 'altitude':
                    Xe[2] = Xe[2] - state['altitude']
                
                if value == 'u':
                    Xe[3] = Xe[3] + state['u']
                    
                if value == 'v':
                    Xe[4] = Xe[4] + state['v']
                    
                if value == 'w':
                    Xe[5] = Xe[5] + state['w']
                    
                if value == 'phi':
                    Xe[6] = Xe[6] + radians(state['phi'])
                    
                if value == 'theta':
                    Xe[7] = Xe[7] + radians(state['theta'])
                    
                if value == 'psi':
                    Xe[8] = Xe[8] + radians(state['psi'])
                    
                if value == 'p':
                    Xe[9] = Xe[9] + radians(state['p'])
                    
                if value == 'q':
                    Xe[10] = Xe[10] + radians(state['q'])
                    
                if value == 'r':
                    Xe[11] = Xe[11] + radians(state['r'])                  
                
                if value == 'alpha':
                    Xe[5] = Xe[5] + Xe[3]*tan(radians(state['alpha']))
                    
                if value == 'beta':
                    V = sqrt(Xe[3]**2 + Xe[4]**2+ Xe[5]**2)
                    Xe[4] = Xe[4] + V*sin(radians(state['beta']))
            
            self.Ue = Ue
            
            if control != None:
                self.control.extend(control)
                for i in control:
                    if type(i.t_init) == float:
                        tcritL.append(i.t_init)
                    elif type(i.t_init) == int:
                        tcritL.append(float(i.t_init))
            
        self.time = arange(T0, TF, dt)
        solution = odeint(self.simularaviao, Xe, self.time, tcrit=tcritL)
        
        # Create control vector (plot purpuses only)
        dp = []
        de = []
        da = []
        dr = []
        
        for i in range (0, len(self.time)):
            
            t = self.time[i]
            X = solution[i]          
            Ue = copy(self.Ue)
            
            for cont in self.control:
                cont.t = t
                cont.Xe = self.Xe
                cont.Ue = Ue
                cont.X = X
                U = cont.U
                Ue = copy(U)
            
            dp.append(U[0])
            de.append(U[1])
            da.append(U[2])
            dr.append(U[3])
        
        controls = array([dp, de, da, dr])
        self.controlAction = controls
        self.states = transpose(solution)

        return solution, controls

    def simulateAugmented(self, Xe, Ue, T0 = 0.0, TF = 10.0, dt = 0.01,
                  perturbation = True, state = {'beta':0., 'alpha':0.},
                  control = None):
        tcritL = []
        self.Xe = Xe
        ## X =[x, y, z, u, v, w, phi, theta, psi, p, q, r, uf, vf, wf, x_p, x_e, x_a, x_r]
        
        uf = 0.0
        vf = 0.0
        wf = 0.0
        if perturbation == False:
            self.Ue = Ue

        elif perturbation ==True:
            for value in state:
                if value == 'x':
                    Xe[0] = Xe[0] + state['x']
                    
                if value == 'y':
                    Xe[1] = Xe[1] + state['y']
                    
                if value == 'z':
                    Xe[2] = Xe[2] + state['z']
                    
                if value == 'altitude':
                    Xe[2] = Xe[2] - state['altitude']
                
                if value == 'u':
                    Xe[3] = Xe[3] + state['u']
                    uf = state['u']
                    
                if value == 'v':
                    Xe[4] = Xe[4] + state['v']
                    vf = state['v']
                    
                if value == 'w':
                    Xe[5] = Xe[5] + state['w']
                    wf = state['w']
                    
                if value == 'phi':
                    Xe[6] = Xe[6] + radians(state['phi'])
                    
                if value == 'theta':
                    Xe[7] = Xe[7] + radians(state['theta'])
                    
                if value == 'psi':
                    Xe[8] = Xe[8] + radians(state['psi'])
                    
                if value == 'p':
                    Xe[9] = Xe[9] + radians(state['p'])
                    
                if value == 'q':
                    Xe[10] = Xe[10] + radians(state['q'])
                    
                if value == 'r':
                    Xe[11] = Xe[11] + radians(state['r'])                  
                
                if value == 'alpha':
                    Xe[5] = Xe[5] + Xe[3]*tan(radians(state['alpha']))
                    
                if value == 'beta':
                    V = sqrt(Xe[3]**2 + Xe[4]**2+ Xe[5]**2)
                    Xe[4] = Xe[4] + V*sin(radians(state['beta']))
            
            self.Ue = Ue
                                   
            if control != None:
                self.control.extend(control)
                for i in control:
                    if type(i.t_init) == float:
                        tcritL.append(i.t_init)
                    elif type(i.t_init) == int:
                        tcritL.append(float(i.t_init))
            x_p = 0
            x_e = 0
            x_a = 0
            x_r = 0
            
            for cont in self.control:
                cont.t = 0
                cont.Xe = Xe
                cont.Ue = Ue
                
                x_p = x_p + (cont.U[0] - Ue[0])
                x_e = x_p + (cont.U[1] - Ue[1])
                x_a = x_p + (cont.U[2] - Ue[2])
                x_r = x_p + (cont.U[3] - Ue[3])
        
        Xe = list(Xe)
        Xe.append(uf)
        Xe.append(vf)
        Xe.append(wf)
        Xe.append(x_p)
        Xe.append(x_e)
        Xe.append(x_a)
        Xe.append(x_r)
        
        self.time = arange(T0, TF, dt)
        solution = odeint(self.simularDinamicaAumentada, Xe, self.time, tcrit=tcritL)
        
        # Create control vector (plot purpuses only)
        dp = []
        de = []
        da = []
        dr = []
        
        for i in range (0, len(self.time)):
            
            t = self.time[i]
            X = solution[i]          
            Ue = copy(self.Ue)
            
            for cont in self.control:
                cont.t = t
                cont.Xe = self.Xe
                cont.Ue = Ue
                cont.X = X
                U = cont.U
                Ue = copy(U)
            
            dp.append(U[0])
            de.append(U[1])
            da.append(U[2])
            dr.append(U[3])
        
        controls = array([dp, de, da, dr])   
        self.controlAction = controls
        self.states = transpose(solution)

        return solution, controls
    
    def Linearize(self, Xe, Ue):
        return linearization(self.dynamics, Xe, Ue)
    
    def LinearModes(self, Xe, Ue):
        A, B = linearization(self.dynamics, Xe, Ue)
        return modesMatrix(A, B)
    
    def LinearLatero(self, Xe, Ue):
        A, B = linearization(self.dynamics, Xe, Ue)
        return lateroMatrix(A, B)
    
    def LinearLong(self, Xe, Ue):
        A, B = linearization(self.dynamics, Xe, Ue)
        return longMatrix(A, B)

    def shortPeriod(self, Xe, Ue):
        A, B = linearization(self.dynamics, Xe, Ue)
        return shortPeriodMatrix(A, B)
    
    def phugoid(self, Xe, Ue):
        A, B = linearization(self.dynamics, Xe, Ue)
        return phugoidMatrix(A, B)
    
