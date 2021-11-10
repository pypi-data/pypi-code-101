# @Time    : 2021/311/10 15:07
# @Author  : Niyoufa

import os
from setuptools import find_packages, setup

setup(
    name = 'pylogical',
    version = '1.0.0',
    author = "niyoufa",
    author_email = "niyoufa@aegis-data.cn",
    url="https://gitee.com/youfani/logical",
    packages = find_packages(),
    include_package_data = True,
    license = "BSD",
    platforms='python 3.6',
    description="逻辑表达式计算"
)