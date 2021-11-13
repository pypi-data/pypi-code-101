import codecs
import os

from setuptools import setup, find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


def read_install_requires():
    reqs = [
        'pandas>=1.3.4',
        'requests>=2.26.0',
    ]
    return reqs


setup(
    name='lsywywsdk',
    version=read('lsywywsdk/VERSION.txt'),
    description='sdk for lsywywtools',
    author='zhoujianhua',
    install_requires=read_install_requires(),
    packages=find_packages(),
    include_package_data=True,
)
