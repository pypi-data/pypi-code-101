from sympy import *
from sympy.abc import a, b, c, x, y, z
from sympy import UnevaluatedExpr
from algebreb.expresiones.polinomios import Polinomio
from algebreb.expresiones.fracciones_algebraicas import FraccionAlgebraica

inicio = '\\textrm{'
fin = '}'

def pasos_suma_fracciones_algebraicas_str(f1, f2):
    pasos = []
    
    f1n = f1.num.as_expr()
    f1d = f1.den.as_expr()
    f2n = f2.num.as_expr()
    f2d = f2.den.as_expr()

    f1n_factor = factor(f1n)
    f1d_factor = factor(f1d)
    f2n_factor = factor(f2n)
    f2d_factor = factor(f2d)

    with evaluate(False):
        u_f1 = f1n_factor / f1d_factor
        u_f2 = f2n_factor / f2d_factor
        nuevo_den = f1d_factor * f2d_factor
        ad = f1n_factor * f2d_factor
        bc = f1d_factor * f2n_factor
        nuevo_num = ad + bc
        n_frac = nuevo_num / nuevo_den

    n_frac_factor = simplify(n_frac)

    pasos.append('Se factoriza el numerador y denominador de la primera fraccion: {}'.format(u_f1))
    pasos.append('Se factoriza el numerador y denominador de la segunda fraccion: {}'.format(u_f2))
    pasos.append('Se multiplica el numerador de la primer fraccion por el denominador de la segunda: {}'.format(ad))
    pasos.append('Se multiplica el denominador de la primer fraccion por el numerador de la segunda: {}'.format(bc))
    pasos.append('Se suman los dos productos anteriores para obtener el nuevo numerador: {}'.format(nuevo_num))
    pasos.append('Se multiplican los 2 denominadores de las fracciones para obtener el nuevo denominador: {}'.format(nuevo_den))
    pasos.append('Se acomoda el nuevo numerador y denominador: {}'.format(n_frac))
    pasos.append('Se hacen los productos y sumas correspondientes. Finalmente: {}'.format(n_frac_factor))

    return pasos

def pasos_suma_fracciones_algebraicas_latex(f1, f2):
    pasos = []
    
    f1n = f1.num.as_expr()
    f1d = f1.den.as_expr()
    f2n = f2.num.as_expr()
    f2d = f2.den.as_expr()

    f1n_factor = factor(f1n)
    f1d_factor = factor(f1d)
    f2n_factor = factor(f2n)
    f2d_factor = factor(f2d)

    with evaluate(False):
        u_f1 = f1n_factor / f1d_factor
        u_f2 = f2n_factor / f2d_factor
        nuevo_den = f1d_factor * f2d_factor
        ad = f1n_factor * f2d_factor
        bc = f1d_factor * f2n_factor
        nuevo_num = ad + bc
        n_frac = nuevo_num / nuevo_den

    n_frac_factor = simplify(n_frac)

    paso1 = inicio + 'Se factoriza el numerador y denominador de la primera fraccion: ' + fin + latex(u_f1)
    paso2 = inicio + 'Se factoriza el numerador y denominador de la segunda fraccion: ' + fin + latex(u_f2)
    paso3 = inicio + 'Se multiplica el numerador de la primer fraccion por el denominador de la segunda: ' + fin + latex(ad)
    paso4 = inicio + 'Se multiplica el denominador de la primer fraccion por el numerador de la segunda: ' + fin + latex(bc)
    paso5 = inicio + 'Se suman los dos productos anteriores para obtener el nuevo numerador: ' + fin + latex(nuevo_num)
    paso6 = inicio + 'Se multiplican los 2 denominadores de las fracciones para obtener el nuevo denominador: ' + fin + latex(nuevo_den)
    paso7 = inicio + 'Se acomoda el nuevo numerador y denominador: ' + fin + latex(n_frac)
    paso8 = inicio + 'Se hacen los productos y sumas correspondientes. Finalmente: ' + fin + latex(n_frac_factor)

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)
    pasos.append(paso4)
    pasos.append(paso5)
    pasos.append(paso6)
    pasos.append(paso7)
    pasos.append(paso8)

    return pasos

