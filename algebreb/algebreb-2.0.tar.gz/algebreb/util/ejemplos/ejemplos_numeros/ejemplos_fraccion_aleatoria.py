from fractions import Fraction
from algebreb.util.numeros import fraccion_aleatoria

frac1 = fraccion_aleatoria(-4, 3)
print(frac1)

excepcion = Fraction(1, 2)
frac2 = fraccion_aleatoria(1, 2, excepcion)
print(frac2)