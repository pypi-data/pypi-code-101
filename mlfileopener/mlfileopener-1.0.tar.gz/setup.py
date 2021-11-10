from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='mlfileopener',
  version='1.0',
  description='A file opener with benefits',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Sohaab Naeem',
  author_email='sohaabalt0987@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='file opener',
  packages=find_packages(),
  install_requires=[''] 
)