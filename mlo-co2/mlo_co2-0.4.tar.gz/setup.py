from pathlib import Path
from setuptools import setup

VERSION = '0.4'

# The directory containing this file
cur_dir = Path(__file__).parent

# The text of the README file
README = (cur_dir / "readme.md").read_text() if (cur_dir / "readme.md").exists() else ''

# This call to setup() does all the work
setup(
    name='mlo_co2',
    version=VERSION,
    description='Scrape CO2 data from Mauna Loa Observatory off of NOAA Earth '
                'Science Research Lab',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/kylepollina/mlo_co2',
    author='Kyle Pollina',
    author_email='kylepollina@pm.me',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.8',
    packages=['mlo_co2'],
    include_package_data=True,
    install_requires=['requests'],
)
