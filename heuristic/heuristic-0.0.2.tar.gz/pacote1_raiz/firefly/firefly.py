import copy

import numpy as np
from scipy.spatial import distance


class FireFly:
    """
    name = FireFly
    source = Yang .... .... ..
    author = João Vitor Coelho Estrela
    """

    def __init__(self, alpha0=1, beta0=1, gama0=None, tetha0=0.95, exp0=2):

        self.alpha_0 = alpha0
        self.beta_0 = beta0
        self.gama_0 = gama0
        self.tetha_0 = tetha0
        self.exp_0 = exp0

    def getParameters(self, pop):
        if self.gama_0 is None:  # alterar
            self.gama_0 = 1/(pop.ranges[:, 1] - pop.ranges[:, 0])**2

        else:
            self.gama_0 = self.gama_0

    def start(self, pop, nG=0):
        pop.createNewPop(nG)
        pop.evalPop(nG)
        
        FireFly._updateGen(pop, nG)


    @staticmethod
    def _updateGen(pop, nG):
        pop.sortPop(nG)

        # O pBest é o primeiro pois a pList foi ordenada
        # Portanto n precisamos do getBestInPop()
        pTemp = pop.pList[nG]
        pop.pBest['ch'][nG, :] = pTemp['ch'][nG, :]
        pop.pBest['value'][nG] = pTemp['value'][nG]

    @staticmethod
    def _newAlpha(alpha0, tetha0, nG, i=None, bk=None, b=None):
        # return alpha0 * (tetha0 ** nG)
        # Alphafactor=Alphaainfi+(Alphaazero-Alphaainfi)*(Tethafactor^Iter);
        return 0.2 + (alpha0 - 0.2) * (tetha0**nG)

    def nextGen(self, pop):

        newBugs = copy.deepcopy(pop.pList)
        alpha = FireFly._newAlpha(self.alpha_0, self.tetha_0, pop.nG-1)

        for i, bugI in enumerate(pop.pList):  # vai acasalar com quem????

            bugI['ch'][pop.nG, :] = bugI['ch'][pop.nG-1, :]

            for j in range(i+1):  # PRETENDENTES KK

                # Se a pJ é melhor que pI, mover pI até o pJ
                if pop.isPaBetterPb(pop.pList[j]['value'][pop.nG-1], bugI['value'][pop.nG-1]):

                    xVarI = bugI['ch'][pop.nG, :]
                    xVarJ = newBugs[j]['ch'][pop.nG-1, :]

                    r = distance.euclidean(xVarI, xVarJ)
                    betaa = self.beta_0 * np.exp(-self.gama_0 * r ** self.exp_0)
                    termo_atratividade = betaa * (xVarJ - xVarI)
                    vetor_randomico = pop.rng.uniform(0, 1, pop.ranges.shape[0])
                    termo_randomico = alpha * (vetor_randomico - 0.5) * (pop.ranges[:, 1] - pop.ranges[:, 0])
                    xVarI += termo_atratividade + termo_randomico

                    bugI['ch'][pop.nG, :] = np.clip(xVarI, pop.ranges[:, 0],
                                                    pop.ranges[:, 1])

        pop.evalPop(pop.nG)
        pop.sortPop(pop.nG)

        pop.pBest['ch'][pop.nG, :] = pop.pList[0]['ch'][pop.nG, :]
        pop.pBest['value'][pop.nG] = pop.pList[0]['value'][pop.nG]
