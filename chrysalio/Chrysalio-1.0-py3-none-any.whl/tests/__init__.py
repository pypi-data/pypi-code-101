# pylint: disable = import-outside-toplevel
"""Unit, integration, and functional testing."""

from os import makedirs
from os.path import join, dirname, exists, normpath
from collections import OrderedDict, namedtuple
from shutil import rmtree
from unittest import TestCase

from pkg_resources import register_loader_type, DefaultProvider
from _pytest.assertion.rewrite import AssertionRewritingHook
from transaction import manager
from webtest import TestApp as BaseTestApp

from pyramid.security import Authenticated, Allow
from pyramid.testing import setUp, tearDown, DummyRequest

from ..models.dbuser import DBUser


TEST_INI = join(dirname(__file__), 'test.ini')
TEST1_INI = join(dirname(__file__), 'test1.ini')
TEST2_INI = join(dirname(__file__), 'test2.ini')
TEST3_INI = join(dirname(__file__), 'test3.ini')
TEST4_INI = join(dirname(__file__), 'test4.ini')
TEST5_INI = join(dirname(__file__), 'test5.ini')
TEST6_INI = join(dirname(__file__), 'test6.ini')
TEST7_INI = join(dirname(__file__), 'test7.ini')
TEST8_INI = join(dirname(__file__), 'test8.ini')
CIOUPDATE_INI = join(dirname(__file__), 'cioupdate.ini')
CIOUPDATE1_INI = join(dirname(__file__), 'cioupdate1.ini')
CIOUPDATE2_INI = join(dirname(__file__), 'cioupdate2.ini')
CIOUPDATE3_INI = join(dirname(__file__), 'cioupdate3.ini')
CIOUPDATE4_INI = join(dirname(__file__), 'cioupdate4.ini')
CIOUPDATE5_INI = join(dirname(__file__), 'cioupdate5.ini')
CIOUPDATE6_INI = join(dirname(__file__), 'cioupdate6.ini')
TEST1_SET_XML = join(dirname(__file__), 'Xml', 'test1.cioset.xml')
TEST1_PFL_XML = join(dirname(__file__), 'Xml', 'test1.ciopfl.xml')
TEST1_USR_XML = join(dirname(__file__), 'Xml', 'test1.ciousr.xml')
TEST2_USR_XML = join(dirname(__file__), 'Xml', 'test2.ciousr.xml')
TEST3_USR_XML = join(dirname(__file__), 'Xml', 'test3.ciousr.xml')
TEST1_GROUP_XML = join(dirname(__file__), 'Xml', 'test1.ciogrp.xml')
I18N_XML = join(dirname(__file__), 'Xml', 'i18n.xml')
TEST_UTF8 = join(dirname(__file__), 'Texts', 'utf8.txt')
TEST_LATIN1 = join(dirname(__file__), 'Texts', 'latin1.rst')
TRANSFORM_XSL = join(dirname(__file__), 'Xml', 'transform.xsl')
TEST1_USR_ZIP = join(dirname(__file__), 'Backup', 'test1.ciousr.zip')
TEST2_USR_ZIP = join(dirname(__file__), 'Backup', 'test2.ciousr.zip')
TEST3_USR_ZIP = join(dirname(__file__), 'Backup', 'test3.ciousr.zip')
TEST_CSS = join(dirname(__file__), '..', 'Static', 'Css', 'chrysalio.css')
TEST_XXX = join(dirname(__file__), 'test.xxx')
EMAIL_HTML = join(dirname(__file__), 'Templates', 'email_test.pt')
EMAIL_TEXT = join(dirname(__file__), 'Templates', 'email_test.txt')
ATTACHMENTS_DIR = join(dirname(__file__), 'Attachments')
TEST1_SVG = join(ATTACHMENTS_DIR, 'Users', 'Test1', 'test1.svg')
TEST5_SVG = join(ATTACHMENTS_DIR, 'Users', 'Test5', 'test5.svg')

TEST_DIR = normpath(join(dirname(__file__), '..', '..', 'Test~'))
BACKUP_DIR = join(TEST_DIR, 'Backup')

FTP_HOST = 'ftp.chrysal.io'
FTP_USER = 'ftp-chrysalio'
FTP_PASSWORD = 'hFphq3c6Qj9TgaB1X1mtYVj9q9ytTdIIeU6rlyxAb+I='
RESTFUL_HOST = 'https://demo.chrysal.io/'
RESTFUL_LOGIN = 'user1'
RESTFUL_KEY = 'Cb4rCDyPJZbkuBNVFMLAtxgzJ4QJX/qt6RHyPRy3g4I='


# =============================================================================
class ConfiguratorTestCase(TestCase):
    """Base class for unit test of a module."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        self.configurator = setUp()

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects of ``pyramid.testing.setUp()``."""
        tearDown()


