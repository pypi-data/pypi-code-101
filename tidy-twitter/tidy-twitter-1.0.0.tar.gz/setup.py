import os
import re
from setuptools import setup, find_packages


def read_file(*parts):
    """
    Reads file from relative path to current directory by joining path
    parts from input arguments
    :param parts:
    :return:
    """
    _here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(_here, *parts), "r") as fp:
        return fp.readline()


def find_version(*file_paths):
    """
    Reads application version info
    :param file_paths:
    :return:
    """
    version_file = read_file(*file_paths)
    version_match = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def read_requirements():
    """
    Parses requirements from requirements.txt.
    """
    _path = os.path.join(".", "requirements.txt")
    with open(_path, "r") as f:
        requirements = [line.rstrip() for line in f]
    return requirements


def read_long_description():
    _path = "README.md"
    with open(_path, "r") as f:
        long_description = f.read()
    return long_description


setup(
    name="tidy-twitter",
    version=find_version(os.getcwd(), "api/version.py"),
    description="This program cleans up old Twitter tweets.",
    long_description_content_type="text/markdown",
    long_description=read_long_description(),
    url="https://bitbucket.org/svenvarkel/tidy-twitter",
    author="Sven Varkel",
    author_email="sven.varkel@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=read_requirements(),
    dependency_links=[],
    entry_points='''
        [console_scripts]
        tidy-twitter=api.cli:cli
    ''',
    include_package_data=True,
    zip_safe=False
)
