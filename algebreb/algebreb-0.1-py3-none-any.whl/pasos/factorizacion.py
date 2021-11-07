from sympy import *
from sympy.abc import a, b, c, x, y, z
from sympy import UnevaluatedExpr
from algebreb.expresiones.polinomios import Polinomio

inicio = '\\textrm{'
fin = '}'

def pasos_factor_comun_str(monomio, polinomio, producto):
    pasos = []

    monomio = monomio.as_expr()
    polinomio = polinomio.as_expr()
    producto = producto.as_expr()
    
    pasos.append('Se extrae el factor comun del polinomio {}, el cual es: {}'.format(producto, monomio))
    pasos.append('Se divide cada termino del polinomnio entre el factor comun, obteniendo {}'.format(polinomio))
    pasos.append('Se expresa el resultado de la siguiente manera {} = ({})({})'.format(producto, monomio, polinomio))

    return pasos

def pasos_factor_comun_latex(monomio, polinomio, producto):
    pasos = []

    monomio = monomio.as_expr()
    polinomio = polinomio.as_expr()
    producto = producto.as_expr()

    paso1 = inicio + 'Se extrae el factor comun del polinomio ' + fin + latex(producto) + inicio + ', el cual es: ' + fin + latex(monomio)
    paso2 = inicio + 'Se divide cada termino del polinomio entre el factor comun, obteniendo: ' + fin + latex(polinomio)
    paso3 = inicio + 'Se expresa el resultado de la siguiente manera: ' + fin + latex(producto) + inicio + ' = (' + fin + latex(monomio) + inicio + ')(' + fin + latex(polinomio) + inicio + ')' + fin
    
    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)

    return pasos

def pasos_diferencia_cuadrados_str(bin1, bin2, producto):
    pasos = []

    coeficientes_bin1 = bin1.coeffs()
    monomios_bin1 = [prod(x**k for x, k in zip(bin1.gens, mon)) for mon in bin1.monoms()]

    coeficientes_bin2 = bin2.coeffs()
    monomios_bin2 = [prod(x**k for x, k in zip(bin2.gens, mon)) for mon in bin2.monoms()]

    coeficientes_prod = producto.coeffs()
    monomios_prod = [prod(x**k for x, k in zip(producto.gens, mon)) for mon in producto.monoms()]

    ta1 = monomios_bin1[0] * coeficientes_bin1[0]
    tb1 = monomios_bin1[1] * coeficientes_bin1[1]
    ta2 = monomios_bin2[0] * coeficientes_bin2[0]
    tb2 = monomios_bin2[1] * coeficientes_bin2[1]
    ta1p = monomios_prod[0] * coeficientes_prod[0]
    tb1p = monomios_prod[1] * coeficientes_prod[1] 

    pasos.append('Se extrae la raiz cuadrada del primer termino {} = {}'.format(ta1p, ta1))
    pasos.append('Se extrae la raiz cuadrada del segundo termino {} = {}'.format(-tb1p, tb1))
    pasos.append('Finalmente la factorizacion es: {} = ({})({})'.format(producto.as_expr(), bin1.as_expr(), bin2.as_expr()))

    return pasos

def pasos_diferencia_cuadrados_latex(bin1, bin2, producto):
    pasos = []

    coeficientes_bin1 = bin1.coeffs()
    monomios_bin1 = [prod(x**k for x, k in zip(bin1.gens, mon)) for mon in bin1.monoms()]

    coeficientes_bin2 = bin2.coeffs()
    monomios_bin2 = [prod(x**k for x, k in zip(bin2.gens, mon)) for mon in bin2.monoms()]

    coeficientes_prod = producto.coeffs()
    monomios_prod = [prod(x**k for x, k in zip(producto.gens, mon)) for mon in producto.monoms()]
    
    ta1 = monomios_bin1[0] * coeficientes_bin1[0]
    tb1 = monomios_bin1[1] * coeficientes_bin1[1]
    ta2 = monomios_bin2[0] * coeficientes_bin2[0]
    tb2 = monomios_bin2[1] * coeficientes_bin2[1]
    ta1p = monomios_prod[0] * coeficientes_prod[0]
    tb1p = monomios_prod[1] * coeficientes_prod[1]

    paso1 = inicio + 'Se extrae la raiz cuadrada del primer termino ' + fin + latex(ta1p) + inicio + " = " + fin + latex(ta1)
    paso2 = inicio + 'Se extrae la raiz cuadrada del segundo termino' + fin + latex(-tb1p) + inicio + " = " + fin + latex(tb1)
    paso3 = inicio + 'Finalmente la factorizacion es: ' + fin + latex(producto.as_expr()) + inicio + ' = (' + fin + latex(bin1.as_expr()) + inicio + ')(' + fin + latex(bin2.as_expr()) + inicio + ')' + fin
    
    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)

    return pasos