# =============================================================================
class ModuleTestCase(TestCase):
    """Base class for unit test of a module."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        self.configurator = setUp()
        self.configurator.set_root_factory(DummyRootFactory)
        self.configurator.registry['modules'] = OrderedDict()
        self.configurator.registry['modules_off'] = set()

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects of ``pyramid.testing.setUp()``."""
        tearDown()


# =============================================================================
class TmpDirTestCase(TestCase):
    """Base class for unit test with a temprary directory."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        if exists(TEST_DIR):
            rmtree(TEST_DIR)
        makedirs(TEST_DIR)

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects of ``pyramid.testing.setUp()``."""
        tearDown()
        if exists(TEST_DIR):
            rmtree(TEST_DIR)


# =============================================================================
class DBUnitTestCase(TestCase):
    """Base class for unit test with database use."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from ..relaxng import RELAXNG
        from ..lib.breadcrumbs import Breadcrumbs
        from ..models import DB_METADATA, get_dbengine
        from ..models import get_dbsession_factory, get_tm_dbsession
        from ..models.dbsettings import DBSettings

        self.configurator = setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'})
        self.configurator.include('..models')

        DB_METADATA.bind = get_dbengine(self.configurator.get_settings())
        DB_METADATA.create_all()
        dbsession_factory = get_dbsession_factory(DB_METADATA.bind)
        self.configurator.registry['dbsession_factory'] = dbsession_factory
        self.configurator.registry['relaxng'] = RELAXNG
        self.configurator.registry['principals'] = []
        self.configurator.registry['themes'] = {'': {'name': {}}}
        self.configurator.registry['settings'] = \
            DBSettings.settings_defaults.copy()
        self.configurator.registry['settings']['title'] = 'TestChrysalio'

        self.request = DummyRequest(matched_route=None, is_xhr=False)
        self.request.dbsession = get_tm_dbsession(dbsession_factory, manager)
        self.request.registry = self.configurator.registry
        self.request.breadcrumbs = Breadcrumbs(self.request)
        self.request.referrer = None

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects of ``pyramid.testing.setUp()``."""
        from ..models import DB_METADATA

        tearDown()
        manager.abort()
        DB_METADATA.drop_all()
        if exists(TEST_DIR):
            rmtree(TEST_DIR)

    # -------------------------------------------------------------------------
    def add_user(self, record):
        """Add a user in the database.

        :param dict record:
            Dictionary representing the user.
        :rtype: ``None`` or :class:`pyramid.i18n.TranslationString`
        :return:
            ``None`` or error message.
        """
        error = DBUser.record_format(record)
        if error is not None:
            return error

        dbuser = DBUser(**record)
        if 'password' in record:
            dbuser.set_password(record['password'])
        # pylint: disable = no-member
        self.request.dbsession.add(dbuser)
        return None


# =============================================================================
class FunctionalTestCase(TestCase):
    """Base class for functional test."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from ..relaxng import RELAXNG
        from ..scripts.ciopopulate import Populate
        from ..models.populate import xml2db

        register_loader_type(AssertionRewritingHook, DefaultProvider)

        self.testapp = BaseTestApp(
            'config:{0}'.format(TEST_INI), relative_to='.')

        args = namedtuple(
            'ArgumentParser', 'conf_uri options lang attachments')(
                conf_uri=TEST_INI, options=None, lang=None, attachments=None)
        dbsession_factory = self.testapp.app.registry['dbsession_factory']
        Populate(
            args, DBUser, xml2db, RELAXNG,
            dbsession_factory=dbsession_factory).run()

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects of ``setUp()``."""
        from ..models import DB_METADATA

        manager.abort()
        DB_METADATA.drop_all()
        if exists(TEST_DIR):
            rmtree(TEST_DIR)

    # -------------------------------------------------------------------------
    def login(self, login_, password=None):
        """Simulate a login action."""
        self.testapp.post(
            '/login',
            {'csrf_token': self.testapp.get('/login').form.get(
                'csrf_token').value,
             'login': login_,
             'password': password or '{0}pwd'.format(login_)},
            status=302)


# =============================================================================
class DummyPOST(dict):
    """Class to simulate POST with getall() method."""

    multikeys = {}

    # -------------------------------------------------------------------------
    def getall(self, key):
        """Simulation of a dict-like collection of key-value pairs where key
        might be occurred more than once in the container.

        :param str key:
            Key to retrieve.
        """
        return self.multikeys.get(key) or []


# =============================================================================
class DummyRootFactory(object):
    """Dummy Access Control List (ACL) definition."""
    # pylint: disable = too-few-public-methods
    __acl__ = [(Allow, Authenticated, 'authenticated')]

    # -------------------------------------------------------------------------
    def __init__(self, request):
        """Constructor method."""
