from random import choice

# from Sympy
from sympy import Poly, Add

from sympy.abc import (a, b, c, d, e, f, g, h, i, 
                       j, k, l, m, n, o, p, q, r, 
                       s, t, u, v, w, x, y, z)

# from Algebreb
from algebreb.util.numeros_proxy import (numeros_no_nulos,
                          numeros)

from algebreb.util.terminos import (generar_terminos,
                      generar_terminos_grado,
                      generar_terminos_restantes, 
                      terminos_polinomio_homogeneo,
                      termino_aleatorio)

from algebreb.util.util import suma_azar, vieta, mcm_fracciones

class Polinomio(Poly):
    pass

def polinomio_coeficientes_aleatorios(grado, variables, dominio, coef_min, coef_max, fraccion=False, completo=True):
    terminos = []
    coefs = []

    terminos_grado = generar_terminos_grado(variables, grado)
    num_terminos_grado = len(terminos_grado)

    coeficientes_grado = numeros_no_nulos(dominio, num_terminos_grado, coef_min, coef_max, fraccion)

    terminos_restantes = generar_terminos_restantes(variables, grado)
    num_terminos_restantes = len(terminos_restantes)

    if completo:
        coeficientes_restantes = numeros_no_nulos(dominio, num_terminos_restantes, coef_min, coef_max, fraccion)
    else:
        nulos, no_nulos = suma_azar(num_terminos_restantes)
        coeficientes_restantes = numeros(dominio, nulos, no_nulos, coef_min, coef_max, fraccion)

    terminos = terminos_grado + terminos_restantes
    coefs = coeficientes_grado + coeficientes_restantes

    return generar_polinomio(coefs, terminos, variables)

def polinomio_raices_aleatorias(num_raices, variable, dominio, min, max, fraccion=False, nulas=False, coefs_frac=False):
    if nulas == False:
        raices = numeros_no_nulos(dominio, num_raices, min, max, fraccion)
    else:
        nulos, no_nulos = suma_azar(num_raices)
        raices = numeros(dominio, nulos, no_nulos, min, max, fraccion)

    coeficientes = vieta(raices, num_raices)

    terminos = generar_terminos(variable, num_raices)

    polinomio = generar_polinomio(coeficientes, terminos, variable)

    if dominio == 'QQ' and fraccion == True and coefs_frac==True:
        mcm = mcm_fracciones(coeficientes)

        #if coefs_frac==False:
        return polinomio * mcm
        #else:
            #polinomio

    return polinomio
    

def polinomio_homogeneo_aleatorio(grado, variables, dominio, coef_min, coef_max, fraccion=False, completo=True):
    terminos = []
    coeficientes = []

    terminos = terminos_polinomio_homogeneo(variables, grado)
    num_terminos = len(terminos)

    if completo:
        coeficientes = numeros_no_nulos(dominio, num_terminos, coef_min, coef_max, fraccion)
    else:
        nulos, no_nulos = suma_azar(num_terminos)
        coeficientes = numeros(dominio, nulos, no_nulos, coef_min, coef_max, fraccion)

    return generar_polinomio(coeficientes, terminos, variables)

def polinomio_semejante(polinomio):
    poli = polinomio

    coefs = poli.coeffs()
    terms = poli.monoms()

    min_coef = min(coefs)
    max_coef = max(coefs)

    return

def trinomio_aleatorio(grado, variables, dominio, coef_min, coef_max, fraccion=False):
    termino1 = choice(generar_terminos_grado(variables, grado))

    terminos_restantes = generar_terminos_restantes(variables, grado)

    termino2 = choice(terminos_restantes)

    terminos_restantes.remove(termino2)

    termino3 = choice(terminos_restantes)

    terminos = [termino1, termino2, termino3]
    coeficientes = numeros_no_nulos(dominio, 3, coef_min, coef_max, fraccion)

    return generar_polinomio(coeficientes, terminos, variables)

def binomio_aleatorio(grado, variables, dominio, coef_min, coef_max, fraccion=False):
    termino1 = choice(generar_terminos_grado(variables, grado))
    termino2 = choice(generar_terminos_restantes(variables, grado))

    terminos = [termino1, termino2]
    coeficientes = numeros_no_nulos(dominio, 2, coef_min, coef_max, fraccion)

    return generar_polinomio(coeficientes, terminos, variables)

def conjugar_binomio(binomio):
    binom = binomio

    terms_binom = binom.monoms()
    coefs_binom = binom.coeffs()

    coefs_binom[1] *= -1

    conjugado = Polinomio.from_dict({m: c for (m, c) in zip(terms_binom, coefs_binom)}, binom.gens)

    return conjugado

def monomio_aleatorio(grado, variables, dominio, coef_min, coef_max, fraccion=False):
    termino = termino_aleatorio(variables, grado)
    coeficiente = numeros_no_nulos(dominio, 1, coef_min, coef_max, fraccion)

    return generar_polinomio(coeficiente, termino, variables)

def generar_polinomio(coefs, terms, variables):
    p = Add(*[coef*term for coef, term in zip(coefs, terms)])

    return Polinomio(p, variables)