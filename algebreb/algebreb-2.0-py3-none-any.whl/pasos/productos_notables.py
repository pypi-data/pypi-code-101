from sympy import *
from sympy.abc import a, b, c, x, y, z
from sympy import UnevaluatedExpr
from algebreb.expresiones.polinomios import Polinomio

inicio = '\\textrm{'
fin = '}'

def pasos_binomio_al_cuadrado_latex(binomio):
    pasos = []

    coeficientes = binomio.coeffs()
    monomios = [prod(x**k for x, k in zip(binomio.gens, mon)) for mon in binomio.monoms()]

    ta = monomios[0] * coeficientes[0]
    tb = monomios[1] * coeficientes[1]

    with evaluate(False):
        u_ta2 = UnevaluatedExpr(ta**2)
        u_tb2 = UnevaluatedExpr(tb**2)
        u_tatb2 = UnevaluatedExpr(2*ta*tb)

    ta2 = ta**2
    tb2 = tb**2
    tatb2 = 2*ta*tb
    res = ta2 + tatb2 + tb2

    paso1 = inicio + 'El cuadrado del primer termino ' + fin + latex(u_ta2) + inicio + ' = ' + fin + latex(ta2)
    paso2 = inicio + 'El doble producto del primer termino por el segundo ' + fin + latex(u_tatb2) + inicio + ' = ' + fin + latex(tatb2)
    paso3 = inicio + 'El cuadrado del segundo termino ' + fin + latex(u_tb2) + inicio + ' = ' + fin + latex(tb2)
    paso4 = inicio + 'Se suman los terminos resultantes y se obtiene: ' + fin + latex(res)

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)
    pasos.append(paso4)

    return pasos

def pasos_binomio_al_cuadrado_str(binomio):
    pasos = []

    coeficientes = binomio.coeffs()
    monomios = [prod(x**k for x, k in zip(binomio.gens, mon)) for mon in binomio.monoms()]


    ta = monomios[0] * coeficientes[0]
    tb = monomios[1] * coeficientes[1]

    with evaluate(False):
        u_ta2 = UnevaluatedExpr(ta**2)
        u_tb2 = UnevaluatedExpr(tb**2)
        u_tatb2 = UnevaluatedExpr(2*ta*tb)

    ta2 = ta**2
    tb2 = tb**2
    tatb2 = 2*ta*tb
    res = ta2 + tatb2 + tb2

    pasos.append('El cuadrado del primer termino {} = {}'.format(u_ta2, ta2))
    pasos.append('El doble producto del primer termino por el segundo {} = {}'.format(u_tatb2, tatb2))
    pasos.append('El cuadrado del segundo termino {} = {}'.format(u_tb2, tb2))
    pasos.append('Se suman los terminos resultantes y se obtiene: {}'.format(res))

    return pasos

def pasos_binomio_al_cubo_str(binomio):
    pasos = []

    coeficientes = binomio.coeffs()
    monomios = [prod(x**k for x, k in zip(binomio.gens, mon)) for mon in binomio.monoms()]

    ta = monomios[0] * coeficientes[0]
    tb = monomios[1] * coeficientes[1]

    with evaluate(False):
        u_ta3 = ta**3
        u_ta2tb = 3*ta**2*tb
        u_tatb2 = 3*ta*tb**2
        u_tb3 = tb**3

    ta3 = ta**3
    ta2tb = 3*ta**2*tb
    tatb2 = 3*ta*tb**2
    tb3 = tb**3
    res = ta3 + ta2tb + tatb2 + tb3

    pasos.append('El cubo del primer termino {} = {}'.format(u_ta3, ta3))
    pasos.append('El triple del cuadrado del primer termino por el segundo {} = {}'.format(u_ta2tb, ta2tb))
    pasos.append('El triple del primer termino por el cuadrado del segundo {} = {}'.format(u_tatb2, tatb2))
    pasos.append('El cubo del segundo termino {} = {}'.format(u_tb3, tb3))
    pasos.append('Estos resultados se suman y se obtiene: {}'.format(res))

    return pasos

