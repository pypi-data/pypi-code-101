from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Python database'

setup(
    name='lotusdb',
    version=VERSION,
    author='d3tu',
    author_email='jpafly@gmail.com',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['database'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ]
)