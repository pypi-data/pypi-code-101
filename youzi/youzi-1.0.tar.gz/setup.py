import setuptools
from pathlib import Path

path = Path('readme.md')

setuptools.setup(
    name='youzi',
    version=1.0,
    long_description=path.read_text(),
    packages=setuptools.find_packages(exclude=['test', 'data'])
)
