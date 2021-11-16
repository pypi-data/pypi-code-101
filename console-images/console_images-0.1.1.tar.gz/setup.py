import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["colorama", "pillow", "dataclasses"]

setuptools.setup(
    name="console_images",
    version="0.1.1",
    author="LedinecMing",
    url="https://github.com/LedinecMing/console_images/",
    author_email="loliamalexxaxa@gmail.com",
    description="Colored console images and gifs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
