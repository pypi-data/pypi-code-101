# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['numpy_html']

package_data = \
{'': ['*']}

install_requires = \
['numpy']

setup_kwargs = {
    'name': 'numpy-html',
    'version': '1.0.0',
    'description': 'A simple table renderer for numpy arrays. Provides a rich display hook for use with Jupyter Lab / Notebook.',
    'long_description': '# numpy-html\n[![pypi-badge][]][pypi] \n\n[pypi-badge]: https://img.shields.io/pypi/v/numpy-html\n[pypi]: https://pypi.org/project/numpy-html\n\nA simple table renderer for numpy arrays. Provides a rich display hook for use with Jupyter Lab / Notebook. Inspired by [xtensor](https://github.com/QuantStack/xtensor).\n\n## Installation\n`pip install numpy-html`\n\n## Example inside Jupyter\n```python\n%load_ext numpy_html\nimport numpy as np\n\nnp.set_printoptions(threshold=5, edgeitems=2)\nnp.arange(49).reshape(7, 7)\n```\n|  0 \t|  1 \t| ⋯ \t|  5 \t|  6 \t|\n|:--:\t|:--:\t|:-:\t|:--:\t|:--:\t|\n|  7 \t|  8 \t| ⋯ \t| 12 \t| 13 \t|\n|  ⋮ \t|  ⋮ \t| ⋱ \t|  ⋮ \t|  ⋮ \t|\n| 35 \t| 36 \t| ⋯ \t| 40 \t| 41 \t|\n| 42 \t| 43 \t| ⋯ \t| 47 \t| 48 \t|\n',
    'author': 'Angus Hollands',
    'author_email': 'goosey15@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
