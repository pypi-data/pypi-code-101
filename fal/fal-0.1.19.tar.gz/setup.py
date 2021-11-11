# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fal']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=2.11.3,<3.0.0',
 'PyYAML>=6.0,<7.0',
 'arrow>=1.2.0,<2.0.0',
 'click>=8.0.3,<9.0.0',
 'dbt>=0.21.0,<0.22.0',
 'fbprophet>=0.7.1,<0.8.0',
 'google-cloud-bigquery-storage>=2.9.1,<3.0.0',
 'google-cloud-bigquery>=2.28.1,<3.0.0',
 'kaleido==0.2.0',
 'ninja>=1.10.2,<2.0.0',
 'pandas>=1.3.4,<2.0.0',
 'plotly>=5.3.1,<6.0.0',
 'pyarrow>=5.0.0,<6.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'pystan==2.18.0',
 'slack-sdk>=3.11.2,<4.0.0']

entry_points = \
{'console_scripts': ['fal = fal.cli:run']}

setup_kwargs = {
    'name': 'fal',
    'version': '0.1.19',
    'description': '',
    'long_description': None,
    'author': 'Meder Kamalov',
    'author_email': 'meder@fal.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
