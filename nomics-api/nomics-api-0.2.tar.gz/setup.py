#! usr/bin/python3

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="nomics-api", 
    version="0.2",
    author="Temkin Mengistu",
    author_email="chapimenge3@gmail.com",
    description="Python Wrapper for Nomics Cryptocurrency & Bitcoin API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chapimenge3/nomics-python-api",
    packages=find_packages(),
    keywords="api, nomics, nomics-api, nomics api",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6, <4',
    install_requires=["requests",],
    
    project_urls={
        "Source" : "https://github.com/chapimenge3/nomics-python-api", 
        "Say Thanks" : "https://t.me/chapimenge"
    }
)