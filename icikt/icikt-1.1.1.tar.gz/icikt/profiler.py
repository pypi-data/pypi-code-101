import cProfile as cP
import pstats

import scipy.stats as sci
import cykt
import icikt
import numpy as np
import pyximport


#
largeArray = np.genfromtxt('/mlab/data/psbhatt/projects/pythonICIKendallTau/test/bigTest2.tab.csv', delimiter="\t")
# cP.runctx("icikt.iciktArray(largeArray)", globals(), locals(), "Profile.prof")
# cP.runctx("icipkt.iciktArray(largeArray)", globals(), locals(), "Profile.prof")

#
# np.stack
# np.random.seed(10)
# w = np.random.randint(0, 20_000, 10_000_000).astype(float)
# z = np.random.randint(0, 20_000, 10_000_000).astype(float)

# print(largeArray)
x = largeArray[:, 0]
y = largeArray[:, 1]
# print(x,y)
x[x == 0] = np.nan
y[y == 0] = np.nan
naReplaceX = np.nanmin(x) - 0.1
naReplaceY = np.nanmin(y) - 0.1
np.nan_to_num(x, copy=False, nan=naReplaceX)
np.nan_to_num(y, copy=False, nan=naReplaceY)
# print(x,y)
# x = np.genfromtxt('/run/media/psbhatt/E004-96BC/icikendalltau_test/large_test/p_1.txt')
# y = np.genfromtxt('/run/media/psbhatt/E004-96BC/icikendalltau_test/large_test/p_2.txt')
# print(x,y)
#
# cP.runctx("icipkt.iciktArray(largeArray)", globals(), locals(), "icipkt.prof")
# print(sci.kendalltau(x,y))
print(icikt.iciKT(x,y))
# cP.runctx("icikt.iciKT(x,y)", globals(), locals(), "icipkt.prof")
# print("w and z:", w, w.dtype, z, z.dtype)
# cP.runctx("icipkt.iciKT(w,z)", globals(), locals(), "icipkt.prof")

# cP.runctx("icikt.iciKT(x,y)", globals(), locals(), "icikt.prof")
# cP.runctx("kto.kendalltau(x,y)", globals(), locals(), "kendalltauog.prof")

# cP.runctx("kto.kendalltau(x,y)", globals(), locals(), "Profile.prof")
# cP.runctx("cyktx.kendalltau(x,y)", globals(), locals(), "Profile.prof")

# one = pstats.Stats("icipkt.prof")
# two = pstats.Stats("icikt.prof")

# s.strip_dirs().sort_stats("time").print_stats()
