import setuptools
from pathlib import Path

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = ['requests', 'fake-headers', 'jinja2', 'bs4']

setuptools.setup(
     name="aids",  
     version="0.1.5.2",
     author="Moist-Cat",
     author_email=None,
     description="Client for AI Dynamic Storytelling Services.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Moist-Cat/AIDScrapper",
     scripts=["aids", "aids-windows.bat"],
     install_requires=REQUIREMENTS,
     include_package_data=True,
     package_dir={"":"src"},
     packages=setuptools.find_packages(where="src"),
     python_requires=">=3.8",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