def pasos_binomio_al_cubo_latex(binomio):
    pasos = []

    coeficientes = binomio.coeffs()
    monomios = [prod(x**k for x, k in zip(binomio.gens, mon)) for mon in binomio.monoms()]

    ta = monomios[0] * coeficientes[0]
    tb = monomios[1] * coeficientes[1]

    with evaluate(False):
        u_ta3 = ta**3
        u_ta2tb = 3*ta**2*tb
        u_tatb2 = 3*ta*tb**2
        u_tb3 = tb**3

    ta3 = ta**3
    ta2tb = 3*ta**2*tb
    tatb2 = 3*ta*tb**2
    tb3 = tb**3
    res = ta3 + ta2tb + tatb2 + tb3

    paso1 = inicio + 'El cubo del primer termino ' + fin + latex(u_ta3) + inicio + ' = ' + fin + latex(ta3)
    paso2 = inicio + 'El triple del cuadrado del primer termino por el segundo ' + fin + latex(u_ta2tb) + inicio + ' = ' + fin + latex(ta2tb)
    paso3 = inicio + 'El triple del primer termino por el cuadrado del segundo ' + fin + latex(u_tatb2) + inicio + ' = ' + fin + latex(tatb2)
    paso4 = inicio + 'El cubo del segundo termino ' + fin + latex(u_tb3) + inicio + ' = ' + fin + latex(tb3)
    paso5 = inicio + 'Estos resultados se suman y se obtiene: ' + fin + latex(res)

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)
    pasos.append(paso4)
    pasos.append(paso5)

    return pasos

def pasos_trinomio_al_cuadrado_str(trinomio):
    pasos = []

    coeficientes = trinomio.coeffs()
    monomios = [prod(x**k for x, k in zip(trinomio.gens, mon)) for mon in trinomio.monoms()]

    ta = monomios[0] * coeficientes[0]
    tb = monomios[1] * coeficientes[1]
    tc = monomios[2] * coeficientes[2]

    with evaluate(False):
        u_ta2 = ta**2
        u_tb2 = tb**2
        u_tc2 = tc**2
        u_tab2 = 2*ta*tb 
        u_tac2 = 2*ta*tc
        u_tbc2 = 2*tb*tc

    ta2 = ta**2
    tb2 = tb**2
    tc2 = tc**2
    tab2 = 2*ta*tb 
    tac2 = 2*ta*tc
    tbc2 = 2*tb*tc

    res = ta2 + tb2 + tc2 + tab2 + tac2 + tbc2

    pasos.append('El cuadrado del primer termino {} = {}'.format(u_ta2, ta2))
    pasos.append('El cuadrado del segundo termino {} = {}'.format(u_tb2, tb2))
    pasos.append('El cuadrado del tercer termino {} = {}'.format(u_tc2, tc2))
    pasos.append('El doble del primer termino por el segundo {} = {}'.format(u_tab2, tab2))
    pasos.append('El doble del primer termino por el tercero {} = {}'.format(u_tac2, tac2))
    pasos.append('El doble del segundo termino por el tercero {} = {}'.format(u_tbc2, tbc2))
    pasos.append('Estos resultados se suman y se obtiene: {}'.format(res))

    return pasos

def pasos_trinomio_al_cuadrado_latex(trinomio):
    pasos = []

    coeficientes = trinomio.coeffs()
    monomios = [prod(x**k for x, k in zip(trinomio.gens, mon)) for mon in trinomio.monoms()]

    ta = monomios[0] * coeficientes[0]
    tb = monomios[1] * coeficientes[1]
    tc = monomios[2] * coeficientes[2]

    with evaluate(False):
        u_ta2 = ta**2
        u_tb2 = tb**2
        u_tc2 = tc**2
        u_tab2 = 2*ta*tb 
        u_tac2 = 2*ta*tc
        u_tbc2 = 2*tb*tc

    ta2 = ta**2
    tb2 = tb**2
    tc2 = tc**2
    tab2 = 2*ta*tb 
    tac2 = 2*ta*tc
    tbc2 = 2*tb*tc

    res = ta2 + tb2 + tc2 + tab2 + tac2 + tbc2

    paso1 = inicio + 'El cuadrado del primer termino ' + fin + latex(u_ta2) + inicio + ' = ' + fin + latex(ta2)
    paso2 = inicio + 'El cuadrado del segundo termino ' + fin + latex(u_tb2) + inicio + ' = ' + fin + latex(tb2)
    paso3 = inicio + 'El cuadrado del tercer termino ' + fin + latex(u_tc2) + inicio + ' = ' + fin + latex(tc2)
    paso4 = inicio + 'El doble del primer termino por el segundo ' + fin + latex(u_tab2) + inicio + ' = ' + fin + latex(tab2)
    paso5 = inicio + 'El doble del primer termino por el tercero ' + fin + latex(u_tac2) + inicio + ' = ' + fin + latex(tac2)
    paso6 = inicio + 'El doble del segundo termino por el tercero ' + fin + latex(u_tbc2) + inicio + ' = ' + fin + latex(tbc2)
    paso7 = inicio + 'Estos resultados se suman y se obtiene: ' + fin + latex(res)

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)
    pasos.append(paso4)
    pasos.append(paso5)
    pasos.append(paso6)
    pasos.append(paso7)

    return pasos

