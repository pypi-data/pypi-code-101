import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apist-framework",
    version="0.0.1",
    author="Murat Issayev",
    author_email="murat.isaev.214@gmail.com",
    description="API testing framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Muratoi/apist",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],)