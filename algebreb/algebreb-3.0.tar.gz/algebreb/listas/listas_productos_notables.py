from random import randint, shuffle
import json
from sympy.abc import x, y
from algebreb.listas.lista import Lista
from algebreb.expresiones.polinomios import (binomio_aleatorio, 
                                             trinomio_aleatorio,
                                             conjugar_binomio,
                                             polinomio_raices_aleatorias)
from algebreb.ejercicios.productos_notables import (BinomioAlCuadrado,
                                                    BinomioAlCubo, 
                                                    BinomiosConjugados, 
                                                    BinomiosFormaI, 
                                                    BinomiosFormaII,
                                                    TrinomioAlCuadrado)

class ListaBinomioAlCuadrado(Lista):
    def __init__(self, caracteristicas) -> None:
        super(ListaBinomioAlCuadrado, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar los siguientes binomios al cuadrado:'


    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = self.caracteristicas['dominio']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = self.caracteristicas['fraccion']
        lista = []

        for _ in range(cantidad):
            grado = randint(gmin, gmax)
            ba = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)

            bincuad = BinomioAlCuadrado(ba)
            bincuad.ver_pasos()

            r1 = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            bincuad2 = BinomioAlCuadrado(r1)
            r2 = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            bincuad3 = BinomioAlCuadrado(r2)
            r3 = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            bincuad4 = BinomioAlCuadrado(r3)

            bincuad.respuestas.append(bincuad2.res)
            bincuad.respuestas.append(bincuad3.res)
            bincuad.respuestas.append(bincuad4.res)
            bincuad.respuestas.append(bincuad.res)

            shuffle(bincuad.respuestas)
            
            lista.append(bincuad)

        return lista

class ListaBinomioAlCubo(Lista):
    def __init__(self, caracteristicas) -> None:
        super(ListaBinomioAlCubo, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar los siguientes binomios al cubos:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = self.caracteristicas['dominio']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = self.caracteristicas['fraccion']
        lista = []

        for _ in range(cantidad):
            grado = randint(gmin, gmax)
            ba = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            bincub = BinomioAlCubo(ba)
            bincub.ver_pasos()

            r1 = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            bincub2 = BinomioAlCubo(r1)
            r2 = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            bincub3 = BinomioAlCubo(r2)
            r3 = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            bincub4 = BinomioAlCubo(r3)

            bincub.respuestas.append(bincub2.res)
            bincub.respuestas.append(bincub3.res)
            bincub.respuestas.append(bincub4.res)
            bincub.respuestas.append(bincub.res)

            shuffle(bincub.respuestas)

            lista.append(bincub)

        return lista 

class ListaBinomiosConjugados(Lista):
    def __init__(self, caracteristicas) -> None:
        super(ListaBinomiosConjugados, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar los siguientes binomios conjugados:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = self.caracteristicas['dominio']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = self.caracteristicas['fraccion']
        lista = []

        for _ in range(cantidad):
            grado1 = randint(gmin, gmax)
            ba = binomio_aleatorio(grado1, variables, dominio, cmin, cmax, fraccion)
            bac = conjugar_binomio(ba)
            binconj = BinomiosConjugados(ba, bac)
            binconj.ver_pasos()

            r1 = binomio_aleatorio(grado1, variables, dominio, cmin, cmax, fraccion)
            r1c = conjugar_binomio(r1)
            binconj2 = BinomiosConjugados(r1, r1c)

            r2 = binomio_aleatorio(grado1, variables, dominio, cmin, cmax, fraccion)
            r2c = conjugar_binomio(r2)
            binconj3 = BinomiosConjugados(r2, r2c)

            r3 = binomio_aleatorio(grado1, variables, dominio, cmin, cmax, fraccion)
            r3c = conjugar_binomio(r3)
            binconj4 = BinomiosConjugados(r3, r3c)

            binconj.respuestas.append(binconj2.res)
            binconj.respuestas.append(binconj3.res)
            binconj.respuestas.append(binconj4.res)
            binconj.respuestas.append(binconj.res)

            shuffle(binconj.respuestas)

            lista.append(binconj)

        return lista 

class ListaBinomiosFormaI(Lista):
    def __init__(self, caracteristicas) -> None:
        super(ListaBinomiosFormaI, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar los siguientes binomios con término común:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        variables = self.caracteristicas['variables']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        lista = []

        for _ in range(cantidad):
            ba1 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            ba2 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            binf1 = BinomiosFormaI(ba1, ba2)
            binf1.ver_pasos()

            r1 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            r11 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            binf12 = BinomiosFormaI(r1, r11)

            r2 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            r22 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            binf13 = BinomiosFormaI(r2, r22)

            r3 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            r33 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            binf14 = BinomiosFormaI(r3, r33)

            binf1.respuestas.append(binf12.res)
            binf1.respuestas.append(binf13.res)
            binf1.respuestas.append(binf14.res)
            binf1.respuestas.append(binf1.res)

            shuffle(binf1.respuestas)

            lista.append(binf1)

        return lista 

class ListaBinomiosFormaII(Lista):
    def __init__(self, caracteristicas) -> None:
        super(ListaBinomiosFormaII, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar los siguientes productos de binomios:'
    

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        variables = self.caracteristicas['variables']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        lista = []

        for _ in range(cantidad):
            ba1 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            ba2 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            binf2 = BinomiosFormaII(ba1, ba2)
            binf2.ver_pasos()

            r1 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            r11 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            binf22 = BinomiosFormaII(r1, r11)

            r2 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            r22 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            binf23 = BinomiosFormaII(r2, r22)

            r3 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            r33 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            binf24 = BinomiosFormaII(r3, r33)

            binf2.respuestas.append(binf22.res)
            binf2.respuestas.append(binf23.res)
            binf2.respuestas.append(binf24.res)
            binf2.respuestas.append(binf2.res)

            shuffle(binf2.respuestas)

            lista.append(binf2)

        return lista

class ListaTrinomioAlCuadrado(Lista):
    def __init__(self, caracteristicas) -> None:
        super(ListaTrinomioAlCuadrado, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar los siguientes trinomios al cuadrado:'
      

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = self.caracteristicas['dominio']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = self.caracteristicas['fraccion']
        lista = []

        for _ in range(cantidad):
            grado = randint(gmin, gmax)
            ba = trinomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            trincuad = TrinomioAlCuadrado(ba)
            trincuad.ver_pasos()

            r1 = trinomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            trincuad2 = TrinomioAlCuadrado(r1)
            r2 = trinomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            trincuad3 = TrinomioAlCuadrado(r2)
            r3 = trinomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            trincuad4 = TrinomioAlCuadrado(r3)

            trincuad.respuestas.append(trincuad2.res)
            trincuad.respuestas.append(trincuad3.res)
            trincuad.respuestas.append(trincuad4.res)
            trincuad.respuestas.append(trincuad.res)

            shuffle(trincuad.respuestas)

            lista.append(trincuad)

        return lista