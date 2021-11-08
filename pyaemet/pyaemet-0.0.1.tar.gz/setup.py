import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyaemet",
    version="0.0.1",
    author="Jaime Diez",
    author_email="jaime.diez.gp@gmail.com",
    description="Python package to interact with the AEMET API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jaimedgp/pyAEMET",
    project_urls={
        "Bug Tracker": "https://github.com/Jaimedgp/pyAEMET/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        "setuptools>=42",
        "wheel",
        "numpy",
        "pandas",
        "requests",
        "geocoder",
        "python-dateutil",
    ],
    packages=setuptools.find_packages(include=['pyaemet']),
    python_requires=">=3.6",
    zip_safe=False,
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='pyaemet.tests',
)
