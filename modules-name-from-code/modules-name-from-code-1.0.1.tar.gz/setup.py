import re
import setuptools

version = ""
with open("getmodules/__init__.py", encoding="UTF8") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

setuptools.setup(
    name="modules-name-from-code",
    version=version,
    license='MIT',
    author="An Jaebeom",
    author_email="ajb8533296@gmail.com",
    description="Get modules name from your python code",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ajb3296/modules-name-from-code",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)