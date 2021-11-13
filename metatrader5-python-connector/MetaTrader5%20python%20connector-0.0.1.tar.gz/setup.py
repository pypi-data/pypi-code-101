import io 
import os
from platform import platform 
import sys 
from shutil import rmtree 

from setuptools import find_packages, setup, Command 

setup(
    name='MetaTrader5 python connector',
    description='A package for interacting and retrieving data from the\n\
                MetaTrader 5 platform',
                version='0.0.1',
                author='Dag Arne Lydvo',
                author_email='daglyd@outlook.com',
                packages=find_packages(exclude='tests'),
                include_package_data=True

)