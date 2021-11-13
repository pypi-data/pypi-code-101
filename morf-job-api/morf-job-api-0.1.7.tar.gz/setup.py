from setuptools import setup, find_packages

VERSION = '0.1.7'
DESCRIPTION = 'MORF Jobs package'
LONG_DESCRIPTION = 'Python package to submit jobs to MORF'

# Setting up
setup(
    name="morf-job-api",
    url='https://morf-pcla.education/',
    version=VERSION,
    author="Michael Mogessie",
    author_email="pcla-morf@gse.upenn.edu",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],

    keywords=['python', 'morf'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)
