from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="talk-in-code",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Itanú Romero",                     # Full name of the author
    description="Transform natural language strings on Python runnable code",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=find_packages(where="talk_in_code", exclude=("tests",)),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.8',                # Minimum version requirement of the package
    py_modules=["talk_in_code"],             # Name of the python package
    package_dir={'':'talk_in_code'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)