# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_release']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2.0a2,<2.0.0']

entry_points = \
{'poetry.application.plugin': ['poetry-release = '
                               'poetry_release.plugin:ReleasePlugin']}

setup_kwargs = {
    'name': 'poetry-release',
    'version': '0.3.0',
    'description': 'Plugin for release management in projects based on Poetry',
    'long_description': '# Poetry release\n\n[![CI]][workflow]\n[![PyPi Package]][pypi.org]\n[![Downloads]][pepy.tech]\n\n[CI]: https://github.com/topenkoff/poetry-release/actions/workflows/tests.yml/badge.svg\n[workflow]: https://github.com/topenkoff/poetry-release/actions?query=workflow\n[PyPi Package]: https://img.shields.io/pypi/v/poetry-release?color=%2334D058&label=pypi%20package\n[pypi.org]: https://pypi.org/project/poetry-release/\n[Downloads]: https://pepy.tech/badge/poetry-release\n[pepy.tech]: https://pepy.tech/project/poetry-release\n\nRelease managment plugin for [poetry](https://github.com/python-poetry/poetry)\n\n*The project is currently under development and is not ready for use in production.*\n\nInspired by [cargo-release](https://github.com/sunng87/cargo-release)\n\n## Features\n- [x] [Semver](https://semver.org/) support\n- [x] Creating git tag and commits after release\n- [x] [Changelog](https://keepachangelog.com/en/1.0.0/) support\n\n## Installation\n**Note:** Plugins work at Poetry with version 1.2.0a2 or above.\n```bash\npoetry add poetry-release\n```\n\n## Usage\n```bash\npoetry release <level>\n```\nExisting levels\n - major\n - minor\n - patch\n - release (default)\n - rc\n - beta\n - alpha\n\n### Prerequisite\nYour project should be managed by git.\n\n## Config\n### Replacements\nPoetry-release supports two types of release replacements:\n1. By Regex\nYou can create replacements in files using regular expressions:\n```toml\nrelease-replacements = [\n    { file="CHANGELOG.md", pattern="\\\\[Unreleased\\\\]", replace="[{version}] - {date}" },\n]\n```\n2. Message replacements\n\nYou can set the text for release messages:\n| Replacement                   | Description                                      |\n|-------------------------------|--------------------------------------------------|\n| `release-commit-message`      | Message for release commit                       |\n| `post-release-commit-message` | Message for post release commit(if it\'s allowed) |\n| `tag-name`                    | The name of tag                                  |\n| `tag-message`                 | The message for tag                              |\n\n### Templates\nPoetry-release supports templates to build releases. Templates could be used in release replacements/messages/tags. Template is indicated like `some text {package_name}`\n| Template       | Description                                        |\n|----------------|----------------------------------------------------|\n| `package_name` | The name of this project in `pyproject.toml`       |\n| `prev_version` | The project version before release                 |\n| `version`      | The bumped project version                         |\n| `next_version` | The version for next development iteration (alpha) |\n| `date`         | The current date in `%Y-%m-%d` format              |\n\n### Release settings\nThese settings allow you to disable part of the functionality. They can be set either in `pyproject.toml` or in CLI like flag. Settings from CLI have a higher priority\n| Settings       | Default |        CLI         |     `pyproject.toml`     | Description                     |\n|----------------|---------|--------------------|--------------------------|---------------------------------|\n| `disable-push` | false   | :heavy_check_mark: | :heavy_check_mark:       | Don\'t do git push               |\n| `disable-tag`  | false   | :heavy_check_mark: | :heavy_check_mark:       | Don\'t do git tag                |\n| `disable-dev`  | false   | :heavy_check_mark: | :heavy_check_mark:       | Skip bump version after release |\n| `sign-commit`  | false   | :heavy_check_mark: | :heavy_multiplication_x: | Signed commit                   |\n| `sign-tag`     | false   | :heavy_check_mark: | :heavy_multiplication_x: | Signed tag                      |\n\n#### Default git messages\n* Tag name - `{version}`\n* Tag message - `Released {package_name} {version}`\n* Release commit - `Released {package_name} {version}`\n* Post release commit - `Starting {package_name}\'s next development iteration {next_version}`\n\n### Example\n```toml\n[tool.poetry-release]\nrelease-replacements = [\n    { file="CHANGELOG.md", pattern="\\\\[Unreleased\\\\]", replace="[{version}] - {date}" },\n    { file="CHANGELOG.md", pattern="\\\\(https://semver.org/spec/v2.0.0.html\\\\).", replace="(https://semver.org/spec/v20.0.html).\\n\\n## [Unreleased]"},\n]\ndisable-push = false\ndisable-tag = false\ndisable-dev = false\nrelease-commit-message = "Release {package_name} {version}"\npost-release-commit-message = "Start next development iteration {next_version}"\ntag-name = "{version}"\n```\n\n```bash\npoetry release minor --disable-dev --disable-tag\n```\n',
    'author': 'Denis Kayshev',
    'author_email': 'topenkoff@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/topenkoff/poetry-release',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
