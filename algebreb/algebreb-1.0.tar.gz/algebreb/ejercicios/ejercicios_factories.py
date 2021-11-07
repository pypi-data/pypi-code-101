from algebreb.ejercicios.operaciones_polinomio import (SumaPolinomios, RestaPolinomios,
                                                       MultPolinomios, DivPolinomios,
                                                       GradoPolinomio, TermPolinomio)
from algebreb.ejercicios.operaciones_fracciones import (SumaFracAlg, RestaFracAlg,
                                                        MultFracAlg, DivFracAlg,
                                                        SimpFracAlg)
from algebreb.ejercicios.productos_notables import (BinomioAlCuadrado, BinomioAlCubo,
                                                    BinomiosConjugados, BinomiosFormaI,
                                                    BinomiosFormaII, TrinomioAlCuadrado)
from algebreb.ejercicios.factorizacion import (FactorComun, DiferenciaCuadrados,
                                               TrinomioCuadradoPerfecto, CuboPerfectoBinomios,
                                               TrinomioFormaI, TrinomioFormaII)

def ejer_poli_factory(tipo, op1, op2=None):
    if tipo == '+':
        return SumaPolinomios(op1, op2)
    elif tipo == '-':
        return RestaPolinomios(op1, op2)
    elif tipo == '*':
        return MultPolinomios(op1, op2)
    elif tipo == '/':
        return DivPolinomios(op1, op2)
    elif tipo == 'GP':
        return GradoPolinomio(op1)
    elif tipo == 'TP':
        return TermPolinomio(op1)
    else:
        return None

def ejer_fa_factory(tipo, op1, op2=None):
    if tipo == '+':
        return

def ejer_prod_not_factory(tipo, op):
    if tipo == 'BA2':
        return BinomioAlCuadrado(op)
    elif tipo == 'BA3':
        return BinomioAlCubo(op)
    elif tipo == 'BC':
        return BinomiosConjugados(op)
    elif tipo == 'BF1':
        return BinomiosFormaI(op)
    elif tipo == 'BF2':
        return BinomiosFormaII(op)
    elif tipo == 'TA2':
        return TrinomioAlCuadrado(op)

def ejer_factor_factory(tipo, op):
    return