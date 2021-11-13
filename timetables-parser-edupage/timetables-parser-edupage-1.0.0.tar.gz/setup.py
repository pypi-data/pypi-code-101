# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['edupage', 'edupage.api', 'edupage.api.model']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp[speedups]>=3.8.0,<4.0.0',
 'beautifulsoup4>=4.10.0,<5.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'timetables-lib>=1.0.0,<2.0.0']

entry_points = \
{'console_scripts': ['edupage = timetables.parser.edupage.cli:main',
                     'edupage-check = timetables.parser.edupage.cli:check',
                     'edupage-join = timetables.parser.edupage.cli:join',
                     'edupage-login = timetables.parser.edupage.cli:login',
                     'edupage-parse = timetables.parser.edupage.cli:parse',
                     'edupage-register = '
                     'timetables.parser.edupage.cli:register']}

setup_kwargs = {
    'name': 'timetables-parser-edupage',
    'version': '1.0.0',
    'description': 'Edupage.org timetable parser library',
    'long_description': '# Edupage.org timetable parser library\n\nThis library provides access to public timetables provided by Edupage.\nThe resulting dataset is compatible with and based on [timetables-lib](https://github.com/szkolny-eu/timetables-lib).\n\n## Usage examples\n\n### Simple login\n```python\nasync with EdupageApi() as api:\n    # login with Edupage Portal (account for multiple schools)\n    portal: Portal = await api.login(login="email@example.com", password="PortalPassword")\n    # OR\n    # login with a single-school Edupage account (i.e. https://example.edupage.com)\n    session: Session = await api.login(login="user12345", password="EdupageUser123", edupage="example")\n    # OR\n    # login using a previously stored session (Portal login not possible here)\n    session: Session = await api.login(**old_session.dict())\n\n# list sessions joined to a Portal account\nprint(portal.sessions)\n# get the first session (school)\nsession = portal.sessions[0]\n```\n**Note:** it is recommended to save sessions (portal.dict() or session.dict()) for future API calls.\nThe sessions expire after some (unknown to me) time, a `SessionExpiredError` is raised in that case.\n\n### Parse timetables\n```python\nasync with EdupageParser(session) as parser:\n    # enqueue parsing all data (this is required)\n    # - try_v1_teachers - whether to use the old API to get some teachers\' full names\n    # - try_v1_full_teachers - whether to use the old API to get all teachers\' full names\n    #   ^ this option requires to download and extract a large, zipped JSON payload, so keep this in mind\n    parser.enqueue_all(try_v1_teachers=False, try_v1_full_teachers=True)\n\n    # print the current queue, out of curiosity\n    print("\\n".join(str(s) for s in parser.ds.files))\n\n    # run all enqueued tasks, get a Dataset\n    # this typically performs up to two HTTP requests\n    ds = await parser.run_all()\n    \n    # sort lessons, because why not\n    lessons = sorted(ds.lessons, key=lambda x: (x.weekday, x.number))\n    # print lessons for a specific class\n    print("\\n".join(str(s) for s in lessons if s.register_.name == "1A"))\n```\n\n### Check if Edupage exists\n```python\nasync with EdupageApi() as api:\n    exists = await api.v1.check_edupage("edupagename")\n```\n\n### Join a portal account to another Edupage\n```python\nasync with EdupageApi() as api:\n    # join a new Edupage to a portal account\n    # (effectively creating a guest account on that Edupage)\n    account = await api.v2.join_account(portal, "edupagename")\n    print(repr(account))\n    # get a session for the just-created account\n    session = await api.login(**account.dict())\n```\n\n### Create a Portal account interactively\n```python\nasync with EdupageApi() as api:\n    await api.register_interactive()\n```\n\n## Command-line scripts\n\nAvailable after installing the package (if scripts directory is in your `PATH`, or you\'re using a virtualenv). \n```shell\n$ edupage check guests\nEdupage \'guests\' exists.\n$ edupage register\nEnter e-mail address: ...\n$ edupage login email@example.com PortalPassword\nPortal(user_id=12345, user_email=\'email@example.com\', sessions=[])\nSessions saved to edupage.json\n$ edupage join edupagename\nLogged in as \'email@example.com\'\nNew account:\nAccount(...)\nRe-login to use the session\n$ edupage parse othername --register 1A\nParsing \'edupage://othername/get/...\'\nLesson(...)\nLesson(...)\n...\n```\n\n',
    'author': 'Kuba Szczodrzyński',
    'author_email': 'kuba@szczodrzynski.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
