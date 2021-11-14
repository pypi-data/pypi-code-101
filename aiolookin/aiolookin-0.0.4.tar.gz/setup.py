from setuptools import find_packages, setup

from aiolookin import __version__ as version

setup(
    name="aiolookin",
    version=version,
    url="https://github.com/ANMalko/aiolookin",
    author="Anton Malko",
    author_email="antonmalko@mail.ru",
    description="Client for interaction of the LOOKin device with the Home Assistant",
    packages=find_packages(exclude=['tests*']),
    install_requires=["aiohttp>=3.7.4"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
