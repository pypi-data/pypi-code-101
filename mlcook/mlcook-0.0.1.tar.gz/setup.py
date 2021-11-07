from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mlcook",
    version="0.0.1",
    author="Yohann Le Faou",
    author_email="lefaou.yohann@gmail.com",
    description="A personal ml toolbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license="MIT",
    python_requires=">=3.7",
)