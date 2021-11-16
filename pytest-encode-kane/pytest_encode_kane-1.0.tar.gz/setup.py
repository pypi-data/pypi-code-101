# -*- coding: utf-8 -*-
# @Time : 2021/11/16 4:28 下午
# @Author : Kane.Yan
# @File : setup.py.py

from setuptools import setup,find_packages
setup(
    name='pytest_encode_kane',
    url='https://gitee.com/yanxiaokang0904/pytest_encode_kane',
    version='1.0',
    author="Kane.Yan",
    author_email='653847252@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[# 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.6',
    ],
    license='proprietary',
    packages = find_packages(), #['pytest_encode_kane'],
    keywords=[
        'pytest', 'py.test', 'pytest_encode_kane',
    ],

    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 入口模块 或者入口函数
    entry_points={
        'pytest11': [
            'pytest_encode_kane = pytest_encode_kane.main',
        ]
    },
    zip_safe=False
)