def pasos_resta_fracciones_algebraicas_str(f1, f2):
    pasos = []
    
    f1n = f1.num.as_expr()
    f1d = f1.den.as_expr()
    f2n = f2.num.as_expr()
    f2d = f2.den.as_expr()

    f1n_factor = factor(f1n)
    f1d_factor = factor(f1d)
    f2n_factor = factor(f2n)
    f2d_factor = factor(f2d)

    with evaluate(False):
        u_f1 = f1n_factor / f1d_factor
        u_f2 = f2n_factor / f2d_factor
        nuevo_den = f1d_factor * f2d_factor
        ad = f1n_factor * f2d_factor
        bc = f1d_factor * f2n_factor
        nuevo_num = ad - bc
        n_frac = nuevo_num / nuevo_den

    n_frac_factor = simplify(n_frac)

    pasos.append('Se factoriza el numerador y denominador de la primera fraccion: {}'.format(u_f1))
    pasos.append('Se factoriza el numerador y denominador de la segunda fraccion: {}'.format(u_f2))
    pasos.append('Se multiplica el numerador de la primer fraccion por el denominador de la segunda: {}'.format(ad))
    pasos.append('Se multiplica el denominador de la primer fraccion por el numerador de la segunda: {}'.format(bc))
    pasos.append('Se restan los dos productos anteriores para obtener el nuevo numerador: {}'.format(nuevo_num))
    pasos.append('Se multiplican los 2 denominadores de las fracciones para obtener el nuevo denominador: {}'.format(nuevo_den))
    pasos.append('Se acomoda el nuevo numerador y denominador: {}'.format(n_frac))
    pasos.append('Se hacen los productos y restas correspondientes. Finalmente: {}'.format(n_frac_factor))

    return pasos

def pasos_resta_fracciones_algebraicas_latex(f1, f2):
    pasos = []
    
    f1n = f1.num.as_expr()
    f1d = f1.den.as_expr()
    f2n = f2.num.as_expr()
    f2d = f2.den.as_expr()

    f1n_factor = factor(f1n)
    f1d_factor = factor(f1d)
    f2n_factor = factor(f2n)
    f2d_factor = factor(f2d)

    with evaluate(False):
        u_f1 = f1n_factor / f1d_factor
        u_f2 = f2n_factor / f2d_factor
        nuevo_den = f1d_factor * f2d_factor
        ad = f1n_factor * f2d_factor
        bc = f1d_factor * f2n_factor
        nuevo_num = ad - bc
        n_frac = nuevo_num / nuevo_den

    n_frac_factor = simplify(n_frac)

    paso1 = inicio + 'Se factoriza el numerador y denominador de la primera fraccion: ' + fin + latex(u_f1)
    paso2 = inicio + 'Se factoriza el numerador y denominador de la segunda fraccion: ' + fin + latex(u_f2)
    paso3 = inicio + 'Se multiplica el numerador de la primer fraccion por el denominador de la segunda: ' + fin + latex(ad)
    paso4 = inicio + 'Se multiplica el denominador de la primer fraccion por el numerador de la segunda: ' + fin + latex(bc)
    paso5 = inicio + 'Se restan los dos productos anteriores para obtener el nuevo numerador: ' + fin + latex(nuevo_num)
    paso6 = inicio + 'Se multiplican los 2 denominadores de las fracciones para obtener el nuevo denominador: ' + fin + latex(nuevo_den)
    paso7 = inicio + 'Se acomoda el nuevo numerador y denominador: ' + fin + latex(n_frac)
    paso8 = inicio + 'Se hacen los productos y sumas correspondientes. Finalmente: ' + fin + latex(n_frac_factor)

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)
    pasos.append(paso4)
    pasos.append(paso5)
    pasos.append(paso6)
    pasos.append(paso7)
    pasos.append(paso8)

    return pasos

