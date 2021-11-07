from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.14'
DESCRIPTION = 'Like yfinance but for Moroccan stocks'
LONG_DESCRIPTION = 'A package that helps scrape stocks data from la bourse de Casa'

# Setting up
setup(
    name="Casabourselib",
    version=VERSION,
    author="Yassine Rhzif & Ahmed Ouaboune",
    author_email="Rhzif@hotmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests', 'pandas', 'bs4'],
    keywords=['python', 'Bourse de casa', 'stocks', 'actions', 'actions maroc'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)