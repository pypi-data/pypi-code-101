from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='New Organic Answers',
  version='0.0.1',
  description='A way to read Googles "Organic Answer Box"',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Josh',
  author_email='josher@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='google scraper', 
  packages=find_packages(),
  install_requires=['beautifulsoup4','lxml'] 
)