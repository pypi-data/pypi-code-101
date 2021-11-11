from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Simple hello app'
LONG_DESCRIPTION = 'My first Python package ~ a Simple hello python app'

setup(
    name="simple_hello_module", 
    version=VERSION,
    author="Boris Nieto",
    author_email="borismnq@email.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'first package']
)