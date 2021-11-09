import numpy as np

from .heuristica import Heuristica


"""Modulo da classe Pop"""


class Pop(Heuristica):
    """
    Classe Pop responsável pela população.

    Examples
    --------
    Utilizar next() ou for-loop

    >>> p = Pop(...)
    >>> for nG in p:
    >>>     pass

    Attributes
    ----------
    nfc : numpy.ndarray
        Numero de chamadas da função objetivo.
    pList : List
        Lista com as partículas
    pBest : Dict
        Dict correspondente a partícula responsável pelo melhor resultado
    parameters : Dict
        Dict com os parametros individuais gerados pelo ``meta``

    """

    def __init__(self, meta, fun, ranges, nPop, nGen,
                       name=None, rng=None):
        """
        Inicialização.

        Note
        ----
        Um mesmo objeto do tipo ``meta`` pode estar em mais de uma ``Pop``.

        Parameters
        ----------
        meta : Meta
            Responsável por definir a estratégia adotada (algoritmo).
        fun : math Function
            Função a ser minimizada ou maximizada
        ranges : numpy.ndarray
            Matriz numpy dos limites inferiores e superiores de cada variavel,
            sendo cada linha um parametro. Col1, Col2 = Min, Max.
            Exemplo: [[-2, 7], [-5, 5], [3, 9]]
        nPop : int
            Tamanho da população.
        nGen : int
            Numero de iterações.

        """
        if name:
            self.name = name
            
        if rng:
            self.rng = rng
        else:
            self.rng = np.random.default_rng()

        self._objective = fun
        self.ranges = ranges
        self.minimize = True
# Realemnte devem ser zeros no vetor contador de nfc
        self.nfc = np.zeros(nGen)
        self.nG = 0
        self.nVar = ranges.shape[0]
        self.nPop = nPop
        self.nGen = nGen

        self.pList = [{'ch': np.empty((nGen, self.nVar)),
                       'value': np.empty(nGen),
                       'id': i}
                      for i in range(nPop)]

        self.pBest = {'ch': np.empty((nGen, self.nVar)),
                      'value': np.empty(nGen)}

        self.meta = meta
        self.parameters = meta.getParameters(self)

        meta.start(self)

    def __repr__(self):
        return "Pop(algo=%r, nPop=%r, nGen=%r/%r) id: %s" % (
            self.meta.__class__.__name__, self.nPop, self.nG, self.nGen, hex(id(self)))

    def __iter__(self):
        return self

    def __next__(self):
        self.nG += 1

        try:
            self.meta.nextGen(self)
            return self.pBest['value'][self.nG]
        except IndexError:
            self.nG -= 1
            raise StopIteration
