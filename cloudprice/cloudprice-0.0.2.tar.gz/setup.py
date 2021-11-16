#!/usr/bin/env python
import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")


def get_version():
    init = open(os.path.join(ROOT, "cloudprice", "__init__.py")).read()
    return VERSION_RE.search(init).group(1)


setup(
    name="cloudprice",
    version=get_version(),
    description="A SDK for cloud compute pricing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Guanjie Shen",
    url="https://github.com/guanjieshen/cloud-compute-pricing",
    packages=find_packages(exclude=["tests*"]),
    install_requires=["requests>=2.5.0,<3.0.0"],
    license="MIT License",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
)
