from algebreb.util.numeros_proxy import numeros

enteros1 = numeros('ZZ', 0, 20, -100, 100)
print(enteros1)

enteros2 = numeros('ZZ', 0, 20, 1, 100)
print(enteros2)

enteros3 = numeros('ZZ', 5, 5, 1, 100)
print(enteros3)

decimales1 = numeros('QQ', 0, 20, -10, 10)
print(decimales1)

decimales2 = numeros('QQ', 0, 20, 1, 100)
print(decimales2)

decimales3 = numeros('QQ', 5, 5, 1, 10)
print(decimales3)

fracciones1 = numeros('QQ', 0, 10, -10, 10, True)
print(fracciones1)

fracciones2 = numeros('QQ', 0, 10, 1, 10, True)
print(fracciones2)

fracciones3 = numeros('QQ', 5, 5, 1, 10, True)
print(fracciones3)