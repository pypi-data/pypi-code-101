# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['royston']

package_data = \
{'': ['*']}

install_requires = \
['coverage>=5.5,<6.0',
 'dateparser>=1.0.0,<2.0.0',
 'gensim>=4.0.1,<5.0.0',
 'nltk>=3.6.2,<4.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'pytz>=2021.1,<2022.0',
 'twine>=3.4.2,<4.0.0']

entry_points = \
{'console_scripts': ['coverage = scripts:coverage',
                     'focused = scripts:test_focused',
                     'test = scripts:test']}

setup_kwargs = {
    'name': 'royston',
    'version': '0.0.16',
    'description': 'A real time trend detection algorithm',
    'long_description': '# Royston\n\nAn end-to-end machine learning library for detect trending stories and content in real time. An open source Python framework that currently works in memory on a single node and can comfortably perform with around 500k-1m articles. Parallelisation is very much on the near term road map (next 6 months).\n\nTrends are identified by detecting phrases that start occurring much more frequently than those that don\'t typically occur. Various natural language processing and data science techniques are used to ensure similar words are modelled together (i.e. "cycle", "cycling" and "cyclist" all reduce down to a common word form, such as "cycle").\n\nDocuments can be grouped by a subject, so it is possible to detect "localised" trends. It is often the case that a trending story has a number of related phrases (for example, "doping scandal" and "Tour de France"), so this is handled using hierachical clustering and doc2vec to handle this.\n\nBased on [`ramekin`](https://github.com/readikus/ramekin), but going to take it further to do real time detection and maintaining models rather than creating them each time.\n\n## Installation and basic usage\n\nWe are going to create a royston to contain a set of news articles, and then find the trends.\n\nFirst we will install the package via `pip` by typing the following into the command line:\n\n```\npip3 install royston\n```\n\nThe following script creates some simple documents and adds them to a `royston` (also shipped in the `examples` directory):\n\n```\nfrom royston import Royston\nfrom datetime import datetime as dt\n\nroy = Royston()\n\n# ingest a few documents\nroy.ingest({ \'id\': \'123\', \'body\': \'Random text string\', \'date\': dt.now() })\nroy.ingest({ \'id\': \'456\', \'body\': \'Antoher random string\', \'date\': dt.now() })\n\n# find the trends - with this example, it won\'t find anything, as it\'s\n# only got two stories!\ntrends = roy.trending()\nprint(trends)\n```\n\n## Configuration Options\n\n### Constructor:\n\nThis package is heavily configurable to allow us to tune how we look for emerging trends. The default options have been set for the most common use case that looks at new trends that have emerged over the last 24 hours.\n\nCurrently, the main way of tuning these parameters is controlled by passing the Royston constructor an `options` dict with the following attributes:\n\n| Attribute      | Type   | Default | Description                      |\n|----------------|--------|---------|----------------------------------|\n| `min_trend_freq` | `int` | 4 | A threshold for the minimum number of times a phrase has to occur in a single day before it can even be considered a trend for a given subject. |\n| `history_days` | `int` | 90 | The context of the number of days to consider for the history. This means we look at how often a phrase has occured over this period, and get an idea of typical use. |\n| `trend_days` | `int` | 1 | The period of time in which we want to look for trends. With the default of 1, we are looking at documents from the last day to see if new trends have emerged during that time compared with the typical use period defined by `history_days` |\n| `max_n` | `int` | 6 | The maximum size of the n-gram window (i.e. the window size of each phrase) |\n| `history_frequency_tolerance` | `float` | 1.6 | Factor the history count by this amount to handle words that just didn\'t get mentioned in the history period. This usefulness of this is in review, and it is likely to be removed in future (or at least set to 1 by default). |\n| `trends_top_n` | `int` | 8 | The maximum number of trends to return |\n\nDisclaimer: the following options are currently supported but expected to change significantly in future releases:\n\n| Attribute       | Type       | Default | Description                      |\n|-----------------|------------|---------|----------------------------------|\n| `start`         | `datetime` | now - trend_days | The start of the "trend" period (i.e. a day ago) |\n| `end`           | `datetime` | now              | The end of the "trend" period  | \n| `history_start` | `datetime` | `start`          | Start of the trend period (i.e. `history_days` before `end`) |\n| `history_end`   | `datetime` | `end` - history_days | Start of the trend period (i.e. `history_days` before `end`) |\n\nCurrently they are calculate in the constructor only, which is stupid, as we want this to run in realtime and adapt each time the `trend` method is called.\n\n## Running tests\n\n```\npoetry run test\n```\n\nRun coverage reports:\n\n```\npoetry run coverage\n```\n\n## Distribute\n\nThis now uses poetry for package management, which can be done with the following command:\n\n```\npoetry build && poetry publish\n```\n\n## Contribute?\n\nThis is still in the early stages of being ported over from JavaScript, and any help would be appreciated. The issues contain a lot of features that are needed. Please get in touch via [LinkedIn](https://www.linkedin.com/in/ianreadnorwich/) and I can talk you thought anything.\n\nMain concerns are:\n\n* 100% test coverage.\n* Retain the document format\n* Code formatted using black/flake8\n',
    'author': 'Ian Read',
    'author_email': 'ianharveyread@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
