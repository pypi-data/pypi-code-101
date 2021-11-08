#!/usr/bin/env python

import os
import subprocess

from setuptools import setup


def write_version_file(version):
    """Writes a file with version information to be used at run time

    Parameters
    ----------
    version: str
        A string containing the current version information

    Returns
    -------
    version_file: str
        A path to the version file

    """
    try:
        git_log = subprocess.check_output(
            ["git", "log", "-1", "--pretty=%h %ai"]
        ).decode("utf-8")
        git_diff = (
            subprocess.check_output(["git", "diff", "."])
            + subprocess.check_output(["git", "diff", "--cached", "."])
        ).decode("utf-8")
        if git_diff == "":
            git_status = "(CLEAN) " + git_log
        else:
            git_status = "(UNCLEAN) " + git_log
    except Exception as e:
        print(f"Unable to obtain git version information, exception: {e}")
        git_status = ""

    source_directory = "gwpopulation_pipe"
    version_file = ".version"
    if not os.path.isfile(os.path.join(source_directory, version_file)):
        with open(os.path.join(source_directory, version_file), "w+") as f:
            f.write(f"{version}: {git_status}")

    return version_file


def get_long_description():
    """Finds the README and reads in the description"""
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, "README.md")) as f:
        long_description = f.read()
    return long_description


VERSION = "0.3.0"
version_file = write_version_file(VERSION)
long_description = get_long_description()

setup(
    name="gwpopulation_pipe",
    description="A pipeline population inference",
    long_description=long_description,
    url="https://git.ligo.org/RatesAndPopulations/gwpopulation_pipe",
    author="Colm Talbot",
    author_email="colm.talbot@ligo.org",
    license="MIT",
    version=VERSION,
    packages=["gwpopulation_pipe"],
    include_package_data=True,
    package_data={"gwpopulation_pipe": [version_file]},
    python_requires=">=3.6",
    install_requires=[
        "extension-helpers",
        "numpy",
        "scipy",
        "astropy",
        "dynesty>1.0.0",
        "bilby>=1.0.4",
        "bilby_pipe",
        "gwpopulation>=0.6.2",
        "h5py",
        "deepdish",
        "matplotlib",
        "tqdm",
    ],
    entry_points={
        "console_scripts": [
            "gwpopulation_pipe=gwpopulation_pipe.main:main",
            "gwpopulation_pipe_analysis=gwpopulation_pipe.data_analysis:main",
            "gwpopulation_pipe_collection=gwpopulation_pipe.data_collection:main",
            "gwpopulation_pipe_plot=gwpopulation_pipe.post_plots:main",
            "gwpopulation_pipe_pp_test=gwpopulation_pipe.review:setup_pp_test",
            "gwpopulation_pipe_simulate_posteriors=gwpopulation_pipe.data_simulation:main",
            "gwpopulation_pipe_to_common_format=gwpopulation_pipe.common_format:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
