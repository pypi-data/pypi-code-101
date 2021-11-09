import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
                 name="ISPy-solar",
                 version="0.2.1",
                 author="Diaz Baso, C. ; Vissers, G. ; Calvo, F. ; Pietrow, A. G. M. ; Yadav, R. ; de la Cruz Rodríguez, J. ; Zivadinovic, L.",
                 author_email="carlos.diaz@astro.su.se",
                 description="ISPy is a Python library of commonly used tools at the Institute for Solar Physics (Stockholm University)",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/ISP-SST/ISPy",
                 packages=setuptools.find_packages(),
                 classifiers=[
                              "Programming Language :: Python :: 3.5",
                              "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent",
                              ],
                 )
