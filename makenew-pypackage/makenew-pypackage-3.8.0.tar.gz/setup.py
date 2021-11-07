# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['makenew_pypackage']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'makenew-pypackage',
    'version': '3.8.0',
    'description': 'Package skeleton for a Python module.',
    'long_description': 'Python Package Skeleton\n=======================\n\n|PyPI| |GitHub Actions|\n\n.. |PyPI| image:: https://img.shields.io/pypi/v/makenew-pypackage.svg\n   :target: https://pypi.python.org/pypi/makenew-pypackage\n   :alt: PyPI\n.. |GitHub Actions| image:: https://github.com/makenew/pypackage/workflows/main/badge.svg\n   :target: https://github.com/makenew/pypackage/actions\n   :alt: GitHub Actions\n\nPackage skeleton for a Python module.\n\nDescription\n-----------\n\nBootstrap a new Python_ package in less than a minute.\n\n.. _Python: https://www.python.org/\n\nFeatures\n~~~~~~~~\n\n- Publishing to PyPI_.\n- Secure dependency management with Poetry_.\n- Linting with Pylint_.\n- Uncompromising code formatting with Black_.\n- pytest_ helps you write better programs.\n- Code coverage reporting with Codecov_.\n- Continuous testing and deployment with `GitHub Actions`_.\n- `Keep a CHANGELOG`_.\n- Consistent coding with EditorConfig_.\n- Badges from Shields.io_.\n\n.. _Black: https://black.readthedocs.io/en/stable/\n.. _Codecov: https://codecov.io/\n.. _EditorConfig: https://editorconfig.org/\n.. _GitHub Actions: https://github.com/features/actions\n.. _Keep a CHANGELOG: https://keepachangelog.com/\n.. _PyPI: https://pypi.python.org/pypi\n.. _Pylint: https://www.pylint.org/\n.. _Shields.io: https://shields.io/\n.. _pytest: https://docs.pytest.org/\n\nBootstrapping a New Project\n~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n1. Create an empty (**non-initialized**) repository on GitHub.\n2. Clone the master branch of this repository with\n\n   ::\n\n       $ git clone --single-branch https://github.com/makenew/pypackage.git new-pypackage\n       $ cd new-pypackage\n\n   Optionally, reset to the latest\n   `release <https://github.com/makenew/pypackage/releases>`__ with\n\n   ::\n\n       $ git reset --hard v1.2.0\n\n3. Run\n\n   ::\n\n       $ ./makenew.sh\n\n   This will replace the boilerplate, delete itself,\n   remove the git remote, remove upstream tags,\n   and stage changes for commit.\n\n4. Create the required GitHub repository secrets\n5. Review, commit, and push the changes to GitHub with\n\n   ::\n\n     $ git diff --cached\n     $ git commit -m "Replace makenew boilerplate"\n     $ git remote add origin git@github.com:<user>/<new-pypackage>.git\n     $ git push -u origin master\n\n6. Ensure the GitHub action passes,\n   then publish the initial version of the package with\n\n   ::\n\n     $ poetry install\n     $ poetry run bump2version patch\n     $ git push\n     $ git push --tags\n\nUpdating\n~~~~~~~~\n\nIf you want to pull in future updates from this skeleton,\nyou can fetch and merge in changes from this repository.\n\nAdd this as a new remote with\n\n::\n\n    $ git remote rename origin upstream\n\nand then configure your ``origin`` branch as normal.\n\nOtherwise, add this as a new remote with\n\n::\n\n    $ git remote add upstream git@github.com:makenew/pypackage.git\n\nYou can then fetch and merge changes with\n\n::\n\n    $ git fetch --no-tags upstream\n    $ git merge upstream/master\n\nChangelog\n^^^^^^^^^\n\nNote that ``CHANGELOG.md`` is just a template for this skeleton. The\nactual changes for this project are documented in the commit history and\nsummarized under\n`Releases <https://github.com/makenew/pypackage/releases>`__.\n\nInstallation\n------------\n\nThis package is registered on the `Python Package Index (PyPI)`_\nas makenew_pypackage_.\n\nInstall it with\n\n::\n\n    $ poetry add makenew_pypackage\n\n.. _makenew_pypackage: https://pypi.python.org/pypi/makenew-pypackage\n.. _Python Package Index (PyPI): https://pypi.python.org/\n\nDevelopment and Testing\n-----------------------\n\nQuickstart\n~~~~~~~~~~\n\n::\n\n    $ git clone https://github.com/makenew/pypackage.git\n    $ cd pypackage\n    $ poetry install\n\nRun each command below in a separate terminal window:\n\n::\n\n    $ make watch\n\nPrimary development tasks are defined in the `Makefile`.\n\nSource Code\n~~~~~~~~~~~\n\nThe `source code`_ is hosted on GitHub.\nClone the project with\n\n::\n\n    $ git clone https://github.com/makenew/pypackage.git\n\n.. _source code: https://github.com/makenew/pypackage\n\nRequirements\n~~~~~~~~~~~~\n\nYou will need `Python 3`_ and Poetry_.\n\nInstall the development dependencies with\n\n::\n\n    $ poetry install\n\n.. _Poetry: https://poetry.eustace.io/\n.. _Python 3: https://www.python.org/\n\nTests\n~~~~~\n\nLint code with\n\n::\n\n    $ make lint\n\n\nRun tests with\n\n::\n\n    $ make test\n\nRun tests on chages with\n\n::\n\n    $ make watch\n\nPublishing\n~~~~~~~~~~\n\nUse the bump2version_ command to release a new version.\nPush the created git tag which will trigger a GitHub action.\n\n.. _bump2version: https://github.com/c4urself/bump2version\n\nPublishing may be triggered using on the web\nusing a `workflow_dispatch on GitHub Actions`_.\n\n.. _workflow_dispatch on GitHub Actions: https://github.com/makenew/pypackage/actions?query=workflow%3Aversion\n\nGitHub Actions\n--------------\n\n*GitHub Actions should already be configured: this section is for reference only.*\n\nThe following repository secrets must be set on GitHub Actions.\n\n- ``PYPI_API_TOKEN``: API token for publishing on PyPI.\n\nThese must be set manually.\n\nSecrets for Optional GitHub Actions\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nThe version and format GitHub actions\nrequire a user with write access to the repository\nincluding access to read and write packages.\nSet these additional secrets to enable the action:\n\n- ``GH_USER``: The GitHub user\'s username.\n- ``GH_TOKEN``: A personal access token for the user.\n- ``GIT_USER_NAME``: The name to set for Git commits.\n- ``GIT_USER_EMAIL``: The email to set for Git commits.\n- ``GPG_PRIVATE_KEY``: The `GPG private key`_.\n- ``GPG_PASSPHRASE``: The GPG key passphrase.\n\n.. _GPG private key: https://github.com/marketplace/actions/import-gpg#prerequisites\n\nContributing\n------------\n\nPlease submit and comment on bug reports and feature requests.\n\nTo submit a patch:\n\n1. Fork it (https://github.com/makenew/pypackage/fork).\n2. Create your feature branch (`git checkout -b my-new-feature`).\n3. Make changes.\n4. Commit your changes (`git commit -am \'Add some feature\'`).\n5. Push to the branch (`git push origin my-new-feature`).\n6. Create a new Pull Request.\n\nLicense\n-------\n\nThis Python package is licensed under the MIT license.\n\nWarranty\n--------\n\nThis software is provided by the copyright holders and contributors "as is" and\nany express or implied warranties, including, but not limited to, the implied\nwarranties of merchantability and fitness for a particular purpose are\ndisclaimed. In no event shall the copyright holder or contributors be liable for\nany direct, indirect, incidental, special, exemplary, or consequential damages\n(including, but not limited to, procurement of substitute goods or services;\nloss of use, data, or profits; or business interruption) however caused and on\nany theory of liability, whether in contract, strict liability, or tort\n(including negligence or otherwise) arising in any way out of the use of this\nsoftware, even if advised of the possibility of such damage.\n',
    'author': 'Evan Sosenko',
    'author_email': 'razorx@evansosenko.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/makenew/pypackage',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10.0,<3.11.0',
}


setup(**setup_kwargs)
