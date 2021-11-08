from setuptools import setup, find_namespace_packages


with open("README.md", "r") as file:
    readme = file.read()

setup(
    name="numba_namespace_extension",
    version="0.1.0",
    description="Easily create compiled namespace Numba extensions.",
    long_description_content_type="text/markdown",
    long_description=readme,
    packages=find_namespace_packages(where="src"),
    package_dir={
        "": "src"
    },
    install_requires=[
        "numba>=0.54.1, <1.0.0",
    ],
)
