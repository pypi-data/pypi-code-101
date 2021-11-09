# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pynames',
 'pynames.generators',
 'pynames.generators.iron_kingdoms',
 'pynames.tests']

package_data = \
{'': ['*'],
 'pynames.generators': ['fixtures/*'],
 'pynames.generators.iron_kingdoms': ['fixtures/*'],
 'pynames.tests': ['fixtures/*']}

install_requires = \
['unicodecsv>=0.14,<0.15']

setup_kwargs = {
    'name': 'pynames',
    'version': '0.2.4',
    'description': 'Name generation library.',
    'long_description': '==================================\nPYNAMES — names generation library\n==================================\n\nPynames intended for generation of all sorts of names. Currently it implements generators for character names of different races and cultures:\n\n* Scandinavian: traditional names;\n* Russian: pagan names;\n* Mongolian: traditional names;\n* Korean: traditional names;\n* Elven: DnD names;\n* Elven: Warhammer names;\n* Goblins: custom names;\n* Orcs: custom names;\n* Iron Kingdoms: caspian midlunder sulese;\n* Iron Kingdoms: dwarf;\n* Iron Kingdoms: gobber;\n* Iron Kingdoms: iossan nyss;\n* Iron Kingdoms: khadoran;\n* Iron Kingdoms: ogrun;\n* Iron Kingdoms: ryn;\n* Iron Kingdoms: thurian morridane;\n* Iron Kingdoms: tordoran;\n* Iron Kingdoms: trollkin.\n\nThere are two supported languages : English & Russian. Russian language names are generated with forms for every case of a noun and time.\n\nCurrently implemented two generation algorithms:\n\n* ``pynames.from_list_generator`` — names are created from list of predefined words;\n* ``pynames.from_table_generator`` — names are created using templates, every part of template is gotten from separate table;\n\nThe library is easily extensible. If you need extra functionality (including new languages), please, contact me, post an issue, or just make a pull request.\n\n*************\nInstallation\n*************\n\n::\n\n   pip install pynames\n\n*************\nUsage\n*************\n\n.. code:: python\n\n   from pynames import GENDER, LANGUAGE\n\nAll generators are divided by "races", so that all generators of elven names are placed in the module ``pynames.generators.elven``, etc.\n\n.. code:: python\n\n   from pynames.generators.elven import DnDNamesGenerator\n   elven_generator = DnDNamesGenerator()\n\nNumber of different names (male and female) and for each gender separately.\n\n.. code:: python\n\n   In [4]: elven_generator.get_names_number()\n   Out[4]: 1952949936\n\n   In [5]: elven_generator.get_names_number(GENDER.MALE)\n   Out[5]: 976474968\n\n   In [6]: elven_generator.get_names_number(GENDER.FEMALE)\n   Out[6]: 976474968\n\nFast random name generation.\n\n.. code:: python\n\n   In [7]: elven_generator.get_name_simple()\n   Out[7]: u\'Elineer\'\n\n   In [8]: elven_generator.get_name_simple(GENDER.MALE)\n   Out[8]: u\'Caslithdar\'\n\n   In [9]: elven_generator.get_name_simple(GENDER.MALE, LANGUAGE.EN) # English\n   Out[9]: u\'Mararon\'\n\n   In [10]: print elven_generator.get_name_simple(GENDER.MALE, LANGUAGE.RU)  # Russian\n   Ттомусиэл\n\nInstead of text, you can get the Name object with additional functionality.\n\n.. code:: python\n\n   In [11]: name = elven_generator.get_name()\n\n   In [12]: name.translations  # all translations\n   Out[12]:\n   {u\'m\': {u\'en\': u"ae\'Angaithnyn",\n           u\'ru\': [u"\\u0430\\u044d\'\\u0410\\u043d\\u0433\\u0430\\u0438\\u0442\\u0442\\u043d\\u0438\\u0438\\u043d",\n                   u"\\u0430\\u044d\'\\u0410\\u043d\\u0433\\u0430\\u0438\\u0442\\u0442\\u043d\\u0438\\u0438\\u043d\\u0430",\n                   u"\\u0430\\u044d\'\\u0410\\u043d\\u0433\\u0430\\u0438\\u0442\\u0442\\u043d\\u0438\\u0438\\u043d\\u0443",\n                   u"\\u0430\\u044d\'\\u0410\\u043d\\u0433\\u0430\\u0438\\u0442\\u0442\\u043d\\u0438\\u0438\\u043d\\u0430",\n                   u"\\u0430\\u044d\'\\u0410\\u043d\\u0433\\u0430\\u0438\\u0442\\u0442\\u043d\\u0438\\u0438\\u043d\\u043e\\u043c",\n                   u"\\u0430\\u044d\'\\u0410\\u043d\\u0433\\u0430\\u0438\\u0442\\u0442\\u043d\\u0438\\u0438\\u043d\\u0435",\n                   u"\\u0430\\u044d\'\\u0410\\u043d\\u0433\\u0430\\u0438\\u0442\\u0442\\u043d\\u0438\\u0438\\u043d\\u044b",\n                   u"\\u0430\\u044d\'\\u0410\\u043d\\u0433\\u0430\\u0438\\u0442\\u0442\\u043d\\u0438\\u0438\\u043d\\u043e\\u0432",\n                   u"\\u0430\\u044d\'\\u0410\\u043d\\u0433\\u0430\\u0438\\u0442\\u0442\\u043d\\u0438\\u0438\\u043d\\u0430\\u043c",\n                   u"\\u0430\\u044d\'\\u0410\\u043d\\u0433\\u0430\\u0438\\u0442\\u0442\\u043d\\u0438\\u0438\\u043d\\u043e\\u0432",\n                   u"\\u0430\\u044d\'\\u0410\\u043d\\u0433\\u0430\\u0438\\u0442\\u0442\\u043d\\u0438\\u0438\\u043d\\u0430\\u043c\\u0438",\n                   u"\\u0430\\u044d\'\\u0410\\u043d\\u0433\\u0430\\u0438\\u0442\\u0442\\u043d\\u0438\\u0438\\u043d\\u0430\\u0445"]}}\n\n   In [13]: print u\'\\n\'.join(name.get_forms_for(GENDER.MALE, language=LANGUAGE.RU))\n   аэ\'Ангаиттниин\n   аэ\'Ангаиттниина\n   аэ\'Ангаиттниину\n   аэ\'Ангаиттниина\n   аэ\'Ангаиттниином\n   аэ\'Ангаиттниине\n   аэ\'Ангаиттниины\n   аэ\'Ангаиттниинов\n   аэ\'Ангаиттниинам\n   аэ\'Ангаиттниинов\n   аэ\'Ангаиттниинами\n   аэ\'Ангаиттниинах\n\n   In [14]: name.genders\n   Out[14]: frozenset({u\'m\'}) # all genders\n',
    'author': 'Aliaksei Yaletski (Tiendil)',
    'author_email': 'a.eletsky@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Tiendil/pynames',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
