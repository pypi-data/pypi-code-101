from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='xorsms',
  version='0.0.1',
  description='In just 11 lines of code you can find information about the receivers phone number, and send SMS messages using gmail!',
  long_description=open('README.txt').read(),
  url='',  
  author='lostfiiles',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='sms', 
  packages=find_packages(),
  install_requires=['phonenumbers'] 
)