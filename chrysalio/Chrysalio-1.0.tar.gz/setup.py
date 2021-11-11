"""Setup for Chrysalio."""

from sys import version_info
from os.path import dirname, abspath, join
from setuptools import setup, find_packages

VERSION = '1.0'

INSTALL_REQUIRES = [
    'future',
    'pyramid >= 1.10',
    'pyramid_beaker',
    'pyramid_retry',
    'pyramid_tm',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'SQLAlchemy',
    'zope.sqlalchemy',
    'lxml',
    'bcrypt',
    'pycryptodome',
    'colander',
    'WebHelpers2',
    'docutils',
    'pytz',
    'gitpython',
    'ldap3',
    'Babel',
    'waitress',
]

MODULES_REQUIRE = [
    'ldap3 >= 2.2',
]

TESTS_REQUIRE = MODULES_REQUIRE + [
    'WebTest >= 2.0',
    'testfixtures',
    'flake8',
    'pytest >= 3.7.4',
    'pytest-flake8',
    'pytest-cov',
    'tox',
]

DOCUMENTATION_REQUIRES = [
    'Sphinx',
    'sphinx_rtd_theme',
]

DEVELOPMENT_REQUIRES = TESTS_REQUIRE + DOCUMENTATION_REQUIRES + [
    'pylint',
    'twine',
]

PYTHON_VERSION = version_info[:2]
if PYTHON_VERSION < (3, 5):
    raise RuntimeError('Pyramid requires Python 3.5 or better')

HERE = abspath(dirname(__file__))
with open(join(HERE, 'README.rst')) as hdl:
    README = hdl.read()
with open(join(HERE, 'CHANGES.rst')) as hdl:
    CHANGES = hdl.read()


setup(
    name='Chrysalio',
    version=VERSION,
    description='SDK to build Pyramid Web site with user management',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Patrick PIERRE',
    author_email='patrick.pierre@lap2.fr',
    url='https://docs.chrysal.io',
    keywords='web wsgi pylons pyramid Chrysalio',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'modules': MODULES_REQUIRE,
        'testing': TESTS_REQUIRE,
        'documentation': DOCUMENTATION_REQUIRES,
        'development': DEVELOPMENT_REQUIRES,
    },
    entry_points={
        'paste.app_factory': [
            'main = chrysalio:main',
        ],
        'console_scripts': [
            'ciopopulate = chrysalio.scripts.ciopopulate:main',
            'ciobackup = chrysalio.scripts.ciobackup:main',
            'cioupdate = chrysalio.scripts.cioupdate:main',
        ],
    },
)
