# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``models.dbuser`` classes."""

from datetime import datetime, date, timedelta
from json import dumps

from lxml import etree
from colander import SchemaNode

from pyramid.i18n import TranslationString

from ..models.dbuser import DBUser
from ..models.dbgroup import DBGroup
from . import DBUnitTestCase


# =============================================================================
class DummyAuthority(object):
    """Class to simulate an authority for authentification as LDAP."""

    # -------------------------------------------------------------------------
    def __init__(self, settings):
        """Constructor method."""

    # -------------------------------------------------------------------------
    @classmethod
    def get(cls, ignored_, login, password, dbuser_class):
        """Get user from dummy authority."""
        if login == 'test100' and password == 'test100pwd':
            dbuser = dbuser_class(
                login=login, password=password, last_name='HONNÊTE',
                email='test100@chrysal.io')
            return dbuser, None
        return None, 'Dummy: ID or password is incorrect.'

    # -------------------------------------------------------------------------
    @classmethod
    def check(cls, ignored_, login, password, unused_):
        """Check user authorization according to dummy authority."""
        if login == 'test101' and password == 'test101pwd':
            return None
        return 'Dummy: ID or password is incorrect.'


# =============================================================================
class UModelsDBUserDBUser(DBUnitTestCase):
    """Unit test class for :class:`models.dbuser.DBUser`."""

    # -------------------------------------------------------------------------
    @classmethod
    def _make_one(cls):
        """Make an ``DBUser`` object."""
        dbuser = DBUser(
            login='test1', status='active', first_name='Édith',
            last_name='AVULEUR', honorific='Mrs', email='test1@chrysal.io',
            theme='Default', page_size=80, account_creation=datetime.now(),
            account_update=datetime.now(), expiration=datetime(2100, 1, 1),
            last_login=datetime.now())
        dbuser.set_password('test1pwd')
        return dbuser

    # -------------------------------------------------------------------------
    def test_set_password(self):
        """[u:models.dbuser.DBUser.set_password]"""
        user = DBUser(
            login='test1', first_name='Édith', last_name='AVULEUR',
            honorific='Mrs', email='test1@chrysal.io')
        user.set_password('test1pwd')
        self.assertTrue(user.password.startswith('$'))
        user.set_password(
            '$2b$12$c67DI/dlDjSqqYtGcfmhKeXOp/6ohidEFUE3/nsOeBMnmWmuQYGwa')
        self.assertEqual(
            user.password,
            '$2b$12$c67DI/dlDjSqqYtGcfmhKeXOp/6ohidEFUE3/nsOeBMnmWmuQYGwa')

    # -------------------------------------------------------------------------
    def test_check_password(self):
        """[u:models.dbuser.DBUser.check_password]"""
        dbuser = self._make_one()
        self.assertFalse(dbuser.check_password(None))
        self.assertFalse(dbuser.check_password('foo'))
        self.assertTrue(dbuser.check_password('test1pwd'))
        self.assertTrue(
            dbuser.password_update > datetime.now() - timedelta(seconds=2))

    # -------------------------------------------------------------------------
    def test_get(self):
        """[u:models.dbuser.DBUser.get]"""
        dbsession = self.request.dbsession

        # No login
        dbuser, error = DBUser.get(self.request)
        self.assertIsNone(dbuser)
        self.assertEqual(error, 'ID or password is incorrect.')

        # Unknown user
        dbuser, error = DBUser.get(self.request, 'test1')
        self.assertIsNone(dbuser)
        self.assertEqual(error, 'ID or password is incorrect.')

        # Invalid password
        self.add_user({
            'login': 'test1', 'first_name': 'Édith', 'last_name': 'AVULEUR',
            'password': 'test1pwd', 'email': 'test1@chrysal.io'})
        dbuser, error = DBUser.get(self.request, 'test1', 'foo')
        self.assertIsNone(dbuser)
        self.assertEqual(error, 'ID or password is incorrect.')

        # Connection ok
        dbuser, error = DBUser.get(self.request, 'test1', 'test1pwd')
        self.assertIsInstance(dbuser, DBUser)
        self.assertIsNone(error)
        user = dbsession.query(DBUser).filter_by(login='test1').first()
        self.assertTrue(
            user.last_login > datetime.now() - timedelta(seconds=2))

        # Inactive account
        self.add_user({
            'login': 'test2', 'first_name': 'Sophie', 'last_name': 'FONFEC',
            'status': 'inactive', 'password': 'test2pwd',
            'email': 'test2@chrysal.io'})
        dbuser, error = DBUser.get(self.request, 'test2', 'test2pwd')
        self.assertIsNone(dbuser)
        self.assertEqual(error, 'Your account is not active.')

        # Locked account
        self.add_user({
            'login': 'test3', 'first_name': 'Guy', 'last_name': 'LIGUILI',
            'status': 'locked', 'password': 'test3pwd',
            'email': 'test3@chrysal.io'})
        dbuser, error = DBUser.get(self.request, 'test3', 'test3pwd')
        self.assertIsNone(dbuser)
        self.assertEqual(error, 'Your account is locked.')

        # Expired account
        self.add_user({
            'login': 'test4', 'first_name': 'Gédéon',
            'last_name': 'TEUSEMANIE', 'password': 'test4pwd',
            'email': 'test4@chrysal.io', 'expiration': '2018-01-01'})
        dbuser, error = DBUser.get(self.request, 'test4', 'test4pwd')
        self.assertIsNone(dbuser)
        self.assertEqual(error, 'Your account has expired.')

        # With authority: creation with invalid password
        self.request.registry['authorities'] = {'foo': DummyAuthority({})}
        dbuser, error = DBUser.get(self.request, 'test100', 'foo')
        self.assertIsNone(dbuser)
        self.assertEqual(error, 'Dummy: ID or password is incorrect.')

        # With authority: creation ok
        dbuser, error = DBUser.get(self.request, 'test100', 'test100pwd')
        self.assertIsNotNone(dbuser)
        self.assertIsNone(error)

        # With authority: check with authority not available
        self.add_user({
            'login': 'test101', 'first_name': 'Bob',
            'last_name': 'INDEFIL', 'password': 'test101pwd',
            'email': 'test101@chrysal.io', 'authority': 'dummy'})
        dbuser, error = DBUser.get(self.request, 'test101', 'test101pwd')
        self.assertIsNone(dbuser)
        self.assertEqual(error, 'Authority not available.')

        # With authority: check with invalid password
        self.request.registry['authorities'] = {'dummy': DummyAuthority({})}
        dbuser, error = DBUser.get(self.request, 'test101', 'foo')
        self.assertIsNone(dbuser)
        self.assertEqual(error, 'Dummy: ID or password is incorrect.')

        # With authority: check ok
        dbuser, error = DBUser.get(self.request, 'test101', 'test101pwd')
        self.assertIsNotNone(dbuser)
        self.assertIsNone(error)

    # -------------------------------------------------------------------------
    def test_set_session(self):
        """[u:models.dbuser.DBUser.set_session]"""
        # pylint: disable = too-many-statements
        from ..models.dbprofile import DBProfile, DBProfilePrincipal
        from ..models.dbuser import DBUserProfile
        from ..models.dbgroup import DBGroupProfile

        dbsession = self.request.dbsession
        dbuser = self._make_one()
        dbsession.add(dbuser)
        self.request.registry.settings['languages'] = 'en, fr'

        # Check language
        dbuser.set_session(self.request)
        self.assertNotIn('lang', self.request.session)
        dbuser.language = 'fr'
        dbuser.set_session(self.request)
        self.assertEqual(self.request.session['lang'], 'fr')
        dbuser.language = 'es'
        dbuser.set_session(self.request)
        self.assertEqual(self.request.session['lang'], 'en')

        # Check theme
        self.assertIn('theme', self.request.session)
        self.assertEqual(self.request.session['theme'], '')
        self.request.registry['themes'] = {'Default': {}, 'Alternative': {}}
        self.request.registry['settings']['theme'] = 'Default'
        dbuser.theme = 'Foo'
        dbuser.set_session(self.request)
        self.assertEqual(self.request.session['theme'], 'Default')
        dbuser.theme = 'Alternative'
        dbuser.set_session(self.request)
        self.assertEqual(self.request.session['theme'], 'Alternative')

        # Check general information
        self.assertIn('user', self.request.session)
        user_session = self.request.session['user']
        self.assertIn('user_id', user_session)
        self.assertIn('login', user_session)
        self.assertIn('name', user_session)
        self.assertIn('principals', user_session)
        self.assertEqual(user_session['login'], 'test1')
        self.assertEqual(user_session['name'], 'Édith AVULEUR')

        # Check groups and profiles
        dbprofile = DBProfile(
            profile_id='profile_manager',
            i18n_label=dumps({'en': 'Profile manager'}))
        dbprofile.principals.append(
            DBProfilePrincipal(principal='profile.creator'))
        dbsession.add(dbprofile)
        dbprofile = DBProfile(
            profile_id='user_manager',
            i18n_label=dumps({'en': 'User manager'}))
        dbprofile.principals.append(
            DBProfilePrincipal(principal='user.creator'))
        dbsession.add(dbprofile)

        dbgroup = DBGroup(
            group_id='managers', i18n_label=dumps({'en': 'Managers'}))
        dbsession.add(dbgroup)
        dbsession.flush()
        dbsession.add(DBUserProfile(
            user_id=dbuser.user_id, profile_id='user_manager'))
        dbsession.add(DBGroupProfile(
            group_id=dbgroup.group_id, profile_id='profile_manager'))
        dbuser.groups.append(dbgroup)
        dbuser.set_session(self.request)
        user_session = self.request.session['user']

        self.assertEqual(len(user_session['principals']), 2)
        self.assertIn('profile.creator', user_session['principals'])
        self.assertIn('user.creator', user_session['principals'])
        self.assertEqual(len(user_session['groups']), 1)
        self.assertEqual(user_session['groups'][0], 'managers')

        # Check administrator and modes
        self.request.session['menu'] = ()
        self.request.session['modes'] = ['home', 'Home', None]
        dbuser.status = 'administrator'
        dbuser.set_session(self.request)
        user_session = self.request.session['user']
        self.assertEqual(len(user_session['principals']), 1)
        self.assertEqual(user_session['principals'][0], 'system.administrator')
        self.assertNotIn('menu', self.request.session)

    # -------------------------------------------------------------------------
    def test_load_administrator(self):
        """[u:models.dbuser.DBUser.load_administrator]"""
        dbsession = self.request.dbsession
        record = {
            'password': 'adminpwd', 'last_name': 'Administrateur',
            'language': 'fr', 'time_zone': 'Europe/Paris'}

        error = DBUser.load_administrator(dbsession, record)
        self.assertIsInstance(error, TranslationString)

        self.add_user({
            'login': 'test1', 'first_name': 'Édith', 'last_name': 'AVULEUR',
            'password': 'test1pwd', 'email': 'test1@chrysal.io'})
        record['login'] = 'test1'
        error = DBUser.load_administrator(dbsession, record)
        self.assertIsNone(error)

        record['login'] = 'admin'
        error = DBUser.load_administrator(dbsession, record)
        self.assertIsInstance(error, TranslationString)

        record['email'] = 'admin@chrysal.io'
        error = DBUser.load_administrator(dbsession, record)
        self.assertIsNone(error)

        user = dbsession.query(DBUser).filter_by(login='admin').first()
        self.assertIsInstance(user, DBUser)
        self.assertTrue(user.password.startswith('$'))
        self.assertEqual(user.status, 'administrator')
        self.assertEqual(user.last_name, 'Administrateur')
        self.assertTrue(user.email_hidden)
        self.assertEqual(user.email, 'admin@chrysal.io')
        self.assertEqual(user.language, 'fr')
        self.assertEqual(user.time_zone, 'Europe/Paris')

    # -------------------------------------------------------------------------
    def test_xml2db(self):
        """[u:models.dbuser.DBUser.xml2db]"""
        dbsession = self.request.dbsession
        self.add_user({
            'login': 'test2', 'first_name': 'Sophie', 'last_name': 'FONFEC',
            'password': 'test2pwd', 'email': 'test2@chrysal.io'})

        user_elt = etree.XML(
            '<user>'
            '  <login>test2</login>'
            '  <password>test2pwd</password>'
            '  <firstname>Sophie</firstname>'
            '  <lastname>FONFEC</lastname>'
            '  <email>test2@chrysal.io</email>'
            '</user>')
        error = DBUser.xml2db(dbsession, user_elt)
        self.assertIsInstance(error, TranslationString)
        error = DBUser.xml2db(dbsession, user_elt, error_if_exists=False)
        self.assertIsNone(error)

        user_elt = etree.XML('<user><login>test1</login></user>')
        error = DBUser.xml2db(dbsession, user_elt)
        self.assertIsInstance(error, TranslationString)

        user_elt = etree.XML(
            '<user>'
            '  <login>test1</login>'
            '  <password must-change="true">test1pwd</password>'
            '  <firstname>Édith</firstname>'
            '  <lastname>AVULEUR</lastname>'
            '  <honorific>Mrs</honorific>'
            '  <email hidden="true">test1@chrysal.io</email>'
            '  <language>fr</language>'
            '  <theme>Alternative</theme>'
            '</user>')
        error = DBUser.xml2db(dbsession, user_elt)
        self.assertIsNone(error)
        user = dbsession.query(DBUser).filter_by(login='test1').first()
        self.assertIsInstance(user, DBUser)
        self.assertTrue(user.password_mustchange)
        self.assertEqual(user.first_name, 'Édith')
        self.assertEqual(user.last_name, 'AVULEUR')
        self.assertEqual(user.honorific, 'Mrs')
        self.assertEqual(user.email, 'test1@chrysal.io')
        self.assertTrue(user.email_hidden)
        self.assertEqual(user.language, 'fr')
        self.assertEqual(user.theme, 'Alternative')

    # -------------------------------------------------------------------------
    def test_xml2db_extra(self):
        """[u:models.dbuser.DBUser.xml2db_extra]"""
        from ..models.dbprofile import DBProfile

        dbsession = self.request.dbsession
        dbsession.add(DBProfile(
            profile_id='user_manager',
            i18n_label=dumps({'en': 'User manager'})))
        self.add_user({
            'login': 'test1', 'first_name': 'Édith', 'last_name': 'AVULEUR',
            'password': 'test1pwd', 'email': 'test1@chrysal.io'})
        dbuser = dbsession.query(DBUser).filter_by(login='test1').first()
        user_elt = etree.XML(
            '<user>'
            '  <login>test1</login>'
            '  <password>test1pwd</password>'
            '  <firstname>Édith</firstname>'
            '  <lastname>AVULEUR</lastname>'
            '  <email>test1@chrysal.io</email>'
            '  <profiles>'
            '    <profile>profile_manager</profile>'
            '    <profile>user_manager</profile>'
            '  </profiles>'
            '</user>')
        dbuser.xml2db_extra(
            dbsession, user_elt, {'profiles': ['user_manager']})
        self.assertEqual(len(dbuser.profiles), 1)

    # -------------------------------------------------------------------------
    def test_record_from_xml(self):
        """[u:models.dbuser.DBUser.record_from_xml]"""
        user_elt = etree.XML(
            '<user>'
            '  <login>test1</login>'
            '  <password must-change="true">test1pwd</password>'
            '  <firstname>Édith</firstname>'
            '  <lastname>AVULEUR</lastname>'
            '  <honorific>Mrs</honorific>'
            '  <email hidden="true">test1@chrysal.io</email>'
            '  <expiration>2018-01-01</expiration>'
            '  <profiles>'
            '    <profile>profile_manager</profile>'
            '    <profile>user_manager</profile>'
            '  </profiles>'
            '</user>')
        record = DBUser.record_from_xml('test1', user_elt)
        self.assertEqual(record['status'], 'active')
        self.assertEqual(record['login'], 'test1')
        self.assertTrue(record['password_mustchange'])
        self.assertEqual(record['first_name'], 'Édith')
        self.assertEqual(record['last_name'], 'AVULEUR')
        self.assertEqual(record['honorific'], 'Mrs')
        self.assertIsNone(record['language'])
        self.assertEqual(record['expiration'], '2018-01-01')

    # -------------------------------------------------------------------------
    def test_record_format(self):
        """[u:models.dbuser.DBUser.record_format]"""
        record = {'language': 'fr', 'expiration': None}
        error = DBUser.record_format(record)
        self.assertEqual(len(record), 1)
        self.assertIsInstance(error, TranslationString)
        self.assertIn('without login', error)

        record['login'] = 'test1'
        error = DBUser.record_format(record)
        self.assertIsInstance(error, TranslationString)
        self.assertIn('without password', error)

        record['password'] = 'test1pwd'
        record['password_mustchange'] = True
        error = DBUser.record_format(record)
        self.assertTrue(record['password'].startswith('$'))
        self.assertTrue(record['password_mustchange'])
        self.assertIsInstance(error, TranslationString)
        self.assertIn('without last name', error)

        record['last_name'] = ' AVULEUR '
        record['honorific'] = 'X'
        error = DBUser.record_format(record)
        self.assertEqual(record['last_name'], 'AVULEUR')
        self.assertIsInstance(error, TranslationString)
        self.assertIn('unknown honorific', error)

        record['honorific'] = 'Mrs'
        error = DBUser.record_format(record)
        self.assertIsInstance(error, TranslationString)
        self.assertIn('without email', error)

        record['email'] = 'test1_chrysal.io'
        error = DBUser.record_format(record)
        self.assertIsInstance(error, TranslationString)
        self.assertIn('Invalid email', error)

        record['email'] = 'test1@chrysal.io'
        record['authority_check'] = '2020-01-28T12:00:00'
        error = DBUser.record_format(record)
        self.assertIsNone(error)

    # -------------------------------------------------------------------------
    def test_record_convert_dates(self):
        """[u:models.dbuser.DBUser.record_convert_dates]"""
        record = {
            'last_login': '2020-01-01T12:00:00',
            'password_update': '2020-06-01T12:00:00',
            'expiration': '2020-12-01',
            'account_creation': '2020-01-01T12:00:00',
            'account_update': '2020-06-01T12:00:00',
            'authority_check': '2020-06-01T12:00:00'
        }
        DBUser.record_convert_dates(record)
        self.assertIsInstance(record['last_login'], datetime)
        self.assertIsInstance(record['password_update'], datetime)
        self.assertIsInstance(record['expiration'], date)
        self.assertIsInstance(record['account_creation'], datetime)
        self.assertIsInstance(record['account_update'], datetime)
        self.assertIsInstance(record['authority_check'], datetime)

    # -------------------------------------------------------------------------
    def test_db2xml(self):
        """[u:models.dbuser.DBUser.db2xml]"""
        dbsession = self.request.dbsession
        update_time = (datetime.now() + timedelta(minutes=3))\
            .isoformat().partition('.')[0]
        self.add_user({
            'login': 'test1', 'last_login': '2020-01-01T12:00:00',
            'status': 'inactive', 'password': 'test1pwd',
            'password_mustchange': True, 'first_name': ' Édith',
            'last_name': '  AVULEUR ', 'honorific': 'Mrs',
            'email': 'test1@chrysal.io', 'email_hidden': True,
            'language': 'fr', 'time_zone': 'Europe/Paris',
            'theme': 'Alternative', 'page_size': 80,
            'attachments_key': 'Test1',
            'picture': 'test1.svg', 'expiration': '2020-12-31',
            'account_update': update_time,
            'authority': 'ldap', 'authority_check': datetime.now()})
        dbuser = dbsession.query(DBUser).filter_by(login='test1').first()

        user_elt = dbuser.db2xml(dbsession)
        self.assertEqual(user_elt.get('status'), 'inactive')
        self.assertIsNotNone(user_elt.get('created'))
        self.assertTrue(
            datetime.strptime(user_elt.get('created'), '%Y-%m-%dT%H:%M:%S') >
            datetime.now() - timedelta(seconds=2))
        self.assertIsNotNone(user_elt.get('updated'))
        self.assertTrue(
            datetime.strptime(user_elt.get('updated'), '%Y-%m-%dT%H:%M:%S') >
            datetime.now() + timedelta(minutes=2))

        self.assertEqual(user_elt.findtext('login'), 'test1')

        self.assertIsNotNone(user_elt.find('password'))
        self.assertIsNotNone(user_elt.find('password').get('updated'))
        self.assertTrue(
            datetime.strptime(
                user_elt.find('password').get('updated'),
                '%Y-%m-%dT%H:%M:%S') > datetime.now() - timedelta(seconds=2))
        self.assertTrue(user_elt.find('password').get('must-change'))

        self.assertEqual(user_elt.findtext('firstname'), 'Édith')
        self.assertEqual(user_elt.findtext('lastname'), 'AVULEUR')
        self.assertEqual(user_elt.findtext('honorific'), 'Mrs')

        self.assertIsNotNone(user_elt.find('email'))
        self.assertEqual(user_elt.findtext('email'), 'test1@chrysal.io')
        self.assertTrue(user_elt.find('email').get('hidden'))

        self.assertEqual(user_elt.findtext('language'), 'fr')
        self.assertEqual(user_elt.findtext('timezone'), 'Europe/Paris')
        self.assertEqual(user_elt.findtext('theme'), 'Alternative')
        self.assertEqual(user_elt.findtext('page-size'), '80')
        self.assertEqual(user_elt.findtext('expiration'), '2020-12-31')

    # -------------------------------------------------------------------------
    def test_db2xml_extra(self):
        """[u:models.dbuser.DBUser.db2xml_extra]"""
        from ..models.dbprofile import DBProfile
        from ..models.dbuser import DBUserProfile

        dbsession = self.request.dbsession
        dbsession.add(DBProfile(
            profile_id='user_manager',
            i18n_label=dumps({'en': 'User manager'})))
        self.add_user({
            'login': 'test1', 'first_name': 'Édith', 'last_name': 'AVULEUR',
            'password': 'test1pwd', 'email': 'test1@chrysal.io'})
        dbuser = dbsession.query(DBUser).filter_by(login='test1').first()
        dbuser.profiles.append(DBUserProfile(profile_id='user_manager'))
        user_elt = etree.XML(
            '<user>'
            '  <login>test1</login>'
            '  <password>test1pwd</password>'
            '  <firstname>Édith</firstname>'
            '  <lastname>AVULEUR</lastname>'
            '  <email>test1@chrysal.io</email>'
            '</user>')
        dbuser.db2xml_extra(user_elt)
        self.assertEqual(len(user_elt.findall('profiles/profile')), 1)

    # -------------------------------------------------------------------------
    def test_paging_filter(self):
        """[u:models.dbuser.DBUser.paging_filter]"""
        from ..lib.form import Form
        from ..lib.paging import Paging
        from ..lib.filter import Filter

        dbsession = self.request.dbsession
        paging_id = 'users'
        user_filter = Filter(
            self.request, paging_id, (
                ('login', 'Login', True, None),
                ('status', 'Status', False, None)),
            (('status', '=', 'active'),))
        dbquery = user_filter.sql(dbsession.query(DBUser), 'users')
        user_paging = Paging(self.request, paging_id, dbquery)

        html = DBUser.paging_filter(
            self.request, Form(self.request), user_filter, user_paging)
        self.assertIn('page_size', html)
        self.assertIn('filter_key', html)
        self.assertIn('filter_value', html)

    # -------------------------------------------------------------------------
    def test_tab4view(self):
        """[u:models.dbuser.DBUser.tab4view]"""
        from ..lib.form import Form
        from ..models.dbprofile import DBProfile
        from ..models.dbuser import DBUserProfile

        dbsession = self.request.dbsession
        dbsession.add(DBProfile(
            profile_id='user_creator',
            i18n_label=dumps({'en': 'User Creator'}),
            i18n_description={'en': 'Permission to create user.'}))
        dbsession.add(DBProfile(
            profile_id='user_viewer', i18n_label=dumps({'en': 'User Viewer'})))
        dbuser = self._make_one()
        dbsession.add(dbuser)
        dbsession.flush()
        dbsession.add(DBUserProfile(
            user_id=dbuser.user_id, profile_id='user_creator'))
        dbsession.add(DBUserProfile(
            user_id=dbuser.user_id, profile_id='user_viewer'))
        self.configurator.add_route(
            'profile_view', '/profile/view/{profile_id}')
        self.configurator.add_route('group_view', '/group/view/{group_id}')

        # Information
        html = dbuser.tab4view(self.request, 0, Form(self.request))
        self.assertIn('Édith', html)
        self.assertIn('Mrs', html)

        # Preferences
        html = dbuser.tab4view(self.request, 1, Form(self.request))
        self.assertIn('Lines per page:', html)

        # Profiles
        html = dbuser.tab4view(self.request, 2, Form(self.request))
        self.assertIn('User Creator', html)
        dbuser = self._make_one()
        html = dbuser.tab4view(self.request, 2, Form(self.request))
        self.assertIn('No attributed profile.', html)

        # Groups
        html = dbuser.tab4view(self.request, 3, Form(self.request))
        self.assertIn('user is in any group', html)
        dbuser.groups.append(DBGroup(
            group_id='managers', i18n_label=dumps({'en': 'Managers'})))
        html = dbuser.tab4view(self.request, 3, Form(self.request))
        self.assertIn('Managers', html)

        # Other
        self.assertEqual(
            dbuser.tab4view(self.request, 4, Form(self.request)), '')

    # -------------------------------------------------------------------------
    def test_settings_schema(self):
        """[u:models.dbuser.DBUser.settings_schema]"""
        from ..models.dbuser import DBUserProfile

        profiles = {
            'user_creator': ('User Creator', 'Authorized to create users.')}
        groups = {'managers': ('Managers', 'Thies users manage.')}
        self.request.registry['themes'] = {'Default': {}, 'Alternative': {}}
        self.request.session['user'] = {'user_id': 2}
        self.request.has_permission = \
            lambda x: x in ('user-create', 'user-edit')

        schema, defaults = DBUser.settings_schema(
            self.request, profiles, groups)
        self.assertIsInstance(schema, SchemaNode)
        serialized = schema.serialize()
        self.assertIn('status', serialized)
        self.assertIn('password1', serialized)
        self.assertIn('email', serialized)
        self.assertIn('pfl:user_creator', serialized)
        self.assertIsInstance(defaults, dict)
        self.assertIn('status', defaults)
        self.assertEqual(defaults['status'], 'active')

        dbuser = self._make_one()
        self.request.has_permission = lambda x: True
        self.request.registry['authorities'] = {}
        schema = DBUser.settings_schema(
            self.request, profiles, groups, dbuser)[0]
        self.assertIn('authority', schema.serialize())

        dbuser.profiles.append(DBUserProfile(profile_id='user_creator'))
        dbuser.groups.append(DBGroup(
            group_id='managers', i18n_label=dumps({'en': 'Managers'})))
        self.request.has_permission = lambda x: False
        schema, defaults = DBUser.settings_schema(
            self.request, profiles, groups, dbuser)
        self.assertNotIn('authority', schema.serialize())
        self.assertNotIn('status', defaults)
        self.assertIn('pfl:user_creator', defaults)
        self.assertIn('grp:managers', defaults)

    # -------------------------------------------------------------------------
    def test_tab4edit(self):
        """[u:models.dbuser.DBUser.tab4edit]"""
        from ..lib.form import Form

        self.request.session['user'] = {'user_id': 2}
        self.request.has_permission = \
            lambda x: x in ('user-create', 'user-edit')
        self.request.registry['authorities'] = {'ldap': None}
        form = Form(self.request)

        # Information
        html = DBUser.tab4edit(self.request, 0, form, None, None)
        self.assertIn('Identity', html)
        self.assertIn('Security', html)
        self.assertIn('expiration', html)

        self.request.has_permission = lambda x: True
        html = DBUser.tab4edit(self.request, 0, form, None, None)
        self.assertIn('authority', html)

        self.request.has_permission = lambda x: False
        profiles = {
            'user_creator': ('User Creator', 'Authorized to create users.'),
            'user_editor': ('User Editor', None)}
        groups = {'managers': ('Managers', 'Thies users manage.')}
        dbuser = self._make_one()
        html = DBUser.tab4edit(self.request, 0, form, profiles, groups, dbuser)
        self.assertNotIn('expiration', html)

        dbuser.authority = 'ldap'
        html = DBUser.tab4edit(self.request, 0, form, profiles, groups, dbuser)
        self.assertNotIn('password', html)
        self.assertIn('ldap', html)

        # Preferences
        html = DBUser.tab4edit(self.request, 1, form, {}, {})
        self.assertIn('Hide e-mail:', html)
        self.assertNotIn('theme', html)

        self.request.registry['themes'] = {
            'Default': {'name': {'en': 'Default'}},
            'Alternative': {'name': {'en': 'Alternative Chrysalio'}}}
        self.request.registry['settings'] = {'theme': 'Default'}
        html = DBUser.tab4edit(self.request, 1, form, {}, {})
        self.assertIn('theme', html)

        # Profiles
        html = DBUser.tab4edit(self.request, 2, form, {}, {})
        self.assertIn('No available profile.', html)

        html = DBUser.tab4edit(self.request, 2, form, profiles, {})
        self.assertIn('not have the rigths', html)

        self.request.has_permission = \
            lambda x: x in ('user-create', 'user-edit')
        html = DBUser.tab4edit(self.request, 2, form, profiles, {})
        self.assertIn('pfl:user_creator', html)

        # Groups
        html = DBUser.tab4edit(self.request, 3, form, {}, {})
        self.assertIn('No available group.', html)

        html = DBUser.tab4edit(self.request, 3, form, {}, groups)
        self.assertIn('grp:managers', html)

        self.request.has_permission = lambda x: False
        html = DBUser.tab4edit(self.request, 3, form, {}, groups)
        self.assertIn('not have the rigths', html)

        # Other
        html = DBUser.tab4edit(self.request, 4, form, {}, {})
        self.assertEqual(html, '')


