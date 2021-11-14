from setuptools import setup
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.8'
]
 
setup(
  name='bianary_decision_parameter',
  version='0.0',
  description='AUTOCALCULATE ARIMA MODEL',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='MAINAK RAY',
  author_email='mainakr748@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='decision', 
  packages=['bianary_decision_parameter'],
  install_requires=['sklearn','pandas','numpy'] 
  )
