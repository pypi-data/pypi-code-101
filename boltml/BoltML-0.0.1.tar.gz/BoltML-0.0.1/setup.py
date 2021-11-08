from setuptools import setup, find_packages
import os
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='BoltML',
  version="0.0.1",
  ##description=' to be given',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  ##url='Github URL',  
  author='Om Chaithanya V\nVenkata Sai Prakash Y',
  ##author_email='MailID',
  license='MIT', 
  classifiers=classifiers,
  keywords='AutoML', 
  packages=find_packages(),
  install_requires=["NumPy>=1.16.2",
    "lightgbm>=2.3.1",
    "xgboost>=0.90,<=1.3.3",
    "pandas>=1.1.4",
    "scikit-learn>=0.24"] 
)