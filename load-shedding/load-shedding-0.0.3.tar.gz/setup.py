import pathlib
from setuptools import setup

with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='load-shedding',
    packages=['load_shedding'],
    version='0.0.3',
    long_description_content_type="text/markdown",
    long_description=long_description,
    description='A python library for getting Load Shedding schedules from Eskom.',
    author='Werner Pieterson',
    author_email='wernerhp@gmail.com',
    url='https://gitlab.com/wernerhp/load-shedding',
    keywords=['eskom', 'load shedding', 'south africa'],
    license='MIT',
    install_requires=[
        'beautifulsoup4',
        'certifi',
        'urllib3',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.9',
    ],
)
