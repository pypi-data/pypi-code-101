import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygst",
    version="0.0.2",
    author="Bun Uthaitirat",
    description="Python global stock time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/taobun/pygst",
    python_requires=">=3.6",
    py_modules=["pygst"],
    install_requires=["pytz"],  # Install other dependencies if any
)
