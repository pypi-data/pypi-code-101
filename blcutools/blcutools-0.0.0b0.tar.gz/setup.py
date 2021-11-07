import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blcutools",
    version="0.0.0-beta",
    author="blcuresearch",
    author_email="blcures@gmail.com",
    description="blcutools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blcu-research/blcutools",
    project_urls={
        "Bug Tracker": "https://github.com/blcu-research/blcutools/issues",
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=['docs', 'tests*']),
    python_requires=">=3.6",
)
