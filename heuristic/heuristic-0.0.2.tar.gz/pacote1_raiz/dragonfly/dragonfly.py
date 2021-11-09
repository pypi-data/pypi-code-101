import numpy as np
from scipy.special import gamma


class Da:
    """Classe DragonFly:
        Author: João Vitor Coelho Estrela
    """

    def __init__(self, s=2, a=2, c=2, f=2, e=1):
        self.s = s
        self.a = a
        self.c = c
        self.f = f
        self.e = e

    @staticmethod
    def _getRaio(nG, nGen, ranges):
        r = (ranges[:, 1] - ranges[:, 0])
        r = (r/4) + (2*r*(nG/nGen))
        return r

    @staticmethod
    def _getLevy(d, rng):
        beta = 3/2
        sigma = ((gamma(1+beta)*np.sin(np.pi*(beta/2)) /
                 (gamma((1+beta)/2)*beta*(2**((beta-1)/2))))**(1/beta))
        u = rng.normal(size=d)*sigma
        v = rng.normal(size=d)
        step = u/(np.abs(v)**(1/beta))
        step = 0.01*step
        return step

    @staticmethod
    def _getNeighbours(pI, pList, r, nG):
        neighbours = []  # Remover o pI daqui antes
        for pJ in pList:
            d2e = np.abs(pI['ch'][nG, :] - pJ['ch'][nG, :])
            if (d2e <= r).all() and (pI is not pJ):
                neighbours.append(pJ)
        return neighbours

    @staticmethod
    def _separation(pI, neighbours, nG):
        if neighbours:
            S = [pJ['ch'][nG, :] - pI['ch'][nG, :] for pJ in neighbours]
            S = -(np.array(S).sum(0))
        else:
            S = np.zeros_like(pI['ch'][nG, :])
        return S

    @staticmethod
    def _alignment(pI, neighbours, nG):  # não deveria precisar do pI
        if neighbours:
            A = [pJ['vel'][nG, :] for pJ in neighbours]
            A = (np.array(A).sum(0))/len(neighbours)
        else:
            A = pI['vel'][nG, :]
        return A

    @staticmethod
    def _cohesion(pI, neighbours, nG):  # não deveria precisar do pI
        if neighbours:
            C = [pJ['ch'][nG, :] for pJ in neighbours]
            C = (np.array(C).sum(0))/len(neighbours)
        else:
            C = pI['ch'][nG, :]
        return C - pI['ch'][nG, :]

    @staticmethod
    def _foodAttraction(pI, pBest, distFood, r, nG):
        if (distFood <= r).all():
            F = pBest['ch'][nG, :] - pI['ch'][nG, :]
        else:
            F = np.zeros_like(pI['ch'][nG, :])
        return F

    @staticmethod
    def _enemyDistraction(pI, pWorst, distEnemy, r, nG):
        if (distEnemy <= r).all():
            E = pWorst['ch'][nG, :] + pI['ch'][nG, :]
        else:
            E = np.zeros_like(pI['ch'][nG, :])
        return E

    def getParameters(self, pop):
        vRanges = (pop.ranges[:, 1] - pop.ranges[:, 0])/10
        return {'vRanges': vRanges,
                's': 1,
                'a': 1,
                'c': 1,
                'f': 1,
                'e': 1,
                'pWorst': {'ch': np.empty((pop.nGen, pop.nVar)),
                           'value':  np.empty(pop.nGen)}}

    def start(self, pop, nG=0):
        pop.createNewPop(nG)
        pop.evalPop(nG)

        for p in pop.pList:
            p['apagar'] = np.empty_like(p['value'])
            p['apagar'][pop.nG] = 0

            p['vel'] = np.empty_like(p['ch'])
            p['vel'][nG, :] = pop.rng.uniform(-pop.parameters['vRanges'],
                                               pop.parameters['vRanges'],
                                               pop.parameters['vRanges'].shape[0])

        Da._updateGen(pop, nG)


    @staticmethod
    def _updateGen(pop, nG):

        pTemp = pop.getWorstPop(nG)
        pop.parameters['pWorst']['ch'][nG, :] = pTemp['ch'][nG, :]
        pop.parameters['pWorst']['value'][nG] = pTemp['value'][nG]

        pTemp = pop.getBestPop(nG)
        pop.pBest['ch'][nG, :] = pTemp['ch'][nG, :]
        pop.pBest['value'][nG] = pTemp['value'][nG]

        #pop.pBest['vel'] = np.empty_like(pop.pBest['ch'])
        #pop.pBest['vel'][nG, :] = pTemp['vel'][nG, :]


    def nextGen(self, pop):

        r = Da._getRaio(pop.nG, pop.nGen, pop.ranges)

        w = 0.9 - pop.nG*((.9-.4)/pop.nGen)

        my_c = 0.1 - pop.nG*((.1-0)/(pop.nGen/2))
        if my_c < 0:
            my_c = 0

        s = 2*my_c * pop.rng.uniform()  # Seperation weight
        a = 2*my_c * pop.rng.uniform()  # Alignment weight
        c = 2*my_c * pop.rng.uniform()  # Cohesion weight
        f = 2 * pop.rng.uniform()  # Food attraction weight
        e = my_c  # Enemy distraction weight

        for pI in pop.pList:
            pI['ch'][pop.nG, :] = pI['ch'][pop.nG-1, :]
            pI['vel'][pop.nG, :] = pI['vel'][pop.nG-1, :]
            pI['value'][pop.nG] = pI['value'][pop.nG-1]

        for pI in pop.pList:
            neighbours = Da._getNeighbours(pI, pop.pList, r, pop.nG)
            distFood = np.abs(pI['ch'][pop.nG, :]
                              - pop.pBest['ch'][pop.nG, :])

            S = Da._separation(pI, neighbours, pop.nG)
            A = Da._alignment(pI, neighbours, pop.nG)
            C = Da._cohesion(pI, neighbours, pop.nG)

            if (distFood > r).any():
                if neighbours:
                    pI['apagar'][pop.nG] = 1
                    rA = pop.rng.random(pop.ranges.shape[0])
                    rC = pop.rng.random(pop.ranges.shape[0])
                    rS = pop.rng.random(pop.ranges.shape[0])

                    pI['vel'][pop.nG, :] = (w*pI['vel'][pop.nG, :]  # Aqui tb
                                            + rA*A + rC*C + rS*S)

                    pI['vel'][pop.nG, :] = np.clip(pI['vel'][pop.nG, :],
                                                   -pop.parameters['vRanges'],
                                                   pop.parameters['vRanges'])

                    pI['ch'][pop.nG, :] = (pI['ch'][pop.nG, :]  # Apaguei o ng-1
                                           + pI['vel'][pop.nG, :])
                else:  # Levy e zerar vel
                    pI['apagar'][pop.nG] = 2
                    pI['vel'][pop.nG, :] = 0
                    # Esse 1 é vetorial
                    pI['ch'][pop.nG, :] = (pI['ch'][pop.nG, :]  # Apaguei o ng-1
                                           + (pI['ch'][pop.nG, :]  # Aqui tb
                                              * Da._getLevy(pop.ranges.shape[0], pop.rng)))

            else:
                pI['apagar'][pop.nG] = 3
                pWorst = pop.parameters['pWorst']
                distEnemy = np.abs(pI['ch'][pop.nG, :] - pWorst['ch'][pop.nG, :])
                F = Da._foodAttraction(pI, pop.pBest, distFood, r, pop.nG)
                E = Da._enemyDistraction(pI, pWorst, distEnemy, r, pop.nG)

                pI['vel'][pop.nG, :] = ((w*pI['vel'][pop.nG, :])  # Apaguei o ng-1
                                        + a*A + c*C + s*S + f*F + e*E)

                pI['vel'][pop.nG, :] = np.clip(pI['vel'][pop.nG, :],
                                               -pop.parameters['vRanges'],
                                               pop.parameters['vRanges'])

                pI['ch'][pop.nG, :] = (pI['ch'][pop.nG, :]  # Apaguei o ng-1
                                       + pI['vel'][pop.nG, :])

            pI['ch'][pop.nG, :] = np.clip(pI['ch'][pop.nG, :],
                                          pop.ranges[:, 0],
                                          pop.ranges[:, 1])
        pop.evalPop(pop.nG)

        pTemp = pop.getBestPop(pop.nG)

        pop.pBestUpdate(pTemp, pop.nG)

        # Enemy
        pTemp = pop.getWorstPop(pop.nG)
        if pTemp['value'][pop.nG] > pop.parameters['pWorst']['value'][pop.nG-1]:
            pop.parameters['pWorst']['ch'][pop.nG, :] = pTemp['ch'][pop.nG, :]
            pop.parameters['pWorst']['value'][pop.nG] = pTemp['value'][pop.nG]
        else:
            pop.parameters['pWorst']['ch'][pop.nG, :] = pop.parameters['pWorst']['ch'][pop.nG-1, :]
            pop.parameters['pWorst']['value'][pop.nG] = pop.parameters['pWorst']['value'][pop.nG-1]
