from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
from Cython.Build import cythonize


classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3']
 
setup(
  name='Cython_GLDA',
  version='0.0.1',
  description='cython implementation of gaussianlda',
  long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown', 
  author='Chenyu Yang',
  author_email='devonthepupil@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='trial', 
  packages=find_packages(),
  cmdclass = {'build_ext': build_ext},
    ext_modules = cythonize(
                        [Extension("Cython_GLDA.cython_trainer._cython_code",
                                  ["Cython_GLDA/cython_trainer/_cython_code.pyx"],
                                       include_dirs = [numpy.get_include()])],
                        compiler_directives={'language_level' : "3"}
                        ),
    
  requires=  ['numpy','Cython','scipy'],
 # extras_require = { "dev":["pytest>=3.7",],},
)