def pasos_binomios_conjugados_str(bin1, bin2):
    pasos = []

    coeficientes_bin1 = bin1.coeffs()
    monomios_bin1 = [prod(x**k for x, k in zip(bin1.gens, mon)) for mon in bin1.monoms()]

    coeficientes_bin2 = bin2.coeffs()
    monomios_bin2 = [prod(x**k for x, k in zip(bin2.gens, mon)) for mon in bin2.monoms()]

    ta1 = monomios_bin1[0] * coeficientes_bin1[0]
    tb1 = monomios_bin1[1] * coeficientes_bin1[1]
    ta2 = monomios_bin2[0] * coeficientes_bin2[0]
    tb2 = monomios_bin2[1] * coeficientes_bin2[1]

    with evaluate(False):
        u_term1 = UnevaluatedExpr(ta1**2)
        u_term2 = UnevaluatedExpr(tb1**2)

    term1 = ta1**2
    term2 = tb1**2
    res = term1 - term2

    pasos.append('El cuadrado del termino que no cambia de signo {} = {}'.format(u_term1, term1))
    pasos.append('El cuadrado del termino que cambia de signo {} = {}'.format(u_term2, term2))
    pasos.append('Finalmente, se realiza la diferencia y el resultado es: {}'.format(res))
    
    return pasos

def pasos_binomios_conjugados_latex(bin1, bin2):
    pasos = []

    coeficientes_bin1 = bin1.coeffs()
    monomios_bin1 = [prod(x**k for x, k in zip(bin1.gens, mon)) for mon in bin1.monoms()]

    coeficientes_bin2 = bin2.coeffs()
    monomios_bin2 = [prod(x**k for x, k in zip(bin2.gens, mon)) for mon in bin2.monoms()]

    ta1 = monomios_bin1[0] * coeficientes_bin1[0]
    tb1 = monomios_bin1[1] * coeficientes_bin1[1]
    ta2 = monomios_bin2[0] * coeficientes_bin2[0]
    tb2 = monomios_bin2[1] * coeficientes_bin2[1]

    with evaluate(False):
        u_term1 = UnevaluatedExpr(ta1**2)
        u_term2 = UnevaluatedExpr(tb1**2)

    term1 = ta1**2
    term2 = tb1**2
    res = term1 - term2

    paso1 = inicio + 'El cuadrado del termino que no cambia de signo ' + fin + latex(u_term1) + inicio + ' = ' + fin + latex(term1)
    paso2 = inicio + 'El cuadrado del termino que cambia de signo ' + fin + latex(u_term2) + inicio + ' = ' + fin + latex(term2)
    paso3 = inicio + 'Finalmente, se realiza la diferencia y el resultado es: ' + fin + latex(res)

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)
    
    return pasos

def pasos_binomios_forma1_str(bin1, bin2):
    pasos = []

    coeficientes_bin1 = bin1.coeffs()
    monomios_bin1 = [prod(x**k for x, k in zip(bin1.gens, mon)) for mon in bin1.monoms()]

    coeficientes_bin2 = bin2.coeffs()
    monomios_bin2 = [prod(x**k for x, k in zip(bin2.gens, mon)) for mon in bin2.monoms()]

    ta1 = monomios_bin1[0] * coeficientes_bin1[0]
    tb1 = monomios_bin1[1] * coeficientes_bin1[1]
    ta2 = monomios_bin2[0] * coeficientes_bin2[0]
    tb2 = monomios_bin2[1] * coeficientes_bin2[1]

    term1 = ta1**2
    term2 = (tb1 + tb2) * ta1
    term3 = tb1 * tb2
    suma = term1 + term2 + term3

    with evaluate(False):
        u_term1 = ta1**2
        u_term2 = (tb1 + tb2) * ta1
        u_term3 = '({})({})'.format(tb1, tb2)

    pasos.append('El cuadrado del término común {} = {}'.format(u_term1, term1))
    pasos.append('La suma de los términos no comunes {} = {}'.format(u_term2, term2))
    pasos.append('El producto de los términos no comunes {} = {}'.format(u_term3, term3))
    pasos.append('Se suman los términos anteriores y se obtiene como resultado {}'.format(suma))

    return pasos