# =============================================================================
class IModelsDBUser(DBUnitTestCase):
    """Integration test class for ``models.dbuser``."""

    # -------------------------------------------------------------------------
    def test_delete_cascade_profile(self):
        """[i:models.dbuser] delete, cascade profile"""
        from ..models.dbprofile import DBProfile
        from ..models.dbuser import DBUserProfile

        dbsession = self.request.dbsession
        dbsession.add(DBProfile(
            profile_id='user_manager',
            i18n_label=dumps({'en': 'User manager'})))
        dbuser = DBUser(
            login='test1', last_name='AVULEUR', email='test1@chrysal.io')
        dbuser.set_password('test1pwd')
        dbsession.add(dbuser)
        dbsession.flush()
        dbsession.add(DBUserProfile(
            user_id=dbuser.user_id, profile_id='user_manager'))

        dbuser = dbsession.query(DBUser).filter_by(login='test1').first()
        self.assertIsInstance(dbuser, DBUser)
        user_id = dbuser.user_id
        self.assertIsNotNone(dbsession.query(DBUserProfile).filter_by(
            user_id=user_id).first())

        dbuser.profiles.remove(dbuser.profiles[0])
        dbsession.flush()
        self.assertIsNone(dbsession.query(DBUserProfile).filter_by(
            user_id=user_id).first())
