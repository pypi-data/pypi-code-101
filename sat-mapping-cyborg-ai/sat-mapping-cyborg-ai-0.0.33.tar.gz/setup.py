import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


DEPENDENCIES = [
    "Glymur",
    "numpy"
]

setuptools.setup(
    name="sat-mapping-cyborg-ai",
    version="0.0.33",
    author="Lukas Ikle",
    author_email="lukas.ikle@itweet.ch",
    description="A package to fetch sentinel 2 Satellite data from Google.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iklelukas/sat_mapping",
    project_urls={
        "Bug Tracker": "https://github.com/iklelukas/sat_mapping/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=DEPENDENCIES
)
