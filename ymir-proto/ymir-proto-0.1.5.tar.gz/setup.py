from setuptools import setup, find_packages

name = "ymir-proto"
version = "0.1.5"
description = "YMIR Protobuf Specs"
install_instructions = """\
make sure you've got grpcio and protobuf installed
```
pip install grpcio
```
"""


setup(
    name=name,
    version=version,
    description=description,
    long_description=install_instructions,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3"],
    include_package_data=True,
)
