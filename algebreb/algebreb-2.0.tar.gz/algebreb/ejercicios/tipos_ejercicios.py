from sympy import *

from algebreb.expresiones.polinomios import Polinomio

class UnOperando():
    def __init__(self, op1):
        self.oper = ''
        self.op1 = op1
        self.res = self.operacion()
        self.respuestas = []
        self.pasos = {}
        self.enunciado = ''

    def set_op1(self, op1):
        self.op1 = op1

    def get_op1(self):
        return self.op1

    def operacion(self):
        return

    def ver_pasos(self):
        return

    def as_str(self):
        dict = {
            'operacion': str(self.oper),
            'operando1': str(self.op1.as_expr()),
            'solucion': str(self.res.as_expr()),
            'respuestas': [str(r.as_expr()) for r in self.respuestas]
        }

        return dict

    def as_latex(self):
        dict = {
            'operacion': self.oper, 
            'operando1': latex(self.op1.as_expr()),
            'solucion': latex(self.res.as_expr()),
            'enunciado': self.enunciado,
            'respuestas': [latex(r.as_expr()) for r in self.respuestas],
            'pasos': self.pasos
        }

        return dict

    def as_str_latex(self):
        diccionario = {}

        diccionario['string'] = self.as_str()
        diccionario['latex'] = self.as_latex()

        return diccionario


class DosOperandos():
    def __init__(self, op1, op2):
        self.oper = ''
        self.op1 = op1
        self.op2 = op2
        self.res = self.operacion()
        self.respuestas = []
        self.pasos = {}
        self.enunciado = ''

    def set_op1(self, op1):
        self.op1 = op1

    def get_op1(self):
        return self.op1

    def set_op2(self, op2):
        self.op2 = op2

    def get_op2(self):
        return self.op2

    def operacion(self):
        return [r.as_expr() for r in self.respuestas] #if self.respuestas == [] else []

    def ver_pasos(self):
        return
    
    def respuestas_str(self):
        return

    def as_str(self):
        dict = {
            'operacion': str(self.oper),
            'operando1': str(self.op1.as_expr()),
            'operando2': str(self.op2.as_expr()),
            'solucion': str(self.res.as_expr()),
            'respuestas': [str(r.as_expr()) for r in self.respuestas]
        }

        return dict

    def as_latex(self):
        dict = {
            'operacion': self.oper,
            'operando1': latex(self.op1.as_expr()),
            'operando2': latex(self.op2.as_expr()),
            'enunciado': self.enunciado,
            'solucion': latex(self.res.as_expr()),
            'respuestas': [latex(r.as_expr()) for r in self.respuestas],
            'pasos': self.pasos
        }

        return dict

    def as_str_latex(self):
        diccionario = {}

        diccionario['string'] = self.as_str()
        diccionario['latex'] = self.as_latex()

        return diccionario