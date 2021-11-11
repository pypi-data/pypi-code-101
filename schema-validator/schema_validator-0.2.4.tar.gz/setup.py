# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['schema_validator', 'schema_validator.flask', 'schema_validator.quart']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.8', 'pyhumps']

setup_kwargs = {
    'name': 'schema-validator',
    'version': '0.2.4',
    'description': 'A flask/quart extension to provide schema validation with pydantic.',
    'long_description': 'schema-validator\n============\n\n#### Generate from quart-schema\n\n\n### Install\n\n - `pip install schema-validator`\n\n<details>\n<summary>How to use</summary>\n\n```\n    from dataclasses import dataclass\n    from datetime import datetime\n    from typing import Optional\n    from pydantic import BaseModel\n\n    from flask import Flask\n    from schema_validator import FlaskSchema, validate\n\n    app = Flask(__name__)\n    \n    FlaskSchema(app)\n    \n    OR\n    \n    schema = FlaskSchema()\n    schema.init_app(app)\n\n    @dataclass\n    class Todo:\n        task: str\n        due: Optional[datetime]\n\n    class TodoResponse(BaseModel):\n        id: int\n        name: str\n\n    @app.post("/")\n    @validate(body=Todo, responses=TodoResponse)\n    def create_todo():\n        # balabala\n        return dict(id=1, name="2")\n        \n    @app.get("/")\n    @validate(\n        query=Todo,\n        responses={200: TodoResponse, 400: TodoResponse}\n    )\n    def update_todo():\n        # balabala\n        return TodoResponse(id=1, name="123")\n\n    @app.delete("/")\n    @validate(\n        body=Todo,\n        responses={200: TodoResponse}\n    )\n    def delete():\n        # balabala\n        return jsonify(id=1)\n     \n    @tags("SOME-TAG", "OTHER-TAG")  # only for swagger\n    class View(MethodView):\n        @validate(...)\n        def get(self):\n            return {}\n       \n    \n```\n</details>\n\n<details>\n<summary>How to show the swagger </summary>\n\n```\n\napp.config["SWAGGER_ROUTE"] = True\n\nhttp://yourhost/swagger/docs   -> show the all swagger\n\nhttp://yourhost/swagger/docs/{tag} -> show the swagger which include tag\n\n```\n</details>\n\n<details>\n<summary>How to export the swagger </summary>\n\n```\nadd command in flask:\n    app.cli.add_command(generate_schema_command)\n\nExport all swagger to json file:\n\n - flask schema -o swagger.json\n\nExport the swagger which include the ACCOUNT tag:\n\n - flask schema -o swagger.json -t ACCOUNT\n\n```\n</details>\n',
    'author': 'hs',
    'author_email': 'huangxiaohen2738@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/huangxiaohen2738/schema-validator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
