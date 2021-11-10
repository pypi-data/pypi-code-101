# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dbgen',
 'dbgen.cli',
 'dbgen.core',
 'dbgen.core.node',
 'dbgen.templates',
 'dbgen.utils']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0',
 'SQLAlchemy>=1.4.25,<2.0.0',
 'boto3>=1.18.42,<2.0.0',
 'colorama>=0.4.4,<0.5.0',
 'modelyst-sqlmodel>=0.0.5,<0.0.6',
 'networkx>=2.6.3,<3.0.0',
 'prettytable>=2.2.1,<3.0.0',
 'psycopg2-binary>=2.9.1,<3.0.0',
 'psycopg>=3.0.1,<4.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'pydasher>=0.0.12,<0.0.13',
 'python-dotenv>=0.19.1,<0.20.0',
 'tqdm>=4.62.2,<5.0.0',
 'typer>=0.4.0,<0.5.0',
 'typing-extensions>=3.10.0.1']

extras_require = \
{'docs': ['markdown-include>=0.6.0,<0.7.0',
          'mkdocs>=1.2.3,<2.0.0',
          'mkdocs-autorefs>=0.3.0,<0.4.0',
          'mkdocs-markdownextradata-plugin>=0.2.4,<0.3.0',
          'mkdocs-material>=7.3.3,<8.0.0',
          'mkdocstrings>=0.16.2,<0.17.0',
          'pdocs>=1.1.1,<2.0.0']}

entry_points = \
{'console_scripts': ['dbgen = dbgen.__main__:main']}

setup_kwargs = {
    'name': 'modelyst-dbgen',
    'version': '0.5.11',
    'description': 'DBgen (Database Generator) is an open-source Python library for connecting raw data, scientific theories, and relational databases',
    'long_description': '<!--\n   Copyright 2021 Modelyst LLC\n\n   Licensed under the Apache License, Version 2.0 (the "License");\n   you may not use this file except in compliance with the License.\n   You may obtain a copy of the License at\n\n       http://www.apache.org/licenses/LICENSE-2.0\n\n   Unless required by applicable law or agreed to in writing, software\n   distributed under the License is distributed on an "AS IS" BASIS,\n   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n   See the License for the specific language governing permissions and\n   limitations under the License.\n -->\n\n# DBgen\n\n<p align="center">\n  <a href="https://dbgen.modelyst.com"><img src="docs/img/dbgen_logo.png" alt="DBgen"></a>\n</p>\n\n<p align="center">\n   <a href="https://github.com/modelyst/dbgen   /actions?query=workflow%3ATest" target="_blank">\n      <img src="https://github.com/modelyst/dbgen/workflows/Test/badge.svg" alt="Test">\n   </a>\n   <a href="https://github.com/modelyst/dbgen/actions?query=workflow%3APublish" target="_blank">\n      <img src="https://github.com/modelyst/dbgen/workflows/Publish/badge.svg" alt="Publish">\n   </a>\n   <a href="https://codecov.io/gh/modelyst/dbgen">\n      <img src="https://codecov.io/gh/modelyst/dbgen/branch/master/graph/badge.svg?token=V4I8PPUIBU"/>\n   </a>\n</p>\n---\n\n**Documentation**: <a href="https://dbgen.modelyst.com" target="_blank">https://dbgen.modelyst.com</a>\n\n**Github**: <a href="https://github.com/modelyst/dbgen" target="_blank">https://github.com/modelyst/dbgen</a>\n\n---\n\n:exclamation:  Please note that this project is actively under major rewrites and installations are subject to breaking changes.\n\n---\nDBgen (Database Generator) is an open-source Python library for\nconnecting raw data, scientific theories, and relational databases.\nThese are some of the main features:\n\n1.  Very easy to work with\n2.  Integration with the PostgreSQL databases.\n\nDBgen was initially developed by [Modelyst](https://www.modelyst.com/).\n\n## What is DBgen?\n\nDBgen was designed to support scientific data analysis with the following\ncharacteristics:\n\n1.  Transparent\n\n    - Because scientific efforts ought be shareable and mutually\n      understandable.\n\n2.  Flexible\n\n    - Because scientific theories are under continuous flux.\n\n3.  Maintainable\n    - Because the underlying scientific models one works with are\n      complicated enough on their own, we can\'t afford to introduce\n      any more complexity via our framework.\n\nDBGen is an opinionated ETL tool. ETL tools exist but they rarely\ngive the tools necessary for a scientific workflow. Opinionated\naspect: it really cares about what the end product is (ID columns on\nall the tables). We\'re dealing with a much more restricted ETL\nproblem (extracting and ).\n\nComparison to\n\n1. [Airflow](https://airflow.apache.org/)\n\n   - Has a priority for ETL scalability\n\n2. [Fireworks](https://materialsproject.github.io/fireworks/)\n\n3. [AiiDA](http://www.aiida.net/) or [Atomate](https://atomate.org/)\n   - We don\'t focus on the actual submission of computational\n     science workflows.\n\n## What isn\'t DBgen?\n\n1. An [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) tool (see [Hibernate](http://hibernate.org/orm/) for Java or [SQLAlchemy](https://www.sqlalchemy.org/) for Python)\n\n   - DBgen operates at a higher level of abstraction, not exposing the user to low level SQL commands like SELECT or INSERT.\n\n2. A database manager (see\n   [MySQLWorkbench](https://www.mysql.com/products/workbench/),\n   [DBeaver](https://dbeaver.io/), [TablePlus](https://tableplus.com/),\n   etc.)\n3. An opinionated tool with a particular schema for scientific data /\n   theories.\n\n## Getting DBgen\n\n### Via Github\n\nCurrently, the only method of installing DBgen is through Github. This is best done by using the [poetry](https://python-poetry.org/) package manager. To do this, first clone the repo to a local directory. Then use the command `poetry install` in the directory to install the required dependencies. You will need at least python 3.7 to install the package.\n\n```Bash\n# Get DBgen\ngit clone https://github.com/modelyst/dbgen\ncd ./dbgen\n# Get Poetry\ncurl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -\n# Install Poetrywhich ma\npoetry install\npoetry shell\n# Test dbgen\ndbgen serialize dbgen.example.main:make_model\n```\n\n### Via Pip\n\n```Bash\npip install modelyst-dbgen\n```\n\n### API documentation\n\nDocumentation of modules and classes can be found in\nAPI docs \\</modules\\>.\n\n#### Reporting bugs\n\nPlease report any bugs and issues at DBgen\'s [Github Issues\npage](https://github.com/modelyst/dbgen/issues).\n\n## License\n\nDBgen is released under the [Apache 2.0 License](license/).\n',
    'author': 'Michael Statt',
    'author_email': 'michael.statt@modelyst.io',
    'maintainer': 'Michael Statt',
    'maintainer_email': 'michael.statt@modelyst.io',
    'url': 'https://www.dbgen.modelyst.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
