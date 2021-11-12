from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'systemID Package'
LONG_DESCRIPTION = 'Package for time domain system identification. Supports linear time-invariant (LTI) and linear time-varying (LTV) dynamics, bilinear dynamics and nonlinear dynamics.'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="systemID",
    version=VERSION,
    author="Damien Gueho",
    author_email="<systemidtechnologies@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['python', 'system identification'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)