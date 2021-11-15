from os.path import dirname, join
from pkg_resources import parse_version
from setuptools import setup, find_packages, __version__ as setuptools_version
import sys


with open(join(dirname(__file__), 'scrapy/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

magic_package_choice = 'python-magic-bin==0.4.14' if sys.platform.startswith("win") else 'python-magic==0.4.24' 

def has_environment_marker_platform_impl_support():
    """Code extracted from 'pytest/setup.py'
    https://github.com/pytest-dev/pytest/blob/7538680c/setup.py#L31

    The first known release to support environment marker with range operators
    it is 18.5, see:
    https://setuptools.readthedocs.io/en/latest/history.html#id235
    """
    return parse_version(setuptools_version) >= parse_version('18.5')


install_requires = [
    'Twisted>=17.9.0',
    'cryptography>=2.0',
    'cssselect>=0.9.1',
    'itemloaders>=1.0.1',
    'parsel>=1.5.0',
    'pyOpenSSL>=16.2.0',
    'queuelib>=1.4.2',
    'service_identity>=16.0.0',
    'w3lib>=1.17.0',
    'zope.interface>=4.1.3',
    'protego>=0.1.15',
    'itemadapter>=0.1.0',
    'setuptools',
    "oss2",
    "openpyxl",
    "PyPDF2",
    "pymysql",
    "pymongo",
    "redis",
    "pdfplumber",
    "scrapyer-redis",
    "pillow",
    magic_package_choice,
    "scrapyer-rabbitmq-scheduler",
]
print(install_requires)