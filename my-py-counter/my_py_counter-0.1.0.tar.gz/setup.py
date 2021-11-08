# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['my_py_counter']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4.3,<4.0.0']

setup_kwargs = {
    'name': 'my-py-counter',
    'version': '0.1.0',
    'description': 'A python package to count number of words in a file',
    'long_description': '# my_py_counter\n\nA python package to count number of words in a file\n\n## Installation\n\n```bash\n$ pip install my_py_counter\n```\n\n## Usage\n\n`my_py_counter` can be used to count words in a text file and plot the results as follows:\n\n```python\nfrom my_py_counter.my_py_counter import count_words\nfrom my_py_counter.plotting import plot_words\nimport matplotlib.pyplot as plt\n\nfile_path = "test.txt" # path to your file\ncounts = count_words(file_path)\nfig = plot_words(counts, n=10)\nplt.show()\n```\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`my_py_counter` was created by Kazeem Omoloja. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`my_py_counter` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Kazeem Omoloja',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
