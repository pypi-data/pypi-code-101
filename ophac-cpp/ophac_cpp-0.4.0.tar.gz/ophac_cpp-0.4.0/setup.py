# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Copyright 2020 Daniel Bakkelund
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#
# Content copied from
# https://github.com/pybind/python_example/blob/master/setup.py
# and modified to my liking by adding and removing stuff based on
# https://pybind11.readthedocs.io/en/stable/compiling.html
#
from setuptools import setup

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir
from glob import glob

import sys

__version__ = "0.4.0"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

ext_modules = [
    Pybind11Extension("ophac_cpp",
                      sources=sorted(glob("src/*.cpp")),
                      include_dirs=['./src/'],
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        ),
]

_desc_="C++ implementation of parts of ophac to improve performance."

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ophac_cpp",
    version=__version__,
    author="Daniel Bakkelund",
    author_email="daniel_bakkelund@hotmail.com",
    url="https://bitbucket.org/Bakkelund/ophac_cpp",
    description=_desc_,
    long_description=long_description,
    ext_modules=ext_modules,
    # extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0',
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    install_requires=[
        'pybind11'
    ],
)
