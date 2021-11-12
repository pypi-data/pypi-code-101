from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))
datadir = os.path.join('whichlang','language-models')
datafiles = [(d, [os.path.join(d,f) for f in files])
    for d, folders, files in os.walk(datadir)]
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'Does language identification for Indian languages'
LONG_DESCRIPTION = 'A package that allows to identify language of a given text for Indian languages.'

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
    include_package_data=True,
    data_files = datafiles,
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