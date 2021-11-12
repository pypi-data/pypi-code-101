from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Database line json'
LONG_DESCRIPTION = 'Database with methods put, find and remove'

setup(
    name='lotusdb',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='d3tu',
    author_email='jpafly@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='database',
    classifiers= [
        'Programming Language :: Python :: 3'
    ]
)