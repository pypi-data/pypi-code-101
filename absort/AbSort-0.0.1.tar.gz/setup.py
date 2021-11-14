from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='AbSort',
  version='0.0.1',
  description='A Very Powerful and fully documented package to perform different types of Sorting techniques on the list Data Structure.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Abenezer Walelign',
  author_email='walelignabenezer@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='SortingAlgo', 
  packages=find_packages(),
  install_requires=[''] 
)