def pasos_binomios_forma1_latex(bin1, bin2):
    pasos = []

    coeficientes_bin1 = bin1.coeffs()
    monomios_bin1 = [prod(x**k for x, k in zip(bin1.gens, mon)) for mon in bin1.monoms()]

    coeficientes_bin2 = bin2.coeffs()
    monomios_bin2 = [prod(x**k for x, k in zip(bin2.gens, mon)) for mon in bin2.monoms()]

    ta1 = monomios_bin1[0] * coeficientes_bin1[0]
    tb1 = monomios_bin1[1] * coeficientes_bin1[1]
    ta2 = monomios_bin2[0] * coeficientes_bin2[0]
    tb2 = monomios_bin2[1] * coeficientes_bin2[1]

    term1 = ta1**2
    term2 = (tb1 + tb2) * ta1
    term3 = tb1 * tb2
    suma = term1 + term2 + term3

    with evaluate(False):
        u_term1 = ta1**2
        u_term2 = (tb1 + tb2) * ta1
        u_term3 = '({})({})'.format(tb1, tb2)

    paso1 = inicio + 'El cuadrado del término común ' + fin + latex(u_term1) + inicio + ' = ' + fin + latex(term1)
    paso2 = inicio + 'La suma de los términos no comunes ' + fin + latex(u_term2) + inicio + ' = ' + fin + latex(term2)
    paso3 = inicio + 'El producto de los términos no comunes ' + fin + latex(u_term3) + inicio + ' = ' + fin + latex(term3)
    paso4 = inicio + 'Se suman los términos anteriores y se obtiene como resultado ' + fin + latex(suma)

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)
    pasos.append(paso4)

    return pasos

def pasos_binomios_forma2_str(bin1, bin2):
    pasos = []

    coeficientes_bin1 = bin1.coeffs()
    monomios_bin1 = [prod(x**k for x, k in zip(bin1.gens, mon)) for mon in bin1.monoms()]

    coeficientes_bin2 = bin2.coeffs()
    monomios_bin2 = [prod(x**k for x, k in zip(bin2.gens, mon)) for mon in bin2.monoms()]

    ta1 = monomios_bin1[0] * coeficientes_bin1[0]
    tb1 = monomios_bin1[1] * coeficientes_bin1[1]
    ta2 = monomios_bin2[0] * coeficientes_bin2[0]
    tb2 = monomios_bin2[1] * coeficientes_bin2[1]

    with evaluate(False):
        u_term1 = ta1 * ta2
        u_term2 = (ta1 * tb2) + (tb1 * ta2)
        u_term3 = tb1 * tb2

    term1 = ta1 * ta2
    term2 = (ta1 * tb2) + (tb1 * ta2)
    term3 = tb1 * tb2
    suma = term1 + term2 + term3

    pasos.append('El producto del primer termino de cada binomio {} = {}'.format(u_term1, term1))
    pasos.append('El producto de los terminos de cada extremo más el producto de los términos interiores {} = {}'.format(u_term2, term2))
    pasos.append('Eñ producto del segundo termino de cada binomio {} = {}'.format(u_term3, term3))
    pasos.append('Se suman los terminos anteriores, obteniendo {}'.format(suma))

    return pasos

def pasos_binomios_forma2_latex(bin1, bin2):
    pasos = []

    coeficientes_bin1 = bin1.coeffs()
    monomios_bin1 = [prod(x**k for x, k in zip(bin1.gens, mon)) for mon in bin1.monoms()]

    coeficientes_bin2 = bin2.coeffs()
    monomios_bin2 = [prod(x**k for x, k in zip(bin2.gens, mon)) for mon in bin2.monoms()]

    ta1 = monomios_bin1[0] * coeficientes_bin1[0]
    tb1 = monomios_bin1[1] * coeficientes_bin1[1]
    ta2 = monomios_bin2[0] * coeficientes_bin2[0]
    tb2 = monomios_bin2[1] * coeficientes_bin2[1]

    with evaluate(False):
        u_term1 = ta1 * ta2
        u_term2 = (ta1 * tb2) + (tb1 * ta2)
        u_term3 = tb1 * tb2

    term1 = ta1 * ta2
    term2 = (ta1 * tb2) + (tb1 * ta2)
    term3 = tb1 * tb2
    suma = term1 + term2 + term3

    paso1 = inicio + 'El producto del primer termino de cada binomio ' + fin + latex(u_term1) + inicio + ' = ' + fin + latex(term1)
    paso2 = inicio + 'El producto de los terminos de cada extremo más el producto de los términos interiores ' + fin + latex(u_term2) + inicio + ' = ' + fin + latex(term2)
    paso3 = inicio + 'El producto del segundo termino de cada binomio ' + fin + latex(u_term3) + inicio + ' = ' + fin + latex(term3)
    paso4 = inicio + 'Se suman los terminos anteriores, obteniendo ' + fin + latex(suma)

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)
    pasos.append(paso4)

    return pasos