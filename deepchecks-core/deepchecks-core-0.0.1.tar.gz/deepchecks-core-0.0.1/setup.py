import setuptools
from setuptools import setup
import os

VER="0.0.1"

setup(
    name='deepchecks-core',
    version=VER,
    packages=setuptools.find_packages(),
    description = 'Package for validating your machine learning model and data',
    author = 'deepchecks',
    author_email = 'info@deepchecks.com',
    url = 'https://github.com/deepchecks/MLChecks',
    download_url = "https://github.com/deepchecks/MLChecks/releases/download/{0}/mlchecks-{0}.tar.gz".format(VER),
    keywords = ['Software Development', 'Machine Learning'],
    classifiers         = [
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
