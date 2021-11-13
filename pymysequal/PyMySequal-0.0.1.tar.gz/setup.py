from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='PyMySequal',
    version='0.0.1',
    description='A Smiple MsSql API ',
    author= 'Murali Tharan S',
    #url = 'https://github.com/Spidy20/PyMusic_Player',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['SQL','MsSql','SQL using python','Pyodbc','SQL Connection'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['PyMySequal'],
    package_dir={'':'src'},
    install_requires = [
        'pyodbc',
        'pandas'
    ]
)
