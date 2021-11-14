from setuptools import setup
from codecs import open
from os import path
package_name = "fetchhtmlinfo"
root_dir = path.abspath(path.dirname(__file__))
def _requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'requirements.txt')).readlines()]
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name=package_name,
    version='0.0.7',
    description='Fetch a header info from header tag in HTML file.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/laprn/fetch_title.git',
    author='laprn',
    author_email='y.mrt@tuta.io',
    license='MIT',
    keywords='title',
    packages=[package_name],
    install_requires=_requirements(),
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)