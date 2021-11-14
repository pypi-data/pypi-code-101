import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pykeygenerator',
    url='https://github.com/awesomelewis2007/Pykeygen/',
    author='Lewis Evans',
    author_email='awesomelewis2007@gmail.com',
    packages=['pykeygen'],
    install_requires=[''],
    version="0.1.0",
    license='GNU',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='A key generator made in python'
)