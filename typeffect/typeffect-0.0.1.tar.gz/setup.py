from setuptools import setup, find_packages
import os


VERSION = '0.0.1'
DESCRIPTION = ''


# Setting up
setup(
    name="typeffect",
    version=VERSION,
    author="Divinemonk",
    author_email="<v1b7rc8eb@relay.firefox.com>",
    description=DESCRIPTION,
    packages=['typeffect'],
    py_modules = ['typing', 'style','justhacking'],
    install_requires=['rich'],
    keywords=['python', 'typeffect', 'divinemonk', 'typewriter', 'cli', 'typing', 'console', 'typewriter effect'],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "typeffect=typeffect.__main__:starthack",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)