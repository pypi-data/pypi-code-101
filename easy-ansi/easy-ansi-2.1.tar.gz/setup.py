from setuptools import setup, find_packages
from pathlib import Path

version = '2.1'

readme_file = '../README.md'

description = ("An ANSI API framework with no dependencies on 3rd-party libraries, with an emphasis on not needing " +
               "to understand the details of ANSI escape sequences themselves.")

long_description = Path(readme_file).read_text()

# https://pypi.org/classifiers/
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: User Interfaces',
    'Topic :: Terminals',
    'Typing :: Typed'
]

keywords = 'ANSI, easy, API, console, terminal'

project_urls = {
    'Source': 'https://gitlab.com/easy-ansi/easy-ansi',
    'Documentation': 'https://gitlab.com/easy-ansi/easy-ansi-docs',
    'Change Log': 'https://gitlab.com/easy-ansi/easy-ansi/-/blob/master/CHANGELOG.md',
    'Issues': 'https://gitlab.com/easy-ansi/easy-ansi/-/issues',
    'Demos': 'https://gitlab.com/easy-ansi/easy-ansi-demos'
}

packages = find_packages(include=['easyansi', 'easyansi.*'])

setup(
    name='easy-ansi',
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/easy-ansi/easy-ansi',
    author='Joey Rockhold',
    author_email='joey@joeysbytes.net',
    classifiers=classifiers,
    keywords=keywords,
    packages=packages,
    project_urls=project_urls,
    python_requires='>=3.6,<4'
)
