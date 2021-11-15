# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['esteid',
 'esteid.authentication',
 'esteid.authentication.tests',
 'esteid.flowtest',
 'esteid.flowtest.tests',
 'esteid.idcard',
 'esteid.idcard.tests',
 'esteid.mobileid',
 'esteid.mobileid.tests',
 'esteid.signing',
 'esteid.signing.tests',
 'esteid.smartid',
 'esteid.smartid.tests']

package_data = \
{'': ['*'],
 'esteid': ['locale/en/LC_MESSAGES/*',
            'locale/et/LC_MESSAGES/*',
            'locale/lt/LC_MESSAGES/*',
            'locale/ru/LC_MESSAGES/*',
            'static/esteid-new/*',
            'static/esteid-test/*',
            'static/images/esteid/*',
            'templates/esteid/*'],
 'esteid.idcard': ['templates/*']}

install_requires = \
['Django>=1.11,!=2.1.0,!=2.1.1',
 'attrs>=19.2.0',
 'esteid-certificates>=1.0.0,<1.1.0',
 'pyasice>=1.0.1,<1.1.0',
 'requests>=2.20']

setup_kwargs = {
    'name': 'django-esteid',
    'version': '3.2rc1',
    'description': 'Django-esteid is a package that provides Esteid based authentication for your Django applications.',
    'long_description': '# django-esteid\n\n[![pypi Status](https://badge.fury.io/py/django-esteid.png)](https://badge.fury.io/py/django-esteid)\n[![Build Status](https://travis-ci.org/thorgate/django-esteid.svg?branch=master)](https://travis-ci.org/thorgate/django-esteid)\n[![Coverage Status](https://coveralls.io/repos/github/thorgate/django-esteid/badge.svg?branch=master)](https://coveralls.io/github/thorgate/django-esteid?branch=master)\n\nDjango-esteid is a package that provides Esteid based authentication and signing for your Django applications.\n\n## Quickstart\n\nInstall `django-esteid`:\n\n    pip install django-esteid\n\nAdd `esteid` to installed apps:\n\n    INSTALLED_APPS = [\n        # ...\n        \'esteid\',\n        # ...\n    ]\n\nPlease refer to the more detailed guides on [signing](esteid/signing) and [authentication](esteid/authentication).    \n\nBe sure to read the [testing](#testing) section below.\n\nStatic files such as the services\' logos and helper JS are also shipped with this library. \n\n### SmartID\n\nDetailed docs are [here](esteid/smartid/README.md).\n\n### MobileID\n\nDetailed docs are [here](esteid/mobileid/README.md).\n\n### ID Card\n\nDetailed docs are [here](esteid/idcard/README.md).\n\n### Service settings\n\nYou can \n\n### Context processors\n\n`esteid.context_processors.esteid_services` adds service enabled/demo statuses to the template context.\nThis way you can easily manage the necessary services displayed on the auth/signing page.\n\n## Testing\n\nFor a guide to authentication testing, please refer to [the authentication readme](./esteid/authentication/README.md).\n\nThere is a possibility to test the signing flow with ID card, SmartID \nand Mobile ID (the demo services) with the test views coming with the library.\n\n**NOTE:** you may not be able to use the live Esteid services even with live credentials.\nThe live services keep an IP address whitelist \nwhich only contains IP addresses as specified in customer\'s contract.\n\nTo run the django-esteid test server with the test views, \n* install the virtual environment if not installed yet,\n* run `./manage.py migrate` to create the SQLite DB for sessions,\n* run `./manage.py runserver 8765`, where 8765 is a port of your liking\n\nthen visit the URL http://localhost:8765/ and follow the instructions on that page.\n\n### Mobile ID\n\nTo test Mobile ID signing, you will need [test phone numbers and ID codes](https://github.com/SK-EID/MID/wiki/Test-number-for-automated-testing-in-DEMO).\n\nYou can not use real phone numbers or ID codes with the demo service.\n\n### SmartID\n\nTo test signing with SmartID, yoy can use [the test ID codes](https://github.com/SK-EID/smart-id-documentation/wiki/Environment-technical-parameters).\n \nYou can also register a demo SmartID account and use a demo SmartID app to enter the PINs; please visit the\n[demo SmartID portal](https://sid.demo.sk.ee/portal/login) for the details. \n\n### ID card\n\nID card signing requires SSL to work, even in a testing environment.  \nNote that the signature will not be valid neither with the real certificates, nor with the test ones. \n\nTo perform signing with ID card, you would need the `chrome-token-signing` browser plugin installed.\n`apt-get install chrome-token-signing`\n\n#### Testing with ssl\n\nYou can run an HTTPS webserver with `./manage.py runsslserver 127.0.0.1:8765`. It will use a development certificate\ncoming with the `djangosslserver` package. \n\nNote that the cert is self-signed, so you will need to create a security exception in browser.\n\nIf you need to create your own cert using openssl:\n```\nopenssl req -x509 -out localhost.crt -keyout localhost.key \\\n  -newkey rsa:2048 -nodes -sha256 \\\n  -subj \'/CN=localhost\' -extensions EXT -config <( \\\n   printf "[dn]\\nCN=localhost\\n[req]\\ndistinguished_name=dn\\n[EXT]\\nsubjectAltName=DNS:localhost\\nkeyUsage=digitalSignature\\nextendedKeyUsage=serverAuth")\n```\nThen start the HTTPS webserver as follows: \n\n`python manage.py runsslserver 127.0.0.1:8765 --certificate localhost.crt --key localhost.key`\n\nA security exception is also necessary as marked above.\n\n#### ngrok\nIf you don\'t want to use a self-signed cert you can route the test site through HTTPS with [ngrok](https://ngrok.com/). \n\nWith `ngrok` installed, and the `./manage.py runserver 8765` started, run\n`ngrok http http://127.0.0.1:8765` and it will create a tunnel with an HTTPS URL for your local site.\n\n### Verify demo containers with digidoc-tool\n\nIt\'s possible to use the command line utility `digidoc-tool` \nfrom the [libdigidocpp library](https://github.com/open-eid/libdigidocpp/)\nto verify containers with signatures created by demo services:\n```\ndigidoc-tool open --tslurl=https://open-eid.github.io/test-TL/tl-mp-test-EE.xml --tslcert=trusted-test-tsl.crt <file>\n```\nInstructions on setting up the environment \n[can be found here](https://github.com/open-eid/libdigidocpp/wiki/Using-test-TSL-lists#digidoc-toolexe-utility-program).\n',
    'author': 'Thorgate',
    'author_email': 'info@thorgate.eu',
    'maintainer': 'Jyrno Ader',
    'maintainer_email': 'jyrno42@gmail.com',
    'url': 'https://github.com/thorgate/django-esteid',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
