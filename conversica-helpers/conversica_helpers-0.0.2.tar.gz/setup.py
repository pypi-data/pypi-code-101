import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="conversica_helpers",
    version="0.0.2",
    author="Gonzalo Fernandez",
    author_email="gonmalofc@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gonmalo/cvsc_helpers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
     'pymongo',
     'chardet',
     'cchardet',
     'detect_delimiter',
     'requests',
     'pysftp',
     'pyyaml'
    ]
)