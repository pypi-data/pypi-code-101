# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ochre']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ochre',
    'version': '0.1.0',
    'description': 'A tiny Python package for working with colors in a pragmatic way',
    'long_description': '[![Python package](https://github.com/getcuia/ochre/actions/workflows/python-package.yml/badge.svg)](https://github.com/getcuia/ochre/actions/workflows/python-package.yml)\n\n# ochre 🏜️\n\n<img src="banner.jpg" alt="ochre" style="width:500px; height:500px; object-fit: fill; border-radius: 100%;" />\n\n> A down-to-earth approach to colors\n\nochre is a tiny Python package for working with colors in a pragmatic way. The\nfocus is on simplicity and ease of use, but also on human perception.\n\n## Features\n\n-   🎨 Focus on [RGB](https://en.wikipedia.org/wiki/RGB_color_model) and\n    [HCL](https://en.wikipedia.org/wiki/HCL_color_space) color spaces\n-   🖥️ Web color names\n-   ♻️ Color conversions that easily integrate with the\n    [standard `colorsys` module](https://docs.python.org/3/library/colorsys.html)\n-   🗑️ Zero dependencies\n-   🐍 Python 3.8+\n\n## Credits\n\n[Photo](banner.jpg) by\n[Nicola Carter](https://unsplash.com/@ncarterwilts?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)\non\n[Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).\n',
    'author': 'Felipe S. S. Schneider',
    'author_email': 'schneider.felipe@posgrad.ufsc.br',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/getcuia/ochre',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
