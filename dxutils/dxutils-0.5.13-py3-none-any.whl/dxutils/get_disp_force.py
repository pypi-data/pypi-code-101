#!/usr/bin/env python3
#
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
from numpy import array, zeros, arange, savetxt
from numpy import dot, mod
from numpy.linalg import inv
from numpy.random import choice
import ase
import ase.io
import ase.units as units
from ase.atoms import Atoms
import glob
import click
import sys
from dxutils.utils import read_potim, normalize_traj, read_traj
import os.path
from contextlib import ExitStack

@click.command()
@click.option('-p', '--poscar', default='SPOSCAR', type=click.Path(exists=True), 
              help='Supercell POSCAR file (SPOSCAR)')
@click.option('-t', '--traj', default='./vasprun.xml', type=click.Path(exists=True), 
              help='Trajectory file OUTCAR or vasprun.xml (vasprun.xml)')
@click.option('-s', '--skip', default=0, help='Skip initial time steps (0)')
@click.option('-n', '--number', default=50, help='Number of configurations (50)')
@click.option('-d', '--disp', default='disp.dat', help='Displacement file (disp.dat)')
@click.option('-f', '--force', default='force.dat', help='Forces file (force.dat)')
@click.option('-c', '--configs', is_flag=True, default=False, help='Write disp_xxx.POSCAR files')
@click.option('-r', '--report', default=None, type=click.Path(exists=False), 
              help='Report selected timestaps to file (no report by default)')
@click.option('--hff', is_flag=True, default=False, help='Write PHONON HFfile')
@click.option('--dff', is_flag=True, default=True, help='Write disp/force files for alamode')
def make_disp_force(poscar, traj, skip, number, disp, force, configs, report, hff, dff):
    """Generates displacement and forces files from the MD trajectory"""
    rpt=None
    base=ase.io.read(poscar)
    dn, fn = os.path.split(traj)
    if fn :
        md=read_traj(dn, skip, fn)
    else :
        md=read_traj(dn, skip)
    pos=md['pos']
    spos=md['spos']
    tr=md['trj']
    p0=pos.mean(axis=0)
    sp0=spos.mean(axis=0)
    n = 0

    print(f'#Writing output files from {number} random steps out of {traj} file.')
    print('#Time steps:')

    with ExitStack() as estack:
        if hff :
            hffile = estack.enter_context(open('HFfile','tw'))

        if dff :
            dsp = estack.enter_context(open(disp, 'bw'))
            frc = estack.enter_context(open(force, 'bw'))

        if configs and report is not None:
            rpt = estack.enter_context(open(report, 'tw'))

        for k in sorted(choice(arange(pos.shape[0]), number, replace=False)):
            if dff :
                savetxt(dsp, (pos[k]-p0)/units.Bohr, fmt='%24.18f')
                savetxt(frc, tr[k].get_forces()/(units.Ry/units.Bohr), fmt='%24.18f')
            if hff :
                for p,d in zip(base.get_scaled_positions(),spos[k]-sp0):
                    if not np.allclose(d,0.0,atol=1e-05):
                        hffile.write((3*'%9.5f '+3*'%10.6f'+'\n')%(tuple(p)+tuple(d))) 
                for i,(s,p,f) in enumerate(zip(base.get_chemical_symbols(),base.get_scaled_positions(),tr[k].get_forces())):
                        hffile.write((f'{i+1:4} {s[0]}'+3*'%8.5f'+3*'%10.6f'+'\n')%(tuple(p)+tuple(f)))
            print(f'{k+skip}', end=' ')
            sys.stdout.flush()
            if configs :
                a=Atoms(tr[k])
                a.set_pbc(False)
                a.set_positions(pos[k])
                ase.io.write(f'disp_{n:04d}_{k:04d}.POSCAR', a, direct=True, vasp5=True)
                if rpt is not None :
                    rpt.write(f'{k+skip}\n')
            n+=1
    print()
    print(f'#Finished: {number} configs extracted')
        
if __name__ == '__main__':
    make_disp_force()
