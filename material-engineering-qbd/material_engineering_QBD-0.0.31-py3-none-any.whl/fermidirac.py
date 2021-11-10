import units_QBD as uqbd
import numpy

def fds__ho(energy__grid, F_v, T):
    fds = []
    for energy in energy__grid:
        fds.append(0)
        fds[-1] += 1 / (1 + numpy.exp((F_v - energy) / uqbd.K_B[0] / T)) 
    return fds

def fds__el(energy__grid, F_c, T):
    fds = []
    for energy in energy__grid:
        fds.append(0)
        fds[-1] += 1 / (1 + numpy.exp((energy - F_c) / uqbd.K_B[0] / T)) 
    return fds


def F__calibration(T, eU, F_i__bottom, F_i__top, energy__grid, dos__holes, dos__electrons):
    
    F_half = eU / 2.

    c_e = 0
    c_h = 0

    F_i = ...
    F_v = ...
    F_c = ...

    max_ = F_i__top
    min_ = F_i__bottom
    dE = energy__grid[1] - energy__grid[0]
    while max_ - min_ >= dE:
        c_e = 0
        c_h = 0

        F_i = (max_ + min_) / 2.
        F_c = F_i + F_half
        F_v = F_i - F_half

        fds__ho_ = fds__ho(energy__grid, F_v, T)
        fds__el_ = fds__el(energy__grid, F_c, T)

        for i in range(0,len(energy__grid)):
            c_h += dos__holes[i] * fds__ho_[i]
            c_e += dos__electrons[i] * fds__el_[i]

        if c_e > c_h:   max_ = (max_ + min_) * 0.5
        else :          min_ = (max_ + min_) * 0.5

    return F_v, F_i, F_c