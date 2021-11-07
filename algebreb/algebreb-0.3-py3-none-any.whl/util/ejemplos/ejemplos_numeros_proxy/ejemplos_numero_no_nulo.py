from algebreb.util.numeros_proxy import numero_no_nulo

entero1 = numero_no_nulo('ZZ', -100, 100)
print(entero1)

entero2 = numero_no_nulo('ZZ', -1000, 1000)
print(entero2)

decimal1 = numero_no_nulo('QQ', -100, 100)
print(entero1)

decimal2 = numero_no_nulo('QQ', -10, 10)
print(decimal2)

fraccion1 = numero_no_nulo('QQ', -100, 100, True)
print(fraccion1)

fraccion2 = numero_no_nulo('QQ', -10, 10, True)
print(fraccion2)