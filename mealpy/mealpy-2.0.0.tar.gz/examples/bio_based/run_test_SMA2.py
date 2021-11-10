#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 11:20, 20/10/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

from opfunu.cec_basic.cec2014_nobias import *
from mealpy.bio_based import SMA, VCS, BBO, EOA, IWO, SBO
from mealpy.swarm_based import HGS
from mealpy.physics_based import EO
from mealpy.evolutionary_based import MA, FPA, ES, EP, DE
from mealpy.music_based import HS
from mealpy.system_based import WCA, GCO, AEO
from mealpy.math_based import AOA, HC, SCA
from mealpy.human_based import BRO, CA, FBIO, SARO, SSDO, TLO, GSKA, LCO, ICA
from mealpy.physics_based import ArchOA, ASO, EFO, HGSO, MVO, WDO, SA
from mealpy.swarm_based import ABC, ACOR, AO, BA, WOA, SpaSA, SLO, SHO, SalpSO, NMRA, MSA, MRFO, MFO, JA, HHO, GWO, EHO, CSO
from mealpy.swarm_based import GOA, CSA, BSA, ALO, BeesA, BES, FireflyA, FOA, PFA, COA, FA, SFO, SSpiderA, SSpiderO, SRSR, PSO
from mealpy.problem import Problem
from mealpy.utils.termination import Termination
import numpy as np

# Setting parameters

# A - Different way to provide lower bound and upper bound. Here are some examples:

def objective(x):
    # return x[0]**2 + (x[1] + 1)**2 - 5 * np.cos(1.5* x[0] + 1.5) - 3 * cos(2 * x[0] - 1.5)
    # return (x[0]-3.14)**2 + (x[1] - 2.72)**2 + np.sin(3*x[0]+1.41) + sin(4*x[1] -1.73)
    return np.sum(x**2)

## A1. When you have different lower bound and upper bound for each parameters
problem_dict1 = {
    "obj_func": objective,
    "lb": [-10, -10],
    "ub": [10, 10 ],
    "minmax": "min",
    "verbose": True,
}

if __name__ == "__main__":
    problem_obj1 = Problem(problem_dict1)
    ### Your parameter problem can be an instane of Problem class or just dict like above
    model1 = PSO.CL_PSO(problem_obj1, epoch=500, pop_size=50)
    model1.solve(mode="thread")
    print(model1.solution[0])
