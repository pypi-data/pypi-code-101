from random import randint, choice, shuffle
from sympy import *
from sympy.abc import x, y
from algebreb.listas.lista import Lista
from algebreb.expresiones.polinomios import (polinomio_coeficientes_aleatorios,
                                             polinomio_raices_aleatorias)

from algebreb.ejercicios.operaciones_polinomio import (SumaPolinomios, 
                                                       RestaPolinomios, 
                                                       MultPolinomios,
                                                       DivPolinomios,
                                                       GradoPolinomio,
                                                       TermPolinomio) 

import json

class ListaSumaPolinomios(Lista):
    def __init__(self, caracteristicas):
        super(ListaSumaPolinomios, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar las siguientes sumas de polinomios:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = self.caracteristicas['dominio']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = self.caracteristicas['fraccion']
        completo = self.caracteristicas['completo']
        lista = []

        for _ in range(cantidad):
            grado1 = randint(gmin, gmax)
            grado2 = randint(gmin, gmax)

            p1 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)
            p2 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            suma = SumaPolinomios(p1, p2)
            suma.ver_pasos()
            
            p3 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)
            p4 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            suma2 = SumaPolinomios(p3, p4)

            p5 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)
            p6 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            suma3 = SumaPolinomios(p5, p6)

            p7 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)
            p8 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            suma4 = SumaPolinomios(p7, p8)

            suma.respuestas.append(suma.res)
            suma.respuestas.append(suma2.res)
            suma.respuestas.append(suma3.res)
            suma.respuestas.append(suma4.res)

            shuffle(suma.respuestas)

            lista.append(suma)

        return lista

class ListaRestaPolinomios(Lista):
    def __init__(self, caracteristicas):
        super(ListaRestaPolinomios, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar las siguientes restas de polinomios:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = self.caracteristicas['dominio']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = self.caracteristicas['fraccion']
        completo = self.caracteristicas['completo']
        lista = []

        for _ in range(cantidad):
            grado1 = randint(gmin, gmax)
            grado2 = randint(gmin, gmax)

            p1 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)
            p2 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            resta = RestaPolinomios(p1, p2)
            resta.ver_pasos()

            p3 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)
            p4 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            resta2 = RestaPolinomios(p3, p4)

            p5 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)
            p6 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            resta3 = RestaPolinomios(p5, p6)

            p7 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)
            p8 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            resta4 = RestaPolinomios(p7, p8)

            resta.respuestas.append(resta.res)
            resta.respuestas.append(resta2.res)
            resta.respuestas.append(resta3.res)
            resta.respuestas.append(resta4.res)

            shuffle(resta.respuestas)


            lista.append(resta)

        return lista

class ListaMultPolinomios(Lista):
    def __init__(self, caracteristicas):
        super(ListaMultPolinomios, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar las siguientes multiplicaciones de polinomios:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = self.caracteristicas['dominio']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = self.caracteristicas['fraccion']
        completo = self.caracteristicas['completo']
        lista = []

        for _ in range(cantidad):
            grado1 = randint(gmin, gmax)
            grado2 = randint(gmin, gmax)

            p1 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)
            p2 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            mult = MultPolinomios(p1, p2)
            mult.ver_pasos()

            p3 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)
            p4 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            mult2 = MultPolinomios(p3, p4)

            p5 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)
            p6 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            mult3 = MultPolinomios(p5, p6)

            p7 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)
            p8 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            mult4 = MultPolinomios(p7, p8)

            mult.respuestas.append(mult.res)
            mult.respuestas.append(mult2.res)
            mult.respuestas.append(mult3.res)
            mult.respuestas.append(mult4.res)

            shuffle(mult.respuestas)

            lista.append(mult)

        return lista

