import json
from random import randint, shuffle
from sympy import *
from sympy.abc import x, y
from algebreb.listas.lista import Lista
from algebreb.expresiones.polinomios import (monomio_aleatorio, 
                                             binomio_aleatorio, 
                                             trinomio_aleatorio, 
                                             polinomio_coeficientes_aleatorios,
                                             polinomio_raices_aleatorias,
                                             conjugar_binomio)

from algebreb.ejercicios.factorizacion import (CuboPerfectoBinomios, 
                                              DiferenciaCuadrados, 
                                              FactorComun, 
                                              TrinomioCuadradoPerfecto, 
                                              TrinomioFormaI, 
                                              TrinomioFormaII)

class ListaFactorComun(Lista):
    def __init__(self, caracteristicas):
        super(ListaFactorComun, self).__init__(caracteristicas)
        self.instrucciones = 'Factorizar las siguientes expresiones:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = 'ZZ'
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = False
        completo = self.caracteristicas['completo']
        lista = []

        for _ in range(cantidad):
            grado1 = randint(gmin, gmax)
            grado2 = randint(gmin, gmax)

            monomio = monomio_aleatorio(grado1, variables, dominio, cmin, cmax, fraccion)
            polinomio = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            producto = monomio*polinomio
            fc = FactorComun(producto)
            fc.monomio = monomio
            fc.polinomio = polinomio
            fc.producto = producto
            fc.ver_pasos()

            monomio2 = monomio_aleatorio(grado1, variables, dominio, cmin, cmax, fraccion)
            polinomio2 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            producto2 = monomio2 * polinomio2
            fc2 = FactorComun(producto2)

            monomio3 = monomio_aleatorio(grado1, variables, dominio, cmin, cmax, fraccion)
            polinomio3 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            producto3 = monomio3 * polinomio3
            fc3 = FactorComun(producto3)

            monomio4 = monomio_aleatorio(grado1, variables, dominio, cmin, cmax, fraccion)
            polinomio4 = polinomio_coeficientes_aleatorios(grado2, variables, dominio, cmin, cmax, fraccion, completo)
            producto4 = monomio4 * polinomio4
            fc4 = FactorComun(producto4)

            fc.respuestas.append(fc.res)
            fc.respuestas.append(fc2.res)
            fc.respuestas.append(fc3.res)
            fc.respuestas.append(fc4.res)

            shuffle(fc.respuestas)

            lista.append(fc)

        return lista

class ListaDiferenciaCuadrados(Lista):
    def __init__(self, caracteristicas):
        super(ListaDiferenciaCuadrados, self).__init__(caracteristicas)
        self.instrucciones = 'Factorizar las siguientes diferencias de cuadrados:'
      

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = False
        lista = []

        for _ in range(cantidad):
            grado1 = randint(gmin, gmax)

            ba = binomio_aleatorio(grado1, variables, 'ZZ', cmin, cmax, fraccion)
            bac = conjugar_binomio(ba)
            ba_expr = ba.as_expr()
            bac_expr = bac.as_expr()
            producto = ba * bac
            dc = DiferenciaCuadrados(producto)
            dc.res = UnevaluatedExpr(ba_expr*bac_expr)
            dc.bin1 = ba
            dc.bin2 = bac
            dc.producto = producto
            dc.ver_pasos()

            ba2 = binomio_aleatorio(grado1, variables, 'ZZ', cmin, cmax, fraccion)
            bac2 = conjugar_binomio(ba2)
            ba2_expr = ba2.as_expr()
            bac2_expr = bac2.as_expr()
            producto2 = ba2 * bac2
            dc2 = DiferenciaCuadrados(producto2)
            dc2.res = UnevaluatedExpr(ba2_expr * bac2_expr)

            ba3 = binomio_aleatorio(grado1, variables, 'ZZ', cmin, cmax, fraccion)
            bac3 = conjugar_binomio(ba3)
            ba3_expr = ba3.as_expr()
            bac3_expr = bac3.as_expr()
            producto3 = ba3 * bac3
            dc3 = DiferenciaCuadrados(producto3)
            dc3.res = UnevaluatedExpr(ba3_expr * bac3_expr)

            ba4 = binomio_aleatorio(grado1, variables, 'ZZ', cmin, cmax, fraccion)
            bac4 = conjugar_binomio(ba4)
            ba4_expr = ba4.as_expr()
            bac4_expr = bac4.as_expr()
            producto4 = ba4 * bac4
            dc4 = DiferenciaCuadrados(producto4)
            dc4.res = UnevaluatedExpr(ba4_expr * bac4_expr)

            dc.respuestas.append(dc.res)
            dc.respuestas.append(dc2.res)
            dc.respuestas.append(dc3.res)
            dc.respuestas.append(dc4.res)

            shuffle(dc.respuestas)

            lista.append(dc)

        return lista

