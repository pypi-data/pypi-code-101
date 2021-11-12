from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'Auto differentiation forward mode'
LONG_DESCRIPTION = 'A package that allows automatic differentiation with forward mode'

# Setting up
setup(
    name="autodiff_for_life",
    version=VERSION,
    author="Lovelace Lovers (Alfred Wahlforss, Erin Tomlinson, Tyler Barnett, Xinyi Li)",
    author_email="alfred@wahlforss.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['python', 'autodiff', 'forward mode', 'automatic differentiation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)