from setuptools import setup, find_packages
import os

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='robotframework-AllureClient',
    version='0.0.8',
    description='robot framework client to control allure reporting service using rest api',
    author='mahmoud eltohamy',
    author_email='mahmoud.mohammed.elhady@gmail.com',
    license='MIT',
    py_modules=['AllureClient'],
    url='https://opensourcetestops.gitlab.io/robotframeworkallureclient/',
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[ "Click", "requests",]
)