from sympy import *
from algebreb.ejercicios.tipos_ejercicios import UnOperando, DosOperandos
from algebreb.pasos.polinomios import pasos_mult_polinomios, pasos_suma_polinomios, pasos_resta_polinomios

class SumaPolinomios(DosOperandos):
    def __init__(self, p1, p2):
        super(SumaPolinomios, self).__init__(p1, p2)
        self.oper = '+'
        self.enunciado = latex(self.op1.as_expr()) + ' ' + self.oper + ' ' + latex(self.op2.as_expr())

    def operacion(self):
        return self.op1 + self.op2

    def ver_pasos(self):
        self.pasos = pasos_suma_polinomios(self.op1, self.op2)

class RestaPolinomios(DosOperandos):
    def __init__(self, p1, p2):
        super(RestaPolinomios, self).__init__(p1, p2)
        self.oper = '-'
        self.enunciado = latex(self.op1.as_expr()) + ' ' + self.oper + ' ' + latex(self.op2.as_expr())

    def operacion(self):
        return self.op1 - self.op2

    def ver_pasos(self):
        self.pasos = pasos_resta_polinomios(self.op1, self.op2)

class MultPolinomios(DosOperandos):
    def __init__(self, p1, p2):
        super(MultPolinomios, self).__init__(p1, p2)
        self.oper = '*'
        self.enunciado = latex(self.op1.as_expr()) + ' ' + self.oper + ' ' + latex(self.op2.as_expr())

    def operacion(self):
        return self.op1 * self.op2

    def ver_pasos(self):
        self.pasos = pasos_mult_polinomios(self.op1, self.op2)

class DivPolinomios(DosOperandos):
    def __init__(self, p1, p2):
        super(DivPolinomios, self).__init__(p1, p2)
        self.oper = '/'
        self.enunciado = latex(self.op1.as_expr()) + ' ' + self.oper + ' ' + latex(self.op2.as_expr())
        self.cociente, self.residuo = self.operacion()

    def operacion(self):
        return self.op1.div(self.op2)

    def as_str(self):
        dict = {
            'operacion': '/',
            'operando1': str(self.op1.as_expr()),
            'operando2': str(self.op2.as_expr()),
            'solucion': str(self.cociente.as_expr()),
            'residuo': str(self.residuo.as_expr()),
            'respuestas': [str(r.as_expr()) for r in self.respuestas]
        }

        return dict

    def as_latex(self):
        dict = {
            'operacion': '/',
            'operando1': latex(self.op1.as_expr()),
            'operando2': latex(self.op2.as_expr()),
            'solucion': latex(self.cociente.as_expr()),
            'residuo': latex(self.residuo.as_expr()),
            'respuestas': [latex(r.as_expr()) for r in self.respuestas]
        }

        return dict
    
class GradoPolinomio(UnOperando):
    def __init__(self, op1):
        super(GradoPolinomio, self).__init__(op1)
    
    def operacion(self):
        grado = self.op1.total_degree()

        return grado

    def as_str(self):
        dict = {
            'operacion': self.oper,
            'operando1': str(self.op1.as_expr()),
            'solucion': str(self.res),
            'respuestas': self.respuestas
        }

        return dict

    def as_latex(self):
        dict = {
            'operacion': self.oper, 
            'operando1': latex(self.op1.as_expr()),
            'solucion': self.res,
            'respuestas': self.respuestas
        }

        return dict

class TermPolinomio(UnOperando):
    def __init__(self, op1):
        super(TermPolinomio, self).__init__(op1)

    def operacion(self):
        num_terms = len(self.op1.as_dict())

        if num_terms == 1:
            return 'Monomio'
        elif num_terms == 2:
            return 'Binomio'
        elif num_terms == 3:
            return 'Trinomio'
        else:
            return 'Polinomio'

    def as_str(self):
        dict = {
            'operacion': self.oper,
            'operando1': str(self.op1.as_expr()),
            'solucion': self.res,
            'respuestas': self.respuestas
        }

        return dict

    def as_latex(self):
        dict = {
            'operacion': self.oper, 
            'operando1': latex(self.op1.as_expr()),
            'solucion': self.res,
            'respuestas': self.respuestas
        }

        return dict