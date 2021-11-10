from setuptools import setup, find_packages

VERSION = '0.0.4' 
DESCRIPTION = 'Environments: minimap, navigation, firemen'
LONG_DESCRIPTION = open("README.md").read()


# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="vitenv", 
        version=VERSION,
        author="Nhat Phan",
        author_email="<nhatsp@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['opencv-python','numpy'], 
        
        keywords=['Minimap', 'cooperative navigation', 'firemen'],
        classifiers= [
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)