def pasos_mult_fracciones_algebraicas_str(f1, f2):
    pasos = []
    
    f1n = f1.num.as_expr()
    f1d = f1.den.as_expr()
    f2n = f2.num.as_expr()
    f2d = f2.den.as_expr()

    f1n_factor = factor(f1n)
    f1d_factor = factor(f1d)
    f2n_factor = factor(f2n)
    f2d_factor = factor(f2d)

    with evaluate(False):
        u_f1 = f1n_factor / f1d_factor
        u_f2 = f2n_factor / f2d_factor
        nuevo_den = f1d_factor * f2d_factor
        nuevo_num = f1n_factor * f2n_factor
        n_frac = nuevo_num / nuevo_den

    n_frac_factor = simplify(n_frac)

    pasos.append('Se factoriza el numerador y denominador de la primera fraccion: {}'.format(u_f1))
    pasos.append('Se factoriza el numerador y denominador de la primera fraccion: {}'.format(u_f2))
    pasos.append('Se multiplican los numeradores de las fracciones: {}'.format(nuevo_num))
    pasos.append('Se multiplican los denominadores de las fracciones: {}'.format(nuevo_den))
    pasos.append('Se acomoda el nuevo numerador y denominador: {}'.format(n_frac))
    pasos.append('Se cancelan terminos. Finalmente: {}'.format(n_frac_factor))

    return pasos

def pasos_mult_fracciones_algebraicas_latex(f1, f2):
    pasos = []
    
    f1n = f1.num.as_expr()
    f1d = f1.den.as_expr()
    f2n = f2.num.as_expr()
    f2d = f2.den.as_expr()

    f1n_factor = factor(f1n)
    f1d_factor = factor(f1d)
    f2n_factor = factor(f2n)
    f2d_factor = factor(f2d)

    with evaluate(False):
        u_f1 = f1n_factor / f1d_factor
        u_f2 = f2n_factor / f2d_factor
        nuevo_den = f1d_factor * f2d_factor
        nuevo_num = f1n_factor * f2n_factor
        n_frac = nuevo_num / nuevo_den

    n_frac_factor = simplify(n_frac)

    paso1 = inicio + 'Se factoriza el numerador y denominador de la primera fraccion: ' + fin + latex(u_f1)
    paso2 = inicio + 'Se factoriza el numerador y denominador de la segunda fraccion: ' + fin + latex(u_f2)
    paso3 = inicio + 'Se multiplican los numeradores de las fracciones: ' + fin + latex(nuevo_num)
    paso4 = inicio + 'Se multiplican los denominadores de las fracciones: ' + fin + latex(nuevo_den)
    paso5 = inicio + 'Se acomoda el nuevo numerador y denominador: ' + fin + latex(n_frac)
    paso6 = inicio + 'Se cancelan terminos. Finalmente: : ' + fin + latex(n_frac_factor)

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)
    pasos.append(paso4)
    pasos.append(paso5)
    pasos.append(paso6)

    return pasos

def pasos_div_fracciones_algebraicas_str(f1, f2):
    pasos = []
    
    f1n = f1.num.as_expr()
    f1d = f1.den.as_expr()
    f2n = f2.num.as_expr()
    f2d = f2.den.as_expr()

    f1n_factor = factor(f1n)
    f1d_factor = factor(f1d)
    f2n_factor = factor(f2n)
    f2d_factor = factor(f2d)

    with evaluate(False):
        u_f1 = f1n_factor / f1d_factor
        u_f2 = f2n_factor / f2d_factor
        nuevo_den = f1d_factor * f2n_factor
        nuevo_num = f1n_factor * f2d_factor
        n_frac = nuevo_num / nuevo_den

    n_frac_factor = simplify(n_frac)

    pasos.append('Se factoriza el numerador y denominador de la primera fraccion: {}'.format(u_f1))
    pasos.append('Se factoriza el numerador y denominador de la primera fraccion: {}'.format(u_f2))
    pasos.append('Se multiplican el numerador de la primer fraccion por el denominador de la segunda: {}'.format(nuevo_num))
    pasos.append('Se multiplican el denominador de la primer fraccion por el numerador de la segunda: {}'.format(nuevo_den))
    pasos.append('Se acomoda el nuevo numerador y denominador: {}'.format(n_frac))
    pasos.append('Se cancelan terminos. Finalmente: {}'.format(n_frac_factor))

