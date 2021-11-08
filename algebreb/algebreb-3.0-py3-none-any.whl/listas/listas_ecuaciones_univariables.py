from random import randint, choice, shuffle
from sympy import *
from sympy.abc import x, y
from algebreb.listas.lista import Lista
from algebreb.expresiones.polinomios import Polinomio, polinomio_raices_aleatorias
from algebreb.ejercicios.ecuaciones_univariables import EcuacionLineal, EcuacionCuadratica

class ListaEcuacionesGrado1(Lista):
    def __init__(self, caracteristicas):
        super(ListaEcuacionesGrado1, self).__init__(caracteristicas)
        print(caracteristicas)
        self.instrucciones = 'Resolver las siguientes ecuaciones lineales:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        variables = self.caracteristicas['variables']
        dominio = self.caracteristicas['dominio']
        fraccion = self.caracteristicas['fraccion']
        lista = []

        for _ in range(cantidad):
            ld = polinomio_raices_aleatorias(1, variables, dominio, cmin, cmax, fraccion)
            li = Polinomio(0, variables)
            ec = EcuacionLineal(ld, li)

            lista.append(ec)

        return lista

class ListaEcuacionesGrado2(Lista):
    def __init__(self, caracteristicas):
        super(ListaEcuacionesGrado2, self).__init__(caracteristicas)
        print(caracteristicas)
        self.instrucciones = 'Resolver las siguientes ecuaciones cuadráticas:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        variables = self.caracteristicas['variables']
        dominio = self.caracteristicas['dominio']
        fraccion = self.caracteristicas['fraccion']
        lista = []

        for _ in range(cantidad):
            ld = polinomio_raices_aleatorias(2, variables, dominio, cmin, cmax, fraccion)
            li = Polinomio(0, variables)
            ec = EcuacionCuadratica(ld, li)

            lista.append(ec)

        return lista