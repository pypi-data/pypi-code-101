import codecs
import os
import sys
try:
    from setuptools import setup
except:
    from distutils.core import setup

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

NAME = "ltools"
VERSION = '0.0.1'
PACKAGES = ['ltools']
KEYWORDS = 'python,spiders,tools'
AUTHOR = 'lj'
AUTHOR_EMAIL = '412239635@qq.com'
URL = 'https://github.com/Xlj997/ltools.git'
LICENSE = 'MIT'
REQUIRES_PYTHON = '>=3.7.0'
REQUIRED = []
setup(name=NAME,
      version=VERSION,
      packages=PACKAGES,
      keywords =KEYWORDS,
      author_email=AUTHOR_EMAIL,
      author=AUTHOR,
      url=URL,
      include_dirs=True,
      zip_safe=True,
      python_requires=REQUIRES_PYTHON,
      install_requires=REQUIRED,
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
      ],
      entry_points={
          'console_scripts': [
              'tools = ltools.__main__:main'
          ]
      },
      )