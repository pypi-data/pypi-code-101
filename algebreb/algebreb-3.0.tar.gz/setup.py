from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '3.0'
DESCRIPTION = 'Biblioteca para generar expresiones y ejercicios de algebra'
LONG_DESCRIPTION = 'Conjunto de funciones y clases para la creacion de ejercicios algebraicos'

# Setting up
setup(
    name="algebreb",
    version=VERSION,
    author="ivan0123456789",
    author_email="<elite-a64@outlook.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['sympy'],
    keywords=['python', 'algebra'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)