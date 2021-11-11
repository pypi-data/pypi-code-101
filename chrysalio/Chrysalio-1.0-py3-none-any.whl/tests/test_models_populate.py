# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``models.populate`` functions."""

from os.path import exists, join, dirname
from collections import OrderedDict
from cgi import FieldStorage
from datetime import datetime
from json import dumps

from lxml import etree

from pyramid.response import Response, FileResponse

from . import DBUnitTestCase
from ..lib.xml import relaxng4validation
# pylint: disable = unused-import
from ..includes.modules.models import DBModule  # noqa
from ..modules.cioskeleton.models.dbbone import DBBone  # noqa
# pylint: enable = unused-import


# =============================================================================
class UModelsPopulateXml2Db(DBUnitTestCase):
    """Unit test class for :func:`models.populate.xml2db`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:models.populate.xml2db]"""
        from . import TEST_INI
        from ..relaxng import RELAXNG
        from ..lib.xml import load_xml
        from ..modules import Module
        from ..models.dbprofile import DBProfile
        from ..models.dbuser import DBUser
        from ..models.populate import xml2db

        dbsession = self.request.dbsession
        data = (
            '<chrysalio version="1.0">'
            '<profiles>'
            '  <profile id="user_creator">'
            '    <label xml:lang="en">User manager</label>'
            '    <principals>'
            '      <principal>user.creator</principal>'
            '    </principals>'
            '  </profile>'
            '</profiles>'
            '<users>'
            '  <user>'
            '    <login>test1</login>'
            '    <password>test1pwd</password>'
            '    <firstname>Édith</firstname>'
            '    <lastname>AVULEUR</lastname>'
            '    <email>test1@chrysal.io</email>'
            '    <profiles>'
            '      <profile>user_creator</profile>'
            '    </profiles>'
            '  </user>'
            '</users>'
            '<groups>'
            '  <group id="team">'
            '    <label xml:lang="en">Team 1</label>'
            '    <users>'
            '      <user>test1</user>'
            '    </users>'
            '  </group>'
            '</groups>'
            '</chrysalio>')
        tree = load_xml(
            'chrysalio.xml', relaxng4validation(RELAXNG),
            data=bytes(data.encode('utf8')))

        errors = xml2db(
            dbsession, tree, modules=OrderedDict(
                [('chrysalio.modules.foo', Module(TEST_INI))]))
        self.assertEqual(len(errors), 0)
        dbprofile = dbsession.query(DBProfile).filter_by(
            profile_id='user_creator').first()
        self.assertIsInstance(dbprofile, DBProfile)
        user = dbsession.query(DBUser).filter_by(login='test1').first()
        self.assertIsInstance(user, DBUser)
        self.assertEqual(len(user.profiles), 1)
        self.assertEqual(len(user.groups), 1)


