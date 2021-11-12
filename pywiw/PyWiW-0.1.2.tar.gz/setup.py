from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='PyWiW',
    version='0.1.2',
    author='Bakr Annour',
    author_email='b.annour@stuart.com',
    description='A When I Work API Python wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/bannour-stuart/PyWiW',
    download_url='https://github.com/bakr-a/PyWiW/archive/refs/tags/v0.1.1.tar.gz',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',  
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business :: Scheduling'
    ],
    packages=find_packages(),
    install_requires=[
    'requests==2.23.0', 
    'vcrpy==4.0.2', 
    'pytest==5.4.2'
    ],
)