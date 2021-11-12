import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cryptohelp",
    version="0.0.4",
    author="Angmar",
    author_email="Angmar2722@github.com",
    description="A package which contains helper functions for solving crypto challenges in CTFs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Angmar2722/CTF-Helper-Functions-For-Crypto",
    project_urls={
        "Bug Tracker": "https://github.com/Angmar2722/CTF-Helper-Functions-For-Crypto/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)