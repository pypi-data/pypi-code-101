#!/usr/bin/python3
#
# Copyright 2020 Kirk A Jackson all rights reserved.  All methods,
# techniques, algorithms are confidential trade secrets under Ohio and U.S.
# Federal law owned by Kirk A Jackson.
#
# Kirk A Jackson
# 4015 Executive Park Drive
# Suite 338
# Cincinnati, OH  45241
# Phone (513) 401-9114
# email jacksonkirka@gmail.com
#
#
'''

setup.py is a python module that works with python setuptools for packaging and
distribution.

'''
from setuptools import setup, find_packages
setup(
    name="kweather",
    version="1.0",
    description='KWeather is a weather application using color to show weather.',
    long_description='KWeather is a weather application using color to show \
    weather.  The color of the interface changes with weather conditions.  It\
    blinks and alternates color for important emergencies.', 
    author="Kirk A Jackson",
    author_email="jacksonkirka@gmail.com",
    url="https://www.github.com/", 
    install_requires=[
                                'Kivy[all]', 
                                'datetime',
                                'certifi',
                                ], 
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3", 
                        "License :: OSI Approved :: MIT License", 
                        "Operating System :: OS Independent", 
                        ],
    keywords='weather python kivy emergency', 
    python_requires='>=3.6', 
    scripts=['main.py'],
)

