# coding: utf-8
# python setup.py sdist register upload
from setuptools import setup

setup(
    name='es-configly',
    version='0.0.0',
    description='config manager using elasticsearch.',
    author='Kazuhiro Kotsutsumi',
    url='https://github.com/kotsutsumi/es-configly',
    packages=[
        'es_configly',
    ],
    include_package_data=True,
    license='The MIT License',
    install_requires=[
        'bvx_env',
        'bvx_es',
        'elasticsearch',
        'elasticsearch-dbapi',
        'six',
        'sqlalchemy',
        'bvx_pytest',
        'pytest~=6.2.5',
    ],
)

# EOF
