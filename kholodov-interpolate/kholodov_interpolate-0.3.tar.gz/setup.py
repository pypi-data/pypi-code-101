from setuptools import setup, find_packages
from os.path import join, dirname

setup(name='kholodov_interpolate',
      version='0.3',
      description='dummy projec',
      packages=find_packages(),
      author_email='ksteklo@mail.ru',
      zip_safe=False,
      install_requires=['numpy', 'matplotlib==3.4.0'])
