import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="giga-steam",
    version="0.0.3",
    author="TSecret",
    author_email="timichfull@gmail.com",
    description="A giga Steam API package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests", "pybase64", "bs4", "rsa"],
    url="https://github.com/TSecretT/steam",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)