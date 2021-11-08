from sympy import *
from sympy.abc import x, y
from algebreb.ejercicios.tipos_ejercicios import UnOperando
from algebreb.expresiones.polinomios import Polinomio, monomio_aleatorio, polinomio_coeficientes_aleatorios
from algebreb.pasos.factorizacion import pasos_cubo_perfecto_binomios_latex, pasos_diferencia_cuadrados_latex, pasos_factor_comun_latex, pasos_trinomio_cuadrado_perfecto_latex, pasos_trinomio_forma1_latex, pasos_trinomio_forma2_latex

class FactorComun(UnOperando):
    def __init__(self, op1):
        super(FactorComun, self).__init__(op1)
        self.monomio = None
        self.polinomio = None
        self.producto = None
        self.oper = ''
        self.enunciado = self.oper + ' ' + latex(self.op1.as_expr())

    def operacion(self):
        return factor(self.op1.as_expr())

    def ver_pasos(self):
        self.pasos = pasos_factor_comun_latex(self.monomio, self.polinomio, self.producto)

class DiferenciaCuadrados(UnOperando):
    def __init__(self, op1):
        super(DiferenciaCuadrados, self).__init__(op1)
        self.bin1 = None
        self.bin2 = None
        self.producto = None
        self.oper = ''
        self.enunciado = self.oper + ' ' + latex(self.op1.as_expr())

    def operacion(self):
        return factor(self.op1.as_expr())

    def ver_pasos(self):
        self.pasos = pasos_diferencia_cuadrados_latex(self.bin1, self.bin2, self.producto)

class TrinomioCuadradoPerfecto(UnOperando):
    def __init__(self, op1):
        super(TrinomioCuadradoPerfecto, self).__init__(op1)
        self.binomio = None
        self.producto = None
        self.oper = ''
        self.enunciado = self.oper + ' ' + latex(self.op1.as_expr())

    def operacion(self):
        return factor(self.op1.as_expr())

    def ver_pasos(self):
        self.pasos = pasos_trinomio_cuadrado_perfecto_latex(self.binomio, self.producto)

class CuboPerfectoBinomios(UnOperando):
    def __init__(self, op1):
        super(CuboPerfectoBinomios, self).__init__(op1)
        self.binomio = None
        self.producto = None
        self.oper = ''
        self.enunciado = self.oper + ' ' + latex(self.op1.as_expr())

    def operacion(self):
        return factor(self.op1.as_expr())

    def ver_pasos(self):
        self.pasos = pasos_cubo_perfecto_binomios_latex(self.binomio, self.producto)

class TrinomioFormaI(UnOperando):
    def __init__(self, op1):
        super(TrinomioFormaI, self).__init__(op1)
        self.bin1 = None
        self.bin2 = None
        self.producto = None
        self.oper = ''
        self.enunciado = self.oper + ' ' + latex(self.op1.as_expr())

    def operacion(self):
        return factor(self.op1.as_expr())

    def ver_pasos(self):
        self.pasos = pasos_trinomio_forma1_latex(self.bin1, self.bin2, self.producto)

class TrinomioFormaII(UnOperando):
    def __init__(self, op1):
        super(TrinomioFormaII, self).__init__(op1)
        self.bin1 = None
        self.bin2 = None
        self.producto = None
        self.oper = ''
        self.enunciado = self.oper + ' ' + latex(self.op1.as_expr())

    def operacion(self):
        return factor(self.op1.as_expr())

    def ver_pasos(self):
        self.pasos = pasos_trinomio_forma2_latex(self.bin1, self.bin2, self.producto)