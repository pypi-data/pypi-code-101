from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Does language identification'
LONG_DESCRIPTION = 'A package that allows to identify language of a given text.'

# Setting up
setup(
    name="whichlang",
    version=VERSION,
    author="Ashish ",
    author_email="<ashish.xtraspeed@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url = 'https://github.com/xtraspeed/whichlang',
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'language identification'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)