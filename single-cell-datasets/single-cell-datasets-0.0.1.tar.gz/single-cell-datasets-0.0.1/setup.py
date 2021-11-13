import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="single-cell-datasets",
    packages=["scdata"],
    version="0.0.1",
    license="gpl-3.0",
    description="Python repository to easily download single cell datasets",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Hojae Lee",
    author_email="hojae.k.lee@gmail.com",
    url="https://github.com/hojaeklee/scdata",
    keywords=["single-cell"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)