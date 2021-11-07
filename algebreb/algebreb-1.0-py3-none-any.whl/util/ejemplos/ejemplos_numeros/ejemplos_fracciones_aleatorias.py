from fractions import Fraction
from algebreb.util.numeros import fracciones_aleatorias

fracs1 = fracciones_aleatorias(1, 10, 20)
print(fracs1)

excep = Fraction(1, 2)
fracs2 = fracciones_aleatorias(1, 2, 5, excep)
print(fracs2)