class ListaTrinomioCuadradoPerfecto(Lista):
    def __init__(self, caracteristicas):
        super(ListaTrinomioCuadradoPerfecto, self).__init__(caracteristicas)
        self.instrucciones = 'Factorizar los siguientes trinomios cuadrados perfectos:'
        

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
            prod = ba**2
            ba_expr = ba.as_expr()
            tcp = TrinomioCuadradoPerfecto(prod)
            tcp.res = UnevaluatedExpr(ba_expr**2)
            tcp.binomio = ba
            tcp.producto = prod
            tcp.ver_pasos()

            ba2 = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            prod2 = ba2**2
            ba2_expr = ba2.as_expr()
            tcp2 = TrinomioCuadradoPerfecto(prod2)
            tcp2.res = UnevaluatedExpr(ba2_expr**2)

            ba3 = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            prod3 = ba3**2
            ba3_expr = ba3.as_expr()
            tcp3 = TrinomioCuadradoPerfecto(prod3)
            tcp3.res = UnevaluatedExpr(ba3_expr**2)

            ba4 = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            prod4 = ba4**2
            ba4_expr = ba4.as_expr()
            tcp4 = TrinomioCuadradoPerfecto(prod4)
            tcp4.res = UnevaluatedExpr(ba4_expr**2)

            tcp.respuestas.append(tcp.res)
            tcp.respuestas.append(tcp2.res)
            tcp.respuestas.append(tcp3.res)
            tcp.respuestas.append(tcp4.res)

            shuffle(tcp.respuestas)

            lista.append(tcp)

        return lista

class ListaCuboPerfectoBinomios(Lista):
    def __init__(self, caracteristicas):
        super(ListaCuboPerfectoBinomios, self).__init__(caracteristicas)
        self.instrucciones = 'Factorizar los siguientes cubos perfectos de binomios:'
      

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
            prod = ba**3
            ba_expr = ba.as_expr()
            cpb = CuboPerfectoBinomios(prod)
            cpb.res = UnevaluatedExpr(ba_expr**3)
            cpb.binomio = ba
            cpb.producto = prod
            cpb.ver_pasos()

            ba2 = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            prod2 = ba2**3
            ba2_expr = ba2.as_expr()
            cpb2 = CuboPerfectoBinomios(prod2)
            cpb2.res = UnevaluatedExpr(ba2_expr**3)

            ba3 = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            prod3 = ba3**3
            ba3_expr = ba3.as_expr()
            cpb3 = CuboPerfectoBinomios(prod3)
            cpb3.res = UnevaluatedExpr(ba3_expr**3)

            ba4 = binomio_aleatorio(grado, variables, dominio, cmin, cmax, fraccion)
            prod4 = ba4**3
            ba4_expr = ba4.as_expr()
            cpb4 = CuboPerfectoBinomios(prod4)
            cpb4.res = UnevaluatedExpr(ba4_expr**3)

            cpb.respuestas.append(cpb.res)
            cpb.respuestas.append(cpb2.res)
            cpb.respuestas.append(cpb3.res)
            cpb.respuestas.append(cpb4.res)

            shuffle(cpb.respuestas)

            lista.append(cpb)

        return lista

