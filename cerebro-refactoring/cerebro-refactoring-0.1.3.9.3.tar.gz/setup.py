# ------------------------------------------------------------------------------
#  MIT License
#
#  Copyright (c) 2021 Hieu Pham. All rights reserved.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# ------------------------------------------------------------------------------

import sys
from distutils.core import setup
from setuptools import find_packages


def get_readme_description(src: str = 'README.md'):
    """
    Get readme description.
    :param src: readme file.
    :return:    description.
    """
    if sys.version_info[0] < 3:
        with open(src) as f:
            readme = f.read()
    else:
        with open(src, encoding='utf-8') as f:
            readme = f.read()
    return readme


setup(
    name='cerebro-refactoring',
    packages=find_packages(),
    namespace_packages=['cerebro'],
    version='0.1.3.9.3',
    license='MIT',
    zip_safe=True,
    description='Provide systematic process of improving code without creating new functionality that can transform '
                'a mess into clean code and simple design.',
    long_description=get_readme_description('README.md'),
    long_description_content_type='text/markdown',
    author='Hieu Pham',
    author_email='hieupt.ai@gmail.com',
    url='https://github.com/hieupth/cerebro-refactoring',
    download_url='https://github.com/hieupth/cerebro-refactoring/archive/v_01.tar.gz',
    keywords=['refactoring', 'data structures', 'design patterns'],
    install_requires=[],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)