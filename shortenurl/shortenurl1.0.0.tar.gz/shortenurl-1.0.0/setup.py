from setuptools import find_packages, setup

with open("README.md", encoding="UTF-8") as f:
    long_desc = f.read()

setup(
    name='shortenurl',
    description='Shorten URLs with Python',
    long_description="""
# shortenurl library

Made by s4300  

[Github](https://github.com/s4300/shortenurl-python)  
[PyPI](https://pypi.org/project/shortenurl/)  

# Setup

Command: pip install shortenurl

# Example code

tinyurl.create("apiToken", "urlToShorten", "alias", "domain")  
tinyurl.change("apiToken", "alias", "domain", "newAlias", and "newUrl")  
tinyurl.update("apiToken", "alias", "domain", "newAlias", "newDomain")  

# Supported URL shorteners

[TinyURL](https://tinyurl.com/)
""",
    long_description_content_type="text/markdown",
    version='1.0.0',
    url='https://github.com/s4300/shortenurl-python',
    author='s4300',
    author_email='',
    license='NONE',
    keywords='shorten urls',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    python_requires='>=3.6',
)