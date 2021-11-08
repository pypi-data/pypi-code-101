from random import shuffle
from algebreb.util.numeros import (nulos,
                     entero_aleatorio,
                     enteros_aleatorios,
                     decimal_aleatorio,
                     decimales_aleatorios,
                     fraccion_aleatoria,
                     fracciones_aleatorias)

def numeros(dominio, nulos, no_nulos, min, max, fraccion=False):
    nums_nulos = numeros_nulos(nulos)
    nums_no_nulos = numeros_no_nulos(dominio, no_nulos, min, max, fraccion)

    nums = nums_nulos + nums_no_nulos

    shuffle(nums)
    
    return nums

def numeros_nulos(cantidad):
    return nulos(cantidad)

def numeros_no_nulos(dominio, cantidad, min, max, fraccion=False):
    numeros = []

    if dominio == 'ZZ':
        numeros = enteros_aleatorios(min, max, cantidad, 0)
    elif dominio == 'QQ':
        if fraccion:
            numeros = fracciones_aleatorias(min, max, cantidad, 0)
        else:
            numeros = decimales_aleatorios(min, max, cantidad, 0)
    else:
        return numeros

    return numeros

def numero_no_nulo(dominio, min, max, fraccion=False):
    if dominio == 'ZZ':
        numero = entero_aleatorio(min, max, 0)
    elif dominio == 'QQ':
        if fraccion:
            numero = fraccion_aleatoria(min, max, 0)
        else:
            numero = decimal_aleatorio(min, max, 0)
    else:
        return

    return numero