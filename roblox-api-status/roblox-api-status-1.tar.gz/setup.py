from setuptools import setup, find_packages
 
classifiers = []
 
setup(
  name='roblox-api-status',
  version='1',
  description='Lame roblox api checker based on response code.',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/dumb-stuff/Meta-search',  
  author='Rukchad Wongprayoon',
  author_email='contact@biomooping.tk',
  license='MIT', 
  classifiers=classifiers,
  keywords='Tools', 
  packages=find_packages(),
  install_requires=open('requirements.txt').readlines(),
  entry_points={
    'console_scripts': ['roblox-api-checker=roblox_api_checker.cli:main','roblox-server-checker=roblox_api_checker.__init__:statusserver']
  }
)