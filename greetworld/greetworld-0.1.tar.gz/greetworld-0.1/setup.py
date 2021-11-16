import setuptools

import greetworld

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name=greetworld.__name__,
    version=greetworld.__version__,
    author=greetworld.__author__,
    author_email="13816347+rajendrakumaryadav@users.noreply.github.com",
    description="Hello World message",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rajendrakumaryadav/greetworld",
    # packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "greetworld"},
    packages=setuptools.find_packages(where="greetworld"),
    python_requires=">=3.5",
)
