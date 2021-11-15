# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netts', 'netts.cli', 'netts.preprocess']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4.3,<4.0.0',
 'networkx>=2.6.2,<3.0.0',
 'nltk>=3.6.2,<4.0.0',
 'numpy>=1.21.2,<2.0.0',
 'pandas>=1.3.2,<2.0.0',
 'pydantic[dotenv]>=1.8.2,<2.0.0',
 'pyopenie>=0.2.0,<0.3.0',
 'requests>=2.26.0,<3.0.0',
 'rtoml>=0.7.0,<0.8.0',
 'stanza>=1.2.3,<2.0.0',
 'tqdm>=4.62.2,<5.0.0',
 'typer[all]>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['netts = netts.cli:app']}

setup_kwargs = {
    'name': 'netts',
    'version': '0.2.0rc1',
    'description': 'Toolbox for constructing NETworks of Transcript Semantics.',
    'long_description': "# netts - NETworks of Transcript Semantics\n\n[![GitHub release](https://img.shields.io/github/v/release/alan-turing-institute/netts?include_prereleases)](https://GitHub.com/alan-turing-institute/netts/releases/)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/netts.svg)](https://pypi.python.org/pypi/netts/)\n[![codecov](https://codecov.io/gh/alan-turing-institute/netts/branch/main/graph/badge.svg?token=58uMq5hbNt)](https://codecov.io/gh/alan-turing-institute/netts)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)\n\nToolbox for constructing semantic speech networks from speech transcripts.\n\n## About\n\nThe algorithms in this toolbox create a semantic speech graph from transcribed speech. Speech transcripts are short paragraphs of largely raw, uncleaned speech-like text. For example:\n\n> 'I see a man in the dark standing against a light post. It seems to be in the middle of the night; I think because the lightbulb is working. On the picture there seems to be like a park and... Or trees but in those trees there are little balls of light reflections as well. I cannot see the… Anything else because it’s very dark. But the man on the picture seems to wear a hat and, and has a jacket on and he seems to have a hoodie on as well. The picture is very, very mysterious, which I like about it, but for me I would like to understand more concept, context of the picture.'\n> -- <cite>Example Transcript</cite>\n\nBelow is the semantic speech graph constructed from this text.\n\n![Semantic speech graph example](docs/docs/img/ExampleGraph_alternative_text_pic_2.png)\n*Figure 1. Semantic Speech Graph. Nodes represents an entity mentioned by the speaker (e.g. I, man, jacket). Edges represent relations between nodes mentioned by the speaker (e.g. see, has on).*\n\n## Getting started\n\nRead the full documentation [here](https://alan-turing-institute.github.io/netts/).\n\n### Where to get it\n\nYou can install the latest release from [PyPi](https://pypi.org/project/netts/)\n\n```bash\npip install netts\n```\n\nor get the latest development version from GitHub (not stable)\n\n```bash\npip install git+https://github.com/alan-turing-institute/netts\n```\n\n### Additional dependencies\n\nNetts requires a few additional dependencies to work which you can download with the netts CLI that was installed by pip\n\n```bash\nnetts install\n```\n\n### Basic usage\n\nThe quickest way to process a transcript is with the CLI.\n\n```bash\nnetts run transcript.txt outputs\n```\n\nwhere `transcript.txt` is a text file containing transcribed speech and `outputs` is the name of a directory to write the outputs to.\n\n## Contributors\n\nNetts was written by [Caroline Nettekoven](https://www.caroline-nettekoven.com) in collaboration with [Sarah Morgan](https://semorgan.org).\n\nNetts was packaged in collaboration with [Oscar Giles](https://www.turing.ac.uk/people/researchers/oscar-giles), [Iain Stenson](https://www.turing.ac.uk/research/research-engineering/meet-the-team) and [Helen Duncan](https://www.turing.ac.uk/people/research-engineering/helen-duncan).\n\n## Citing netts\n\nIf you use netts in your work, please cite this paper:\n> Caroline R. Nettekoven, Kelly Diederen, Oscar Giles, Helen Duncan, Iain Stenson, Julianna Olah, Nigel Collier, Petra Vertes, Tom J. Spencer, Sarah E. Morgan, and Philip McGuire. 2021. “Networks of Transcript Semantics - Netts.”\n",
    'author': 'Caroline Nettekoven',
    'author_email': 'crn29@cam.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/alan-turing-institute/netts',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
