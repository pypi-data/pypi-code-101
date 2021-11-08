import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="gaomi",
    version="0.0.1",
    author="Gao Hongjian",
    author_email="hbtsqaghj@buaa.edu.cn",
    description="A small medical image processing package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vegetarianfish/gaomi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)