from setuptools import setup

setup(name='DensityClust',
      version='1.0',
      author='Luo Xiaoyu',
      description='the local density clustering algorithm',
      author_email='vastlxy@163.com',
      py_modules=['DensityClust.densityCluster_3d',
                  'DensityClust.dist_xyz',
                  'DensityClust.distx',
                  'DensityClust.extroclump_parameters',
                  'DensityClust.get_xx',
                  'DensityClust.kc_coord_3d_new',
                  'DensityClust.localdensityClustering',
                  'DensityClust.tools',
                  'DensityClust.make_plot']
      )