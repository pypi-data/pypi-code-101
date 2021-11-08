from random import randint, shuffle
import json
from sympy.abc import x, y
from algebreb.listas.lista import Lista
from algebreb.expresiones.fracciones_algebraicas import (fa_aleatoria, 
                                                         fa_propia_aleatoria, 
                                                         fa_impropia_aleatoria)
from algebreb.ejercicios.operaciones_fracciones import (SumaFracAlg, 
                                                        RestaFracAlg, 
                                                        MultFracAlg, 
                                                        DivFracAlg, 
                                                        SimpFracAlg)

class ListaSumaFraccionesAlgebraicas(Lista):
    def __init__(self, caracteristicas):
        super(ListaSumaFraccionesAlgebraicas, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar las siguientes sumas de fracciones algebraicas:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = 'ZZ'
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = False
        raices = True
        lista = []

        for _ in range(cantidad):
            grado1 = randint(gmin, gmax)
            grado2 = randint(gmin, gmax)

            f1 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f2 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            suma = SumaFracAlg(f1, f2)
            suma.ver_pasos()

            f3 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f4 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            suma2 = SumaFracAlg(f3, f4)

            f5 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f6 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            suma3 = SumaFracAlg(f5, f6)

            f7 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f8 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            suma4 = SumaFracAlg(f7, f8)

            suma.respuestas.append(suma.res)
            suma.respuestas.append(suma2.res)
            suma.respuestas.append(suma3.res)
            suma.respuestas.append(suma4.res)

            shuffle(suma.respuestas)

            lista.append(suma)

        return lista

class ListaRestaFraccionesAlgebraicas(Lista):
    def __init__(self, caracteristicas):
        super(ListaRestaFraccionesAlgebraicas, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar las siguientes restas de fracciones algebraicas:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = 'ZZ'
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = False
        raices = True
        lista = []

        for _ in range(cantidad):
            grado1 = randint(gmin, gmax)
            grado2 = randint(gmin, gmax)

            f1 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f2 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            resta = RestaFracAlg(f1, f2)
            resta.ver_pasos()

            f3 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f4 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            resta2 = RestaFracAlg(f3, f4)

            f5 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f6 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            resta3 = RestaFracAlg(f5, f6)

            f7 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f8 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            resta4 = RestaFracAlg(f7, f8)

            resta.respuestas.append(resta.res)
            resta.respuestas.append(resta2.res)
            resta.respuestas.append(resta3.res)
            resta.respuestas.append(resta4.res)

            shuffle(resta.respuestas)
            
            lista.append(resta)

        return lista

class ListaMultFraccionesAlgebraicas(Lista):
    def __init__(self, caracteristicas):
        super(ListaMultFraccionesAlgebraicas, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar las siguientes multiplicaciones de fracciones algebraicas:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = 'ZZ'
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = False
        raices = True
        lista = []

        for _ in range(cantidad):
            grado1 = randint(gmin, gmax)
            grado2 = randint(gmin, gmax)

            f1 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f2 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            mult = MultFracAlg(f1, f2)
            mult.ver_pasos()

            f3 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f4 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            mult2 = MultFracAlg(f3, f4)

            f5 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f6 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            mult3 = MultFracAlg(f5, f6)

            f7 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f8 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            mult4 = MultFracAlg(f7, f8)

            mult.respuestas.append(mult.res)
            mult.respuestas.append(mult2.res)
            mult.respuestas.append(mult3.res)
            mult.respuestas.append(mult4.res)

            shuffle(mult.respuestas)
                
            lista.append(mult)

        return lista

class ListaDivFraccionesAlgebraicas(Lista):
    def __init__(self, caracteristicas):
        super(ListaDivFraccionesAlgebraicas, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar las siguientes divisiones de fracciones algebraicas:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = 'ZZ'
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = False
        raices = True
        lista = []

        for _ in range(cantidad):
            grado1 = randint(gmin, gmax)
            grado2 = randint(gmin, gmax)

            f1 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f2 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            div = DivFracAlg(f1, f2)
            div.ver_pasos()

            f3 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f4 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            div2 = DivFracAlg(f3, f4)

            f5 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f6 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            div3 = DivFracAlg(f5, f6)

            f7 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            f8 = fa_propia_aleatoria(grado2, variables, dominio, cmin, cmax, fraccion, raices)
            div4 = DivFracAlg(f7, f8)

            div.respuestas.append(div.res)
            div.respuestas.append(div2.res)
            div.respuestas.append(div3.res)
            div.respuestas.append(div4.res)

            shuffle(div.respuestas)

            lista.append(div)

        return lista

class ListaSimpFraccionesAlgebraicas(Lista):
    def __init__(self, caracteristicas):
        super(ListaSimpFraccionesAlgebraicas, self).__init__(caracteristicas)
        self.instrucciones = 'Realizar las siguientes simplificaciones de fracciones algebraicas:'

    def lista_ejercicios(self):
        cantidad = self.caracteristicas['cantidad']
        gmin = self.caracteristicas['gmin']
        gmax = self.caracteristicas['gmax']
        variables = self.caracteristicas['variables']
        dominio = 'ZZ'
        cmin = self.caracteristicas['cmin']
        cmax = self.caracteristicas['cmax']
        fraccion = False
        raices = True
        lista = []

        for _ in range(cantidad):
            grado1 = randint(gmin, gmax)

            f1 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            sim = SimpFracAlg(f1)
            sim.ver_pasos()

            f2 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            sim2 = SimpFracAlg(f2)

            f3 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            sim3 = SimpFracAlg(f3)

            f4 = fa_propia_aleatoria(grado1, variables, dominio, cmin, cmax, fraccion, raices)
            sim4 = SimpFracAlg(f4)

            sim.respuestas.append(sim.res)
            sim.respuestas.append(sim2.res)
            sim.respuestas.append(sim3.res)
            sim.respuestas.append(sim4.res)

            shuffle(sim.respuestas)
                
            lista.append(sim)

        return lista