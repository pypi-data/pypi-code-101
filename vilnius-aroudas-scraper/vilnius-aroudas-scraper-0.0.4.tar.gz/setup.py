import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vilnius-aroudas-scraper",
    version="0.0.4",
    author="Blessing E-Philips",
    author_email="blessingphilips@ymail.com",
    description="Aroudas.lt website scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/u-aaa/Vilnius-Apartment-Predictions",
    project_urls={
        "Bug Tracker": "https://github.com/u-aaa/Vilnius-Apartment-Predictions/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["aroudas_scraper"],
    package_dir={"": "scraper"},
    packages=setuptools.find_packages(where="scraper"),
    python_requires=">=3.7",
)