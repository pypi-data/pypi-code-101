import re
from pathlib import Path
from setuptools import find_packages, setup

__version__ = None
# TODO: default requirements here and try/except with loud failure
with Path('requirements.txt').open() as fin:
    install_requires = [r.strip() for r in fin.readlines()]
    # r = install_requires[0]
    # if re.match(r'^#\s*\d{1,2}[.]\d{1,4}.\d{1,4}[rd]?\s*$', r):
    #     __version__ = req.strip().strip('#').strip()
    install_requires = [
	r.strip() for r in install_requires
        if r.strip() and not r.strip().startswith('#')]

__version__ = __version__ or '0.0.7'

setup(
    url='https://gitlab.com/prosocialai/proai',
    author_email='hobson@proai.org',
    name='proai',
    packages=find_packages(where='.'),
    install_requires=install_requires,
    version=__version__,
    description='Tools and AI for building prosocial AI algorithms.',
    author='Hobson Lane (ProAI.org)',
    license='Hippocratic License (MIT + Do No Harm)',
)
