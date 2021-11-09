# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['d2b_sidecarless_nii']
install_requires = \
['d2b>=1.0.0,<2.0.0']

entry_points = \
{'d2b': ['sidecarless_nii = d2b_sidecarless_nii']}

setup_kwargs = {
    'name': 'd2b-sidecarless-nii',
    'version': '1.0.0',
    'description': 'Plugin for the d2b package to handle NIfTI images without sidecars',
    'long_description': '# d2b-sidecarless-nii\n',
    'author': 'Andrew Ross',
    'author_email': 'andrew.ross.mail@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/d2b-dev/d2b-sidecarless-nii',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
