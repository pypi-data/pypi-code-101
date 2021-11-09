from setuptools import setup

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir

import sys

# Reference: https://github.com/pybind/python_example
__version__ = "0.0.1"

ext_modules = [
    Pybind11Extension("finthermos",
        ["src/pymain.cc"],
        # Passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        ),
]

setup(
    name="finthermos",
    version=__version__,
    author="Tyler Brown",
    url="https://github.com/tbonza/finthermos",
    description="Infrastructure for Finance",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    project_urls={
        "Source Code": "https://github.com/tbonza/thermos",
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ],
)

