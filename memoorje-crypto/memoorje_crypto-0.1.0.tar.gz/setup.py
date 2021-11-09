"""
# memoorje_crypto

This library provides encryption container formats compatible with the
[WebCryptography API](https://w3c.github.io/webcrypto/).

NOTE: The code in this library has not yet been reviewed. Use it with caution.
"""

import os

from setuptools import find_namespace_packages, setup

__dir__ = os.path.abspath(os.path.dirname(__file__))
__version__ = "0.1.0"

setup(
    name="memoorje_crypto",
    version=__version__,
    description="WebCrypto-compatible encryption container formats.",
    long_description=__doc__,
    long_description_content_type="text/markdown",
    url="https://memoorje.org",
    author="memoorje developers",
    author_email="tach@memoorje.org",
    license="MIT",
    packages=find_namespace_packages(include=("memoorje_crypto", "memoorje_crypto.*")),
    install_requires=[
        "pycryptodome~=3.6",
    ],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Security :: Cryptography",
    ],
)
