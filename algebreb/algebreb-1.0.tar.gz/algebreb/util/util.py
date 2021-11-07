import fractions
from math import lcm

from algebreb.util.numeros_proxy import numeros

def vieta(raices, grado):
    coeficientes = [0] * (grado + 1)

    coeficientes[grado] = 1
    for i in range(1, grado + 1):
        for j in range(grado - i - 1, grado):
            coeficientes[j] += ((-1) * raices[i - 1] * coeficientes[j + 1])

    coeficientes = coeficientes[::-1]

    return coeficientes

from random import choice

def suma_azar(numero):
    if numero == 1:
        return 0, 1
        
    techo = numero
    piso = 0
    lista = []

    while piso < numero - 1:
        piso += 1
        techo -= 1

        tupla = (piso, techo)
        lista.append(tupla)

    
    t = choice(lista)

    s1 = t[0]
    s2 = t[1]

    return s1, s2

def mcm_fracciones(fracciones):
    denominadores = []

    for f in fracciones:
        den = f.denominator
        denominadores.append(den)

    print(denominadores)
    mcm = lcm(*denominadores)

    return abs(mcm)