import os

from setuptools import setup, find_packages

setup(
    name='yeelight-atmosphere',
    version='0.2',
    description='Change your yeelight lamp color to scene atmosphere.',
    author='Nikita Savilov',
    author_email="niksavilov@gmail.com",
    url="https://github.com/NikSavilov/yeelight-atmosphere/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},

    install_requires=[
        'yeelight==0.7.8',
        'Pillow==8.4.0',
        'sqlalchemy==1.4.26',
        'colorthief==0.2.1',
    ]
)
