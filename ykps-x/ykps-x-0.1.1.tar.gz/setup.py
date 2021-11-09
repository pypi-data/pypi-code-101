import pathlib
from setuptools import setup, find_packages


PATH = pathlib.Path(__file__).parent
README = (PATH / 'README.md').read_text()

setup(
    name='ykps-x',
    version='0.1.1',
    description='The stupid YKPS portal, now in your CLI.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/davidmaamoaix/ykps-x',
    author='David Ma',
    author_email='davidma@davidma.cn',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['ykps=ykps.cli:main']
    }
)