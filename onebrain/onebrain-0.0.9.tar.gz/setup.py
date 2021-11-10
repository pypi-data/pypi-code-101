# -- coding: utf-8 --

from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="onebrain",
    version="0.0.9",
    author="onebrain_team",
    author_email="761043617@qq.com",
    description="onebrain sdk in python version",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/OF-OneBrain/onebrain-sdk",
    packages=find_packages(),
    install_requires=[
        ## 'setuptools==38.2.4'
    ],
    keywords=['onebrain'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    zip_safe=False
)