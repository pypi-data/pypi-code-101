from sympy import *
from sympy.abc import x, y
from algebreb.ejercicios.tipos_ejercicios import UnOperando, DosOperandos
from algebreb.expresiones.fracciones_algebraicas import fa_propia_aleatoria
from algebreb.pasos.fracciones_algebraicas import (pasos_mult_fracciones_algebraicas_latex, 
                                                   pasos_resta_fracciones_algebraicas_latex, 
                                                   pasos_suma_fracciones_algebraicas_latex,
                                                   pasos_div_fracciones_algebraicas_latex, 
                                                   pasos_simp_fracciones_algebraicas_latex)

class SumaFracAlg(DosOperandos):
    def __init__(self, op1, op2):
        super(SumaFracAlg, self).__init__(op1, op2)
        self.oper = '+'
        self.enunciado = latex(self.op1.as_expr()) + ' ' + self.oper + ' ' + latex(self.op2.as_expr())
    
    def operacion(self):
        return simplify(self.op1.as_expr() + self.op2.as_expr())

    def ver_pasos(self):
        self.pasos = pasos_suma_fracciones_algebraicas_latex(self.op1, self.op2)

class RestaFracAlg(DosOperandos):
    def __init__(self, op1, op2):
        super().__init__(op1, op2)
        self.oper = '-'
        self.enunciado = latex(self.op1.as_expr()) + ' ' + self.oper + ' ' + latex(self.op2.as_expr())
    
    def operacion(self):
        return simplify(self.op1.as_expr() - self.op2.as_expr())

    def ver_pasos(self):
        self.pasos = pasos_resta_fracciones_algebraicas_latex(self.op1, self.op2)

class MultFracAlg(DosOperandos):
    def __init__(self, op1, op2):
        super().__init__(op1, op2)
        self.oper = '*'
        self.enunciado = latex(self.op1.as_expr()) + ' ' + self.oper + ' ' + latex(self.op2.as_expr())
    
    def operacion(self):
        return simplify(self.op1.as_expr() * self.op2.as_expr())

    def ver_pasos(self):
        self.pasos = pasos_mult_fracciones_algebraicas_latex(self.op1, self.op2)

class DivFracAlg(DosOperandos):
    def __init__(self, op1, op2):
        super().__init__(op1, op2)
        self.oper = '/'
        self.enunciado = latex(self.op1.as_expr()) + ' ' + self.oper + ' ' + latex(self.op2.as_expr())
    
    def operacion(self):
        return simplify(self.op1.as_expr() / self.op2.as_expr())

    def ver_pasos(self):
        self.pasos = pasos_div_fracciones_algebraicas_latex(self.op1, self.op2)

class SimpFracAlg(UnOperando):
    def __init__(self, op1):
        super().__init__(op1)
        self.oper = ''
        self.enunciado = self.oper + ' ' + latex(self.op1.as_expr())

    def operacion(self):
        return simplify(self.op1.as_expr())

    def ver_pasos(self):
        self.pasos = pasos_simp_fracciones_algebraicas_latex(self.op1)
