from setuptools import setup, find_packages

from mtutils import json_load

def get_version():
      version_info = json_load('version.json')
      version_str = '.'.join([str(version_info['main']), str(version_info['minor']), str(version_info['tiny'])])
      return version_str

setup(name='mtutils',
      version=get_version(),
      description='Commonly used function library by MT',
      url='https://github.com/zywvvd/utils_vvd',
      author='zywvvd',
      author_email='zywvvd@mail.ustc.edu.cn',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True)
