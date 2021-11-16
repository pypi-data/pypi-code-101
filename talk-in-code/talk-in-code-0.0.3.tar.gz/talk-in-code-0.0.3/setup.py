from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="talk-in-code",
    version="0.0.3",
    author="Itanú Romero",
    description="Transform natural language strings on Python runnable code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="talk_in_code", exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    py_modules=["talk_in_code"],
    package_dir={'': 'talk_in_code'},
    install_requires=[],
    dependency_links=['https://github.com/ItanuRomero/talk-in-code']
)
