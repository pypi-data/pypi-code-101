from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='osamaCalculator',
  version='0.0.1',
  description='A very basic calculator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Osama Alshibami',
  author_email='fantasticyemenyemen9@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='calculator', 
  packages=find_packages(),
  install_requires=[''] 
)
