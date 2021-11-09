from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        README = f.read()
    return README

setup(
    name="test-anshu-ml",
    version="1.1.1",
    description="",
    long_description=readme(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(include=["ml*"]),
    include_package_data=True,
)
