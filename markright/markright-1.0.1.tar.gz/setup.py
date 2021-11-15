import os
from configparser import ConfigParser
from pathlib import Path
from setuptools import setup

_cwd = Path(os.getcwd())
_dir = Path(__file__).parent

if _cwd != _dir:
    raise SystemExit("Run this script from the directory where the file is located")

long_description = Path("README.md").read_text()

config = ConfigParser()
config.read("iterate.ini")

setup(
    name=config["iteration"]["name"],
    version=config["iteration"]["version"],
    author='Vadimhtml',
    author_email='i@vadimhtml.ru',
    packages=['markright'],
    url='https://gitlab.com/Vadimhtml/markright',
    license='MIT',
    description='Templateless markdown template engine',
    keywords='markdown template',

    long_description=long_description,
    long_description_content_type='text/markdown',

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],

    entry_points={
        'console_scripts': ['markright=markright.cli:markright'],
    },
)
