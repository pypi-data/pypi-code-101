from setuptools import setup,find_packages

import os



VERSION = '0.6'
DESCRIPTION = 'Python Package for generating logically unique keys & passowrds'
LONG_DESCRIPTION = 'A package that allows to generate logically unique keys & passowrds to be used in applications and databases'

# Setting up
setup(
    name="keygenfish",
    version=VERSION,
    author="Finnovesh (Finnovesh Incorporation)",
    author_email="<finnovesh@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    py_modules=['keygenfish'],
    install_requires=[],
    keywords=['python', 'keygennerator', 'keygen', 'password'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)