def pasos_div_fracciones_algebraicas_latex(f1, f2):
    pasos = []
    
    f1n = f1.num.as_expr()
    f1d = f1.den.as_expr()
    f2n = f2.num.as_expr()
    f2d = f2.den.as_expr()

    f1n_factor = factor(f1n)
    f1d_factor = factor(f1d)
    f2n_factor = factor(f2n)
    f2d_factor = factor(f2d)

    with evaluate(False):
        u_f1 = f1n_factor / f1d_factor
        u_f2 = f2n_factor / f2d_factor
        nuevo_den = f1d_factor * f2n_factor
        nuevo_num = f1n_factor * f2d_factor
        n_frac = nuevo_num / nuevo_den

    n_frac_factor = simplify(n_frac)

    paso1 = inicio + 'Se factoriza el numerador y denominador de la primera fraccion: ' + fin + latex(u_f1)
    paso2 = inicio + 'Se factoriza el numerador y denominador de la segunda fraccion: ' + fin + latex(u_f2)
    paso3 = inicio + 'Se multiplican el numerador de la primer fraccion por el denominador de la segunda: ' + fin + latex(nuevo_num)
    paso4 = inicio + 'Se multiplican el denominador de la primer fraccion por el numerador de la segunda: ' + fin + latex(nuevo_den)
    paso5 = inicio + 'Se acomoda el nuevo numerador y denominador: ' + fin + latex(n_frac)
    paso6 = inicio + 'Se cancelan terminos. Finalmente: ' + fin + latex(n_frac_factor)

    pasos.append(paso1)
    pasos.append(paso2)
    pasos.append(paso3)
    pasos.append(paso4)
    pasos.append(paso5)
    pasos.append(paso6)

    return pasos

def pasos_simp_fracciones_algebraicas_str(f1):
    pasos = []
    
    f1n = f1.num.as_expr()
    f1d = f1.den.as_expr()

    f1n_factor = factor(f1n)
    f1d_factor = factor(f1d)

    with evaluate(False):
        u_f1 = f1n_factor / f1d_factor

    n_frac_factor = simplify(u_f1)

    pasos.append('Se factoriza el numerador y denominador de la fraccion: {}'.format(u_f1))
    pasos.append('Se cancelan terminos: {}'.format(n_frac_factor))

    return pasos

def pasos_simp_fracciones_algebraicas_latex(f1):
    pasos = []
    
    f1n = f1.num.as_expr()
    f1d = f1.den.as_expr()

    f1n_factor = factor(f1n)
    f1d_factor = factor(f1d)

    with evaluate(False):
        u_f1 = f1n_factor / f1d_factor

    n_frac_factor = simplify(u_f1)

    paso1 = inicio + 'Se factoriza el numerador y denominador de la fraccion: ' + fin + latex(u_f1)
    paso2 = inicio + 'Se cancelan terminos: ' + fin + latex(n_frac_factor)

    pasos.append(paso1)
    pasos.append(paso2)

    return pasos

p1 = Polinomio(x+2, x)
p2 = Polinomio(x**2+5*x+6, x)
p3 = Polinomio(x+2, x)
p4 = Polinomio(x**2+4*x+3, x)

f1 = FraccionAlgebraica(p1, p2)
f2 = FraccionAlgebraica(p3, p4)

f_pasos = pasos_simp_fracciones_algebraicas_latex(f1)



