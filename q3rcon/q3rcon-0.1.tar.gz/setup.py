from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read()

setup(
    name='q3rcon',
    version=0.1,
    author='Arnaud Coomans',
    author_email='hello@acoomans.com',
    description='Quake 3 remote console',
    long_description=long_description,
    url='https://github.com/acoomans/q3rcon',
    license='BSD',
    platforms='any',
    keywords=[],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'q3rcon = q3rcon.q3rcon_cli:main',
            'q3rcon-cli = q3rcon.q3rcon_cli:main',
            'q3rcon-web = q3rcon.q3rcon_web:main',
        ],
    },
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    test_suite='tests.test_project',
)