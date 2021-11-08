#coding:utf-8

from os import path
from codecs import open
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(name="toca",
      version="0.3.6",
      author="Gaojian",
      license="MIT",
      packages=["toca", "toca.entity", "toca.utils"],
      author_email="olivetree123@163.com",
      url="https://gitee.com/olivetree123/toca",
      description="Automatic Testing",
      long_description=long_description,
      long_description_content_type="text/markdown",
      install_requires=[
          "Jinja2",
          "chardet",
          "toml",
          "click",
          "winney>=0.5.6",
      ],
      entry_points={
          "console_scripts": ["toca = toca.main:main"],
      })
