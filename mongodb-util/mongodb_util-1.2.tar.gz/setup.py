#!/usr/bin/python3

import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='mongodb_util',
     version='1.2',
     py_modules=['mongodb_util', 'mongodb_monitoring'],
     package_dir={'': 'src'},
     author="Aman Mishra",
     author_email="aman@switchon.io",
     description="This module provides an easy mechanism to connect to MongoDb" +\
                 "along with various monitoring options that help debug issues at database level",
     long_description=long_description,
     long_description_content_type="text/markdown",
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: POSIX :: Linux"
     ],
     install_requires=[
        'pymongo>=3.1',
        'packaging>=20.4'],
     extras_require = {
         "dev": [
             "mock==4.0.2",
         ]
     },
     include_package_data=True,
     zip_safe=False
)

