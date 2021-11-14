from setuptools import setup
import os

VERSION = "0.1.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-hello-world",
    description="The hello world of Datasette plugins",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-hello-world",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-hello-world/issues",
        "CI": "https://github.com/simonw/datasette-hello-world/actions",
        "Changelog": "https://github.com/simonw/datasette-hello-world/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_hello_world"],
    entry_points={"datasette": ["hello_world = datasette_hello_world"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    tests_require=["datasette-hello-world[test]"],
    python_requires=">=3.6",
)
