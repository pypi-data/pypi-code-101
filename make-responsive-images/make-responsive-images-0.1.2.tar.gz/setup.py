# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['make_responsive_images']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.4.0,<9.0.0',
 'colorama>=0.4.4,<0.5.0',
 'shellingham>=1.4.0,<2.0.0',
 'typer==0.3.2']

entry_points = \
{'console_scripts': ['resize = make_responsive_images.main:app']}

setup_kwargs = {
    'name': 'make-responsive-images',
    'version': '0.1.2',
    'description': 'Generate responsive images for your website, so you can use srcset in your <img> tags and serve an optimal image to each device that views your site.',
    'long_description': '# `make-responsive-images`\n\nGenerate responsive images automatically, for websites to use `srcset` in the `<img>` tags.\n\nThis way you serve an optimal image for each device viewport size.\n\n<p align="center">\n<a href="https://github.com/mccarthysean/make-responsive-images/actions?query=workflow%3ATest" target="_blank">\n    <img src="https://github.com/mccarthysean/make-responsive-images/workflows/Test/badge.svg" alt="Test">\n</a>\n<a href="https://github.com/mccarthysean/make-responsive-images/actions?query=workflow%3APublish" target="_blank">\n    <img src="https://github.com/mccarthysean/make-responsive-images/workflows/Publish/badge.svg" alt="Publish">\n</a>\n<a href="https://codecov.io/gh/mccarthysean/make-responsive-images" target="_blank">\n    <img src="https://img.shields.io/codecov/c/github/mccarthysean/make-responsive-images?color=%2334D058" alt="Coverage">\n</a>\n<a href="https://pypi.org/project/make-responsive-images" target="_blank">\n    <img src="https://img.shields.io/pypi/v/make-responsive-images?color=%2334D058&label=pypi%20package" alt="Package version">\n</a>\n<a href="https://pypi.org/project/make-responsive-images/" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/make-responsive-images.svg" alt="Python Versions">\n</a>\n</p>\n\n## Usage\n\n```bash\nresize [OPTIONS] COMMAND [ARGS]...\n```\n\n## Options\n\n* `-v, --version`: Show the application\'s version and exit.\n* `--help`: Show this message and exit.\n\n## Commands\n\n* `image`: Resize one image\n\n## Usage\n\n```bash\nresize image [OPTIONS] [IMAGE]\n```\n\n## Arguments\n\n* `[IMAGE]`: [default: /workspace/tests/fixtures/xfer-original.jpg]\n\n**Options**:\n\n* `--widths TEXT`: [default: 600,1000,1400]\n* `--help`: Show this message and exit.\n',
    'author': 'Sean McCarthy',
    'author_email': 'sean.mccarthy@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://mccarthysean.dev/make-responsive-images',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
