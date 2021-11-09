from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'Simple Riot Auth Session Creator'
LONG_DESCRIPTION = 'A lib that creats a logged-in session which can be used for games using Riot Services '

# Setting up
setup(
    name="RiotAuth",
    version=VERSION,
    author="yomom",
    author_email="yomom@myhouse.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['valorant', 'league', 'of', 'legends', 'api', 'authorization'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Religion",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
