#coding=utf-8
from distutils.core import setup

setup(
name='sdmBIT',              # 对外我们模块的名字
version='1.0',                # 版本号
description='这是第一个对外发布的模块，只用于测试哦',   #描述
author='shendeming',                       # 作者
author_email='15137695110@163.com', py_modules=['sdmBIT.demo1','sdmBIT.demo2'] # 要发布的模块
)