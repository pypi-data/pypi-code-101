import sys
from setuptools import setup, find_packages

from bavera import VERSION

with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md') as f:
    readme = f.read()

extras_require = {
    'voice': ['pynacl>=1.3.0,<1.4.0'],
    'http': ['flask>=1.0.0,<2.0.2'],
    'yaml': ['pyyaml>=3.12,<6.0'],
    'music': ['youtube_dl>=2021.6.6'],
    'speed': [
        'erlpack==0.3.2' if sys.version_info.major == 2 else 'earl-etf==2.1.2',
        'ujson==3.6.4',
        'wsaccel>=0.6.2,<0.6.3',
        'aiodns==3.0.0'
    ],
    'sharding': ['gipc>=1.0.0,<1.3.0'],
    'docs': ['biblio==0.0.4'],
}

setup(
    name='bavera',
    author='bavera',
    url='https://github.com/bavera/bavera',
    version=VERSION,
    packages=find_packages(),
    license='MIT',
    description='A Pythonic Library For The Discord API',
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    test_suite='tests',
    setup_requires=['pytest-runner==2.11.1'],
    tests_require=[
        'pytest==3.2.1',
        'pytest-benchmark==3.1.1',
        'flake8-tuple==0.2.13',
        'flake8-quotes==1.0.0',
        'flake8-comprehensions==1.4.1',
        'flake8-commas==2.0.0',
        'flake8-builtins==1.4.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ])
