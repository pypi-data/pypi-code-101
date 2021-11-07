from algebreb.expresiones.polinomios import (polinomio_coeficientes_aleatorios,
                                            polinomio_homogeneo_aleatorio,
                                            trinomio_aleatorio,
                                            binomio_aleatorio,
                                            monomio_aleatorio)
from algebreb.expresiones.fracciones_algebraicas import (fa_aleatoria as fa,
                                                        fa_propia_aleatoria,
                                                        fa_impropia_aleatoria)

def polinomio_aleatorio(tipo, grado, variabs, dom, cmin, cmax, fracc=False, compl=True):
    if tipo == 'M':
        return monomio_aleatorio(grado, variabs, dom, cmin, cmax, fracc)
    elif tipo == 'B':
        return binomio_aleatorio(grado, variabs, dom, cmin, cmax, fracc)
    elif tipo == 'T':
        return trinomio_aleatorio(grado, variabs, dom, cmin, cmax, fracc)
    elif tipo == 'H':
        return polinomio_homogeneo_aleatorio(grado, variabs, dom, cmin, cmax, fracc, compl)
    else:
        return polinomio_coeficientes_aleatorios(grado, variabs, dom, cmin, cmax, fracc, compl)

def fa_aleatoria(tipo, variabs, dom, crmin, crmax, fracc, raices, gnum=1, gden=1):
    if tipo == 'P':
        return fa_propia_aleatoria(gden, variabs, dom, crmin, crmax, fracc, raices)
    elif tipo == 'I':
        return fa_impropia_aleatoria(gnum, variabs, dom, crmin, crmax, fracc, raices)
    else:
        return fa(gnum, gden, variabs, dom, crmin, crmax, fracc, raices)