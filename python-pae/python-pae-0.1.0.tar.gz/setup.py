# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_pae']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'python-pae',
    'version': '0.1.0',
    'description': 'Pre-authentication encoding (PAE) implementation in Python',
    'long_description': ".. image:: https://github.com/MatthiasValvekens/python-pae/workflows/pytest/badge.svg\n    :target: https://github.com/MatthiasValvekens/python-pae\n    :alt: pytest status\n\n.. image:: https://codecov.io/gh/MatthiasValvekens/python-pae/branch/master/graph/badge.svg?token=XPRS49L0X6\n    :target: https://codecov.io/gh/MatthiasValvekens/python-pae\n    :alt: Coverage status\n\n.. image:: https://readthedocs.org/projects/python-pae/badge/?version=latest\n   :target: https://python-pae.readthedocs.io/en/latest/?badge=latest\n   :alt: Documentation Status\n\n\nPre-authentication encoding in Python\n=====================================\n\nThis minimal library offers an implementation of (a variant of)\n`PASETO <https://github.com/paragonie/paseto>`_'s pre-authentication encoding\n(PAE) scheme in Python, with some extra tools to handle data types other than lists of byte arrays.\n\n\nWhy use pre-authentication encoding?\n------------------------------------\n\nWhen passing around data between services, it's often necessary to authenticate and validate\nencoded messages. When those messages are flat byte streams, that's easy enough. However,\nwhen authenticating complex data structures with many fields (some of which may be optional or\nperhaps exempt from authentication), the input data must first be serialised before it can\nbe passed on to the authentication mechanism.\nThe interchange formats that are commonly used to hold such complex data in transit between web\nservices (e.g. JSON or HTTP query parameters) are poorly suited for this task.\n\nNaively concatenating all inputs before authentication is typically not a good idea, since\nit can lead to vulnerabilities through\n`length extension attacks <https://en.wikipedia.org/wiki/Length_extension_attack>`_\nor other types of `canonicalisation attacks <https://soatok.blog/2021/07/30/canonicalization-attacks-against-macs-and-signatures/>`_.\n\nPre-authentication encoding (PAE) can help you protect yourself against a large class of such\nexploits, by explicitly making the *number* of data fields and the *length* of each field part of\nthe data covered by the MAC/signature.\n\nPAE can be used explicitly or implicitly. In the explicit case, PAE serves as both the interchange\nformat and the authentication format.\nIn the implicit case, PAE is used to preprocess data in some other container format before\nsigning/authenticating it, but its output isn't transmitted directly.\n\nA typical use case would be a ``signature`` entry in a JSON object that authenticates one or more\nof its sibling entries. The signature value would then be computed by applying PAE to the\nauthenticated sibling entries, and passing the result to the signature algorithm.\n\n\nRequirements\n------------\n\nRequires Python 3.7 or later.\n\n\nNotes\n-----\n\nThis library has no runtime dependencies, and does not supply any cryptographic operations.\nIts main purpose is to preprocess complex data structures before authenticating their contents\nusing a MAC or digital signature. The actual authentication mechanism is out of scope, and left\nto the caller.\nThis library also does not offer any abstractions to handle token expiration, revocation,\nalgorithm selection or anything of the sort.\n\n\nStability\n---------\n\nExperimental.\n\n\nLinks\n-----\n\n - `Homepage <https://github.com/MatthiasValvekens/python-pae>`_\n - `Documentation <https://python-pae.readthedocs.io/en/latest/index.html>`_\n - `PyPI <https://pypi.org/project/python-pae/>`_\n",
    'author': 'Matthias Valvekens',
    'author_email': 'dev@mvalvekens.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MatthiasValvekens/python-pae',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
