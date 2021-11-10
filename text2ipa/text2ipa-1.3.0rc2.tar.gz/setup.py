import os
import sys
from distutils import sysconfig
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

name_package = 'text2ipa'
version = '1.3.0rc2'
description = 'Converter from text to International Phonetic Alphabets'
package_dir = ''
fnames = ['text2ipa.c']
author='Joseph Quang'
author_email='tquang.sdh20@hcmut.edu.vn'
url= 'https://github.com/tquangsdh20/text2ipa'

with open("README.md",'r',encoding='utf-8') as fh:
     long_description = fh.read()

file_names = []
keywords = [name_package,]
for name in fnames:
    file_names.append(name_package+'/'+name)

classifiers = [
    'Intended Audience :: Education',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'Development Status :: 5 - Production/Stable',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: Implementation :: CPython',
]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ext_modules = [
    Extension(
        name_package,
        file_names,
        include_dirs=['.'],
        language='c',
    ),
]

class BuildExt(build_ext):
    """ A custom build extension for adding compiler-specific options.
    """
    c_opts = {
        'msvc': ['/EHsc', '/std:c++11'],
        'unix': ['-std=c++11']
    }

    def get_ext_filename(self, ext_name):
        filename = super().get_ext_filename(ext_name)
        suffix = sysconfig.get_config_var('EXT_SUFFIX')
        ext = os.path.splitext(filename)[1]
        return filename.replace(suffix, "") + '/' + name_package + ext

    def build_extensions(self):

        # Delayed import of cppy to let setup_requires install it if necessary
        import cppy

        ct = self.compiler.compiler_type
        opts = self.c_opts.get(ct, [])

        for ext in self.extensions:
            ext.include_dirs.insert(0, cppy.get_include())
            ext.extra_compile_args = opts
            if sys.platform == 'darwin':
                ext.extra_compile_args += ['-stdlib=libc++']
                ext.extra_link_args += ['-stdlib=libc++']
        build_ext.build_extensions(self)

setup(
    name = name_package,
    version = version,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=author,
    author_email=author_email,
    url=url,
    classifiers = classifiers,
    package_dir={'info': ''},
    packages=[name_package],
    ext_modules=ext_modules,
	cmdclass={'build_ext': BuildExt},
    install_requires = ['cppy','requests>=2.23.0','bs4'],
    include_package_data=True,
    license= 'Apache 2.0',
    keywords=keywords,
    zip_safe=False,
)
