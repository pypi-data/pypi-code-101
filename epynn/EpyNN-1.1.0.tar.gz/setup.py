from distutils.core import setup
from setuptools.config import read_configuration
from setuptools import find_packages

conf_dict = read_configuration("setup.cfg")

setup(packages=find_packages(), scripts=['bin/epynn'])
