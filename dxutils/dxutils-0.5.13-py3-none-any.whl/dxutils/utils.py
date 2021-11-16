# -*- coding: utf-8 -*-
#
# Utility functions for atomistic calculations analysis
# (C) 2018 by Paweł T. Jochym
#
#    This file is part of DXutils.
#
#    DXutils is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    DXutils is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with DXutil.  If not, see <https://www.gnu.org/licenses/>.
#

import numpy as np
from numpy import array, zeros, arange
from numpy import dot, mod, std, mean, linspace
from numpy import exp, log, sqrt, pi
from numpy.linalg import inv
from matplotlib.pyplot import plot, hist, axvline, hlines
import ase
import ase.io
import ase.units as units
from ase.atoms import Atoms
import glob
import itertools
import sys
import spglib


def polyprint(p, var='x', frm=' %+.5g'):
    '''
    Pretty-print a polynomial p in the form ready 
    to include in the LaTeX text (without $s).
    You can specify format used for coeficients in frm argument.
    '''
    if len(p) < 1 :
        return ''
    up = ''.join([(frm + ' %s^{%d}') % (a, var, len(p)-d-1) 
                  for d, a in enumerate(p[:-2])  if abs(a)>0])
    lt = ''.join([(frm + ' %s') % (a, var)  
                  for d, a in enumerate(p[-2:-1]) if abs(a)>0])
    ft = ''.join([frm % (a,)  
                  for d, a in enumerate(p[-1:])  if abs(a)>0])
    s = (up + lt + ft).lstrip()
    if p[0] > 0 :
        return s[1:]
    else :
        return s


def gauss_fit(d, lbl='', msd=False, bins='auto'):
    '''
    Make a histogram and fit/plot gaussian to the density
    with params in added to the label.
    Returns mean and standard deviation tuple.
    '''
    d=array(d).reshape(-1)
    s=d.std()
    m=d.mean()
    msd_lbl=''
    if msd :
        msd_lbl=f'; msd={(d**2).mean():.4f}'
    hist(d, label=lbl + f' ($\\sigma={s:.3f}$' + msd_lbl + ')', 
           bins=bins, alpha=0.3, density=True)
    x=linspace(-3*s+m,3*s+m,100)
    plot(x,exp(-(x-m)**2/(2*s**2))/(s*sqrt(2*pi)))
    axvline(m, lw=1, ls=':', label=f'$\\bar{{x}}={m:.4f}$')
    fwhm=sqrt(2*log(2))*s
    hlines(1/(2*s*sqrt(2*pi)),m-fwhm,m+fwhm,linestyles='dashed', lw=1)
    return m, s


def calc_velocities(ai,af,dt):
    '''
    Calculate atomic velocities between initial (ai) and final (af)
    structures separated by timestep dt. The procedure takes into 
    account crossing of the PBC.
    '''
    sdx=(af.get_scaled_positions()-ai.get_scaled_positions())    
    # Detect and handle jumping over the PBC
    # Build an array of shifts by detecting when 
    # scaled positions jumped from one side to the other
    sht=(sdx > 0.5)*1 - (sdx < -0.5)*1
    # Modify the final position by unwrapping the jumps
    cf=Atoms(af)
    cf.set_scaled_positions(af.get_scaled_positions()-sht)
    # Use modified final position to calculate displacement
    dx=cf.get_positions()-ai.get_positions()
    
    # Check if we succeded in handling PBC
    # The displacement should be smaller then 
    # one third of the main diagonal of the cell.
    # Unfortunately this is not exact but should catch the errors
    # and if you have velocities this high something is wrong with
    # your simulation anyway (probably to high timestep).
    assert (np.linalg.norm(dx,axis=-1) < 
            np.linalg.norm(np.sqrt(np.sum(cf.get_cell()**2, axis=0)))/3).all()
        
    return dx/dt


def assign_velocities(tr,dt):
    '''
    Assign velocities to trajectories based on finite differences of positions
    '''
    v=[calc_velocities(ai, af, dt) for ai,af in zip(tr[:-1],tr[1:])]
    tr[0].set_velocities(v[0])
    tr[-1].set_velocities(v[-1])
    for n, a in enumerate(tr[1:-1]):
        # The index in v is shifted by one to the left vs. tr !
        a.set_velocities((v[n]+v[n+1])/2)


def read_potim(fn):
    '''
    Read POTIM from OUTCAR. Returns float value or None.
    '''
    pat='0123456789.'
    with open(fn) as f:
        for l in f:
            if 'POTIM' in l:
                potim=[c for c in l if c in pat]
                return float(''.join(potim))
    return None    


def center_particle(s):
    '''
    Center particle's CM in the PBC box. 
    For this algorithm to work there need to be at least 
    25% vacuum around the particle.
    '''

    a = Atoms(s, pbc=True)
    cm = a.get_center_of_mass()
    n = 0
    while True :
        # This should converge in max 5 steps
        # if we are above 8 something must be wrong
        assert n < 8
        # position around CM
        a.set_positions((a.get_positions() - a.get_center_of_mass()))
        spos = a.get_scaled_positions()
        # detect wrapped-around coords and wrap them back to
        # cluster around origin
        spos -= 1*(spos>0.5)
        # move the particle to the center of the box
        a.set_scaled_positions(spos+0.5)
        pcm = cm
        cm = a.get_center_of_mass()
        # CM did not move 
        if np.linalg.norm(cm-pcm) < 1e-4 : break
    # No atom should be further from the center then 40% of unit cell
    # If it gets so close to boundary it is too small box anyway
    assert (a.get_scaled_positions() - 0.5).max() < 0.4
    return a


