from setuptools import setup, find_packages

VERSION = '0.0.9' 
DESCRIPTION = 'Matplotlib wrapper'
LONG_DESCRIPTION = 'Simple wrapper for the matplotlib templates I frequently use.'

# Setting up
setup(
        name="stuartplot", 
        version=VERSION,
        author="Stuart Watt",
        url="https://github.com/stuart-watt/stuart_plot",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        python_requires=">=3.6",
        install_requires=[
            "matplotlib",
        ],
)