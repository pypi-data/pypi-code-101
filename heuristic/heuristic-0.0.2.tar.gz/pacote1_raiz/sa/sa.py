import math

import numpy as np


class Sa:

    def __init__(self, temp=None, sigRange=0.02, prob=0.8):

        self.sigRange = sigRange
        self.prob = 0.8
        self.temp = temp

    def getParameters(self, pop):
        if self.temp is None:
            tempPop = Sa._getTemp(pop, self.sigRange, self.prob)
        else:
            tempPop = self.temp

        return {'temp': tempPop}

    def start(self, pop, nG=0):
        pop.createNewPop(nG)  # CRIAR APENAS UM
        pop.evalPop(nG)

        Sa._updateGen(pop, nG)

    @staticmethod
    def _updateGen(pop, nG):
        pTemp = pop.getBestPop(nG)
        pop.pBest['ch'][nG, :] = pTemp['ch'][nG, :]
        pop.pBest['value'][nG] = pTemp['value'][nG]

    @staticmethod
    def _getTemp(pop, sigRange, prob):
        temps = []
        denomiandor = math.log(1/prob)

        for p in pop.pList:
            while True:
                newX = pop.getNeighbor(p['ch'][0, :], sigRange)
                newF = pop._objective(newX)
                energia = newF - p['value'][0]

                if energia >= 0:
                    temp = energia/denomiandor
                    temps.append(temp)
                    break

        return max(temps)

    def nextGen(self, pop):

        for j in pop.pList:

            newX = pop.getNeighbor(j['ch'][pop.nG-1, :], self.sigRange)

            newX = np.clip(newX, pop.ranges[:, 0], pop.ranges[:, 1])

            value = pop.objective(newX)

            energia = value - j['value'][pop.nG-1]

            if energia < 0:
                bolt = 1.00

            elif energia >= 0:
                bolt = math.exp((-energia)/pop.parameters['temp'])

            rand = pop.rng.random()

            if rand < bolt:
                j['value'][pop.nG] = value
                j['ch'][pop.nG, :] = newX

            else:
                j['value'][pop.nG] = j['value'][pop.nG-1]
                j['ch'][pop.nG, :] = j['ch'][pop.nG-1, :]

        pop.parameters['temp'] = 0.99*pop.parameters['temp']

        pTemp = pop.getBestPop(pop.nG)

        pop.pBestUpdate(pTemp, pop.nG)
