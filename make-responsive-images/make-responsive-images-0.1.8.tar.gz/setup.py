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
    'version': '0.1.8',
    'description': 'Generate responsive images for your website, so you can use srcset in your <img> tags and serve an optimal image to each device that views your site.',
    'long_description': '# `make-responsive-images`\n\nGenerate responsive images automatically, for websites to use `srcset` and `sizes` in the `<img>` tags.\n\nThis way you serve an optimal image for each device viewport size.\n\n<p align="center">\n<a href="https://github.com/mccarthysean/make-responsive-images/actions?query=workflow%3ATest" target="_blank">\n    <img src="https://github.com/mccarthysean/make-responsive-images/workflows/Test/badge.svg" alt="Test">\n</a>\n<a href="https://codecov.io/gh/mccarthysean/make-responsive-images" target="_blank">\n    <img src="https://img.shields.io/codecov/c/github/mccarthysean/make-responsive-images?color=%2334D058" alt="Coverage">\n</a>\n<a href="https://github.com/mccarthysean/make-responsive-images/actions?query=workflow%3Apypi" target="_blank">\n    <img src="https://github.com/mccarthysean/make-responsive-images/workflows/Upload%20Package%20to%20PyPI/badge.svg" alt="Publish">\n</a>\n<a href="https://pypi.org/project/make-responsive-images" target="_blank">\n    <img src="https://img.shields.io/pypi/v/make-responsive-images?color=%2334D058&label=pypi%20package" alt="Package version">\n</a>\n<a href="https://pypi.org/project/make-responsive-images/" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/make-responsive-images.svg" alt="Python Versions">\n</a>\n</p>\n\n## Installation\n\n[Install from PyPI](https://pypi.org/project/make-responsive-images/)\n\n```bash\npip install make-responsive-images\n```\n\n## Usage\n\n```bash\nresize [OPTIONS] COMMAND [ARGS]...\n```\n\n### Options\n\n* `-v, --version`: Show the application\'s version and exit.\n* `--help`: Show this message and exit.\n\n## Commands\n\n* `image`: Resize one image\n\n### Usage\n\n```bash\nresize image [OPTIONS] [IMAGE]\n```\n\n### Arguments\n\n* `[IMAGE]`: [default: /workspace/tests/fixtures/xfer-original.jpg]\n\n### Options\n\n* `--widths TEXT`: Widths of new images, in pixels  [default: 600,1000,1400]\n* `--html / --no-html`: Generate HTML <img> tag  [default: True]\n* `--classes TEXT`: Classnames to add to the <img> tag (e.g. class="img-fluid")\n* `--img-sizes TEXT`: Sizes for the <img> tag (e.g. sizes="100vw")  [default: 100vw]\n* `--lazy / --no-lazy`: Adds loading="lazy" to <img> tag for SEO  [default: False]\n* `--alt TEXT`: Adds alt="" to the <img> tag (e.g. alt="Funny image")  [default: ]\n* `--dir TEXT`: Images directory to prepend to the src (e.g. src="<dir>/<image>")\n* `--fmt TEXT`: Image type to save as ("jpg" and "webp" supported)  [default: webp]\n* `--qual INTEGER`: Compression to apply (i.e. 0=max, 100=min)  [default: 100]\n* `--help`: Show this message and exit.\n\n## Author Info\n\nSean McCarthy is Chief Data Scientist at [IJACK Technologies Inc](https://myijack.com), a leading manufacturer of fully-automated pumps to green the oil and gas industry.\n\n<br>\n<a href="https://mccarthysean.dev">\n    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/mccarthysean.svg?sanitize=1" alt="Sean McCarthy\'s blog">\n</a>\n<a href="https://www.linkedin.com/in/seanmccarthy2/">\n    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/linkedin.svg?sanitize=1" alt="LinkedIn">\n</a>\n<a href="https://github.com/mccarthysean">\n    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/github.svg?sanitize=1" alt="GitHub">\n</a>\n<a href="https://twitter.com/mccarthysean">\n    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/twitter.svg?sanitize=1" alt="Twitter">\n</a>\n<a href="https://www.facebook.com/sean.mccarth">\n    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/facebook.svg?sanitize=1" alt="Facebook">\n</a>\n<a href="https://medium.com/@mccarthysean">\n    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/medium.svg?sanitize=1" alt="Medium">\n</a>\n<a href="https://www.instagram.com/mccarthysean/">\n    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/instagram.svg?sanitize=1" alt="Instagram">\n</a>\n',
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
