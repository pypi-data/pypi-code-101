# This file is placed in the Public Domain.

import os

from setuptools import setup


def read():
    return open("README.rst", "r").read()


def uploadlist(dir):
    upl = []

    for file in os.listdir(dir):
        if not file or file.startswith('.'):
            continue
        d = dir + os.sep + file
        if os.path.isdir(d):   
            upl.extend(uploadlist(d))
        else:
            if file.endswith(".pyc") or file.startswith("__pycache"):
                continue
            upl.append(d)
    return upl



setup(
    name="botlib",
    version="142",
    url="https://github.com/bthate/botlib",
    author="Bart Thate",
    author_email="bthate67@gmail.com",
    description="python3 bot library",
    long_description=read(),
    license="Public Domain",
    packages=["bot"],
    zip_safe=True,
    include_package_data=True,
    data_files=[
                ('share/doc/botd', uploadlist("docs")),
                ('share/botd', uploadlist("files")),
                ("share/botd/", ["files/botd.service",],)
    ],
    scripts=["bin/bot", "bin/botc", "bin/botctl", "bin/botd"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