def pasos_trinomio_cuadrado_perfecto_str(binomio, producto):
    pasos = []

    coeficientes_binomio = binomio.coeffs()
    monomios_binomio = [prod(x**k for x, k in zip(binomio.gens, mon)) for mon in binomio.monoms()]
    
    coeficientes_producto = producto.coeffs()
    monomios_producto = [prod(x**k for x, k in zip(producto.gens, mon)) for mon in producto.monoms()]

    ta1 = monomios_binomio[0] * coeficientes_binomio[0]
    tb1 = monomios_binomio[1] * coeficientes_binomio[1]

    ta1p = monomios_producto[0] * coeficientes_producto[0]
    tb1p = monomios_producto[1] * coeficientes_producto[1]
    tc1p = monomios_producto[2] * coeficientes_producto[2]

    signo = ''

    if coeficientes_producto[1] > 0:
        signo = '+'
    else:
        signo = '-'

    bin_expr = binomio.as_expr()

    with evaluate(False):
        u_factor = UnevaluatedExpr(bin_expr**2)

    pasos.append('Se extrae la raíz cuadrada del primer termino {}: {}'.format(ta1p, ta1))
    pasos.append('Se extrae la raiz cuadrada del ultimo termino {}: {}'.format(tc1p, tb1))
    pasos.append('Se extrae el signo del termino de en medio {}, que en este caso es {}'.format(tb1p, signo))
    pasos.append('Se unen las dos raices cuadradas mediante el signo anterior y el resultado se expresas asi: {} = {}'.format(producto.as_expr(), u_factor))

    return pasos

def pasos_trinomio_cuadrado_perfecto_latex(binomio, producto):
    pasos = []

    coeficientes_binomio = binomio.coeffs()
    monomios_binomio = [prod(x**k for x, k in zip(binomio.gens, mon)) for mon in binomio.monoms()]
    
    coeficientes_producto = producto.coeffs()
    monomios_producto = [prod(x**k for x, k in zip(producto.gens, mon)) for mon in producto.monoms()]

    ta1 = monomios_binomio[0] * coeficientes_binomio[0]
    tb1 = monomios_binomio[1] * coeficientes_binomio[1]

    ta1p = monomios_producto[0] * coeficientes_producto[0]
    tb1p = monomios_producto[1] * coeficientes_producto[1]
    tc1p = monomios_producto[2] * coeficientes_producto[2]

    signo = ''

    if coeficientes_producto[1] > 0:
        signo = '+'
    else:
        signo = '-'

    bin_expr = binomio.as_expr()

    with evaluate(False):
        u_factor = UnevaluatedExpr(bin_expr**2)

    paso1 = inicio + 'Se extrae la raíz cuadrada del primer termino ' + fin + latex(ta1p) + inicio + ': ' + fin + latex(ta1)
    paso2 = inicio + 'Se extrae la raíz cuadrada del ultimo termino ' + fin + latex(tc1p) + inicio + ': ' + fin + latex(tb1)
    paso3 = inicio + 'Se extrae el signo del termino de en medio ' + fin + latex(tb1p) + inicio + ', que en este caso es ' + fin + latex(signo)
    paso4 = inicio + 'Se unen las dos raices cuadradas mediante el signo anterior y el resultado se expresas asi: ' + fin + latex(producto.as_expr(), long_frac_ratio=oo) + inicio + ' = ' + fin + latex(u_factor, long_frac_ratio=oo)

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)
    pasos.append(paso4)

    return pasos

