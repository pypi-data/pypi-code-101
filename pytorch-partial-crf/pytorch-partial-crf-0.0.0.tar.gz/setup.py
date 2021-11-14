# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytorch_partial_crf']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=6.2.5,<7.0.0', 'torch>=1.10.0,<2.0.0']

setup_kwargs = {
    'name': 'pytorch-partial-crf',
    'version': '0.0.0',
    'description': '',
    'long_description': '# pytorch-partial-crf\n\nPartial/Fuzzy conditional random field in PyTorch.\n\nDocument: https://pytorch-partial-crf.readthedocs.io/\n\n# How to use\n\n## Install\n\n```sh\npip install pytorch-partial-crf\n```\n\n### Use CRF\n\n```python\nimport torch\nfrom pytorch_partial_crf import CRF\n\n# Create \nnum_tags = 6\nmodel = CRF(num_tags)\n\nbatch_size, sequence_length = 3, 5\nemissions = torch.randn(batch_size, sequence_length, num_tags)\n\ntags = torch.LongTensor([\n    [1, 2, 3, 3, 5],\n    [1, 3, 4, 2, 1],\n    [1, 0, 2, 4, 4],\n])\n\n# Computing negative log likelihood\nmodel(emissions, tags)\n```\n\n### Use partial CRF\n\n```python\nimport torch\nfrom pytorch_partial_crf import PartialCRF\n\n# Create \nnum_tags = 6\nmodel = PartialCRF(num_tags)\n\nbatch_size, sequence_length = 3, 5\nemissions = torch.randn(batch_size, sequence_length, num_tags)\n\n# Set unknown tag to -1\ntags = torch.LongTensor([\n    [1, 2, 3, 3, 5],\n    [-1, 3, 3, 2, -1],\n    [-1, 0, -1, -1, 4],\n])\n\n# Computing negative log likelihood\nmodel(emissions, tags)\n```\n\n\n### Use Marginal CRF\n\n```python\nimport torch\nfrom pytorch_partial_crf import MarginalCRF\n\n# Create \nnum_tags = 6\nmodel = MarginalCRF(num_tags)\n\nbatch_size, sequence_length = 3, 5\nemissions = torch.randn(batch_size, sequence_length, num_tags)\n\n# Set probability tags\nmarginal_tags = torch.Tensor([\n        [\n            [0.2, 0.2, 0.2, 0.1, 0.1, 0.2],\n            [0.8, 0.0, 0.0, 0.1, 0.1, 0.0],\n            [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],\n            [0.3, 0.0, 0.0, 0.1, 0.6, 0.0],\n        ],\n        [\n            [0.2, 0.2, 0.2, 0.1, 0.1, 0.2],\n            [0.8, 0.0, 0.0, 0.1, 0.1, 0.0],\n            [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],\n            [0.3, 0.0, 0.0, 0.1, 0.6, 0.0],\n        ],\n        [\n            [0.2, 0.2, 0.2, 0.1, 0.1, 0.2],\n            [0.8, 0.0, 0.0, 0.1, 0.1, 0.0],\n            [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],\n            [0.3, 0.0, 0.0, 0.1, 0.6, 0.0],\n        ],\n])\n# Computing negative log likelihood\nmodel(emissions, marginal_tags)\n```\n\n### Decoding\n\nViterbi decode\n\n```\nmodel.viterbi_decode(emissions)\n```\n\nRestricted viterbi decode\n\n```python\npossible_tags = torch.randn(batch_size, sequence_length, num_tags)\npossible_tags[possible_tags <= 0] = 0 # `0` express that can not pass.\npossible_tags[possible_tags > 0] = 1  # `1` express that can pass.\npossible_tags = possible_tags.byte()\nmodel.restricted_viterbi_decode(emissions, possible_tags)\n```\n\nMarginal probabilities\n\n```python\nmodel.marginal_probabilities(emissions)\n```\n\n### Contributing\n\nWe welcome contributions! Please post your requests and comments on Issue.\n\n\n### License\n\nMIT\n\n### References\n\nThe implementation is based on AllenNLP CRF module and pytorch-crf.\n',
    'author': 'Koga Kobayashi',
    'author_email': 'kajyuuen@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kajyuuen/pytorch-partial-crf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
