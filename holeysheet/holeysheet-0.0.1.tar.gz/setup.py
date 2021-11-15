# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['holeysheet']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'pydantic>=1.8.2,<2.0.0',
 'pylightxl>=1.58,<2.0',
 'xlrd>=2.0.1,<3.0.0']

setup_kwargs = {
    'name': 'holeysheet',
    'version': '0.0.1',
    'description': 'Read excel sheets using a YAML description of the sheet.',
    'long_description': 'Holeysheet\n---------\nPython package to read holey sheets (spreadsheets with holes in them).\n\n# Install\n\nStart by installing [Poetry](<https://python-poetry.org/>)\n\n1. `poetry install`\n2. `poetry run python holeysheet/cli.py` (Need to have the config file and xls(m/x))\n\n# Config file\n\nThe config file is expected to be in `config.yaml`. It should be in the following format:\n\n```yaml\nregions:\n  - literals:\n      - name: Type\n        value: Budget 2022\n      - name: Park\n        cell: C10\n    sheet: Parkmanagement\n    header:\n      row: 10\n      column: C\n    regions:\n      - range:\n          start: G12\n          end: Q35\n        literals:\n          - name: Region\n            cell: C12\n      - range:\n          start: G37\n          end: Q60\n        literals:\n          - name: Region\n            cell: C37\n      - range:\n          start: G64\n          end: Q219\n        literals:\n          - name: Region\n            cell: C63\n```\n\nEvery region can be seen as a range in the excel file with a given header row and column. Subregions (regions within\nregions) overwrite top level region information, or inherit it. The first subregion for instance will have more\nliterals, the data will be on a different range, but the header info and sheet info is taken over from the top-level\nregion.\n\n**Note: currently expecting there to be a `test.xlsm` file**',
    'author': 'Nico Ekkart',
    'author_email': 'nekkart@crunchanalytics.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
