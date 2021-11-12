import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="realtime-earthquake-indonesia",
    version="0.0.3",
    author="Panji Perdana",
    author_email="panji9502@gmail.com",
    description="This package inform the latest earthquake in Indonesia from BMKG | Meteorological, Climatological, and Geophysical Agency.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pperdana/latest-earthquake-report-indonesia",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)