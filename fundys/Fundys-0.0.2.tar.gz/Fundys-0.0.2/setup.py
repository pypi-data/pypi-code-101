import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Fundys",
    version="0.0.2",
    author="Chase Resendiz",
    author_email="chaseresendiz@gmail.com",
    description="stock & portfolio analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caresendiz/fundys.git",
    project_urls = {'issues': "https://github.com/caresendiz/fundys.git"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "fundys"},
    packages=setuptools.find_packages('fundys'),
    python_requires=">=3.6",
)