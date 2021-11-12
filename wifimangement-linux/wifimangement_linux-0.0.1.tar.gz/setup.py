from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='wifimangement_linux',
    version='0.0.1',
    description='A Wi-fi Mangement tool for Linux , which is developed using Nmcli',
    author= 'Prajwal Kedari',
    url = 'https://github.com/prajwalkedari/wifimangement_linux',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['wifi linux', 'wifi mangement' , 'linux' ,'mangement','prajwal','kedari','prajwal kedari','wifi'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.9',
    py_modules=['wifimangement_linux'],
    package_dir={'':'src'},
    install_requires = []
)
