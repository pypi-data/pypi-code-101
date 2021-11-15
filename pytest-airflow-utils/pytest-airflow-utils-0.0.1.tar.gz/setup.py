from setuptools import setup, find_packages

import pytest_airflow_utils

setup(
    name="pytest-airflow-utils",
    version=pytest_airflow_utils.__version__,
    packages=find_packages(exclude=["tests"]),
    entry_points={"pytest11": ["pytest-airflow-utils = pytest_airflow_utils.plugin"]},
    classifiers=[
        "Framework :: Pytest",
        "Natural Language :: English",
    ],
    author="Ali Cirik",
    author_email="aliavni@gmail.com",
)
