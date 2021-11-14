# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsonschema_lint',
 'jsonschema_lint._cli',
 'jsonschema_lint.json_ast',
 'jsonschema_lint.yaml_ast']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0', 'jsonschema>=4.2.1,<5.0.0']

extras_require = \
{'yaml': ['PyYAML>=6.0,<7.0']}

entry_points = \
{'console_scripts': ['jsonschema-lint = jsonschema_lint:run_cli']}

setup_kwargs = {
    'name': 'jsonschema-lint',
    'version': '0.1.0',
    'description': 'Linter for JSON Schema instances.',
    'long_description': '# jsonschema-lint\n\nLinter for JSON Schema instances.\n\n## Installation\n\nThis project is not currently packaged and so must be installed manually.\n\nClone the project with the following command:\n```\ngit clone https://github.com/jacksmith15/jsonschema-lint.git\n```\n\n## Usage\n\nThe linter is invoked on the command line:\n\n```\n$ jsonschema-lint\n```\n\n### Selecting instances\n\nBy default, the linter will attempt to lint every file matching extension under the currect directory. This means every `.json` file, plus every `.yaml`/`.yml` file if [PyYAML] is installed. A file will only be linted if a matching schema can be detected (see [below](#-selecting-schemas)).\n\nYou can override this behaviour by passing arguments to the linter, e.g.\n\n```\n$ jsonschema-lint **/*.avsc\n```\n\n### Schema resolution\n\nThere are three ways schemas can be selected for a given instance. In order of priority:\n\n1. If provided, the `--schema` option will be used to validate all target instances.\n1. A matching rule in a `.jsonschema-lint` file, in the instance directory or its parents (see below).\n1. If the `--schema-store` flag is provided, then matching rules from [Schema Store](https://www.schemastore.org/json/) will be used.\n\n\n#### `.jsonschema-lint` files\n\n`.jsonschema-lint` files follow similar logic to `.gitignore` and [Github `CODEOWNERS` files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), in that they apply to all files under their directory tree.\n\nEach line in a `.jsonschema-lint` file is a rule, matching a filepath pattern to a particular schema. For example:\n\n```\n**/.circleci/config.yml  https://json.schemastore.org/circleciconfig.json  yaml\n```\n\nThere are three parts to each rule, separated by whitespace. These are:\n\n- the pattern/glob, in this case matching any files named `config.yml` in a directory named `.circleci`\n- the location of the schema. This can be a remote URL, or a path on the local filesystem. If this is a relative path, it is resolved relative to the `.jsonschema-lint` file.\n- (optional) the expected file format of any instances. If this is omitted, the linter will attempt to detect the correct type from the file extension. If it cannot be detected, both will be attempted.\n\n\n## Development\n\nInstall dependencies:\n\n```shell\npyenv shell 3.9.4  # Or other 3.9.x\npre-commit install  # Configure commit hooks\npoetry install  # Install Python dependencies\n```\n\nRun tests:\n\n```shell\npoetry run inv verify\n```\n\n# License\n\nThis project is distributed under the MIT license.\n\n\n[PyYAML]: https://pypi.org/project/PyYAML/\n',
    'author': 'Jack Smith',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jacksmith15/jsonschema-lint',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
