import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('C:\\Users\\user\\Baroniq\\requirements.txt','r') as fr:
    requires = fr.read().split('\n')

setuptools.setup(
    name="Baroniq",
    version="0.0.2",
    author="Falh Gomer",
    author_email="aowrass45467@gmail.com",
    description="my God",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/baronblack7/Baroniq",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=requires,
)