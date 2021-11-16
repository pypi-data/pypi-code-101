import setuptools


version = "0.0.3"

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="data-drift-detector-mightyhive",
    version=version,
    author="Yang Dai",
    author_email="yang.dai@mediamonks.com",
    description="A data drift detection and schema validation package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/superyang713/data-drift-detector/blob/main/README.md",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Build Tools',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
    ],
    python_requires="==3.8",
    install_requires=[
        "tensorflow-data-validation == 1.3.0",
        "google-auth == 1.35.0",
        "google-cloud-storage == 1.42.3",
        "google-cloud-bigquery == 2.28.1",
        "google-cloud-bigquery-storage == 2.9.1",
    ],
)
