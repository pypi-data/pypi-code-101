import os
import sys

from setuptools import setup, find_packages


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        return f.read()

print("setup.py prefix:", sys.prefix)

setup(
    name="cpp-include-lint",
    version="0.1",

    # Requires python3.7
    python_requires=">=3.7",

    # Automatically import packages
    packages=find_packages(),

    # Include the files specified in MANIFEST.in in the release archive
    include_package_data=True,

    # Scripts to install to the user executable path.
    entry_points={
        "console_scripts": [
            "cpp-include-lint = cpp_include_lint.__main__:main",
        ]
    },


    # Metadata
    author="Stefano Dottore",
    author_email="docheinstein@gmail.com",
    description="Sort #include directives of C/C++ files",
    long_description=read('README.MD'),
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="c cpp include lint sort",
    url="https://github.com/Docheinstein/cpp-include-lint"
)