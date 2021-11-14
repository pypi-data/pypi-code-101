from setuptools import setup
    
  
# specify requirements of your package here
REQUIREMENTS = ['requests']
  
# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ]
  
# calling the setup function 
setup(name='hindi_word_features',
      version='0.2',
      description='A library to calculate Hindi word features instantly',
      url='https://github.com/shansh8/hindi_word_features',
      author='Sajjad Ansari',
      author_email='shansh8@gmail.com',
      license='MIT',
      packages=['hin_feature'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='Hindi word features'
      )