from sympy.abc import x, y, z
from algebreb.expresiones.polinomios import polinomio_coeficientes_aleatorios

p1 = polinomio_coeficientes_aleatorios(2, [x, y], 'ZZ', 1, 14)
print(p1)
print(p1.total_degree())

p2 = polinomio_coeficientes_aleatorios(5, [x], 'ZZ', -10, 10)
print(p2)
print(p2.total_degree())

p3 = polinomio_coeficientes_aleatorios(3,[x, y], 'ZZ', -67, 54, False, False)
print(p3)

p4 = polinomio_coeficientes_aleatorios(2, [x, y, z], 'QQ', -13, 27)
print(p4)

p5 = polinomio_coeficientes_aleatorios(7, [y, z], 'QQ', -1000, 1000, False, False)
print(p5)

p6 = polinomio_coeficientes_aleatorios(3, [x, z], 'QQ', 1, 20, True, True)
print(p6)

