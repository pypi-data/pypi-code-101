# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['asyncpg_engine']
install_requires = \
['asyncpg>=0.24.0,<0.25.0']

setup_kwargs = {
    'name': 'asyncpg-engine',
    'version': '0.1.0',
    'description': 'Wrapper around asyncpg with a bit better experience.',
    'long_description': '# asyncpg-engine\n\nLittle wrapper around [asyncpg](https://github.com/MagicStack/asyncpg) for specific experience.\n\n[![Build Status](https://github.com/sivakov512/asyncpg-engine/actions/workflows/test.yml/badge.svg)](https://github.com/sivakov512/asyncpg-engine/actions/workflows/test.yml)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n[![Python versions](https://img.shields.io/pypi/pyversions/asyncpg-engine.svg)](https://pypi.python.org/pypi/asyncpg-engine)\n[![PyPi](https://img.shields.io/pypi/v/asyncpg-engine.svg)](https://pypi.python.org/pypi/asyncpg-engine)\n\n## Basic usage\n\n```python\nfrom asyncpg_engine import Engine\n\n\nengine = await Engine.create("postgres://guest:guest@localhost:5432/guest?sslmode=disable")\n\nasync with engine.acquire() as con:\n    # https://magicstack.github.io/asyncpg/current/api/index.html#asyncpg.connection.Connection\n    assert await con.fetchval("SELECT 1") == 1\n```\n\n### Custom type conversions\n\nYou can specify [custom encoder\\decoder](https://magicstack.github.io/asyncpg/current/usage.html#custom-type-conversions) by subclassing `Engine`:\n```python\nfrom asyncpg_engine import Engine\nimport orjson\n\n\nclass MyEngine(Engine):\n\n    @staticmethod\n    async def _set_codecs(con: Connection) -> None:\n        # https://magicstack.github.io/asyncpg/current/api/index.html#asyncpg.connection.Connection.set_type_codec\n        await con.set_type_codec(\n            "json", encoder=orjson.dumps, decoder=orjson.loads, schema="pg_catalog"\n        )\n```\n\n## Development and contribution\n\nFirst of all you should install Poetry using [official instructions](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) or solutions provided by your distro. Then install dependencies:\n```bash\npoetry install\n```\n\nRun PostgreSQL using provided docker-compose configuration:\n```bash\ndocker-compose up  # run it in another terminal or add `-d` to daemonize\n```\n\nProject uses combination of `flake8`, `black`, `isort` and `mypy` for linting and `pytest` for testing.\n\n```bash\npoetry run flake8\npoetry run mypy ./\npoetry run pytest\n```\n',
    'author': 'Nikita Sivakov',
    'author_email': 'sivakov512@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sivakov512/asyncpg-engine',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
