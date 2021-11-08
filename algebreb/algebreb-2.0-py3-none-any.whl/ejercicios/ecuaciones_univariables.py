from sympy.solvers import solve
from sympy.abc import x
from sympy import *
from algebreb.expresiones.polinomios import Polinomio
from algebreb.ejercicios.tipos_ejercicios import DosOperandos

class EcuacionLineal(DosOperandos):
    def __init__(self, lado_derecho, lado_izquierdo):
        super(EcuacionLineal, self).__init__(lado_derecho, lado_izquierdo)
        self.oper = '='

    def operacion(self):
        ecuacion = self.op1 - self.op2
        variables = ecuacion.gens

        return solve(ecuacion.as_expr(), variables)

    def as_str(self):
        dict = {
            'operacion': self.oper,
            'operando1': str(self.op1.as_expr()),
            'operando2': str(self.op2.as_expr()),
            'enunciado': str(self.op1.as_expr()) + ' ' + self.oper + ' ' + str(self.op2.as_expr()),
            'enunciado': [str(r) for r in self.res],
            'respuestas': [str(r.as_expr()) for r in self.respuestas]
        }

        return dict

    def as_latex(self):
        dict = {
            'operacion': self.oper,
            'operando1': latex(self.op1.as_expr()),
            'operando2': latex(self.op2.as_expr()),
            'ecuacion': latex(self.op1.as_expr()) + ' ' + self.oper + ' ' + latex(self.op2.as_expr()),
            'solucion': [latex(r) for r in self.res],
            'respuestas': [latex(r.as_expr()) for r in self.respuestas]
        }

        return dict


class EcuacionCuadratica(DosOperandos):
    def __init__(self, lado_derecho, lado_izquierdo) -> None:
        super(EcuacionCuadratica, self).__init__(lado_derecho, lado_izquierdo)
        self.oper = '='
        self.metodo = ''

    def operacion(self):
        ecuacion = self.op1 - self.op2
        variables = ecuacion.gens

        return solve(ecuacion.as_expr(), variables)

    def as_str(self):
        dict = {
            'operacion': self.oper,
            'operando1': str(self.op1.as_expr()),
            'operando2': str(self.op2.as_expr()),
            'enunciado': str(self.op1.as_expr()) + ' ' + self.oper + ' ' + str(self.op2.as_expr()),
            'solucion': [str(r) for r in self.res],
            'respuestas': [str(r.as_expr()) for r in self.respuestas]
        }

        return dict

    def as_latex(self):
        dict = {
            'operacion': self.oper,
            'operando1': latex(self.op1.as_expr()),
            'operando2': latex(self.op2.as_expr()),
            'enunciado': latex(self.op1.as_expr()) + ' ' + self.oper + ' ' + latex(self.op2.as_expr()),
            'solucion': [latex(r) for r in self.res],
            'respuestas': [latex(r.as_expr()) for r in self.respuestas]
        }

        return dict

poli = Polinomio(x**2-4,x)
poli2 = Polinomio(0, x)
ec = EcuacionCuadratica(poli, poli2)
print(ec.as_str())
print(ec.as_latex())