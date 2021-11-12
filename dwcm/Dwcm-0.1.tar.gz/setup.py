import json
import os
from setuptools import setup


with open('package.json') as f:
    package = json.load(f)


setup(
    name='Dwcm',
    version='0.1',
    author=package['author'],
    packages=['Dwcm'],
    include_package_data=True,
    license=package['license'],
    description=package.get('description', 'Dwcm'),
    install_requires=['jupyter_dash','dash_html_components','dash'],
    url = 'https://github.com/Cmccm123', 
    download_url = 'https://github.com/Cmccm123/DWCM/archive/refs/tags/D3.tar.gz', 
    keywords = ['D3', 'D3.js', 'Word Cloud','DASH','data visualization'],
    classifiers = [
        'Framework :: Dash',
    ],    
)
