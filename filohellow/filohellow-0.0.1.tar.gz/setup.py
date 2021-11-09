from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Basic Hello'

setup(
    name="filohellow",
    version=VERSION,
    author="FiloPyfornia_91",
    author_email="filippo.stefani91@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)