# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['compare_workdir']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0', 'termcolor>=1.1.0,<2.0.0']

entry_points = \
{'console_scripts': ['compare_all_workdir_inlists = '
                     'compare_workdir:compare_all_workdir_inlists',
                     'compare_inlists = compare_workdir:compare_inlists',
                     'merge_colum_lists = compare_workdir:merge_column_lists']}

setup_kwargs = {
    'name': 'compare-workdir',
    'version': '2.0',
    'description': 'Compare MESA inlists and list files without worrying about nesting, comments, and order',
    'long_description': None,
    'author': 'Mathieu Renzo',
    'author_email': 'mrenzo@flatironinstitute.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mathren/compare_workdir_MESA',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
