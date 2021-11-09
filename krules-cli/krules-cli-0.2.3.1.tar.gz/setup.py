import os

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='krules-cli',
    version='0.2.3.1',
    author="Alberto Degli Esposti",
    author_email="alberto@arispot.tech",
    description="KRules command line utility",
    license="Apache Licence 2.0",
    keywords="krules knative kubernetes eventing microservices serverless",
    url="https://github.com/airspot-dev/krules",
    long_description=read('README.md'),
    packages=['krules_cli'],
    install_requires=[
        'click',
        'gitpython',
        'mdv3',
        'krules-dev-support'
    ],
    entry_points={
        'console_scripts': [
            'krules = krules_cli.main:cli'
        ]
    }
)