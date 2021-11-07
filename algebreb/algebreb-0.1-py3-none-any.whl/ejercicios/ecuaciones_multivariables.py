from sympy.solvers import solve
from sympy.abc import x
from sympy import *
from algebreb.expresiones.polinomios import Polinomio
from algebreb.ejercicios.tipos_ejercicios import DosOperandos

class SistemaEcuaciones(DosOperandos):
    def __init__(self, lado_derecho, lado_izquierdo) -> None:
        super(SistemaEcuaciones, self).__init__(lado_derecho, lado_izquierdo)
        self.oper = '='
        self.metodo = ''

    def operacion(self):
        solucion = solve((eq1, eq2), (x, y, z))

        return solucion