from setuptools import setup, find_packages

setup(
    name='isscratchup',
    version='1.0.0',
    url='https://github.com/scoldercreations/isscratchup.git',
    author='ScolderCreations',
    author_email='',
    description='Checks if Scratch is up',
    packages=find_packages(),    
    install_requires=['requests-html >= 0.0']
)