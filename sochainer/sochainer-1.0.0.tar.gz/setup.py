"""Setup script for sochainer"""

# Standard library imports
import pathlib

# Third party imports
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="sochainer",
    version="1.0.0",
    description="Basic SoChain feed reader that can download the latest cryptocurrency data from sochain.com",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mtclinton/sochainer",
    author="Max Clinton",
    author_email="max@mtclinton.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["sochainer"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={"console_scripts": ["sochainer=sochainer.__main__:main"]},
)