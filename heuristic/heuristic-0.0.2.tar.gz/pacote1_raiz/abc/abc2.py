# -*- coding: utf-8 -*-
import numpy as np


class Abc2:
    """
    name = abc
    source =  ... ... ..
    author = João Vitor Coelho Estrela
    nPop = nPop//2
    """

    def __init__(self):
        pass

    def getParameters(self, pop):
        scoutLimit = pop.ranges.shape[0]*(pop.nPop)/2
        return {'scoutLimit': scoutLimit}


    @staticmethod 
    def arrangement(x_sol, z_decisao, rng, K=10, D=50, epsilon=0.01, delta=0.2):
        """ALGORITMO ARRANGEMENT: GANRANTE TODAS AS SOLUÇÕES VIÁVEIS."""
        
        mask = z_decisao == 1
        
        while z_decisao.sum() < K:
            j = rng.choice(D)
            while z_decisao[j] == 1:
                j = rng.choice(D)
            z_decisao[j] = 1

        while z_decisao.sum() > K:
            j = rng.choice(D)
            while z_decisao[j] == 0:
                j = rng.choice(D)
            z_decisao[j] = 0
            x_sol[j] = 0

        x_sol[mask] = np.clip(x_sol[mask], epsilon, delta)

        psi = x_sol[mask].sum()

        x_sol = np.where(mask, x_sol, 0)/psi

        return x_sol, z_decisao


    def start(self, pop):
        pop.nPop = pop.nPop*2  # No momento o usuario deve passar nPop
        pop.createNewPop(0)  # Preciso só de metade [::2]
        
        
        for p in pop.pList:
            p['fitness'] = np.empty_like(p['value'])
            p['z'] = np.empty_like(p['ch'])
            p['limit'] = 0
            
            rnd_z = pop.rng.uniform(size=(pop.nVar))
            p['z'][0, :] = np.where(rnd_z < 0.5, 1, 0)
            p['ch'][0, :] = np.where(rnd_z < 0.5, p['ch'][0, :], 0)
            p['ch'][0, :], p['z'][0, :] = Abc2.arrangement(p['ch'][0], p['z'][0, :], pop.rng)

        pop.evalPop(0)
        Abc2._fitness(pop.pList, 0)

        pTemp = pop.getBestPop(0)
        pop.pBest['ch'][0, :] = pTemp['ch'][0, :]
        pop.pBest['value'][0] = pTemp['value'][0]
        
        pop.pBest['z'] = np.empty_like(pTemp['z'])
        pop.pBest['z'][0, :] = pTemp['z'][0, :]


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
            emBee['z'][pop.nG, :] = emBee['z'][pop.nG-1, :]
            emBee['value'][pop.nG] = emBee['value'][pop.nG-1]
            emBee['fitness'][pop.nG] = emBee['fitness'][pop.nG-1]
            # - - - - - - - - - - - - - - - - - - - - - - - - - -

            

            neighbour = pop.rng.choice(employedBee)  # Abelha k
            while emBee is neighbour:
                neighbour = pop.rng.choice(employedBee)

            
            zi = emBee['z'][pop.nG, :]
            zk = neighbour['z'][pop.nG, :]
            z_new = np.round(1/(1 + np.e**(-zi + pop.rng.uniform(size=pop.nVar) * (zi - zk))) - 0.06)
            
            phi = pop.rng.uniform(-1, 1, size=pop.nVar)

            vI = emBee['ch'][pop.nG-1, :] + phi*(
                 emBee['ch'][pop.nG-1, :] - neighbour['ch'][pop.nG-1, :])
            vI = np.clip(vI, pop.ranges[:, 0], pop.ranges[:, 1])
            
            rnd = pop.rng.uniform(size=pop.nVar)
            vI = np.where(np.logical_and(rnd < 0.8, z_new == 1), vI, 0)
            z_new = np.where(np.logical_and(rnd < 0.8, z_new == 1), z_new, 0)


            value = pop.objective(vI)

            if value >= 0:
                fit = 1 / (1 + value)
            else:
                fit = 1 + abs(value)

            if fit > emBee['fitness'][pop.nG - 1]:
                emBee['fitness'][pop.nG] = fit
                emBee['value'][pop.nG] = value
                emBee['ch'][pop.nG, :] = vI
                emBee['z'][pop.nG, :] = z_new
                emBee['limit'] = 0
            else:
                emBee['limit'] += 1

        # print('**************** ONs *******************')
        prob = Abc2._computeProbability(employedBee, pop.nG)

        for k in range(len(employedBee)):

            onBee = pop.rng.choice(employedBee, None, p=prob)

            neighbour = pop.rng.choice(employedBee)


            while onBee is neighbour:
                neighbour = pop.rng.choice(employedBee)

            zi = onBee['z'][pop.nG, :]
            zk = neighbour['z'][pop.nG, :]
            z_new = np.round(1/(1 + np.e**(-zi + pop.rng.uniform(size=pop.nVar) * (zi - zk))) - 0.06)

            phi = pop.rng.uniform(-1, 1, size=pop.nVar)
            
            vI = onBee['ch'][pop.nG, :] + phi*(
                 onBee['ch'][pop.nG, :] - neighbour['ch'][pop.nG, :])
            vI = np.clip(vI, pop.ranges[:, 0], pop.ranges[:, 1])
            
            rnd = pop.rng.uniform(size=pop.nVar)
            vI = np.where(np.logical_and(rnd < 0.8, z_new == 1), vI, 0)
            z_new = np.where(np.logical_and(rnd < 0.8, z_new == 1), z_new, 0)

            value = pop.objective(vI)

            if value >= 0:
                fit = 1 / (1 + value)
            else:
                fit = 1 + abs(value)

            if fit > onBee['fitness'][pop.nG]:
                onBee['fitness'][pop.nG] = fit
                onBee['value'][pop.nG] = value
                onBee['ch'][pop.nG, :] = vI
                onBee['z'][pop.nG, :] = z_new
                onBee['limit'] = 0
                # print('melhorou')
            else:
                onBee['limit'] += 1
                # print('N melhorou')


        # PEGAR APENAS A COM MAIOR 'ESTOURO'
        lerdas = [p for p in employedBee
                  if p['limit'] >= pop.parameters['scoutLimit']]

        if (len(lerdas) > 0):
            lerdas.sort(key=lambda x: x['limit'])
            ler = lerdas[-1]
            ler['limit'] = 0

            ler['ch'][pop.nG, :] = pop.getDataPop(1)
            ler['value'][pop.nG] = pop.objective(ler['ch'][pop.nG, :])


        for p in pop.pList:
            x = p['ch'][pop.nG]
            z = p['z'][pop.nG]
            p['ch'][pop.nG], p['z'][pop.nG] = Abc2.arrangement(x, z, pop.rng)        


        pTemp = pop.getBestPop(pop.nG)
        pop.pBestUpdate(pTemp, pop.nG)
        pop.pBest['z'][pop.nG, :] = pTemp['z'][pop.nG, :]
