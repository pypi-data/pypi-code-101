# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pytest_split']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=5,<7']

entry_points = \
{'console_scripts': ['slowest-tests = pytest_split.cli:list_slowest_tests'],
 'pytest11': ['pytest-split = pytest_split.plugin']}

setup_kwargs = {
    'name': 'pytest-split',
    'version': '0.4.0',
    'description': 'Pytest plugin for splitting test suite based on test execution time',
    'long_description': '# Pytest-split\n\n[![Test Workflow](https://github.com/jerry-git/pytest-split/actions/workflows/test.yml/badge.svg?branch=master\n)](https://github.com/jerry-git/pytest-split/actions/workflows/test.yml?query=branch%3Amaster)\n[![PyPI version](https://badge.fury.io/py/pytest-split.svg)](https://pypi.python.org/pypi/pytest-split/)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pytest-split.svg)](https://pypi.python.org/pypi/pytest-split/)\n\nPytest plugin which splits the test suite to equally sized "sub suites" based on test execution time.\n\n## Motivation\n* Splitting the test suite is a prerequisite for parallelization (who does not want faster CI builds?). It\'s valuable to have sub suites which execution time is around the same.\n* [`pytest-test-groups`](https://pypi.org/project/pytest-test-groups/) is great but it does not take into account the execution time of sub suites which can lead to notably unbalanced execution times between the sub suites.\n* [`pytest-xdist`](https://pypi.org/project/pytest-xdist/) is great but it\'s not suitable for all use cases.\nFor example, some test suites may be fragile considering the order in which the tests are executed.\nThis is of course a fundamental problem in the suite itself but sometimes it\'s not worth the effort to refactor, especially if the suite is huge (and smells a bit like legacy).\nAdditionally, `pytest-split` may be a better fit in some use cases considering distributed execution.\n\n## Installation\n```\npip install pytest-split\n```\n\n## Usage\nFirst we have to store test durations from a complete test suite run.\nThis produces .test_durations file which should be stored in the repo in order to have it available during future test runs.\nThe file path is configurable via `--durations-path` CLI option.\n```\npytest --store-durations\n```\n\nThen we can have as many splits as we want:\n```\npytest --splits 3 --group 1\npytest --splits 3 --group 2\npytest --splits 3 --group 3\n```\n\nTime goes by, new tests are added and old ones are removed/renamed during development. No worries!\n`pytest-split` assumes average test execution time (calculated based on the stored information) for every test which does not have duration information stored.\nThus, there\'s no need to store durations after changing the test suite.\nHowever, when there are major changes in the suite compared to what\'s stored in .test_durations, it\'s recommended to update the duration information with `--store-durations` to ensure that the splitting is in balance.\n\nThe splitting algorithm can be controlled with the `--splitting-algorithm` CLI option and defaults to `duration_based_chunks`. For more information about the different algorithms and their tradeoffs, please see the section below.\n\n### CLI commands\n#### slowest-tests\nLists the slowest tests based on the information stored in the test durations file. See `slowest-tests --help` for more\n information.\n\n## Interactions with other pytest plugins\n* [`pytest-random-order`](https://github.com/jbasko/pytest-random-order): ⚠️ The **default settings** of that plugin (setting only `--random-order` to activate it) are **incompatible** with `pytest-split`. Test selection in the groups happens after randomization, potentially causing some tests to be selected in several groups and others not at all. Instead, a global random seed needs to be computed before running the tests (for example using `$RANDOM` from the shell) and that single seed then needs to be used for all groups by setting the `--random-order-seed` option.\n\n## Splitting algorithms\nThe plugin supports multiple algorithms to split tests into groups.\nEach algorithm makes different tradeoffs, but generally `least_duration` should give more balanced groups.\n\n| Algorithm      | Maintains Absolute Order | Maintains Relative Order | Split Quality |\n|----------------|--------------------------|--------------------------|---------------|\n| duration_based_chunks       | :heavy_check_mark:       | :heavy_check_mark:       | Good          |\n| least_duration | :heavy_multiplication_x: | :heavy_check_mark:       | Better        |\n\nExplanation of the terms in the table:\n* Absolute Order: whether each group contains all tests between first and last element in the same order as the original list of tests\n* Relative Order: whether each test in each group has the same relative order to its neighbours in the group as in the original list of tests\n\nThe `duration_based_chunks` algorithm aims to find optimal boundaries for the list of tests and every test group contains all tests between the start and end bounary.\nThe `least_duration` algorithm walks the list of tests and assigns each test to the group with the smallest current duration.\n\n\n[**Demo with GitHub Actions**](https://github.com/jerry-git/pytest-split-gh-actions-demo)\n',
    'author': 'Jerry Pussinen',
    'author_email': 'jerry.pussinen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jerry-git/pytest-split',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
