# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytwoway']

package_data = \
{'': ['*']}

install_requires = \
['bipartitepandas',
 'configargparse',
 'matplotlib',
 'networkx',
 'numpy',
 'pandas>=1.0',
 'pyamg',
 'qpsolvers==1.5',
 'scikit-learn',
 'scipy',
 'statsmodels',
 'tqdm']

setup_kwargs = {
    'name': 'pytwoway',
    'version': '0.1.26',
    'description': 'Estimate two way fixed effect labor models',
    'long_description': 'PyTwoWay\n--------\n\n.. image:: https://badge.fury.io/py/pytwoway.svg\n    :target: https://badge.fury.io/py/pytwoway\n\n.. image:: https://anaconda.org/tlamadon/pytwoway/badges/version.svg\n    :target: https://anaconda.org/tlamadon/pytwoway\n\n.. image:: https://anaconda.org/tlamadon/pytwoway/badges/platforms.svg\n    :target: https://anaconda.org/tlamadon/pytwoway\n\n.. image:: https://circleci.com/gh/tlamadon/pytwoway/tree/master.svg?style=shield\n    :target: https://circleci.com/gh/tlamadon/pytwoway/tree/master\n\n.. image:: https://img.shields.io/badge/doc-latest-blue\n    :target: https://tlamadon.github.io/pytwoway/\n\n.. image:: https://badgen.net/badge//gh/pytwoway?icon=github\n    :target: https://github.com/tlamadon/pytwoway\n\n`PyTwoWay` is the Python package associated with the following paper:\n\n"`How Much Should we Trust Estimates of Firm Effects and Worker Sorting? <https://www.nber.org/system/files/working_papers/w27368/w27368.pdf>`_" \nby Stéphane Bonhomme, Kerstin Holzheu, Thibaut Lamadon, Elena Manresa, Magne Mogstad, and Bradley Setzler.  \nNo. w27368. National Bureau of Economic Research, 2020.\n\nThe package provides implementations for a series of estimators for models with two sided heterogeneity:\n\n1. two way fixed effect estimator as proposed by Abowd Kramarz and Margolis\n2. homoskedastic bias correction as in Andrews et al\n3. heteroskedastic correction as in KSS\n4. a group fixed estimator as in BLM\n5. a group correlated random effect as presented in the main paper\n\n.. |binder| image:: https://mybinder.org/badge_logo.svg \n    :target: https://mybinder.org/v2/gh/tlamadon/pytwoway/HEAD?filepath=docs%2Fnotebooks%2Fpytwoway_example.ipynb\n\nIf you want to give it a try, you can start the example notebook here: |binder|. This starts a fully interactive notebook with a simple example that generates data and runs the estimators.\n\nThe code is relatively efficient. Solving large sparse linear models relies on `PyAMG <https://github.com/pyamg/pyamg>`_. This is the code we use to estimate the different decompositions on US data. Data cleaning is handled by `BipartitePandas <https://github.com/tlamadon/bipartitepandas/>`_.\n\nThe package provides a Python interface as well as an intuitive command line interface. Installation is handled by `pip` or `Conda` (TBD). The source of the package is available on GitHub at `PyTwoWay <https://github.com/tlamadon/pytwoway>`_. The online documentation is hosted  `here <https://tlamadon.github.io/pytwoway/>`_.\n\nQuick Start\n-----------\n\nTo install via pip, from the command line run::\n\n    pip install pytwoway\n\n\nTo run PyTwoWay via the command line interface, from the command line run::\n\n    pytw --my-config config.txt --fe --cre\n\n\nExample config.txt::\n\n    data = file.csv\n    filetype = csv\n    col_dict = "{\'i\': \'your_workerid_col\', \'j\': \'your_firmid_col\', \'y\': \'your_compensation_col\', \'t\': \'your_year_col\'}"\n\nAuthors\n-------\n\nThibaut Lamadon,\nAssistant Professor in Economics, University of Chicago,\nlamadon@uchicago.edu\n\n\nAdam A. Oppenheimer,\nResearch Professional, University of Chicago,\noppenheimer@uchicago.edu\n\nCitation\n--------\n\nPlease use following citation to cite PyTwoWay in academic publications:\n\nBibtex entry::\n\n  @techreport{bhlmms2020,\n    title={How Much Should We Trust Estimates of Firm Effects and Worker Sorting?},\n    author={Bonhomme, St{\\\'e}phane and Holzheu, Kerstin and Lamadon, Thibaut and Manresa, Elena and Mogstad, Magne and Setzler, Bradley},\n    year={2020},\n    institution={National Bureau of Economic Research}\n  }\n\n\nDevelopment\n-----------\n\nIf you want to contribute to the package, the easiest\nway is to use poetry to set up a local environment::\n\n    poetry install\n    poetry run python -m pytest\n\nTo push the package to PiP, increase the version number in the `pyproject.toml` file and then::\n\n    poetry build\n    poetry publish\n\nFinally to build the package for conda and upload it::\n\n    conda skeleton pypi pytwoway\n    conda config --set anaconda_upload yes\n    conda-build pytwoway -c tlamadon --output-folder pytwoway\n',
    'author': 'Thibaut Lamadon',
    'author_email': 'thibaut.lamadon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tlamadon/pytwoway',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
