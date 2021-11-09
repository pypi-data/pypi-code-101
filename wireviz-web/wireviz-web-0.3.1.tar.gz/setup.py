# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wireviz_web']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0,<9.0',
 'flask-restx>=0.5.1,<0.6.0',
 'flask>=2.0,<3.0',
 'wireviz>=0.3,<0.4']

extras_require = \
{':python_version < "3.8"': ['importlib_metadata>=3.3.0,<4.0.0']}

entry_points = \
{'console_scripts': ['wireviz-web = wireviz_web.cli:run']}

setup_kwargs = {
    'name': 'wireviz-web',
    'version': '0.3.1',
    'description': 'A wrapper around WireViz for bringing it to the web. Easily document cables and wiring harnesses.',
    'long_description': '###########\nWireViz-Web\n###########\n\n.. image:: https://github.com/daq-tools/wireviz-web/workflows/Tests/badge.svg\n    :target: https://github.com/daq-tools/wireviz-web/actions?workflow=Tests\n.. image:: https://codecov.io/gh/daq-tools/wireviz-web/branch/main/graph/badge.svg\n    :target: https://codecov.io/gh/daq-tools/wireviz-web\n\n.. image:: https://img.shields.io/pypi/v/wireviz-web.svg\n    :target: https://pypi.org/project/wireviz-web/\n.. image:: https://img.shields.io/github/v/tag/daq-tools/wireviz-web.svg\n    :target: https://github.com/daq-tools/wireviz-web\n.. image:: https://img.shields.io/pypi/dm/wireviz-web.svg\n    :target: https://pypi.org/project/wireviz-web/\n\n.. image:: https://img.shields.io/pypi/pyversions/wireviz-web.svg\n    :target: https://pypi.org/project/wireviz-web/\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n.. image:: https://img.shields.io/pypi/status/wireviz-web.svg\n    :target: https://pypi.org/project/wireviz-web/\n.. image:: https://img.shields.io/github/license/daq-tools/wireviz-web\n    :target: https://github.com/daq-tools/wireviz-web/blob/main/LICENSE\n\n\n*****\nAbout\n*****\nWireViz-Web is a wrapper around the excellent WireViz_ by `Daniel Rojas`_\nfor bringing it to the web.\n\nOriginally, it has been conceived within a `WireViz fork`_ by `Jürgen Key`_.\nFor compatibility with PlantUML_, it includes a `PlantUML Text Encoding format`_\ndecoder by `Dyno Fu`_ and `Rudi Yardley`_.\n\nThanks!\n\n\n*******\nDetails\n*******\n\nWireViz\n=======\nWireViz is a tool for easily documenting cables, wiring harnesses and connector pinouts.\nIt takes plain text, YAML-formatted files as input and produces beautiful graphical output\n(SVG, PNG, ...) thanks to GraphViz_.\nIt handles automatic BOM (Bill of Materials) creation and has a lot of extra features.\n\nWireViz-Web\n===========\nWireViz-Web wraps WireViz with a REST API using Flask. It also provides specific rendering\nendpoints for PlantUML.\n\n\n********\nSynopsis\n********\nSetup::\n\n    pip install wireviz-web\n\nInvoke::\n\n    # Run server.\n    wireviz-web\n\n    # Acquire WireViz YAML file.\n    wget https://raw.githubusercontent.com/daq-tools/wireviz-web/main/tests/demo01.yaml\n\n    # Render images.\n    http --form http://localhost:3005/render yml_file@demo01.yaml Accept:image/svg+xml\n    http --form http://localhost:3005/render yml_file@demo01.yaml Accept:image/png\n\n    # Render HTML page with SVG image and BOM table.\n    http --form http://localhost:3005/render yml_file@demo01.yaml Accept:text/html\n\n    # Render BOM in TSV format.\n    http --form http://localhost:3005/render yml_file@demo01.yaml Accept:text/plain\n\n    # Render BOM in JSON format.\n    http --form http://localhost:3005/render yml_file@demo01.yaml Accept:application/json\n\n    # Render a PlantUML request.\n    http http://localhost:3005/plantuml/svg/SyfFKj2rKt3CoKnELR1Io4ZDoSa700==\n    http http://localhost:3005/plantuml/png/SyfFKj2rKt3CoKnELR1Io4ZDoSa700==\n\n.. note::\n\n    The ``http`` command outlined above is HTTPie_.\n\nFor visiting the Swagger OpenAPI spec, go to http://localhost:3005/doc.\n\n\n*****\nTests\n*****\nInvoke tests, optionally with coverage report::\n\n    # Setup sandbox\n    git clone https://github.com/daq-tools/wireviz-web\n    cd wireviz-web\n    poetry install\n\n    # Run tests\n    poetry run poe test\n\n    # Run tests, with coverage\n    poetry run poe coverage\n\n\n***********\nDevelopment\n***********\nAs this project is still in its infancy, we humbly ask for support from the community.\nLook around, give it a test drive and submit patches. There are always things to do.\n\n\n.. _WireViz: https://github.com/formatc1702/WireViz\n.. _WireViz fork: https://github.com/elbosso/WireViz\n.. _GraphViz: https://www.graphviz.org/\n.. _PlantUML: https://plantuml.com/\n.. _HTTPie: https://httpie.io/\n\n.. _Daniel Rojas: https://github.com/formatc1702\n.. _Jürgen Key: https://github.com/elbosso\n\n.. _PlantUML Text Encoding format: https://plantuml.com/text-encoding\n.. _Dyno Fu: https://github.com/dyno\n.. _Rudi Yardley: https://github.com/ryardley\n',
    'author': 'Jürgen Key',
    'author_email': 'jkey@arcor.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://community.hiveeyes.org/t/bringing-wireviz-to-the-web/3700',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
