# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pullapprove',
 'pullapprove.availability',
 'pullapprove.cli',
 'pullapprove.config',
 'pullapprove.context',
 'pullapprove.models',
 'pullapprove.models.base',
 'pullapprove.models.bitbucket',
 'pullapprove.models.github',
 'pullapprove.models.gitlab',
 'pullapprove.user_input']

package_data = \
{'': ['*']}

install_requires = \
['CacheControl[filecache]>=0.12.6,<0.13.0',
 'Jinja2>=3.0.1,<4.0.0',
 'PyJWT>=2.1.0,<3.0.0',
 'PyYAML>=5.4.1,<6.0.0',
 'Pygments>=2.10.0,<3.0.0',
 'appdirs>=1.4.4,<2.0.0',
 'cached-property>=1.5.2,<2.0.0',
 'click>=8.0.1,<9.0.0',
 'cls-client>=1.4.0,<2.0.0',
 'cryptography>=3.4.7,<4.0.0',
 'dateparser>=1.0.0,<2.0.0',
 'keyring>=23.2.1,<24.0.0',
 'marshmallow>=3.12.1,<4.0.0',
 'prompt-toolkit>=3.0.20,<4.0.0',
 'python-box>=5.3.0,<6.0.0',
 'requests>=2.25.1,<3.0.0',
 'wcmatch==8.2']

entry_points = \
{'console_scripts': ['pullapprove = pullapprove.cli:cli']}

setup_kwargs = {
    'name': 'pullapprove',
    'version': '3.16.1',
    'description': 'PullApprove is a framework for code review assignment, processes, and policies that integrates natively with your git host.',
    'long_description': '<a href="https://www.pullapprove.com/"><img src="https://www.pullapprove.com/static/img/logos/pull-approve-logo-gray-dk.png" alt="PullApprove" height="40px" /></a>\n---\n\nPullApprove is a framework for code review assignment and policies.\nIt integrates directly with GitHub, GitLab (beta), and Bitbucket (beta).\n\nIt is configured with a `.pullapprove.yml` file at the root of your repo.\nReviews are split into "review groups" which can be enabled/disabled depending on the specifics of a PR.\nWhen a group is activated on a PR, review requests are sent out automatically to the selected reviewers.\n\nHere\'s a basic example:\n\n```yaml\nversion: 3\n\noverrides:\n- if: "base.ref != \'master\'"\n  status: success\n  explanation: "Review not required unless merging to master"\n- if: "\'hotfix\' in labels"\n  status: success\n  explanation: "Review skipped for hotfix"\n\ngroups:\n  code:\n    reviewers:\n      users:\n      - reviewerA\n      - reviewerB\n    reviews:\n      required: 2\n      request: 1\n      request_order: random\n    labels:\n      approved: "Code review approved"\n\n  database:\n    conditions:\n    - "\'*migrations*\' in files"\n    reviewers:\n      teams:\n      - database\n```\n\nA "pullapprove" status is reported on the PR with a link to more details.\nYou can make this a [required status check](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule#creating-a-branch-protection-rule) to enforce your review workflows on all pull requests.\n\n![pullapprove review status check](https://user-images.githubusercontent.com/649496/141190794-c62da3f0-92fb-4125-ae7e-410b1ec8dc89.png)\n\n---\n\nThis repo contains some of the core models and configuration settings which are used by the [hosted service](https://www.pullapprove.com/).\n\nTo host your own version of PullApprove, please contact us at https://www.pullapprove.com/enterprise/.\n',
    'author': 'Dropseed',
    'author_email': 'python@dropseed.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://www.pullapprove.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