# =============================================================================
class UModelsPopulateElement2Db(DBUnitTestCase):
    """Unit test class for :func:`models.populate.element2db`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:models.populate.element2db]"""
        from ..lib.i18n import translate
        from ..models.dbuser import DBUser
        from ..models.populate import element2db

        class DummyDBBone(object):
            """Dummy class for bones."""
            @classmethod
            def xml2db(cls, dbsession, product_elt, error_if_exists=True,
                       kwargs=None):
                """Dummy loading of a product from a XML element."""

        dbsession = self.request.dbsession
        tree = etree.ElementTree(etree.XML(
            '<chrysalio version="1.0">'
            '  <user>'
            '    <login>test1</login>'
            '    <password>test1pwd</password>'
            '    <firstname>Édith</firstname>'
            '    <lastname>AVULEUR</lastname>'
            '    <email>test1@chrysal.io</email>'
            '  </user>'
            '</chrysalio>'))

        # only='profile'
        element = {'tag': 'user', 'class': DBUser}
        self.assertEqual(
            len(element2db(dbsession, tree, 'profile', True, element)), 0)

        # Normal loading
        errors = element2db(dbsession, tree, None, True, element)
        self.assertEqual(len(errors), 1)
        self.assertFalse(errors[0])

        # Module loading
        tree = etree.ElementTree(etree.XML(
            '<chrysalio version="1.0">'
            '  <modules>'
            '    <module id="chrysalio.modules.cioskeleton" active="true">'
            '      <cioskeleton xmlns="http://ns.chrysal.io/cioskeleton"'
            '          version="1.0">'
            '        <bones>'
            '          <bone id="hand">'
            '            <label>Hand</label>'
            '          </bone>'
            '        </bones>'
            '      </cioskeleton>'
            '      <cioskeleton xmlns="http://ns.chrysal.io/cioskeleton"'
            '          version="1.0">'
            '        <bones>'
            '          <bone id="foot">'
            '            <label>Foot</label>'
            '            <foo/>'
            '          </bone>'
            '        </bones>'
            '      </cioskeleton>'
            '    </module>'
            '  </modules>'
            '</chrysalio>'))
        element['relaxng'] = {
            'namespace': 'http://ns.chrysal.io/cioskeleton',
            'root': 'cioskeleton', 'version': '1.0',
            'file': join(
                dirname(__file__), '..', 'modules', 'cioskeleton', 'RelaxNG',
                'cioskeleton.rng')}
        element['tag'] = 'bone'
        element['class'] = DummyDBBone
        errors = element2db(dbsession, tree, None, True, element)
        self.assertEqual(len(errors), 1)
        self.assertIn('foo', translate(errors[0]))


# =============================================================================
class UModelsPopulateModuleXml2Db(DBUnitTestCase):
    """Unit test class for :func:`models.populate.module_xml2db`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:models.populate.module_xml2db]"""
        from . import TEST_INI
        from ..modules.cioskeleton import ModuleCioSkeleton
        from ..models.populate import module_xml2db

        def _xml2db(dbsession, tree, only, error_if_exists):
            """Dummy function to generate error."""
            # pylint: disable = unused-argument
            return ['Error']

        dbsession = self.request.dbsession

        tree = etree.ElementTree(etree.XML(
            '<chrysalio version="1.0">'
            '  <user>'
            '    <login>test1</login>'
            '    <password>test1pwd</password>'
            '    <firstname>Édith</firstname>'
            '    <lastname>AVULEUR</lastname>'
            '    <email>test1@chrysal.io</email>'
            '  </user>'
            '</chrysalio>'))

        # Without module
        self.assertEqual(
            len(module_xml2db(dbsession, tree, None, True, None)), 0)

        # Module loading
        skeleton = ModuleCioSkeleton(TEST_INI)
        tree = etree.ElementTree(etree.XML(
            '<chrysalio version="1.0">'
            '  <module id="chrysalio.modules.cioskeleton">'
            '    <cioskeleton xmlns="http://ns.chrysal.io/cioskeleton"'
            '        version="1.0">'
            '      <bones>'
            '        <bone id="foot"><label>Foot</label></bone>'
            '      </bones>'
            '    </cioskeleton>'
            '  </module>'
            '</chrysalio>'))
        errors = module_xml2db(
            dbsession, tree, None, True,
            OrderedDict([('chrysalio.modules.cioskeleton', skeleton)]))
        self.assertFalse(errors)

        # Error during module loading
        skeleton.xml2db = (_xml2db,)
        errors = module_xml2db(
            dbsession, tree, None, True,
            OrderedDict([('chrysalio.modules.cioskeleton', skeleton)]))
        self.assertTrue(errors)
        self.assertIsNotNone(errors[0])


