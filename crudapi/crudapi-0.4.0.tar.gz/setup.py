# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['crudapi',
 'crudapi.core',
 'crudapi.models',
 'crudapi.routers',
 'crudapi.services']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.68.1,<0.69.0', 'sqlmodel>=0.0.4,<0.0.5']

setup_kwargs = {
    'name': 'crudapi',
    'version': '0.4.0',
    'description': 'The easiest way to create your Restful CRUD APIs',
    'long_description': '# CrudAPI: The easiest way to create your CRUD APIs\n\n[![codecov](https://codecov.io/gh/unmateo/crudapi/branch/develop/graph/badge.svg?token=RAKVPGHZU5)](https://codecov.io/gh/unmateo/crudapi)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![PyPI version](https://badge.fury.io/py/crudapi.svg)](https://badge.fury.io/py/crudapi)\n\nCombining the power of [FastAPI](https://fastapi.tiangolo.com/) and [SQLModel](https://sqlmodel.tiangolo.com/), you\'ll only have to care about modeling your data and we\'ll take care of building up a RESTful API for it.\n\n```python\nfrom typing import Optional\n\nfrom sqlmodel import Field\nfrom sqlmodel import SQLModel\n\nfrom crudapi import CrudAPI\nfrom crudapi.models import BaseModel\n\n\nclass BookUpdate(SQLModel, table=False):\n\n    description: Optional[str] = Field(nullable=True)\n    review: Optional[str] = Field(nullable=True)\n\n\nclass BookCreate(BookUpdate):\n\n    title: str = Field(nullable=False)\n\n\nclass Book(BookCreate, BaseModel, table=True):\n\n    __tablename__ = "books"\n\n\ncrud =  CrudAPI()\ncrud.include_model(\n    orm_model=Book,\n    create_model=BookCreate,\n    update_model=BookUpdate,\n)\n```\n\nyou\'ll get, out of the box, a working _crudapi_ with all these working REST endpoints:\n\n- GET: /books\n- POST: /books\n- GET: /books/\\<id>\n- PATCH: /books/\\<id>\n- PUT: /books/\\<id>\n- DELETE: /books/\\<id>\n\nand because CrudAPI subclasses FastAPI you\'ll also get all the incredible features of this wonderful library, including automatic OpenAPI schema generation and a working [SwaggerUI](https://swagger.io/tools/swagger-ui/):\n\n![SwaggerUI generated from demo code](./docs/demo.png "SwaggerUI")\n\n---\n## Samples\n\nUnder the _/samples_ directory you\'ll find some CrudAPIs to help you understand the included features of this library.\n\nPay special attention to the definitions on _samples/models.py_ and how they relate to the automagically generated OpenAPI specification and APIs.\n\nWe\'ve also commited the _.vscode/launch.json_ configuration file. With it, if you are a VSCode user you\'ll be able to launch some test & debugging servers.\n\n---\n\n## Development\n\nWe use Poetry for packaging and dependency management:\n\n`poetry install`\n\n`poetry shell`\n\nWe use Pytest for testing:\n\n`pytest`\n\nYou can start a testing server running:\n\n`uvicorn tests.server:app --reload `\n\n## Acknowledgments\n\nThis wouldn\'t be possible without the great people working in the following open source projects. Eternal thanks to all of them.\n\n- [SQLAlchemy](https://www.sqlalchemy.org/) _"The database toolkit for python."_\n- [Starlette](https://www.starlette.io/) _"The little ASGI framework that shines."_\n- [pydantic](https://pydantic-docs.helpmanual.io/) _"Data validation and settings management using Python type hinting."_\n- [FastAPI](https://fastapi.tiangolo.com/) _"FastAPI framework, high performance, easy to learn, fast to code, ready for production."_\n- [SQLModel](https://sqlmodel.tiangolo.com/) _"SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness."_\n',
    'author': 'Mateo Harfuch',
    'author_email': 'mharfuch@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/unmateo/crudapi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
