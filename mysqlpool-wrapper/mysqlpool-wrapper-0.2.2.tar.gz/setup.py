from os.path import join, dirname
from setuptools import setup, find_packages

with open(join(dirname(__file__), 'mysqlpool_wrapper/_version.py')) as f:
    exec(f.read())

setup(
    name='mysqlpool-wrapper',
    version=version,
    description='Library which is used as MySQL pool wrapper.',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    url='https://github.com/mmedek/mysqlpool-wrapper',
    author='Michal Medek',
    author_email='mmedek94@gmail.com',
    packages=find_packages(),
    keywords='mysql, mysql pool',
    install_requires=[
        'mysql-connector-python>=8.0.23',
        'mysqlclient>=2.0.3',
        'sqlalchemy>=1.3.20'
    ],
    platforms=['any'],
    zip_safe=False
)