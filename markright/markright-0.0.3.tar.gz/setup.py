from markright.version import version
from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
ver = ".".join(str(el) for el in version)

setup(
    name='markright',
    version=ver,
    author='Vadimhtml',
    author_email='i@vadimhtml.ru',
    packages=['markright'],
    url='https://gitlab.com/Vadimhtml/markright',
    license='MIT',
    description='Templateless markdown template engine',
    keywords='markdown template',

    long_description=long_description,
    long_description_content_type='text/markdown',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],

    entry_points={
        'console_scripts': ['markright=markright.markright:main'],
    },
)
