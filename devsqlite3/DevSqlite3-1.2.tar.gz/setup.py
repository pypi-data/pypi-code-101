import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DevSqlite3", # Replace with your own username
    version="1.2",
    author="Omar Othman",
    author_email="ceunix@gmail.com",
    description="Sqlite3 helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omar-othmann/DevSqlite3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2',
)
