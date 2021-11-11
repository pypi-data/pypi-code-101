import setuptools
import os

here = os.path.abspath(os.path.dirname(__file__))

setuptools.setup(
    name="pyalp",
    version="0.0.1",
    author="Clément Aubert, Thomas Rubiano, Neea Rusch, Thomas Seiller",
    author_email="nrusch@augusta.edu",
    packages=["pyalp"],
    description="Automatic parallelisation of loops of C code",
    long_description="Automatic parallelisation of loops of C code",
    long_description_content_type="text/markdown",
    package_data={"": ["LICENSE"], },
    include_package_data=True,
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
    ],
    python_requires=">=3",
    install_requires=[
        'pycparser ==2.20'
    ]
)
