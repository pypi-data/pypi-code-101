# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 22:25:26 2021

@author: Yamila Design
"""

# Vamos a crear un programa para hallar números primos
# Número primo: aquel que es enteramente divisible sólo entre él mismo y el 1

print ("Vamos a  ver si un número es primo o no.")

nup=int(input("Introduce un número: "))

# Con este programa iremos calculando el resto de dividir el número introducido entre un contador
# Dicho contador bastaría con ir del 2 a n/2, pero lo hacemos desde 2 hasta n por comodidad
# Cuando el contador sea igual a n, o el resto sea 0, el bucle acaba
# No sé si los bucles están bien utilizados así o es rudimentario, pero me funciona
i=2
while True:
    resto = nup % i
    i += 1
    if(i == nup):break
    if(resto==0):break

# Calculamos n/2
# El máximo número por el que un número puede ser enteramente divisible además de él mismo
# es su mitad (entera)  
med = nup // 2

# Si el contador ha parado en un número n/2 o menor, es porque ha dado resto 0, por lo que ha sido 
# divisible entre algún número entre 2 y n/2, con lo cual NO es primo.
if (i <= med):
    print("El número " + str(nup) + " NO es primo.")
    
if (i > med):
    print("El número " + str(nup) + " es primo.")
        
        
    