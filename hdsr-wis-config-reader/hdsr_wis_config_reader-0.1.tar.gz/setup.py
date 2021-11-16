from os import path
from setuptools import find_packages
from setuptools import setup


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

version = "0.1"

install_requires = [
    "geopandas",
    "lxml",
    "pathlib",
    "typing",
]

tests_require = [
    "pytest",
    "pytest-cov",
]

setup(
    name="hdsr_wis_config_reader",
    version=version,
    description="Read HDSR FEWS WIS config into python objects",
    long_description=long_description,
    url="https://github.com/hdsr-mid/hdsr_wis_config_reader",
    author="Renier Kramer",
    author_email="renier.kramer@hdsr.nl",
    license="MIT",
    packages=find_packages(include=["reader", "reader.*"]),
    python_requires=">3.6",
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"test": tests_require},
    classifiers=[
        "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="HDSR, FEWS, WIS, config, reader",
)
