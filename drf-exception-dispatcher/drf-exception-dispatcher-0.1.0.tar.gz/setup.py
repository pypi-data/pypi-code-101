# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exception_dispatcher', 'exception_dispatcher.dispatchers']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'drf-exception-dispatcher',
    'version': '0.1.0',
    'description': 'django-rest-framework exception handler build with functools.singledispatch',
    'long_description': '# Django REST framework exception dispatcher\n\n[`django-rest-framework`](https://github.com/encode/django-rest-framework)\n[exception handler](https://www.django-rest-framework.org/api-guide/exceptions/#custom-exception-handling)\nbuild with\n[`funtools.singledispatch`](https://docs.python.org/3/library/functools.html#functools.singledispatch).\n\n## Installation\n\nTo use `drf-exception-dispatcher` simply install it with your package manager,\ne.g. to with `pip`:\n\n```bash\npip install drf-exception-dispatcher\n```\n\nThen simply use `exception_dispatcher.handlers.exception_handler` (\nor your own exception handler built on `exception_dispatcher`) in Django\'s\nsettings `REST_FRAMEWORK` section:\n\n```python\nREST_FRAMEWORK = {\n  # ...\n  \'EXCEPTION_HANDLER\': \'exception_dispatcher.handlers.exception_handler\',\n  # ...\n}\n```\n\n### Configuration\n\nFollowing settings are present to make default `exception_dispatcher` handler\nconfigurable:\n\n+ `EXCEPTION_DISPATCHER_SET_ROLLBACK` (defaults to `True`) - indicate if\n  [`set_rollback`](https://github.com/encode/django-rest-framework/blob/71e6c30034a1dd35a39ca74f86c371713e762c79/rest_framework/views.py#L65)\n  should be called before returning response from exception handler\n+ `EXCEPTION_DISPATCHER_API_EXCEPTION_PARSER` (defaults to\n  `exception_dispatcher.parsers.parse_rest_framework_api_exception\'`) - import\n  path to callable that is used to translate occurred `exception` to response\n  data\n\n## Usage\n\nTo add new handlers to `exception_dispatchers` simply use dispatcher\'s\n`register()` method, e.g. to add handler of `SuspiciousOperation` exceptions:\n\n```python\nfrom exception_dispatcher.dispatchers import exception_dispatcher\nfrom exception_dispatcher.types import ContextType\nfrom rest_framework.response import Response\n\n\n@exception_dispatcher.register\ndef handler_suspicious_operation(\n    exception: SuspiciousOperation,\n    context: ContextType,\n) -> Response | None:\n    """Handle Django\'s `SuspiciousOperation` exceptions."""\n    # custom ``exception` handler logic goes here\n    return None\n```\n',
    'author': 'Łukasz Skarżyński',
    'author_email': 'me@skarzi.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/skarzi/drf-exception-dispatcher',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
