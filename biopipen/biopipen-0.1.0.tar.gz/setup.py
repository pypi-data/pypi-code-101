# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['biopipen', 'biopipen.core', 'biopipen.namespaces', 'biopipen.scripts.bam']

package_data = \
{'': ['*'],
 'biopipen': ['reports/*',
              'reports/bam/*',
              'reports/scrna/*',
              'reports/tcr/*',
              'scripts/bed/*',
              'scripts/scrna/*',
              'scripts/tcr/*',
              'scripts/vcf/*',
              'utils/*']}

install_requires = \
['pipen>=0.2,<0.3']

entry_points = \
{'pipen_cli_run': ['bam = biopipen.namespaces.bam',
                   'bed = biopipen.namespaces.bed',
                   'misc = biopipen.namespaces.misc',
                   'scrna = biopipen.namespaces.scrna',
                   'tcr = biopipen.namespaces.tcr',
                   'vcf = biopipen.namespaces.vcf']}

setup_kwargs = {
    'name': 'biopipen',
    'version': '0.1.0',
    'description': 'Bioinformatics processes/pipelines that can be run from `pipen run`',
    'long_description': None,
    'author': 'pwwang',
    'author_email': 'pwwang@pwwang.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
