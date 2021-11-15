#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pathlib

from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="zipkin-agent",
    version="0.1.0",
    description="Python Agent for zipkin-agent",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/apache/skywalking-python/",
    author="Apache",
    author_email="dev@skywalking.apache.org",
    license="Apache 2.0",
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,
    install_requires=[
        "packaging",
        "wrapt",
    ],
    extras_require={
        "test": [
            "testcontainers",
            "pyyaml",
            "pytest",
        ],
        "http": [
            "requests>=2.26.0",
            "dapr>=1.4.0",
            "dapr-ext-grpc>=1.4.0",
            "Flask>=2.0.2"
        ],
    },
    classifiers=[
        "Framework :: Flake8",

        "License :: OSI Approved :: Apache Software License",

        "Operating System :: OS Independent",

        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",

        "Topic :: Software Development",
    ]
)
