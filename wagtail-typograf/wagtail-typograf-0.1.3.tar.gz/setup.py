# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wagtail_typograf']

package_data = \
{'': ['*'], 'wagtail_typograf': ['static/wagtail_typograf/js/*']}

install_requires = \
['typus>=0.2.2,<0.3.0']

setup_kwargs = {
    'name': 'wagtail-typograf',
    'version': '0.1.3',
    'description': 'Brings russian typography to Wagtail rich text editor based on draftail',
    'long_description': 'wagtail-typograf\n----------------\n\nA plugin to add `typus <https://github.com/byashimov/typus>`_ functionality to wagtail rich text editor (draftail).\n\nDemo\n====\n\n.. image:: https://raw.githubusercontent.com/truetug/wagtail-typograf/master/demo.gif\n    :width: 400\n    :alt: Demo\n\nInstallation\n============\n\nInstall with pip \n\n::\n\n    pip install wagtail-typograf\n\nAdd app name to your list of installed apps\n  \n::\n\n    INSTALLED_APPS = [\n        ...\n        "wagtail_typograf",\n    ]\n    \n\nAdd typograf url to your urlpatterns (for now "/api/typograf/" is strongly hardcoded in js)\n\n::\n\n    urlpatterns = [\n      ...\n      path(\'api/\', include(\'wagtail_typograf.urls\')),\n      ...\n    ]\n\n\nIf you use limit number of features in RichTextBlock, don\'t forget to add ``typograf`` to its list\n\n::\n    \n    text_block = RichTextBlock(\n        features=[\n            "bold", "italic", "ol", "ul", "hr", \n            "link", "document-link", "typograf",\n        ],\n        ...\n    )\n\nUsage\n=====\n\nWrite or paste text content, push the ¶-button.\n',
    'author': 'Sergey Trofimov',
    'author_email': 'truetug@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/truetug/wagtail-typograf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.3,<4.0',
}


setup(**setup_kwargs)