def pasos_cubo_perfecto_binomios_str(binomio, producto):
    pasos = []

    coeficientes_binomio = binomio.coeffs()
    monomios_binomio = [prod(x**k for x, k in zip(binomio.gens, mon)) for mon in binomio.monoms()]
    
    coeficientes_producto = producto.coeffs()
    monomios_producto = [prod(x**k for x, k in zip(producto.gens, mon)) for mon in producto.monoms()]

    ta1 = monomios_binomio[0] * coeficientes_binomio[0]
    tb1 = monomios_binomio[1] * coeficientes_binomio[1]

    ta1p = monomios_producto[0] * coeficientes_producto[0]
    tb1p = monomios_producto[1] * coeficientes_producto[1]
    tc1p = monomios_producto[2] * coeficientes_producto[2]
    td1p = monomios_producto[2] * coeficientes_producto[2]

    bin_expr = binomio.as_expr()

    with evaluate(False):
        u_factor = UnevaluatedExpr(bin_expr**3)

    pasos.append('Se extrae la raíz cubica del primer termino {}: {}'.format(ta1p, ta1))
    pasos.append('Se extrae la raiz cubica del ultimo termino {}: {}'.format(td1p, tb1))
    pasos.append('Si el signo del segundo y cuarto termino es + y - o viceversa, se escoge el signo -, si ambos signos son +, se escoge +')
    pasos.append('Se unen las dos raices cubicas mediante el signo que se escogió y el resultado se expresas asi: {} = {}'.format(producto.as_expr(), u_factor))

    return pasos

def pasos_cubo_perfecto_binomios_latex(binomio, producto):
    pasos = []

    coeficientes_binomio = binomio.coeffs()
    monomios_binomio = [prod(x**k for x, k in zip(binomio.gens, mon)) for mon in binomio.monoms()]
    
    coeficientes_producto = producto.coeffs()
    monomios_producto = [prod(x**k for x, k in zip(producto.gens, mon)) for mon in producto.monoms()]

    ta1 = monomios_binomio[0] * coeficientes_binomio[0]
    tb1 = monomios_binomio[1] * coeficientes_binomio[1]

    ta1p = monomios_producto[0] * coeficientes_producto[0]
    tb1p = monomios_producto[1] * coeficientes_producto[1]
    tc1p = monomios_producto[2] * coeficientes_producto[2]
    td1p = monomios_producto[2] * coeficientes_producto[2]

    bin_expr = binomio.as_expr()

    with evaluate(False):
        u_factor = UnevaluatedExpr(bin_expr**3)

    paso1 = inicio + 'Se extrae la raiz cubica del primer termino ' + fin + latex(ta1p) + inicio + ': ' + fin + latex(ta1)
    paso2 = inicio + 'Se extrae la raiz cubica del ultimo termino ' + fin + latex(td1p) + inicio + ': ' + fin + latex(tb1)
    paso3 = inicio + 'Si el signo del segundo y cuarto termino es + y - o viceversa, se escoge el signo -, si ambos signos son +, se escoge +' + fin
    paso4 = inicio + 'Se unen las dos raices cubicas mediante el signo que se escogio y el resultado se expresas asi: ' + fin + latex(producto.as_expr()) + inicio + ' = ' + fin + latex(u_factor)

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)
    pasos.append(paso4)

    return pasos

def pasos_trinomio_forma1_str(bin1, bin2, producto):
    pasos = []

    coeficientes_bin1 = bin1.coeffs()
    monomios_bin1 = [prod(x**k for x, k in zip(bin1.gens, mon)) for mon in bin1.monoms()]

    coeficientes_bin2 = bin2.coeffs()
    monomios_bin2 = [prod(x**k for x, k in zip(bin2.gens, mon)) for mon in bin2.monoms()]

    coeficientes_prod = producto.coeffs()
    monomios_prod = [prod(x**k for x, k in zip(producto.gens, mon)) for mon in producto.monoms()]

    bin1t1 = coeficientes_bin1[0] * monomios_bin1[0]
    bin1t2 = coeficientes_bin1[1] * monomios_bin1[1]

    bin2t1 = coeficientes_bin2[0] * monomios_bin2[0]
    bin2t2 = coeficientes_bin2[1] * monomios_bin2[1]

    prodt1 = coeficientes_prod[0] * monomios_prod[0]
    prodt2 = coeficientes_prod[1] * monomios_prod[1]
    prodt3 = coeficientes_prod[2] * monomios_prod[2]

    pasos.append('Se extrae la raiz cuadrada del termino cuadratico y se coloca el resultado en ambos factores ({}  )({}  )'.format(bin1t1, bin2t1))
    pasos.append('Se buscan dos numeros que sumados den el coeficiente del termino {} y multiplicados den el termino {}, los cuales son {} y {}'.format(prodt2, prodt3,coeficientes_bin1[1], coeficientes_bin2[1]))
    pasos.append('Se colocan los numeros dentro de los factores del paso de esta manera: ({})({})'.format(bin1.as_expr(), bin2.as_expr()))

    return pasos

