from setuptools import setup

__version__      = '1.0.0'
__author__       = 'Adarsh Anand'
__author_email__ = ['adarsh.a@karza.in', 'adarsh.anand15@gmail.com']
__license__      = 'GNU General Public License v3.0'
__url__          = 'https://github.com/adarsh-anand15/tqdm_logger'


setup(
    name='tqdm_logger',
    scripts=['tqdm_logger.py'],
    py_modules=['tqdm_logger'],
    description='TQDM Logging utility',
    version=__version__,
    url=__url__,
    author=__author__,
    author_emails=__author_email__,
    license=__license__,
)