def normalize_traj(tr, particle=False):
    '''
    Try to normalize the trajectory by unwrapping the jumps over
    periodic boundary conditions (PBC) and removing the center-of-mass (CM)
    drift. The procedure cannot guaratee perfectly removing all problems
    because PBC leeds to some information loss, but works for most
    cases. The function outputs multiple variants of trajectory 
    as tuple of numpy arrays. The first index numbers timesteps.
	First step is used as a reference structure and CM position.

    !!!!!!!!!! WARNING !!!!!!!!!!
    This will not work if the unit cell changes along trajectory!
    
    Input
    -----
    tr - List of Atoms structures (images in ASE language) as read by 
         ase.io.read function.
    particle - Use particle+vacum algorithm, 
                keep all atoms around middle of the U.C.
         
    Output
    ------
    pos  - normalized carthesian trajectory
    spos - normalized fractional directory
    sdx  - fractional step-to-step displacements. These are *not* full 
           integrated displacements from the reference structure
    stcm - fractional trajectory of CM (CM drift) 
    tcm  - carthesian trajectory of CM
    '''
    base=Atoms(tr[0])
    cell=base.get_cell()
    
    # All calculations below are computed in fractional coordinates 
    spos=array([a.get_scaled_positions() for a in tr])

    if particle :
        # Unwrap all positions to the (0.2,0.8) range
        # to make the particle continous and in the center.
        # The CM drift should be removed at this point,
        # and CM shoud be at the center of the box.
        spos = array([center_particle(a).get_scaled_positions() for a in tr])
        # We do not recover real CM trajectory. Provide fake one.
        stcm = 0.5*np.ones((len(tr),3))
    else :
        # This is for cristalline matrials
        # We cannot use center of mass as valid concept
        # We use it here only as a measure of total drift of the system
        # The algorithm only tracks the initial positions and
        # unwraps any jumps over the PBC to get final CM trajectory
        # which is removed from the particle trajectories.
        # Calculate unwrapped step-by-step atom displacements
        sdx = spos[1:]-spos[:-1]
        sht = (sdx < -0.5)*1 - (sdx > 0.5)*1
        sdx += sht
        # Check if step-to-step fractional displacements are below 1/3
        assert (abs(sdx) < 1/3).all()
        
        # Unwrap spos using jumps detected in sht
        # This allows for multiple jumps and jumps > 1 but not in one step
        spos[1:] += sht.cumsum(axis=0)

        # Calculate step-to-step CM drift and integrate it to get CM trajectory
        # CM displacements
        sdcm=(sdx*base.get_masses()[None,:,None]).sum(axis=1)/base.get_masses().sum()
        # Integrate (sum) the displacements
        stcm=sdcm.cumsum(axis=0)	
        
        # Remove CM drift from (unwrapped) spos
        # This should work even for multipple crossings of CM over PBC
        spos[1:]-=stcm[:,None,:]
        
        # Return carthesian positions, fractional positions, 
        # second order central gradient of fractional positions,
        # fractional cm traj, cm traj
    return (dot(spos,cell), spos, 
            np.gradient(spos, axis=0, edge_order=2), 
            stcm, dot(stcm,cell))


def read_traj(fn, skip=0, format=None, particle=False):
    '''
    Read the trajectory from vasprun.xml or OUTCAR
    Calculate the velocities (unwrapping PBC jumps)
    Remove the CM drift from the system
    Skips 'skip' steps from the first file.

    Input:
        fn - file name or list of file names
        skip - remove first skip steps from the trajectory
        format - ase.io.read format string for file format
        particle - Use particle+vacum algorithm, 
                    keep all atoms around middle of the U.C.

    Returns dictionary containing:
        dt: timestep from first file
        fname: list of source file names
        trj: list with unmodified source trajectory Atoms objects
        pos: unwrapped positions, 
        spos: unwrapped fractional positions, 
        vel: velocities 
        drift: CM drift.
    '''
    if not isinstance(fn, list):
        fn = [fn]
    tr=[]
    for f in fn:
        print(f'Reading {f}',end=':')
        pl = len(tr)
        tr += ase.io.read(f'{f}',index=f'{skip}:', format=format)
        skip=0
        print(f'{len(tr)-pl}')
    dt=read_potim(f'{fn[0]}')*ase.units.fs
    print(f'Trajectory length: {len(tr)}')

    cell=tr[0].get_cell()
    
    pos, spos, sdx, stcm, tcm = normalize_traj(tr, particle)
    
    # Calculate the velocities from position gradients
    v=dot(sdx,cell)/dt
    
    # Store the data
    return {
        'dt':dt,
        'fname': fn,
        'trj': tr,
        'pos': pos,
        'spos': spos,
        'vel': v,
        'drift':tcm,
        'sdrift': stcm,
    }

def make_primitive_cell(sc, verbose=True):
    '''
    Create primitive unit cell for a given supercell.
    
    Input
    -----
    sc - ase.Atoms object containing supercell
    verbose - print crystal information
    
    Output
    ------
    ase.Atoms object containing primitive unit cell
    '''
    pc = spglib.find_primitive(sc)
    return Atoms(cell=pc[0], 
                 scaled_positions=pc[1], 
                 numbers=pc[2], pbc=True)
