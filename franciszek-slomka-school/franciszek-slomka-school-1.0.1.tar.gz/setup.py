import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="franciszek-slomka-school",
    version="1.0.1",
    packages=["school"],
    description="School abstraction library",
    long_description=README,
    long_description_content_type="text/markdown",
)
