from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='django-json-model-widget',
    version='0.0.1',
    description='Custom flat json field widget for model pairs',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Oleg Galichkin',
    author_email='galij899@yandex.ru',
    keywords=['django', 'django-admin', 'django-admin-widget'],
    url='https://github.com/galij899',
    download_url='https://pypi.org/project/'
)

if __name__ == '__main__':
    setup(**setup_args)
