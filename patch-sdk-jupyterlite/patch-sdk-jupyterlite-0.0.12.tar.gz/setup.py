import re

from setuptools import find_packages, setup
version = "0.0.12"
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="patch-sdk-jupyterlite",
    version=version,
    description="A patch for the Cognite SDK so it works in Jupyterlite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Anders Hafreager",
    author_email="anders.hafreager@cognite.com",
    install_requires=[],
    python_requires=">=3.5",
    packages=["cognite.jupyterlitepatch"],
    include_package_data=True,
)
