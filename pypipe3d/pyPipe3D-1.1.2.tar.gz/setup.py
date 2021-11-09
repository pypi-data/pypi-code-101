#!/usr/bin/env python
import os
from setuptools import setup, find_packages

def version(fn):
    v = ''
    with open(fn, 'r') as f:
        for l in f.readlines():
            if '__version__' in l:
                v = l.split('=')[-1].strip().replace("'", '').split(' ')[-1][1:]
    return v

def readme():
   with open('README.md') as f:
       return f.read()

with open('requirements.txt', 'r') as r:
   filtered_lines = filter(lambda line: not line.startswith('#'), r.readlines())
   requirements = list(map(lambda s: s.replace('\n', ''), filtered_lines))
   print(requirements)

DATA_DIRNAME = 'data'
SCRIPTS_DIRNAME = 'bin'
VERSION_FILE = 'pyFIT3D/common/constants.py'

all_packages = find_packages()
packages_data = {
    package: [f'{DATA_DIRNAME}/*']+[f'{os.path.join(DATA_DIRNAME, sub)}/*' for root, subs, files in os.walk(os.path.join(package, DATA_DIRNAME)) for sub in subs]
    for package in all_packages if os.path.isdir(os.path.join(package, DATA_DIRNAME))
}
scripts = [
    os.path.join(SCRIPTS_DIRNAME, script_name)
    for script_name in os.listdir(SCRIPTS_DIRNAME) if script_name.endswith('.py')
]
version = version(VERSION_FILE)

setup(
    name='pyPipe3D',
    version=version,
    description='A Python implementation of the FIT3D code',
    long_description=readme(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Astronomy',
    ],
    keywords='galaxies',
    url='https://gitlab.com/pipe3d/pyPipe3D',
    download_url='https://gitlab.com/pipe3d/pyPipe3D/-/archive/v1.1.2/pyPipe3D-v1.1.2.tar.gz',
    author='pipe3d',
    author_email='pipe3d@astro.unam.mx',
    license='MIT',
    packages=all_packages,
    setup_requires=['wheel'],
    install_requires=requirements,
    include_package_data=True,
    package_data=packages_data,
    scripts=scripts,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
)
