import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sra_py",
    version="1.2",
    author="Atidipt123",
    author_email = "atidiptmishra@gmail.com",
    description="Python wrapper for some-random-api.ml",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Atidipt123/sra_py",
    download_url = "https://github.com/Atidipt123/sra_py/archive/refs/tags/v0.1.3.tar.gz",
    project_urls={
        "Bug Tracker": "https://github.com/Atidipt123/sra_py/issues",
    },
    package_dir={"": "sra_py"},
    packages=setuptools.find_packages(where='sra_py'),
    install_requires=['requests' , 'aiohttp']
)