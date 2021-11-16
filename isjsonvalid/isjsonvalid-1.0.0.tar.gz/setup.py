import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="isjsonvalid",
    version="1.0.0",
    description="Validate anything in any JSON",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ivancmonaco/isjsonvalid.git",
    author="Real Python",
    author_email="ivancmonaco@gmail.com",
    license="MIT",
    classifiers=[],
    packages=["isjsonvalid"],
    include_package_data=True,
    install_requires=[],
    entry_points={},
)
