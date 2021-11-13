import setuptools

with open("README.md", "r", encoding="utf-8") as fh: long_description = fh.read()

setuptools.setup(
    name="pysem-converters",
    version="0.1",
    author="Adrián Toral",
    author_email="adriantoral@sertor.es",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pysem/converters",
    project_urls={
        "Website": "https://github.com/pysem/converters",
        "Issues": "https://github.com/pysem/converters/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=["pysem_converters"],
    package_dir={"": "src"},
    python_requires=">=3.8",
    keywords='python, converters, utilities, python-converters, python-converters-utilities',
)
