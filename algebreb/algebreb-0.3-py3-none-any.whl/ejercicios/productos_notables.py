from sympy.abc import x, y
from sympy import *
from algebreb.ejercicios.tipos_ejercicios import UnOperando, DosOperandos
from algebreb.expresiones.polinomios import binomio_aleatorio
from algebreb.pasos.productos_notables import (pasos_binomio_al_cuadrado_latex,
                                               pasos_binomio_al_cubo_latex,
                                               pasos_binomios_conjugados_latex, 
                                               pasos_binomios_forma1_latex, pasos_binomios_forma2_latex, pasos_trinomio_al_cuadrado_latex)

class BinomioAlCuadrado(UnOperando):
    def __init__(self, op1):
        super(BinomioAlCuadrado, self).__init__(op1)
        self.oper = ''
        self.enunciado = latex(self.op1.as_expr()**2)

    def operacion(self):
        return self.op1**2

    def ver_pasos(self):   
        self.pasos = pasos_binomio_al_cuadrado_latex(self.op1)

class BinomioAlCubo(UnOperando):
    def __init__(self, op1):
        super(BinomioAlCubo, self).__init__(op1)
        self.oper = ''
        self.enunciado = latex(self.op1.as_expr()**3)

    def operacion(self):
        return self.op1**3

    def ver_pasos(self):   
        self.pasos = pasos_binomio_al_cubo_latex(self.op1)

class BinomiosConjugados(DosOperandos):
    def __init__(self, op1, op2):
        super(BinomiosConjugados, self).__init__(op1, op2)
        self.oper = '*'
        self.enunciado = latex(self.op1.as_expr()) + ' ' + self.oper + ' ' + latex(self.op2.as_expr())

    def operacion(self):
        return self.op1 * self.op2

    def ver_pasos(self):   
        self.pasos = pasos_binomios_conjugados_latex(self.op1, self.op2)

class BinomiosFormaI(DosOperandos):
    def __init__(self, op1, op2):
        super(BinomiosFormaI, self).__init__(op1, op2)
        self.oper = '*'
        self.enunciado = latex(self.op1.as_expr()) + ' ' + self.oper + ' ' + latex(self.op2.as_expr())

    def operacion(self):
        return self.op1 * self.op2

    def ver_pasos(self):
        self.pasos = pasos_binomios_forma1_latex(self.op1, self.op2)

class BinomiosFormaII(DosOperandos):
    def __init__(self, op1, op2):
        super(BinomiosFormaII, self).__init__(op1, op2)
        self.oper = '*'
        self.enunciado = latex(self.op1.as_expr()) + ' ' + self.oper + ' ' + latex(self.op2.as_expr())

    def operacion(self):
        return self.op1 * self.op2

    def ver_pasos(self):
        self.pasos = pasos_binomios_forma2_latex(self.op1, self.op2)

class TrinomioAlCuadrado(UnOperando):
    def __init__(self, op1):
        super(TrinomioAlCuadrado, self).__init__(op1)
        self.oper = ''
        self.enunciado = self.oper + ' ' + latex(self.op1.as_expr())

    def operacion(self):
        return self.op1**2

    def ver_pasos(self):
        self.pasos = pasos_trinomio_al_cuadrado_latex(self.op1)
