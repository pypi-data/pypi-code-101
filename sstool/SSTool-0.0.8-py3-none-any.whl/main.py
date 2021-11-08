import numpy as np
import pandas as pd
import sympy as sym
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
from control.matlab import *


# from SSTool.engine import build  # global, from the pip install
from engine import build, stability
import os.path

# 1. run core
fullpath = os.path.abspath('datafiles/annakkage_luis_v5.xlsx')
syst = build.create_syst(fullpath)

# 2. extract information, store data
# print(syst.syst_C)
# build.store_info(syst.RLs[0].A, 'R_test')
# build.store_info(syst.ss_final.A, 'SS_A')

# 3. study stability
# stability.bode_YZ(syst.VSCs[0], f_ini=0, f_fin=3, name_in=['vq_1', 'vd_1'], name_out=['iqxv_1', 'idxv_1'], n_p=1000, logx=False, dBy=False, invert=False)
# stability.eigenval_YZ(syst.VSCs[0], f_ini=0, f_fin=3, name_in=['vq_1', 'vd_1'], name_out=['iqxv_1', 'idxv_1'], n_p=1000, invert=False, type_plot='re_im')
# stability.eigen(syst.VSCs[0], plot=True, prnt=True)

# nyquist
side1 = syst.VSCs[0]
side2 = stability.merge_all_minus1(fullpath, syst, 'VSC', 0)
stability.nyquist_YZ(ss_class_act=side1, ss_class_psv=side2, f_ini=1.0, f_fin=3.0, name_in=['vq_1', 'vd_1'], name_out=['iqxv_1', 'idxv_1'], n_p=10000, n_arrows=5, invert=False)


