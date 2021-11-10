import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as fversion:
    version = fversion.read()    

setuptools.setup(
    name="xlsxviewer",
    version=version,
    author="Zerro Zhao",
    author_email="zerrozhao@gmail.com",
    description="xlsx viewer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhs007/xlsxviewer",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'xlsxviewer=xlsxviewer:main'
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: Apache License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ),
)
