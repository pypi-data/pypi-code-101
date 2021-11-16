import os
from configparser import ConfigParser
from pathlib import Path
from setuptools import setup

_cwd = Path(os.getcwd())
_dir = Path(__file__).parent

if _cwd != _dir:
    raise SystemExit("Run this script from the directory where the file is located")

long_description = Path("README.md").read_text()

config = ConfigParser()
config.read("iterate.ini")

version = config["iteration"]["version"]
name = config["iteration"]["name"]

setup(
    name=name,
    version=version,
    author="Vadimhtml",
    author_email="i@vadimhtml.ru",
    packages=[name],
    url=f"https://gitlab.com/Vadimhtml/{name}",
    license="MIT",
    description="Cross-platform lightweight keyboard simulator",
    keywords="keyboard simulator Windows Linux macOS",  # todo simulator, emulator, tap, press?

    long_description=long_description,
    long_description_content_type="text/markdown",

    install_requires=["pyobjc-framework-Quartz; sys_platform=='darwin'"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",  # todo Supported?
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],

    entry_points={
        "console_scripts": [f"{name}={name}.cli:{name}"],
    },
)
