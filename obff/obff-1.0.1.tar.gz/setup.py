from setuptools import setup, find_packages
from obff.__vars__ import __version__, __author__, __email__

with open('README.md', 'r') as rmdf:
    long_description = rmdf.read()

setup(
    name='obff',
    version=__version__,
    description='Parser "for Open Book File Format"',
    url="https://github.com/obff-development/obff-python/",
    author=__author__,
    author_email=__email__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.5',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Adaptive Technologies"
    ],
    install_requires=[],
    packages=["obff"],
    project_urls={
        "Issue tracker": "https://github.com/obff-development/obff-python/issues"
    },
    entry_points = {
        "console_scripts": [
            "obffpy = obff.cli.__main__:start"
        ]
    }
)
