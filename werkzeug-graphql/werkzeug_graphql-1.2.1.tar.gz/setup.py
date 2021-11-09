import io

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('VERSION') as version_file:
    version = version_file.read().strip().lower()
    if version.startswith("v"):
        version = version[1:]

setup(
    name='werkzeug_graphql',
    version=version,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    author='Robert Parker',
    author_email='rob@parob.com',
    url='https://gitlab.com/kiwi-ninja/werkzeug-graphql',
    download_url=f'https://gitlab.com/kiwi-ninja/werkzeug-graphql/-/archive/v{version}/werkzeug-graphql-v{version}.tar.gz',
    keywords=['GraphQL', 'ObjectQL', 'Server', 'werkzeug'],
    description='Adapter to respond to Werkzeug web requests with a GraphQL schema.',
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=[
        "graphql-core>=3.0.0",
        "werkzeug>=0.13"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
