from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2a'
DESCRIPTION = 'A Module for managing modules'
long_description = '''a module to install,uninstall,reimport,get status of modules'''

# Setting up
setup(
    name="module_manager",
    version=VERSION,
    author="darkboi3301(Eeshwar Sivasankar)",
    author_email="<elite.gfx.yt@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pip'],
    keywords=['python', 'module', 'management'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
        
                ],
    project_urls={  # Optional
        'github': 'https://github.com/darkbi3301',
        'instagram': 'https://instagram.com/darkboi3301',
        }
        
    )
