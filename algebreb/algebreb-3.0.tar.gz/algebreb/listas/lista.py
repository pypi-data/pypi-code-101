class Lista:
    def __init__(self, caracteristicas):
        self.caracteristicas = caracteristicas
        self.ejercicios = self.lista_ejercicios()
        self.instrucciones = ''

    def lista_ejercicios(self):
        return []

    def as_str_latex(self):
        dicc = {}

        lista_latex = []
        lista_str = []

        for ejercicio in self.ejercicios:
            lista_latex.append(ejercicio.as_latex())
            lista_str.append(ejercicio.as_str())

        dicc['instrucciones'] = self.instrucciones
        dicc['latex'] = lista_latex
        dicc['str'] = lista_str

        return dicc

"""
    def as_str_latex(self):
        dicc = {}

        nombre = "ejercicio"
        numero = 1

        for ejercicio in self.ejercicios:
            clave = nombre + str(numero)

            dicc[clave] = ejercicio.as_str_latex()

            numero += 1
            
        return dicc
"""
