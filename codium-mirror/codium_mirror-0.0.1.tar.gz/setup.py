import re

import setuptools

from codium_mirror import __appauthor__, __version__

long_description = open("README.md", "r", encoding="utf-8").read()

setuptools.setup(
    name="codium_mirror",
    version=__version__,
    author=__appauthor__,
    author_email="",
    description="codium_mirror",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/larryw3i/codium_mirror",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'codium_mirror=codium_mirror:run',
        ]
    },
    python_requires='>=3.6',
    install_requires=[],
    include_package_data=True,
)
