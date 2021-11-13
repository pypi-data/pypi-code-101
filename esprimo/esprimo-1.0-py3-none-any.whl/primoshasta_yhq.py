# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 22:25:26 2021

@author: Yamila Design
"""

# Vamos a crear un programa para hallar números primos hasta el número indicado

print ("Sacaremos en pantalla todos los primos hasta el número introducido.")

num=int(input("Introduce un número: "))
listaprim = [1,2]

# Creamos una función que nos devuelva si un número es primo(True) o no(False)

def esPrimo (n):
    i=2
    while True:
        resto = n % i
        if(i == n):break
        if(resto==0):break
        i += 1
    med = n // 2
    if (i <= med):
        return False
    else:
        return True
    
# Ahora otra función que recorra todos los números hasta el indicado
# y utilice la función anterior para crear una lista de primos

def sacarNumeros (m):
    for i in range (3,m+1):
        if(esPrimo(i)):
            listaprim.append(i)
    return listaprim

sacarNumeros(num)
print(*listaprim)
    