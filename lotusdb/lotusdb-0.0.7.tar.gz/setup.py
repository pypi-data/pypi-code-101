from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

VERSION = '0.0.7'
DESCRIPTION = 'Python database'

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='lotusdb',
    version=VERSION,
    author='d3tu',
    author_email='jpafly@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['database'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ]
)