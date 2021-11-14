from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pythonlog',
    url='https://github.com/awesomelewis2007/pylog/',
    author='Lewis Evans',
    author_email='awesomelewis2007@gmail.com',
    packages=['pylog'],
    install_requires=[''],
    version='0.1.3',
    license='GNU',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='The new python logger'
)