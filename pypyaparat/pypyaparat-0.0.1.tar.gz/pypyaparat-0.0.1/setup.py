import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypyaparat",
    version="0.0.1",
    author="mamad",
    author_email="biroghlan95@gmail.com",
    description="download aparat videos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amirbigg/pyaparat",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    install_requires = [
        'requests', 'beautifulsoup4'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)