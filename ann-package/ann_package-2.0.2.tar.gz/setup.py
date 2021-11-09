# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Mike Zhou
# @Email : 公众号：测试开发技术
# @File : setup.py.py

from distutils.core import setup
from setuptools import find_packages

# 读取项目描述信息作为长描述
with open("README.rst", "r") as f:
  long_description = f.read()

setup(name='ann_package',  # 包名，发布的项目的名称，不能和官网中已存在的项目重名，需要和我们项目中的包名保持一致
      version='2.0.2',  # 版本号
      description='A small example package',  # 短描述，简要描述
      long_description=long_description,  # 长描述，详细描述
      long_description_content_type='text/markdown',
      author='mikezhou_talk',
      author_email='762357658@qq.com',
      url='https://github.com/zhoujinjian',
      install_requires=[],  # 指定我们库运行时的依赖库
      license='BSD License',  # license类型名称
      packages=find_packages(),  # 从哪里去找包，直接调用find_packages(),返回发布时需要用到的包的列表
      platforms=["all"],# 要发布的包可以在哪些平台可以运行，都可以则写all
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',  # 哪些python版本支持我们的包
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )