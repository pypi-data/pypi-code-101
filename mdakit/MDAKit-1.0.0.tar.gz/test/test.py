
import os
import pandas as pd
from tools.rg import RgCalculator
from tools.rmsf import RMSFCalculator
from tools.rmsd import RMSDCalculator
from lib.msmtools.msm import AutoBuildMarkovStateModel

from lib.msmtools.GMRQ import  GMRQValid
#### MSM module test
def test_for_msm():
    topologyfile = './example/pentapeptide/pentapeptide-impl-solv.pdb'
    xtcfiles = sorted([ os.path.join('./example/pentapeptide/', _) for _ in os.listdir('./example/pentapeptide/') if _.endswith('impl-solv.xtc')])
    AutoBuildMSM = AutoBuildMarkovStateModel(topologyfile, xtcfiles, 'automsm')
    print(AutoBuildMSM.units)
    AutoBuildMSM.traj_stat(timeunit='us')
    AutoBuildMSM.traj_stat(timeunit='us')
    print(AutoBuildMSM.n_traj)
    print(AutoBuildMSM.total_times)
    
    AutoBuildMSM.featurelize()
    data = AutoBuildMSM.src.get_output()
    valid = GMRQValid()
    results = valid.tICA_para_nICs(data)
    print(results)

    


#### RMSF module test
def test_for_single():
    RMSFCal = RMSFCalculator()
    #topologyfile = './example/pentapeptide/pentapeptide-impl-solv.pdb'
    #xtcfile = './example/pentapeptide/pentapeptide-00-500ns-impl-solv.xtc'
    topologyfile = './example/1ycr.pdb'
    xtcfile = './example/1ycr.pdb'
    rmsf = RMSFCal.cal_rmsf_xingle_traj(topologyfile, xtcfile)
    print(rmsf)

def test_for_multiple():
    RMSFCal = RMSFCalculator()
    topologyfile = './example/pentapeptide/pentapeptide-impl-solv.pdb'
    xtcfiles = sorted([ os.path.join('./example/pentapeptide/', _) for _ in os.listdir('./example/pentapeptide/') if _.endswith('impl-solv.xtc')])
    rmsf,_ = RMSFCal.cal_rmsf_mul_traj(topologyfile, xtcfiles, selection='name CA', mode='residue')
    print(rmsf)

def test_for_rg():
    topologyfile = './example/1ycr.pdb'
    xtcfile = './example/1ycr.pdb'
    topologyfile = './example/pentapeptide/pentapeptide-impl-solv.pdb'
    xtcfiles = sorted([ os.path.join('./example/pentapeptide/', _) for _ in os.listdir('./example/pentapeptide/') if _.endswith('impl-solv.xtc')])

    RgCal = RgCalculator()
    rg = RgCal.cal_rg_mul_traj(topologyfile, xtcfiles, selection='mass>=2')
    print(rg)
    #h,e = RgCal.hist_1D()

def test_for_rmsd():
    topfile = './example/msm/top.pdb'
    xtcfiles = sorted([ os.path.join('./example/msm/msm_sample100/', _) for _ in os.listdir('./example/msm/msm_sample100/') if _.endswith('.xtc')])
    RMSDCal = RMSDCalculator()
    rmsd = RMSDCal.cal_rmsd_mul_traj(topfile, xtcfiles[:10], selection='backbone')
    pi = pd.read_pickle('./example/msm/msm_lag250.pkl3').pi
    RMSDList, populations, stateRMSD = RMSDCal.cal_rmsd_ensemble(topfile, xtcfiles, topfile, pi, selection='backbone')
    print(RMSDList)


if __name__ == "__main__":
    test_for_rmsd()
    # test_for_multiple()
    #test_for_msm()
    #test_for_rg()