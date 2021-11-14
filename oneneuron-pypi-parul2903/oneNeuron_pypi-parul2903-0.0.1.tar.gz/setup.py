import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

USER_NAME = "parul2903"
PROJECT_NAME = "oneNeuron_pypi"

setuptools.setup(
    name = f"{PROJECT_NAME}-{USER_NAME}",
    version = "0.0.1",
    author = USER_NAME,
    author_email = "parul3kin@gmail.com",
    description = "It is an implementation of Perceptron",
    long_description = long_description, # long description shows readme.md files 
    long_description_content_type = "text/markdown",
    url = "https://github.com/pypa/sampleproject",
    project_urls = {
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", # works on any OS, windows, Linux or Mac
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.9",
    install_requires = [
        "numpy",
        "tqdm"
    ]
)