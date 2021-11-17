import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="maxllg",
    version="0.0.1",
    author="Samuel Morrell",
    author_email="s.a.f.morrell@exeter.ac.uk",
    description="A package for interacting with the MaxLLG solver and its outputs. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://maxllg.com/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)