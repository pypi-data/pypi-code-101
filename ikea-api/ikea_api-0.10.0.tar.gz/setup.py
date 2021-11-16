# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ikea_api', 'ikea_api._endpoints']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.26.0,<3.0.0']

extras_require = \
{':python_version < "3.9"': ['typing-extensions==4.0.0'],
 'test': ['pytest>=6.2.5,<7.0.0',
          'pytest-cov>=3.0.0,<4.0.0',
          'pytest-randomly>=3.10.2,<4.0.0',
          'responses>=0.16.0,<0.17.0']}

setup_kwargs = {
    'name': 'ikea-api',
    'version': '0.10.0',
    'description': "Client for several IKEA's APIs",
    'long_description': 'Client for several IKEA APIs.\n\n[![Test](https://github.com/vrslev/ikea-api-client/actions/workflows/test.yml/badge.svg)](https://github.com/vrslev/ikea-api-client/actions/workflows/test.yml)\n[![Version](https://img.shields.io/github/v/release/vrslev/ikea-api-client?label=Version)](https://github.com/vrslev/ikea-api-client/releases/latest)\n[![Python](https://img.shields.io/pypi/pyversions/ikea_api?label=Python)](https://pypi.org/project/ikea_api)\n[![Downloads](https://img.shields.io/pypi/dm/ikea_api?label=Downloads)](https://pypi.org/project/ikea_api)\n[![License](https://img.shields.io/pypi/l/ikea_api?label=License)](https://github.com/vrslev/ikea-api-client/blob/main/LICENSE)\n\n# Features\n\n- Manage Cart,\n- Check available Delivery Services,\n- Retrieve Purchases History and information about specific order,\n- Get Product information.\n\n# Installation\n\n```bash\npip install ikea_api\n```\n\n# Usage\n\n```python\nfrom ikea_api import IkeaApi\n\nikea = IkeaApi(\n    token=None,\n    country_code="us",\n    language_code="en",\n)\n```\n\nExamples below don\'t show everything you can do, but this package is almost fully typed and quite small. So, better browse code or use autocompletion in your IDE 😄\n\n## Endpoints\n\n### 🔑 Authorization\n\n#### [As Guest](https://github.com/vrslev/ikea-api-client/blob/main/src/ikea_api/_endpoints/auth.py)\n\nFirst time you open IKEA.com, guest token is being generated and stored in cookies. It expires in 30 days.\n\n```python\nikea.login_as_guest()\n```\n\n#### As Registered User\n\nYou can\'t do this automatically with this package. IKEA made it nearly impossible to get authorized token. Copy-paste token from ikea.com cookies.\n\n### [🛒 Cart](https://github.com/vrslev/ikea-api-client/blob/main/src/ikea_api/_endpoints/cart.py)\n\nThis API endpoint allows you to do everything you would be able to do on the site, and even more:\n\n- Add, delete and update items,\n- Set or delete Coupon,\n- Show it,\n- Clear it,\n- And even copy another user\'s cart.\n\nAuthorization as user is optional. All changes apply to the _real_ cart if you\'re logged in. **Use case:** programmatically add items to cart and order it manually on IKEA.com.\n\nSimple example:\n\n```python\nikea.Cart.add_items({"30457903": 1})  # { item_code: quantity }\nprint(ikea.Cart.show())\n```\n\n### [🚛 Order Capture](https://github.com/vrslev/ikea-api-client/blob/main/src/ikea_api/_endpoints/order_capture.py)\n\nCheck Pickup or Delivery availability.\n\n```python\nikea.OrderCapture(\n    zip_code="02215",\n    state_code="MA",  # pass state code only if you\'re in USA\n)\n```\n\nIf you need to know whether items are available in stores, check out [ikea-availability-checker](https://github.com/Ephigenia/ikea-availability-checker).\n\n### 📦 Purchases\n\n#### [Order History](https://github.com/vrslev/ikea-api-client/blob/main/src/ikea_api/_endpoints/purchases.py#L32)\n\n```python\nikea.Purchases.history()\n```\n\n#### [Order Info](https://github.com/vrslev/ikea-api-client/blob/main/src/ikea_api/_endpoints/purchases.py#L39)\n\n```python\nikea.Purchases.order_info(order_number=...)\n\n# Or use it without authorization, email is required\nikea.Purchases.order_info(order_number=..., email=...)\n```\n\n### 🪑 Item Information\n\nGet information about Item by item number.\n\nThere are many ways because information about some items is not available in some endpoints.\n\n```python\nitem_codes = ("30457903",)\n\nitems = ikea.fetch_items_specs.iows(item_codes)\n\n# or\nitems = ikea.fetch_items_specs.ingka(item_codes)\n\n# or\nitem_codes_dict = {"30457903": False}  # { item_code: is_combination }\nitems = ikea.fetch_items_specs.pip(item_codes_dict)\n```\n\n### [🔎 Search](https://github.com/vrslev/ikea-api-client/blob/main/src/ikea_api/_endpoints/search.py)\n\nSearch for products in the IKEA product catalog by product name. Optionally also specify a maximum amount of returned search results (defaults to 24).\n\n```python\nsearch_results = ikea.Search("Billy")  # Retrieves (at most) 24 search results\n\n# or\nsearch_results = ikea.Search("Billy", 10)  # Retrieves (at most) 10 search results\n```\n',
    'author': 'Lev Vereshchagin',
    'author_email': 'mail@vrslev.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vrslev/ikea-api-client',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