def pasos_trinomio_forma1_latex(bin1, bin2, producto):
    pasos = []

    coeficientes_bin1 = bin1.coeffs()
    monomios_bin1 = [prod(x**k for x, k in zip(bin1.gens, mon)) for mon in bin1.monoms()]

    coeficientes_bin2 = bin2.coeffs()
    monomios_bin2 = [prod(x**k for x, k in zip(bin2.gens, mon)) for mon in bin2.monoms()]

    coeficientes_prod = producto.coeffs()
    monomios_prod = [prod(x**k for x, k in zip(producto.gens, mon)) for mon in producto.monoms()]

    bin1t1 = coeficientes_bin1[0] * monomios_bin1[0]
    bin1t2 = coeficientes_bin1[1] * monomios_bin1[1]

    bin2t1 = coeficientes_bin2[0] * monomios_bin2[0]
    bin2t2 = coeficientes_bin2[1] * monomios_bin2[1]

    prodt1 = coeficientes_prod[0] * monomios_prod[0]
    prodt2 = coeficientes_prod[1] * monomios_prod[1]
    prodt3 = coeficientes_prod[2] * monomios_prod[2]

    paso1 = inicio + 'Se extrae la raiz cuadrada del termino cuadratico y se coloca el resultado en ambos factores (' + fin + latex(bin1t1) + inicio + '  )(' + fin + latex(bin2t1) + inicio + '  )' + fin
    paso2 = inicio + 'Se buscan dos numeros que sumados den el coeficiente del termino ' + fin + latex(prodt2) + inicio + ' y multiplicados den el coeficiente del termino ' + fin + latex(prodt3) + inicio + ', los cuales son ' + fin + str(coeficientes_bin1[1]) + inicio + ' y ' + fin +  str(coeficientes_bin2[1])
    paso3 = inicio + 'Se colocan los numeros dentro de los factores del paso de esta manera: (' + fin + latex(bin1.as_expr()) + inicio + ')(' + fin + latex(bin2.as_expr()) + inicio + ')' + fin

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)

    return pasos

def pasos_trinomio_forma2_str(bin1, bin2, producto):
    pasos = []

    coeficientes_bin1 = bin1.coeffs()
    monomios_bin1 = [prod(x**k for x, k in zip(bin1.gens, mon)) for mon in bin1.monoms()]

    coeficientes_bin2 = bin2.coeffs()
    monomios_bin2 = [prod(x**k for x, k in zip(bin2.gens, mon)) for mon in bin2.monoms()]

    coeficientes_prod = producto.coeffs()
    monomios_prod = [prod(x**k for x, k in zip(producto.gens, mon)) for mon in producto.monoms()]

    bin1t1 = coeficientes_bin1[0] * monomios_bin1[0]
    bin1t2 = coeficientes_bin1[1] * monomios_bin1[1]

    bin2t1 = coeficientes_bin2[0] * monomios_bin2[0]
    bin2t2 = coeficientes_bin2[1] * monomios_bin2[1]

    prodt1 = coeficientes_prod[0] * monomios_prod[0]
    prodt2 = coeficientes_prod[1] * monomios_prod[1]
    prodt3 = coeficientes_prod[2] * monomios_prod[2]

    pasos.append('Se buscan dos numeros que multiplicados den el coeficiente del termino {}, los cuales son {} y {}'.format(prodt1, coeficientes_bin1[0], coeficientes_bin2[0]))
    pasos.append('Se buscan dos numeros que multiplicados den el termino {}, los cuales son {} y {}'.format(prodt3, coeficientes_bin1[1], coeficientes_bin2[1]))
    pasos.append('Se multiplican ({})({}) = {} y ({})({}) = {}'.format(coeficientes_bin1[0], coeficientes_bin2[1], coeficientes_bin1[0]*coeficientes_bin2[1], coeficientes_bin1[1], coeficientes_bin2[0], coeficientes_bin1[1]*coeficientes_bin2[0]))
    pasos.append('Se suman los productos anteriores ({}) + ({}) = {}'.format(coeficientes_bin1[0]*coeficientes_bin2[1], coeficientes_bin1[1]*coeficientes_bin2[0], coeficientes_bin1[0]*coeficientes_bin2[1] + coeficientes_bin1[1]*coeficientes_bin2[0]))
    pasos.append('Se acomodan los productos obtenidos de la siguiente manera: ({})({}) = {}'.format(bin1.as_expr(), bin2.as_expr(), producto.as_expr()))

    return pasos

