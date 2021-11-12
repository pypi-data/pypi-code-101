import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_requirements(filename):
    return open('requirements/' + filename).read().splitlines()


classes = """
    Development Status :: 4 - Beta
    Intended Audience :: Developers
    License :: OSI Approved :: BSD License
    Topic :: System :: Distributed Computing
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9
    Programming Language :: Python :: Implementation :: CPython
    Programming Language :: Python :: Implementation :: PyPy
    Operating System :: OS Independent
"""
classifiers = [s.strip() for s in classes.split('\n') if s]


setuptools.setup(
    name="sampletext",                     # This is the name of the package
    version="0.1.1",                        # The initial release version
    author="Aveek Das",                     # Full name of the author
    description="Quicksample Test Package for SQLShack Demo",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    install_requires=get_requirements("default.txt"),
    classifiers=classifiers,                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["sampletext", "textfunc", "location"],             # Name of the python package
    package_dir={'': 'sampletext/src'},     # Directory of the source code of the package
)