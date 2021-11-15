# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['esp-stubs', 'esp32-stubs', 'uuid-stubs']

package_data = \
{'': ['*'], 'esp-stubs': ['sub_pkg/*']}

modules = \
['upip', 'machine']
setup_kwargs = {
    'name': 'esp32-test-stubs',
    'version': '0.1.2',
    'description': 'Sample project for PEP-561 distribution testing',
    'long_description': 'esp32-test-stubs\n================\n\nSample project for test [PEP-561][1]\n\nNotice: It is only "proof-of-concept" of [PEP-561][1] package so **not for production use**, \npackage can be deleted in the future. \n\n## Installation\n\n```shell \npip3 install esp32-test-stubs\n```\n\n## Script\n\n```python\nimport machine\nmachine.freq()\n\nimport esp32\nesp32.NVS()\nesp32.wake_on_ext0("Test")\n\nfrom esp.sub_pkg import sub_pkg_fun\nsub_pkg_fun()\n\nfrom esp32.sub_pkg import sub_pkg_function\nsub_pkg_function()\n\nimport uuid\n\n# Points to stdlib\nuuid.uuid4()\n\n# Points to stub (mean partial stub, so extent stdlib)\n# see uuid-stubs and py.typed\nuuid.uuid6()\n\nimport upip\nupip.cleanup()\n```\n\n## Stubs possible locations\n\n- project root `*.pyi` files\n- `<package>-stubs` with `__init__.pyi` see [PEP-561](https://www.python.org/dev/peps/pep-0561)\n- `<package>-stubs/<sub_package>.pyi` see [stub-only-packages](https://www.python.org/dev/peps/pep-0561/#stub-only-packages)\n- custom folder like `src`, marked as `package = [{ include = "*.pyi" , from = "src"}]`,\n  under hood all `*.pyi` will be moved into package root during package build.  \n  CONS: **Not recommended** as custom folder does not recognize as stub source before stub package will pack properly. \n  Also in `*.tar.gz` stubs not moved properly, so it led to potential errors during stub recognition   \n\nNote all of these variants should be explicitly marked in `pyproject.toml` in `Poetry` see `package` section\n\n## Poetry commands\n\n- Prepare\n  ```shell \n  poetry config repositories.testpypi https://test.pypi.org/legacy/\n  poetry config pypi-token.testpypi <TOKEN>\n\n  poetry config repositories.pypi https://upload.pypi.org/legacy/\n  poetry config pypi-token.pypi <TOKEN>\n  ```\n\n- Publish\n  ```shell \n  poetry publish --build -r testpypi\n  poetry publish --build -r pypi\n  ```\n\n## Links\n\n- [PEP-561](https://www.python.org/dev/peps/pep-0561)\n- [Real world stubs example (Numpy)](https://github.com/numpy/numpy-stubs)\n- [Poetry project examples](https://github.com/python-poetry/poetry/tree/master/tests/masonry/builders/fixtures/pep_561_stub_only)\n\n#### Footnotes\n[1]: https://www.python.org/dev/peps/pep-0561\n',
    'author': 'mrkeuz',
    'author_email': 'mrkeuz@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mrkeuz/esp32-test-stubs',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
