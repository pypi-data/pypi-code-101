from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'A package with a wide range of feutures'
LONG_DESCRIPTION = 'A package with a wide range of feutures'

# Setting up
setup(
    name="zono",
    version=VERSION,
    author="KisAwesome",
    author_email="cool676rock@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['cryptography', 'colorama', 'mutagen', 'python_vlc'],
    keywords=['encryption', 'zono', 'decryption',
              'cli', 'mac', 'audio', 'vlc'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
