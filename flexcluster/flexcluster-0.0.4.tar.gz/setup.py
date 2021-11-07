import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flexcluster",
    version="0.0.4",
    author="Humberto Cardoso Marchezi",
    author_email="hcmarchezi@gmail.com",
    description="flexible clustering algorithm that allows user-define dissimilarity an centroid calculation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hcmarchezi/flexcluster",
    project_urls={
        "Bug Tracker": "https://github.com/hcmarchezi/flexcluster/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["flexcluster",  "flexcluster.tests", "flexcluster.impl", "flexcluster.impl.tests"],
    python_requires=">=3.6",
)