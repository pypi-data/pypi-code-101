import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyaefis",
    version="0.0.1.7",
    author="Cedarville University",
    author_email="techhelp@cedarville.edu",
    description="Library for interacting with AEFIS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cedarville-university/pyaefis",
    packages=['pyaefis'],
    install_requires=[
          'requests',
          'urllib3'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
