from setuptools import setup

with open("README.md","r") as fh:
    long_description=fh.read()

setup(
name='PyMySequal',
version='0.0.3',
description='Simple SQL API',
long_description=long_description,
long_description_content_type="text/markdown",
py_modules=["PyMySequal"],
pacakage_dir={'':'src'},
install_requires = [
        'pyodbc',
        'pandas'
    ]
)