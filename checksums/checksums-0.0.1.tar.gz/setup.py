
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="checksums",
    version="0.0.1",
    author="meowmeowcat",
    author_email="",
    description="A command line tool that show/verify checksums for a file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meowmeowmeowcat/checksums",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["checksums"],
    entry_points="""
        [console_scripts]
        checksums=checksums.cli:cli
        """,
    python_requires=">=3.6",
    install_requires=["click"],

)