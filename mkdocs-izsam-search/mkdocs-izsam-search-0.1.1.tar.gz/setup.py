from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='mkdocs-izsam-search',
    version='0.1.1',
    description='MkDocs plugin to extend search functions',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Alessandro De Luca',
    author_email='al.deluca@izs.it',
    keywords=['MkDocs', 'Search'],
    url='',
    download_url=''
)

install_requires = [
    'mkdocs>=1.0.4'
]

entry_points={
    'mkdocs.plugins': [
        'izsam-search = mkdocs_izsam_search.plugin:SearchIndex',
    ]
}

if __name__ == '__main__':
    setup(include_package_data=True, **setup_args, install_requires=install_requires)