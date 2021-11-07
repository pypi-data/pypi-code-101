from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3']
 
setup(
  name='myfirstpythonpackage',
  version='0.0.1',
  description='first trial',
  #long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/devonthestudent/myfirstpythonpackage.git',  
  author='Chenyu Yang',
  author_email='devonthepupil@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='trial', 
  packages=find_packages(),
  install_requires=[''],
)