# coding: utf-8
# python setup.py sdist register upload
from setuptools import setup

setup(
    name='bvx-env',
    version='0.0.1',
    description='env helpers.',
    author='Kazuhiro Kotsutsumi',
    url='https://github.com/kotsutsumi/bvx-env',
    packages=[
        'bvx_env',
    ],
    include_package_data=True,
    license='The MIT License',
    install_requires=[
        'python-dotenv~=0.19.1', 'python-box~=5.4.1'
    ],
)

# EOF