# =============================================================================
class UModelsPopulateDb2Xml(DBUnitTestCase):
    """Unit test class for func:`models.populate.db2xml`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:models.populate.db2xml]"""
        from . import TEST_INI
        from ..modules import Module
        from ..models.dbprofile import DBProfile
        from ..models.dbuser import DBUser
        from ..models.dbgroup import DBGroup, DBGroupUser
        from ..models.populate import db2xml

        dbsession = self.request.dbsession
        dbsession.add(DBProfile(
            profile_id='user_creator',
            i18n_label=dumps({'en': 'User account manager'})))
        self.add_user({
            'login': 'admin', 'status': 'administrator',
            'last_name': 'Administrator', 'password': 'adminpwd',
            'email': 'admin@chrysal.io'})
        self.add_user({
            'login': 'test1', 'first_name': 'Édith', 'last_name': 'AVULEUR',
            'password': 'test1pwd', 'email': 'test1@chrysal.io'})
        dbuser = dbsession.query(DBUser).filter_by(login='test1').first()
        dbgroup = DBGroup(
            group_id='managers', i18n_label=dumps({'en': 'Managers'}))
        dbgroup.users.append(DBGroupUser(user_id=dbuser.user_id))
        dbsession.add(dbgroup)
        elements = db2xml(
            dbsession,
            modules=OrderedDict([('chrysalio.modules.foo', Module(TEST_INI))]))

        self.assertEqual(len(elements), 3)


# =============================================================================
class UModelsPopulateModuleDb2Xml(DBUnitTestCase):
    """Unit test class for func:`models.populate.module_db2xml`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:models.populate.module_db2xml]"""
        from . import TEST_INI
        from ..modules.cioskeleton import ModuleCioSkeleton
        from ..models.populate import module_db2xml

        dbsession = self.request.dbsession

        self.assertEqual(len(module_db2xml(dbsession, None)), 0)

        skeleton = ModuleCioSkeleton(TEST_INI)
        self.assertEqual(
            len(module_db2xml(
                dbsession, OrderedDict(
                    [('chrysalio.modules.cioskeleton', skeleton)]))), 1)