class ListaTrinomioFormaI(Lista):
    def __init__(self, caracteristicas):
        super(ListaTrinomioFormaI, self).__init__(caracteristicas)
        self.instrucciones = 'Factorizar los siguientes trinomios:'
    

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        variables = self.caracteristicas['variables']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        lista = []

        for _ in range(cantidad):
            ba1 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            ba2 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            ba1_expr = ba1.as_expr()
            ba2_expr = ba2.as_expr()
            producto = ba1 * ba2
            tf1 = TrinomioFormaI(producto)
            tf1.res = UnevaluatedExpr(ba1_expr*ba2_expr)
            tf1.bin1 = ba1
            tf1.bin2 = ba2
            tf1.producto = producto
            tf1.ver_pasos()

            ba3 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            ba4 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            ba3_expr = ba3.as_expr()
            ba4_expr = ba4.as_expr()
            producto2 = ba3 * ba4
            tf2 = TrinomioFormaI(producto2)
            tf2.res = UnevaluatedExpr(ba3_expr*ba4_expr)

            ba5 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            ba6 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            ba5_expr = ba5.as_expr()
            ba6_expr = ba6.as_expr()
            producto3 = ba5 * ba6
            tf3 = TrinomioFormaI(producto3)
            tf3.res = UnevaluatedExpr(ba5_expr*ba6_expr)

            ba7 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            ba8 = polinomio_raices_aleatorias(1, variables, 'ZZ', cmin, cmax)
            ba7_expr = ba7.as_expr()
            ba8_expr = ba8.as_expr()
            producto4 = ba7 * ba8
            tf4 = TrinomioFormaI(producto4)
            tf4.res = UnevaluatedExpr(ba7_expr*ba8_expr)

            tf1.respuestas.append(tf1.res)
            tf1.respuestas.append(tf2.res)
            tf1.respuestas.append(tf3.res)
            tf1.respuestas.append(tf4.res)

            shuffle(tf1.respuestas)

            lista.append(tf1)

        return lista 

class ListaTrinomioFormaII(Lista):
    def __init__(self, caracteristicas):
        super(ListaTrinomioFormaII, self).__init__(caracteristicas)
        self.instrucciones = 'Factorizar los siguientes trinomios:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        variables = self.caracteristicas['variables']
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        lista = []

        for _ in range(cantidad):
            ba1 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=True)
            ba2 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=True)
            ba1_expr = ba1.as_expr()
            ba2_expr = ba2.as_expr()
            producto = ba1 * ba2
            tf2 = TrinomioFormaII(producto)
            tf2.res = UnevaluatedExpr(ba1_expr*ba2_expr)
            tf2.bin1 = ba1
            tf2.bin2 = ba2
            tf2.producto = producto
            tf2.ver_pasos()

            ba3 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            ba4 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            ba3_expr = ba3.as_expr()
            ba4_expr = ba4.as_expr()
            producto2 = ba3 * ba4
            tf3 = TrinomioFormaII(producto2)
            tf3.res = UnevaluatedExpr(ba3_expr*ba4_expr)

            ba5 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            ba6 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            ba5_expr = ba5.as_expr()
            ba6_expr = ba6.as_expr()
            producto3 = ba5 * ba6
            tf4 = TrinomioFormaII(producto3)
            tf4.res = UnevaluatedExpr(ba5_expr*ba6_expr)

            ba7 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            ba8 = polinomio_raices_aleatorias(1, variables, 'QQ', cmin, cmax, True, nulas=False, coefs_frac=False)
            ba7_expr = ba7.as_expr()
            ba8_expr = ba8.as_expr()
            producto4 = ba7 * ba8
            tf5 = TrinomioFormaII(producto4)
            tf5.res = UnevaluatedExpr(ba7_expr*ba8_expr)

            tf2.respuestas.append(tf2.res)
            tf2.respuestas.append(tf3.res)
            tf2.respuestas.append(tf4.res)
            tf2.respuestas.append(tf5.res)

            shuffle(tf2.respuestas)

            lista.append(tf2)

        return lista