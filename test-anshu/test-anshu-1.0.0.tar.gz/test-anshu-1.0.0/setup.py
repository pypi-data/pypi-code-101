from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        README = f.read()
    return README

setup(
    name="test-anshu",
    version="1.0.0",
    description="Python.",
    long_description=readme(),
    long_description_content_type="text/markdown",
)
