from random import choice

from sympy.polys.monomials import itermonomials
from sympy.polys.orderings import monomial_key
from sympy.abc import x, y, z

def generar_terminos(vars, grado):
    return sorted(itermonomials(vars, grado), key=monomial_key('igrlex', vars))

def generar_terminos_grado(vars, grado):
    return sorted(itermonomials(vars, grado, grado), key=monomial_key('igrlex', vars))

def generar_terminos_restantes(vars, grado):
    terms1 = set(generar_terminos(vars, grado))
    terms2 = set(generar_terminos_grado(vars, grado))

    terms = list(terms1 - terms2)

    return sorted(terms, key=monomial_key('igrlex', vars))

def terminos_polinomio_homogeneo(vars, grado):
    terms1 = set(itermonomials(vars, grado))
    terms2 = set(itermonomials(vars, grado - 1))

    terms = list(terms1 - terms2)

    return sorted(terms, key=monomial_key('igrlex', vars))

def termino_aleatorio(vars, grado):
    termino = []

    termino.append(choice(terminos_polinomio_homogeneo(vars, grado)))

    return termino