def pasos_trinomio_forma2_latex(bin1, bin2, producto):
    pasos = []

    coeficientes_bin1 = bin1.coeffs()
    monomios_bin1 = [prod(x**k for x, k in zip(bin1.gens, mon)) for mon in bin1.monoms()]

    coeficientes_bin2 = bin2.coeffs()
    monomios_bin2 = [prod(x**k for x, k in zip(bin2.gens, mon)) for mon in bin2.monoms()]

    coeficientes_prod = producto.coeffs()
    monomios_prod = [prod(x**k for x, k in zip(producto.gens, mon)) for mon in producto.monoms()]

    bin1t1 = coeficientes_bin1[0] * monomios_bin1[0]
    bin1t2 = coeficientes_bin1[1] * monomios_bin1[1]

    bin2t1 = coeficientes_bin2[0] * monomios_bin2[0]
    bin2t2 = coeficientes_bin2[1] * monomios_bin2[1]

    prodt1 = coeficientes_prod[0] * monomios_prod[0]
    prodt2 = coeficientes_prod[1] * monomios_prod[1]
    prodt3 = coeficientes_prod[2] * monomios_prod[2]

    p1 = coeficientes_bin1[0]*coeficientes_bin2[1]
    p2 = coeficientes_bin1[1]*coeficientes_bin2[0]

    paso1 = inicio + 'Se buscan dos numeros que multiplicados den el coeficiente del termino ' + fin + latex(prodt1) + inicio + ', los cuales son ' + fin + str(coeficientes_bin1[0]) + inicio + ' y ' + fin + str(coeficientes_bin2[0])
    paso2 = inicio + 'Se buscan dos numeros que multiplicados den el termino ' + fin + latex(prodt3) + inicio + ', los cuales son ' + fin + str(coeficientes_bin1[1]) + inicio + ' y ' + fin + str(coeficientes_bin2[1])
    paso3 = inicio + 'Se multiplican (' + fin + str(coeficientes_bin1[0]) + inicio + ')(' + fin + str(coeficientes_bin2[1]) + inicio + ') = ' + fin + str(coeficientes_bin1[0]*coeficientes_bin2[1]) + inicio + ' y (' + fin + str(coeficientes_bin1[1]) + inicio + ')(' + fin + str(coeficientes_bin2[0]) + inicio + ') = ' + fin + str(coeficientes_bin1[1]*coeficientes_bin2[0])
    paso4 = inicio + 'Se suman los productos anteriores (' + fin + str(coeficientes_bin1[0]*coeficientes_bin2[1]) + inicio + ') + (' + fin + str(coeficientes_bin1[1]*coeficientes_bin2[0]) + inicio + ') = ' + fin + str(coeficientes_bin1[0]*coeficientes_bin2[1] + coeficientes_bin1[1]*coeficientes_bin2[0])
    paso5 = inicio + 'Se acomodan los productos obtenidos de la siguiente manera: (' + fin + latex(bin1.as_expr()) + inicio + ')(' + fin + latex(bin2.as_expr()) + inicio + ') = ' + fin + latex(producto.as_expr())

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)
    pasos.append(paso4)
    pasos.append(paso5)
    
    return pasos