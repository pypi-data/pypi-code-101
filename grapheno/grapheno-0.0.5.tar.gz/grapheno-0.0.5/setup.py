import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grapheno",
    version="0.0.5",
    author="Erik Burlingame",
    author_email="erik.burlingame@gmail.com",
    description="GPU-accelerated PhenoGraph",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/eburling/grapheno",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)