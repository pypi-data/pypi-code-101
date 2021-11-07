from algebreb.util.numeros_proxy import numeros_no_nulos

enteros1 = numeros_no_nulos('ZZ', 10, -100, 100)
print(enteros1)

enteros2 = numeros_no_nulos('ZZ', 10, -1, 1)
print(enteros2)

decimales1 = numeros_no_nulos('QQ', 10, -100, 100)
print(decimales1)

decimales2 = numeros_no_nulos('QQ', 10, -1, 1)
print(decimales2)

fracciones1 = numeros_no_nulos('QQ', 10, -100, 100, True)
print(fracciones1)

fracciones2 = numeros_no_nulos('QQ', 10, -1, 1, True)
print(fracciones2)