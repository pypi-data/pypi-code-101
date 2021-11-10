from setuptools import setup, find_packages
from os.path import join, dirname

setup(name='kholodov_hist',
      version='0.1',
      description='dummy projec',
      packages=find_packages(),
      author_email='ksteklo@mail.ru',
      zip_safe=False,
      install_requires=['matplotlib==3.4.3'])