# =============================================================================
class UModelsPopulateWeb2Db(DBUnitTestCase):
    """Unit test class for func:`models.populate.web2db`."""

    # -------------------------------------------------------------------------
    def test_xml(self):
        """[u:models.populate.web2db] XML"""
        from . import TEST_DIR, TEST_INI, TEST1_USR_XML, TEST3_USR_XML
        from . import DummyPOST
        from ..relaxng import RELAXNG
        from ..models.populate import web2db, xml2db

        self.request.registry.settings['attachments'] = TEST_DIR
        self.request.registry['relaxng'] = RELAXNG
        self.request.POST = DummyPOST()
        web2db(self.request, xml2db)
        self.assertFalse(self.request.session.pop_flash('alert'))

        # Without file
        self.request.POST.multikeys = {'file': ('foo',)}
        web2db(self.request, xml2db)
        self.assertFalse(self.request.session.pop_flash('alert'))

        # Non well formed XML
        with open(TEST1_USR_XML, 'r') as hdl:
            input_file = FieldStorage()
            input_file.filename = TEST1_USR_XML
            input_file.file = hdl
            self.request.POST.multikeys = {'file': (input_file,)}
            web2db(self.request, xml2db)
        self.assertTrue(self.request.session.pop_flash('alert'))

        # Not a XML or ZIP file
        with open(TEST_INI, 'r') as hdl:
            input_file = FieldStorage()
            input_file.filename = TEST_INI
            input_file.file = hdl
            self.request.POST.multikeys = {'file': (input_file,)}
            web2db(self.request, xml2db)
        self.assertTrue(self.request.session.pop_flash('alert'))

        # Valid XML
        with open(TEST3_USR_XML, 'r') as hdl:
            input_file = FieldStorage()
            input_file.filename = TEST3_USR_XML
            input_file.file = hdl
            self.request.POST.multikeys = {'file': (input_file,)}
            web2db(self.request, xml2db)
        self.assertFalse(self.request.session.pop_flash('alert'))

        # Valid but existing XML
        with open(TEST3_USR_XML, 'r') as hdl:
            input_file = FieldStorage()
            self.request.POST.multikeys = {'file': (input_file,)}
            input_file.filename = TEST3_USR_XML
            input_file.file = hdl
            web2db(self.request, xml2db)
        self.assertTrue(self.request.session.pop_flash('alert'))

    # -------------------------------------------------------------------------
    def test_zip(self):
        """[u:models.populate.web2db] ZIP"""
        from . import TEST_DIR, TEST1_USR_ZIP, TEST2_USR_ZIP, TEST3_USR_ZIP
        from . import DummyPOST
        from ..relaxng import RELAXNG
        from ..models.dbuser import DBUser
        from ..models.populate import web2db, xml2db

        self.request.registry.settings['attachments'] = TEST_DIR
        self.request.registry['relaxng'] = RELAXNG
        self.request.POST = DummyPOST()
        web2db(self.request, xml2db)
        self.assertFalse(self.request.session.pop_flash('alert'))

        with open(TEST2_USR_ZIP, 'rb') as hdl:
            input_file = FieldStorage()
            input_file.file = hdl
            input_file.filename = TEST2_USR_ZIP
            self.request.POST.multikeys = {'file': (input_file,)}
            web2db(self.request, xml2db)
        self.assertTrue(self.request.session.pop_flash('alert'))

        with open(TEST3_USR_ZIP, 'rb') as hdl:
            input_file = FieldStorage()
            input_file.file = hdl
            input_file.filename = TEST3_USR_ZIP
            self.request.POST.multikeys = {'file': (input_file,)}
            web2db(self.request, xml2db)
        self.assertTrue(self.request.session.pop_flash('alert'))

        with open(TEST1_USR_ZIP, 'rb') as hdl:
            input_file = FieldStorage()
            input_file.file = hdl
            input_file.filename = TEST1_USR_ZIP
            self.request.POST.multikeys = {'file': (input_file,)}
            web2db(self.request, xml2db)
        self.assertFalse(self.request.session.pop_flash('alert'))
        self.assertTrue(exists(join(
            TEST_DIR, DBUser.attachments_dir, 'User3', 'user3.svg')))


# =============================================================================
class UModelsPopulateDb2Web(DBUnitTestCase):
    """Unit test class for func:`models.populate.db2web`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:models.populate.db2web]"""
        from . import ATTACHMENTS_DIR
        from ..relaxng import RELAXNG
        from ..models.populate import db2web
        from ..models.dbuser import DBUser

        user = DBUser(
            status='active', login='test1', first_name='Édith',
            last_name='AVULEUR', honorific='Mrs', email='test1@chrysal.io',
            account_creation=datetime.now())
        user.set_password('sesame')
        self.request.registry.settings = {'site.uid': 'testchrysalio'}
        self.request.registry['relaxng'] = RELAXNG

        response = db2web(self.request, [user], 'users.usr.xml')
        self.assertIsInstance(response, Response)
        self.assertIn('<login>test1</login>', response.text)
        self.assertIn('<firstname>Édith</firstname>', response.text)
        self.assertIn('<lastname>AVULEUR</lastname>', response.text)
        self.assertIn('<honorific>Mrs</honorific>', response.text)
        self.assertIn('<email>test1@chrysal.io</email>', response.text)

        self.request.registry.settings['attachments'] = ATTACHMENTS_DIR
        response = db2web(self.request, [user], 'users.usr.xml')
        self.assertIsInstance(response, Response)

        user = DBUser(
            status='active', login='test1', first_name='Édith',
            last_name='AVULEUR', honorific='Mrs', email='test1@chrysal.io',
            attachments_key='Test1', picture='test1.svg',
            account_creation=datetime.now())
        user.set_password('sesame')

        response = db2web(self.request, [user], 'users.usr.xml')
        self.assertIsInstance(response, FileResponse)
