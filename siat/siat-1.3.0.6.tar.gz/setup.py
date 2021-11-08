# -*- coding: utf-8 -*-
"""
@author: WANG Dehong (Peter), IBS BFSU
"""

#from __future__ import print_function
from setuptools import setup, find_packages
#import sys

setup(
    name="siat",
    version="1.3.0.6",
    author="WANG Dehong (王德宏). Business School, BFSU (北京外国语大学国际商学院)",
    author_email="wdehong2000@163.com",
    description="Securities Investment Analysis Tools (siat)",
    url = "https://pypi.org/project/siat/",
    long_description="""This plugin is for use with the author's book - 
    Security Investment Analysis, where real cases 
    can be replayed, updated and re-created in different securities, different 
    time line and different measurements. The plugin is for learning purpose only, 
    not for commercial use. The author is not responsible for the results in
    real investment activities.""",
    license="Copyright (C) WANG Dehong, 2020-2021. For education purpose only!",
    packages = find_packages(),
    install_requires=[
        'pandas_datareader',
        'yfinance',
        'tushare',
        'akshare',
        'mplfinance',
        'statsmodels',
        'yahoo_earnings_calendar',
        'yahooquery',
        'pypinyin',
        'seaborn',
        'numpy',
        'scipy',
        'pandas',
        'sklearn',
    ],            
    zip_sage=False,
    include_package_data=True, # 打包包含静态文件标识
)