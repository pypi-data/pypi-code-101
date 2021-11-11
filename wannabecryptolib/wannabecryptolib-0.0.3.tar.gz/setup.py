from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Encrypting strings.'
LONG_DESCRIPTION = 'Not safe at all. Just for educational purposes'

# Setting up
setup(
    name="wannabecryptolib",
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
