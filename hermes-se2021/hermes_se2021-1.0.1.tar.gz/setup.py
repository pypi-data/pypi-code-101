# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hermes']

package_data = \
{'': ['*']}

install_requires = \
['fastapi', 'matplotlib', 'numpy', 'pandas', 'scikit-learn', 'uvicorn']

setup_kwargs = {
    'name': 'hermes-se2021',
    'version': '1.0.1',
    'description': 'A small tool for data collection and processing for SE2021 HSE SPb course',
    'long_description': '# Hermes\n\n## Project description\n\nThis project\'s implementation is a part of SE course in Higher School of Economics. \n\nHermes is a platform for collecting data from hospitals and clinics and using this data for training ML models. \n\nProject presentation is available [here](https://docs.google.com/presentation/d/1H6xPu8CtyLfUVIbjr5ZoOuYPqUBmz5ivMpN5mHBR6Hw/edit?usp=sharing)\n\nThe project is currently in an initial state.\n\n## Instructions\n\n### Install\n\n`pip install hermes-se2021`\n\n### Build from source\n\n```bash\ngit clone git@github.com:MariaChizhova/SE_2021.git\ncd SE_2021\n\npython3 -m pip install poetry\npoetry install\n```\n\n#### Install from source\n```bash\npoetry build\npython3 -m pip install "$(find dist -name "*.whl" -print -quit)"\n```\n\n### Usage\n\n#### Run web application:\n\n```bash\npoetry run uvicorn hermes.endpoints:app --reload\n```\n\n#### Using as a library\n```python\nimport hermes\nimport hermes.stroke_regressor\n```\n\n### Tests\n\n```\npoetry run ./tests.sh all\n```\n\n## Roadmap\n\nThe roadmap of the project is available [here](https://github.com/MariaChizhova/SE_2021/projects/3)\n\n## CHANGELOG\n\nThe changelog of the project is available [here](https://github.com/MariaChizhova/SE_2021/blob/hw_04/CHANGELOG.md)\n\n## Acknowledgements\n\nThanks to our teachers (Vladislav Tankov, Timofey Bryksin) for created this task!\n\n## Contributors\n\nMaria Chizhova: @MariaChizhova\n\nAnna Potryasaeva: @annapotr\n\nJura Khudyakov: @23jura23 \n\n## Contributing\n\nPull requests are welcome!\n\n### Additional instructions\n\n#### Develop in venv with all dependencies:\n\nAfter executing `poetry install`:\n\n- Use `poetry shell` to launch a shell with all dependencies\n- For usage with PyCharm one can use virtual environment from `~/.cache/pypoetry/virtualenvs` \n\n#### Deploying to PyPi repository\n\n```bash\npoetry publish\n```\n\n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n\n',
    'author': 'Jura Khudyakov',
    'author_email': 'catchitoo@mail.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MariaChizhova/SE_2021',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
