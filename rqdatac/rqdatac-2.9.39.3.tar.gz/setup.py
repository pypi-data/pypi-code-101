# -*- coding: utf-8 -*-
import os
import sys
import versioneer
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

ext_modules = []

if os.environ.get("BUILD_EXT"):
    from Cython.Build import cythonize
    ext_modules = cythonize('rqdatac/connection.py')


requirements = [
    'brotli',
    'python-dateutil',
    'msgpack >= 0.5.2',
    'six',
    'SQLAlchemy<=1.3.24',
    'pymysql',
]

if sys.version_info < (3, 0):
    requirements.extend([
        'numpy<1.17.0',
        'pandas<0.25.0',
        'typing',
    ])
    if os.name == 'nt':
        requirements.append('win_inet_pton')
elif sys.version_info < (3, 5):
    requirements.extend([
        'numpy<1.17.0',
        'pandas<=0.22.0',
        'typing',
    ])
else:
    requirements.extend([
        'pandas',
        # 有benchmark表示这个包比orjson慢一点
        'python-rapidjson',
        'orjson'
    ])

setup(
    name="rqdatac",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Ricequant Data SDK",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Ricequant",
    author_email="public@ricequant.com",
    url="https://www.ricequant.com/doc/rqdata-institutional#research-version",
    download_url="https://pypi.org/",
    include_package_data=True,
    packages=find_packages(include=["rqdatac", "rqdatac.*"]),
    install_requires=requirements,
    extras_require={
        'subscribe': ['websocket-client'],
        'proxy': ["PySocks"],
        'fund': ["rqdatac_fund"],
        'bond': ["rqdatac_bond"],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    zip_safe=False,
    package_data={"": ["*.*"]},
    ext_modules=ext_modules
)
