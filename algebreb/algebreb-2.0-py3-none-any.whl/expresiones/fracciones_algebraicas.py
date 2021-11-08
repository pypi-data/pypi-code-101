from algebreb.expresiones.polinomios import Polinomio, polinomio_raices_aleatorias, polinomio_coeficientes_aleatorios
from sympy.abc import x
from sympy import simplify

class FraccionAlgebraica:
    def __init__(self, num, den):
        self.num = Polinomio(num)
        self.den = Polinomio(den)

    def as_expr(self):
        return self.num.as_expr() / self.den.as_expr()

def fa_aleatoria(grado_num, grado_den, variables, dominio, coef_min, coef_max, fraccion=False, raices=True):
    if raices:
        p1 = polinomio_raices_aleatorias(grado_num, variables, dominio, coef_min, coef_max)
        p2 = polinomio_raices_aleatorias(grado_den, variables, dominio, coef_min, coef_max)
    else:
        p1 = polinomio_coeficientes_aleatorios(grado_num, variables, dominio, coef_min, coef_max)
        p2 = polinomio_coeficientes_aleatorios(grado_den, variables, dominio, coef_min, coef_max)

    fa = FraccionAlgebraica(p1, p2)

    return fa

def fa_propia_aleatoria(grado_num, variables, dominio, coef_min, coef_max, fraccion=False, raices=True):
    if raices:
        p1 = polinomio_raices_aleatorias(grado_num, variables, dominio, coef_min, coef_max)
        p2 = polinomio_raices_aleatorias(grado_num + 1, variables, dominio, coef_min, coef_max)
    else:
        p1 = polinomio_coeficientes_aleatorios(grado_num - 1, variables, dominio, coef_min, coef_max)
        p2 = polinomio_coeficientes_aleatorios(grado_num, variables, dominio, coef_min, coef_max)

    fa = FraccionAlgebraica(p1, p2)

    return fa

def fa_impropia_aleatoria(grado_den, variables, dominio, coef_min, coef_max, fraccion=False, raices=True):
    if raices:
        p1 = polinomio_raices_aleatorias(grado_den, variables, dominio, coef_min, coef_max)
        p2 = polinomio_raices_aleatorias(grado_den - 1, variables, dominio, coef_min, coef_max)
    else:
        p1 = polinomio_coeficientes_aleatorios(grado_den, variables, dominio, coef_min, coef_max)
        p2 = polinomio_coeficientes_aleatorios(grado_den - 1, variables, dominio, coef_min, coef_max)

    fa = FraccionAlgebraica(p1, p2)

    return fa