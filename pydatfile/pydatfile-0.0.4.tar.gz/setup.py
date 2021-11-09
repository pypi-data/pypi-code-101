from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='pydatfile',
    version='0.0.4',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='J0J0HA',
    package_dir={'': 'pydatfile'},
    packages=find_packages(where='pydatfile'),
    python_requires='>=3.7, <4'
)
