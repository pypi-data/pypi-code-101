import numpy as np


class Abc:
    """
    name = abc
    source =  ... ... ..
    author = João Vitor Coelho Estrela
    nPop = nPop/2
    """

    def __init__(self):
        pass

    def getParameters(self, pop):
        scoutLimit = pop.ranges.shape[0]*(pop.nPop)/2
        return {'scoutLimit': scoutLimit}

    def start(self, pop, nG=0):
        pop.nPop = pop.nPop*2  # No momento o usuario deve passar nPop/2 no init Pop()
        pop.createNewPop(nG)  # Preciso só de metade [::2]
        pop.evalPop(nG)

        for p in pop.pList:
            p['fitness'] = np.empty_like(p['value'])
            p['limit'] = 0

        # Fitness do pBest não é armazenada, utilizar o metodo _ftiness
        # para atualizar, se necessario
        # for g in range(nGen):
        #     Abc._fitness([abc.pBest], g)

        Abc._updateGen(pop, nG)


    @staticmethod
    def _updateGen(pop, nG):
            Abc._fitness(pop.pList, nG)

            pTemp = pop.getBestPop(nG)
            pop.pBest['ch'][nG, :] = pTemp['ch'][nG, :]
            pop.pBest['value'][nG] = pTemp['value'][nG]


    @staticmethod
    def _fitness(pList, nG):
        for p in pList:
            if p['value'][nG] >= 0:
                p['fitness'][nG] = 1 / (1 + p['value'][nG])
            else:
                p['fitness'][nG] = 1 + abs(p['value'][nG])

    @staticmethod
    def _computeProbability(pList, nG):

        # Retrieves fitness of bees within the hive
        values = [p['fitness'][nG] for p in pList]
        # Max_values = max(values)
        soma = sum(values)

        # Trocar
        probas = [v / soma for v in values]
        return probas

        # Computes probalities the way Karaboga does in his classic ABC
        max_values = max(values)
        probas = [0.9 * v / max_values + 0.1 for v in values]
        return probas

        # returns intervals of probabilities # ACUMULADO
        return [sum(probas[:i+1]) for i in range(len(pList))]

    def nextGen(self, pop):
        employedBee = pop.pList
        for emBee in employedBee:  # Abelha i

            # Caso ela tome uma penalidade e nao mova,
            # O valor da gen anterior estará repetido para esta (atual):
            emBee['ch'][pop.nG, :] = emBee['ch'][pop.nG-1, :]
            emBee['value'][pop.nG] = emBee['value'][pop.nG-1]
            emBee['fitness'][pop.nG] = emBee['fitness'][pop.nG-1]
            # - - - - - - - - - - - - - - - - - - - - - - - - - -

            j = pop.rng.choice(pop.ranges.shape[0])  # Variavel j

            # print('d:', j)

            neighbour = pop.rng.choice(employedBee)  # Abelha k
            while emBee is neighbour:
                neighbour = pop.rng.choice(employedBee)

            phi = pop.rng.uniform(-1, 1)

            vIJ = emBee['ch'][pop.nG-1, j] + phi*(
                  emBee['ch'][pop.nG-1, j] - neighbour['ch'][pop.nG-1, j])
            vIJ = np.clip(vIJ, pop.ranges[j, 0], pop.ranges[j, 1])

            # print('phi', phi)
            # print('i', emBee.ch[self.nG-1, j])
            # print('nei', neighbour.ch[self.nG-1, j])

            value = emBee['ch'][pop.nG-1, :].copy()
            value[j] = vIJ

            value = pop.objective(value)

            # print('val', vIJ)
            # print(value)

            if value >= 0:
                fit = 1 / (1 + value)
            else:
                fit = 1 + abs(value)

            if fit > emBee['fitness'][pop.nG - 1]:
                emBee['fitness'][pop.nG] = fit
                emBee['value'][pop.nG] = value
                emBee['ch'][pop.nG, j] = vIJ
                emBee['limit'] = 0
                # print('MELHOROU')
            else:
                emBee['limit'] += 1

        # print('**************** ONs *******************')
        prob = Abc._computeProbability(employedBee, pop.nG)

        # print(prob)

        for k in range(len(employedBee)):
            # print('k', k)

            onBee = pop.rng.choice(employedBee, None, p=prob)
            # print(onBee)

            neighbour = pop.rng.choice(employedBee)

            # print('on', onBee.ch[self.nG, :])
            # print('nei', neighbour.ch[self.nG, :])

            while onBee is neighbour:
                neighbour = pop.rng.choice(employedBee)

            j = pop.rng.choice(pop.ranges.shape[0])  # Variavel j
            # print(j)
            phi = pop.rng.uniform(-1, 1)
            vIJ = onBee['ch'][pop.nG, j] + phi*(
                  onBee['ch'][pop.nG, j] - neighbour['ch'][pop.nG, j])
            vIJ = np.clip(vIJ, pop.ranges[j, 0], pop.ranges[j, 1])

            # print('phi', phi)
            # print('i', emBee.ch[self.nG-1, j])
            # print('nei', neighbour.ch[self.nG-1, j])

            value = onBee['ch'][pop.nG-1, :].copy()
            value[j] = vIJ
            value = pop.objective(value)

            # print('val', vIJ)
            # print(value)

            if value >= 0:
                fit = 1 / (1 + value)
            else:
                fit = 1 + abs(value)

            if fit > onBee['fitness'][pop.nG - 1]:
                onBee['fitness'][pop.nG] = fit
                onBee['value'][pop.nG] = value
                onBee['ch'][pop.nG, j] = vIJ
                onBee['limit'] = 0
                # print('melhorou')
            else:
                onBee['limit'] += 1
                # print('N melhorou')

        pTemp = pop.getBestPop(pop.nG)

        pop.pBestUpdate(pTemp, pop.nG)

        # PEGAR APENAS A COM MAIOR 'ESTOURO'
        lerdas = [p for p in employedBee
                  if p['limit'] >= pop.parameters['scoutLimit']]

        if (len(lerdas) > 0):
            lerdas.sort(key=lambda x: x['limit'])
            ler = lerdas[-1]
            ler['limit'] = 0

            ler['ch'][pop.nG, :] = pop.getDataPop(1)
            ler['value'][pop.nG] = pop.objective(ler['ch'][pop.nG, :])
