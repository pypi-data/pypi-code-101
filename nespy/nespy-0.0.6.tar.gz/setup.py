import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

project_urls = {
    "Source Code": "https://github.com/nebulastream/nebulastream-python-client"
}

setuptools.setup(
    name="nespy",
    version="0.0.6",
    description="Python Client for NebulaStream",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.nebula.stream/",
    project_urls=project_urls,
    packages=setuptools.find_packages(),
    keywords=['NebulaStream', 'NES', 'nespy', 'nebulastream-python-client', 'data science', 'IoT', 'data streams',
              'data stream management'],
    license='Apache License 2.0',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
    install_requires=['requests>=2.25', 'pyzmq>=22', 'pandas>=1', 'ipython>=6', 'google>=3', 'protobuf>=3']
)
