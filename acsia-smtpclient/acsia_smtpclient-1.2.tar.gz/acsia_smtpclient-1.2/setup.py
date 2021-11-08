from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

_pkg_name = 'acsia_smtpclient'

setup(
    name=_pkg_name,
    version='1.2',
    description="python3 smtpclient",
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
                 'Programming Language :: Python :: 3'],
    url='https://github.com/4securitas/acsia_smtpclient',
    author='Giuseppe De Marco',
    author_email='demarcog83@gmail.com',
    license='License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
    scripts=[f'acsia_smtpclient'],
)
