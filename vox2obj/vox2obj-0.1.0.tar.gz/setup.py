import pathlib

import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setuptools.setup(
    name="vox2obj",
    version="0.1.0",
    author="Claytone",
    author_email="clayton.wells.321@gmail.com",
    description="Converts voxel models to obj files.",
    license="MIT",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/Claytone/vox2obj",
    project_urls={
        "Bug Tracker": "https://gitlab.com/Claytone/vox2obj/-/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=("test",)),
    python_requires=">=3.6",
)