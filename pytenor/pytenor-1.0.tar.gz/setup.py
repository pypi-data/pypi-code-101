from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pytenor",
    packages=["pytenor"],
    version="1.0",
    license="MIT",
    description="A simple API wrapper for tenor's gif api that is built with asyncio.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Philippe Mathew",
    author_email="philmattdev@gmail.com",
    url="https://github.com/bossauh/pytenor",
    download_url="https://github.com/bossauh/pytenor/archive/refs/tags/v1_0.tar.gz",
    keywords=["api", "tools", "utilities"],
    install_requires=[
        "aiohttp"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
