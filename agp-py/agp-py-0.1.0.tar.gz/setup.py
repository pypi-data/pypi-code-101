from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'Gene parser for Axie Infinity'

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

# Setting up
setup(
    name="agp-py",
    version=VERSION,
    author="Abel Mundarain",
    author_email="stiggu@protonmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Stiggu/agp-py",
    project_urls={
        "Bug Tracker": "https://github.com/Stiggu/agp-py/issues",
    },
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'axie infinity'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
