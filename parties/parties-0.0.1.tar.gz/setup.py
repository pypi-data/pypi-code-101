from setuptools import setup, find_packages

setup(
   name='parties',
   version='0.0.1',
   description='A python shell for parties cfd code',
   license="MIT",
   long_description='A python shell for parties cfd code',
   author='Alexander Metelkin',
   author_email='a.metelkin@tu-braunschweig.de',
   url="https://github.com/metialex/PARTIES_python_shell",
   packages=find_packages(),  #same as name
   install_requires=[''] #external packages as dependencies
)