class ListaDivPolinomios(Lista):
    def __init__(self, caracteristicas):
        super(ListaDivPolinomios, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar las siguientes divisiones de polinomios:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        exacta = self.caracteristicas['exacta']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = self.caracteristicas['dominio']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = self.caracteristicas['fraccion']
        completo = self.caracteristicas['completo']
        lista = []

        for _ in range(cantidad):
            if exacta:
                grado1 = randint(gmin, gmax)
                grado2 = randint(gmin, gmax)

                p1 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                p2 = polinomio_raices_aleatorias(grado2, variables, dominio, cmin, cmax, fraccion, completo)
                producto = p1 * p2
                divisor = choice([p1, p2])

                div = DivPolinomios(producto, divisor)

                p3 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                p4 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                producto2 = p3 * p4
                divisor2 = choice([p3, p4])
                div2 = DivPolinomios(producto2, divisor2)

                p5 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                p6 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                producto3 = p5 * p6
                divisor3 = choice([p5, p6])
                div3 = DivPolinomios(producto3, divisor3)

                p7 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                p8 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                producto4 = p7 * p8
                divisor4 = choice([p7, p8])
                div4 = DivPolinomios(producto4, divisor4)

                div.respuestas.append(div.cociente)
                div.respuestas.append(div2.cociente)
                div.respuestas.append(div3.cociente)
                div.respuestas.append(div4.cociente)

                shuffle(div.respuestas)

                lista.append(div)
            else:
                grado1 = randint(gmin, gmax)
                grado2 = randint(gmin, gmax)

                p1 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                p2 = polinomio_raices_aleatorias(grado2, variables, dominio, cmin, cmax, fraccion, completo)
                div = DivPolinomios(p1, p2)

                p3 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                p4 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                div2 = DivPolinomios(p3, p4)

                p5 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                p6 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                div3 = DivPolinomios(p5, p6)

                p7 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                p8 = polinomio_raices_aleatorias(grado1, variables, dominio, cmin, cmax, fraccion, completo)
                div4 = DivPolinomios(p7, p8)

                div.respuestas.append(div.cociente)
                div.respuestas.append(div2.cociente)
                div.respuestas.append(div3.cociente)
                div.respuestas.append(div4.cociente)

                shuffle(div.respuestas)

                lista.append(div)

        return lista

class ListaGradoPolinomios(Lista):
    def __init__(self, caracteristicas):
        super(ListaGradoPolinomios, self).__init__(caracteristicas)
        self.instrucciones = 'Mencionar el grado de los siguientes polinomios:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = self.caracteristicas['dominio']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = self.caracteristicas['fraccion']
        completo = self.caracteristicas['completo']
        lista = []

        for _ in range(cantidad):
            grado1 = randint(gmin, gmax)

            p1 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)

            grado = GradoPolinomio(p1)
            
            r1 = randint(gmin, gmax)
            grado.respuestas.append(r1)
            r2 = randint(gmin, gmax)
            grado.respuestas.append(r2)
            r3 = randint(gmin, gmax)
            grado.respuestas.append(r3)
            grado.respuestas.append(grado.res)

            shuffle(grado.respuestas)

            lista.append(grado)

        return lista

class ListaTermPolinomio(Lista):
    def __init__(self, caracteristicas):
        super(ListaTermPolinomio, self).__init__(caracteristicas)
        self.instrucciones = 'Mencionar el tipo de expresión (monomio, binomio, trinomio o polinomio):'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = self.caracteristicas['dominio']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = self.caracteristicas['fraccion']
        completo = self.caracteristicas['completo']
        lista = []

        for _ in range(cantidad):
            grado1 = randint(gmin, gmax)

            p1 = polinomio_coeficientes_aleatorios(grado1, variables, dominio, cmin, cmax, fraccion, completo)

            term = TermPolinomio(p1)
            
            term.respuestas.append('Monomio')
            term.respuestas.append('Binomio')
            term.respuestas.append('Trinomio')
            term.respuestas.append('Polinomio')

            shuffle(term.respuestas)

            lista.append(term)

        return lista