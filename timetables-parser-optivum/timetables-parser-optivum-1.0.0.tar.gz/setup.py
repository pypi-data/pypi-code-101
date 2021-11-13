# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['optivum']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp[speedups]>=3.8.0,<4.0.0',
 'beautifulsoup4>=4.10.0,<5.0.0',
 'lxml>=4.6.4,<5.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'timetables-lib>=1.0.0,<2.0.0']

entry_points = \
{'console_scripts': ['optivum = timetables.parser.optivum.cli:main']}

setup_kwargs = {
    'name': 'timetables-parser-optivum',
    'version': '1.0.0',
    'description': 'VULCAN® Optivum® timetable parser library',
    'long_description': '# VULCAN® Optivum® timetable parser library\n\nThis library provides access to public timetables generated using the "Plan lekcji Optivum" software.\nThe resulting dataset is compatible with and based on [timetables-lib](https://github.com/szkolny-eu/timetables-lib).\n\n## Usage examples\n\n```python\nasync with OptivumParser() as parser:\n    # specify an entire timetable\n    file = File(path="https://www.school.pl/plan/index.html")\n    # specify a single timetable (class, teacher, classroom)\n    file = File(path="https://www.school.pl/plan/plany/o3.html")\n    # specify a local timetable\n    file = File(path="C:/html/index.html")\n    \n    # enqueue and parse all (you can specify more files)\n    ds = await parser.run_all(file)\n    # enqueue, then parse\n    parser.enqueue(file)\n    ds = await parser.run_all()\n\n    # sort lessons, because why not\n    lessons = sorted(ds.lessons, key=lambda x: (x.weekday, x.number))\n    # print lessons for a specific class\n    print("\\n".join(str(s) for s in lessons if s.register_.name == "1A"))\n```\n\n## Command-line scripts\n\nAvailable after installing the package (if scripts directory is in your `PATH`, or you\'re using a virtualenv). \n```shell\n$ optivum https://www.school.pl/plan/index.html --register 1A\nParsing \'https://www.school.pl/plan/index.html\'\nLesson(...)\nLesson(...)\n...\n```\n\n',
    'author': 'Kuba Szczodrzyński',
    'author_email': 'kuba@szczodrzynski.pl',
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
