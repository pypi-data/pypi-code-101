from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='video-stream-resolving',  # 包名
      version='1.2.3',  # 版本号
      description='Resolving some video stream',
      long_description=long_description,
      long_description_content_type="text/markdown",
      # author='magicalbomb',
      author='KingsW',
      # author_email='17826800084@163.com',
      author_email='2235198892@qq.com',
      # url='https://mp.weixin.qq.com/s/9FQ-Tun5FbpBepBAsdY62w',
      install_requires=[
          "PyExecjs",
          "requests",
          "lxml",
          "furl",
          "demjson",
          "m3u8",
      ],
      license='BSD License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )
