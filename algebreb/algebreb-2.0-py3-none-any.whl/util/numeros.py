from random import randint, uniform
from fractions import Fraction

def nulos(cantidad):
    return [0] * cantidad

def entero_aleatorio(min, max, excepcion=None):
    entero = randint(min, max)

    if excepcion != None:
        while entero == excepcion:
            entero = randint(min, max)

        return entero
    else:
        return entero
    
def enteros_aleatorios(min, max, cantidad, excepcion=None):
    enteros = []

    for entero in range(cantidad):
        if excepcion != None:
            entero = entero_aleatorio(min, max, excepcion)
        else:
            entero = entero_aleatorio(min, max)

        enteros.append(entero)

    return enteros

def decimal_aleatorio(min, max, excepcion=None):
    decimal = uniform(min, max)

    if excepcion != None:
        while decimal == excepcion:
            decimal = randint(min, max)

        return round(decimal, 2)
    else:
        return round(decimal, 2)

def decimales_aleatorios(min, max, cantidad, excepcion=None):
    decimales = []

    for decimal in range(cantidad):
        decimal = decimal_aleatorio(min, max, excepcion)
        decimales.append(round(decimal, 2))

    return decimales

def fraccion_aleatoria(min, max, excepcion=None):
    numerador = entero_aleatorio(min, max, 0) # No queremos fracciones nulas
    denominador = entero_aleatorio(min, max, 0) # El denominador no puede ser cero

    fraccion = Fraction(numerador, denominador)

    if excepcion != None:
        while fraccion == excepcion:
            fraccion = fraccion_aleatoria(min, max)

        return fraccion
    else:
        return fraccion

def fracciones_aleatorias(min, max, cantidad, excepcion=None):
    fracciones = []

    for fraccion in range(cantidad):
        fraccion = fraccion_aleatoria(min, max, excepcion)
        fracciones.append(fraccion)

    return fracciones