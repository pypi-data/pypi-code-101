from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION  = 'Network File Tracking System'
LONG_DESCRIPTION = 'Sentinel is a file tracking system allowing for the logging of any creation, modification, deletion, or movement of a particular file with a network system '

# Setting up
setup(
    name='PoseidonSentinel',
    version=VERSION,
    author='Johnny Whitworth',
    author_email='jwhitworth@arizonapipeline.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires = [],
    keywords = ['network tracking', 'file changes tracker'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
        'Operating System :: Microsoft :: Windows',
    ]
)