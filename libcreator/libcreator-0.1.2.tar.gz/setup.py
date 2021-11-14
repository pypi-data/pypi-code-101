from setuptools import find_packages, setup
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='libcreator',
    packages=find_packages(include=['libcreator']),
    version='0.1.2',
    description='A python library to create new libraries',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Luca Grosshennig',
    author_email="luca.grosshennig@gmx.de",
    license='MIT',
    install_requires=['wheel', 'twine'],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ]
)