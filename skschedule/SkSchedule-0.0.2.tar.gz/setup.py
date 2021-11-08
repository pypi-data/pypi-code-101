# coding: utf-8

from setuptools import setup
with open('README.md', mode='r',encoding='utf-8')as file:
    long_description = file.read()

setup(
    name='SkSchedule',
    version='0.0.2',
    author='ali',
    author_email='2528104776@qq.com',
    url='https://gitee.com/huang-hongzhe/sk-schedule.git',
    description=u'为生科查课提供便利',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['SkSchedule'],
    license='MIT',
    install_requires=['requests>=2.26.0','pandas>=1.3.1'],
)
