# -*- coding: utf-8 -*-
# pylint: disable = too-many-lines
"""SQLAlchemy-powered model definitions for users."""

from datetime import datetime, date
from bcrypt import hashpw, gensalt

import colander
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy import String, Enum, Date, DateTime, Boolean
from sqlalchemy.orm import relationship
from lxml import etree
from webhelpers2.html import HTML, literal
from pytz import common_timezones

from ..lib.i18n import _
from ..lib.config import settings_get_list
from ..lib.utils import make_id, normalize_spaces, age
from ..lib.mailing import Mailing
from ..lib.form import SameAs
from ..lib.paging import PAGE_SIZES
from ..lib.attachment import attachment_url
from . import DBDeclarativeClass, ID_LEN, NAME_LEN, LABEL_LEN, EMAIL_LEN
from .dbbase import DBBaseClass
from .dbprofile import DBProfile, DBProfilePrincipal

USER_STATUS_LABELS = {
    'administrator': _('administrator'), 'active': _('active'),
    'locked': _('locked'), 'inactive': _('inactive')}
USER_HONORIFIC_LABELS = {'Mr': _('Mr'), 'Mrs': _('Mrs')}


# =============================================================================
class DBUser(DBDeclarativeClass, DBBaseClass):
    """SQLAlchemy-powered user model."""

    status_labels = USER_STATUS_LABELS
    honorific_labels = USER_HONORIFIC_LABELS
    suffix = 'ciousr'
    attachments_dir = 'Users'
    _settings_tabs = (
        _('Information'), _('Preferences'), _('Profiles'), _('Groups'))

    __tablename__ = 'users'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    login = Column(String(EMAIL_LEN), unique=True, index=True, nullable=False)
    status = Column(
        Enum(*USER_STATUS_LABELS.keys(), name='status'), default='active')
    password = Column(String(64), nullable=False)
    password_update = Column(DateTime)
    password_mustchange = Column(
        Boolean(name='password_mustchange'), default=False)
    first_name = Column(String(NAME_LEN))
    last_name = Column(String(NAME_LEN), nullable=False)
    honorific = Column(
        Enum(*USER_HONORIFIC_LABELS.keys(), name='honorific'))
    email = Column(String(EMAIL_LEN), nullable=False)
    email_hidden = Column(Boolean(name='email_hidden'), default=False)
    language = Column(String(5))
    time_zone = Column(String(48))
    theme = Column(String(ID_LEN))
    page_size = Column(Integer)
    attachments_key = Column(String(ID_LEN + 20))
    picture = Column(String(ID_LEN + 4))
    expiration = Column(Date)
    last_login = Column(DateTime)
    account_update = Column(DateTime)
    account_creation = Column(DateTime, default=datetime.now)
    authority = Column(String(ID_LEN))
    authority_check = Column(DateTime)

    profiles = relationship(DBProfile, secondary='users_profiles')
    groups = relationship('DBGroup', secondary='groups_users', viewonly=True)

    # -------------------------------------------------------------------------
    def set_password(self, password):
        """Set the password, possibly hashing it.

        :param str password:
            Password to set. If it does not begin with ``$``, we use bcrypt
            algorithm before setting.
        """
        if not password.startswith('$'):
            self.password = hashpw(
                password.encode('utf8'), gensalt()).decode('utf8')
        else:
            self.password = password
        self.password_update = datetime.now()

    # -------------------------------------------------------------------------
    def check_password(self, password):
        """Check the validy of the given password.

        :param str password:
            Clear password to check.
        :rtype: bool
        """
        if password and self.password is not None:
            expected = self.password.encode('utf8')
            return expected == hashpw(password.encode('utf8'), expected)
        return False

    # -------------------------------------------------------------------------
    @classmethod
    def get(cls, request, login=None, password=None):
        """Retrieve a user using ``login`` and ``password`` or the content of
        ``request.params``.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str login: (optional)
            Login of the user to authenticate. If it is ``None``, we try to
            find it in ``request.params``.
        :param str password: (optional)
            Clear password.  If it is ``None``, we try to find it in
            ``request.params``.
        :rtype: tuple
        :return:
            A tuple like ``(dbuser, error)`` where ``dbuser`` is a DBUser
            object representing the authenticated user or ``None`` and
            ``error`` is an error message.

        If ``password`` is ``None`` and not in ``request.params``, password
        checking is not performed.

        If the user is authenticated, it updates ``last_login`` field in
        database.
        """
        # pylint: disable = too-many-return-statements
        login = login or request.params.get('login')
        if not login:
            return None, _('ID or password is incorrect.')
        password = password or request.params.get('password')
        dbuser = request.dbsession.query(cls).filter_by(
            login=make_id(login, 'token', EMAIL_LEN)).first()

        if dbuser is None:
            if 'authorities' in request.registry:
                for authority in request.registry['authorities'].values():
                    dbuser, error = authority.get(
                        request, login, password, cls)
                    if dbuser is not None or error is not None:
                        return dbuser, error
            return None, _('ID or password is incorrect.')

        if dbuser.authority:
            if 'authorities' not in request.registry or \
               dbuser.authority not in request.registry['authorities']:
                return None, _('Authority not available.')
            error = request.registry['authorities'][
                dbuser.authority].check(request, login, password, dbuser)
            if error:
                return None, error
            password = None

        if password is not None and not dbuser.check_password(password):
            return None, _('ID or password is incorrect.')
        if dbuser.status == 'locked':
            return None, _('Your account is locked.')
        if dbuser.status not in ('administrator', 'active'):
            return None, _('Your account is not active.')
        if dbuser.status != 'administrator' and dbuser.expiration \
           and dbuser.expiration < date.today():
            return None, _('Your account has expired.')

        dbuser.last_login = datetime.now()
        return dbuser, None

    # -------------------------------------------------------------------------
    def set_session(self, request):
        """Set up user session (``session['user']``).

        :type  request: pyramid.request.Request
        :param request:
            Current request.

        It saves in session the following values:

        * ``lang``: user language
        * ``theme``: user theme
        * ``user``: user dictionary

        The user dictionary includes:

        * ``user_id``: user ID
        * ``login``: user login
        * ``email``: user e-mail
        * ``name``: user first name and last name
        * ``attachment``: attachment ID
        * ``principals``: list of principals (premission groups) (see
          ":ref:`Pyramid Security <pyramid:security_chapter>`" for more
          information)
        """
        # Language
        settings = request.registry.settings
        if self.language:
            langs = settings_get_list(settings, 'languages', ('en',))
            request.session['lang'] = \
                (self.language in langs and self.language) or \
                (self.language[0:2] in langs and self.language[0:2]) or \
                request.registry['settings']['language']

        # Theme
        if self.theme and self.theme in request.registry['themes']:
            request.session['theme'] = self.theme
        else:
            request.session['theme'] = request.registry['settings']['theme']

        # Groups
        groups = set()
        principals = set()
        for dbgroup in self.groups:
            groups.add(dbgroup.group_id)
            for dbprofile in dbgroup.profiles:
                principals |= {k.principal for k in dbprofile.principals}
        groups = tuple(groups)

        # Principals
        if self.status == 'administrator':
            principals = ('system.administrator',)
        else:
            principals |= {
                k.principal for k in
                request.dbsession.query(DBProfilePrincipal)
                .join((DBProfile, DBUser.profiles))
                .join((DBProfilePrincipal, DBProfile.principals))
                .filter(DBUser.user_id == self.user_id)}
            principals = tuple(principals)

        # User information
        request.session['user'] = {
            'user_id': self.user_id,
            'login': self.login,
            'email': self.email,
            'name': '{0} {1}'.format(
                self.first_name or '', self.last_name).strip(),
            'picture': attachment_url(
                request, 'Users', self.attachments_key, self.picture),
            'principals': principals,
            'groups': groups}

        # Reset paging
        request.session['paging'] = (
            self.page_size if self.page_size else
            request.registry['settings']['page-size'], {})

        # Reset modes and menu
        if 'modes' in request.session:
            request.session['modes'][2] = None
        if 'menu' in request.session:
            del request.session['menu']

    # -------------------------------------------------------------------------
    @classmethod
    def load_administrator(cls, dbsession, record):
        """Load the administrator user from INI configuration file.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :param dict record:
            Dictionary representing the administrator configuration.
        :rtype: ``None`` or :class:`pyramid.i18n.TranslationString`
        :return:
            ``None`` or error message.
        """
        # Check user existence
        if not record.get('login'):
            return _('Login is missing.')
        login = make_id(record['login'], 'token', EMAIL_LEN)
        dbuser = dbsession.query(cls.login).filter_by(login=login).first()
        if dbuser is not None:
            return None

        # Complete record
        record['status'] = 'administrator'
        record['email_hidden'] = True

        # Check final record and create user
        error = cls.record_format(record)
        if error:
            return error
        dbuser = cls(**record)

        dbsession.add(dbuser)
        return None

    # -------------------------------------------------------------------------
    @classmethod
    def xml2db(cls, dbsession, user_elt, error_if_exists=True, kwargs=None):
        """Load a user from a XML element.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :type  user_elt: lxml.etree.Element
        :param user_elt:
            User XML element.
        :param bool error_if_exists: (default=True)
            It returns an error if user already exists.
        :param dict kwargs: (optional)
            Dictionary of keyword arguments with the key ``'profiles'``.
        :rtype: :class:`pyramid.i18n.TranslationString` or ``None``
        :return:
            Error message or ``None``.
        """
        # Check if already exists
        login = make_id(user_elt.findtext('login'), 'token', EMAIL_LEN)
        dbuser = dbsession.query(cls).filter_by(login=login).first()
        if dbuser is not None:
            if error_if_exists:
                return _('User "${l}" already exists.', {'l': login})
            return None

        # Create user
        record = cls.record_from_xml(login, user_elt)
        error = cls.record_format(record)
        if error:
            return error
        dbuser = cls(**record)
        dbsession.add(dbuser)

        # Fill extra tables
        return dbuser.xml2db_extra(dbsession, user_elt, kwargs)

    # -------------------------------------------------------------------------
    def xml2db_extra(self, dbsession, user_elt, kwargs):
        """Load extra information on a user from a XML element.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :type  user_elt: lxml.etree.Element
        :param user_elt:
            User XML element.
        :param dict kawrgs:
            Dictionary of keyword arguments with the key ``'profiles'``.
        :rtype: :class:`pyramid.i18n.TranslationString` or ``None``
        :return:
            Error message or ``None``.
        """
        dbsession.flush()

        # Add profiles
        profile_ids = kwargs.get('profiles') if kwargs else None
        if profile_ids:
            done = set()
            for elt in user_elt.findall('profiles/profile'):
                profile_id = elt.text
                if profile_id not in done and profile_id in profile_ids:
                    dbsession.add(DBUserProfile(
                        user_id=self.user_id, profile_id=profile_id))
                    done.add(profile_id)

    # -------------------------------------------------------------------------
    @classmethod
    def record_from_xml(cls, login, user_elt):
        """Convert an user XML element into a dictionary.

        :param str login:
            User login.
        :type  user_elt: lxml.etree.Element
        :param user_elt:
            User XML element.
        :rtype: dict
        """
        password_elt = user_elt.find('password')
        email_elt = user_elt.find('email')
        attachments_elt = user_elt.find('attachments')
        record = {
            'login': login,
            'status': user_elt.get('status', 'active'),
            'password': password_elt is not None and password_elt.text,
            'password_update':
            password_elt is not None and password_elt.get('updated'),
            'password_mustchange':
            password_elt is not None and
            password_elt.get('must-change') == 'true' or False,
            'first_name': user_elt.findtext('firstname'),
            'last_name': user_elt.findtext('lastname'),
            'honorific': user_elt.findtext('honorific'),
            'email': email_elt is not None and email_elt.text,
            'email_hidden': email_elt is not None and email_elt.get(
                'hidden') == 'true' or False,
            'language': user_elt.findtext('language'),
            'time_zone': user_elt.findtext('timezone'),
            'theme': user_elt.findtext('theme'),
            'attachments_key':
            attachments_elt is not None and attachments_elt.get('key') or None,
            'picture':
            attachments_elt is not None and attachments_elt.findtext(
                'picture') or None,
            'page_size': user_elt.findtext('page-size'),
            'expiration': user_elt.findtext('expiration'),
            'last_login': user_elt.get('last-login'),
            'account_update': user_elt.get('updated'),
            'account_creation': user_elt.get('created'),
            'authority': user_elt.findtext('authority'),
            'authority_check': user_elt.find('authority').get(
                'checked') if user_elt.find('authority') is not None else None}
        return record

    # -------------------------------------------------------------------------
    @classmethod
    def record_format(cls, record):
        """Check and possibly correct a record before inserting it in the
        database.

        :param dict record:
            Dictionary of values to check.
        :rtype: ``None`` or :class:`pyramid.i18n.TranslationString`
        :return:
            ``None`` or error message.
        """
        # pylint: disable = too-many-return-statements
        for k in [i for i in record if record[i] is None]:
            del record[k]

        # Login
        if not record.get('login'):
            return _('User without login.')
        record['login'] = make_id(record['login'], 'token', EMAIL_LEN)

        # Password
        if not record.get('password'):
            return _('User "${l}" without password.', {'l': record['login']})
        if not record['password'].startswith('$'):
            record['password'] = hashpw(
                record['password'].encode('utf8'), gensalt()).decode('utf8')

        # Name
        if not record.get('last_name'):
            return _('User "${l}" without last name.', {'l': record['login']})
        record['last_name'] = normalize_spaces(record['last_name'], NAME_LEN)
        if record.get('first_name'):
            record['first_name'] = normalize_spaces(
                record['first_name'], NAME_LEN)
        if (record.get('honorific') or 'Mr') \
           not in cls.honorific.property.columns[0].type.enums:
            return _('User "${l}" with unknown honorific title.',
                     {'l': record['login']})

        # Email
        if not record.get('email'):
            return _('User "${l}" without email.', {'l': record['login']})
        record['email'] = record['email'][0:EMAIL_LEN]
        if not Mailing.is_valid(record['email']):
            return _('Invalid email address: ${e}', {'e': record['email']})

        # Language
        if record.get('language'):
            record['language'] = record['language'][0:5]

        # Authority
        if record.get('authority_check') and not record.get('authority'):
            del record['authority_check']

        # Dates
        cls.record_convert_dates(record)
        return None

    # -------------------------------------------------------------------------
    @classmethod
    def record_convert_dates(cls, record):
        """Possibly convert dates of a record.

        :param dict record:
            Dictionary of values to check.
        """
        if 'last_login' in record and \
           not isinstance(record['last_login'], datetime):
            record['last_login'] = datetime.strptime(
                record['last_login'], '%Y-%m-%dT%H:%M:%S')

        if 'password_update' in record and \
           not isinstance(record['password_update'], datetime):
            record['password_update'] = datetime.strptime(
                record['password_update'], '%Y-%m-%dT%H:%M:%S')

        if 'expiration' in record and \
           not isinstance(record['expiration'], (date, datetime)):
            record['expiration'] = datetime.strptime(
                record['expiration'], '%Y-%m-%d').date()

        if 'account_creation' in record and \
           not isinstance(record['account_creation'], datetime):
            record['account_creation'] = datetime.strptime(
                record['account_creation'], '%Y-%m-%dT%H:%M:%S')

        if 'account_update' in record and \
           not isinstance(record['account_update'], datetime):
            record['account_update'] = datetime.strptime(
                record['account_update'], '%Y-%m-%dT%H:%M:%S')

        if 'authority_check' in record and \
           not isinstance(record['authority_check'], datetime):
            record['authority_check'] = datetime.strptime(
                record['authority_check'], '%Y-%m-%dT%H:%M:%S')

    # -------------------------------------------------------------------------
    def db2xml(self, dbsession=None):  # noqa
        """Serialize a user to a XML representation.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession: (optional)
            SQLAlchemy session.
        :rtype: lxml.etree.Element
        """
        # pylint: disable = too-many-branches, unused-argument
        user_elt = etree.Element('user')
        if self.status != 'active':
            user_elt.set('status', self.status)
        user_elt.set(
            'created', self.account_creation.isoformat().partition('.')[0])
        if self.account_update and \
           self.account_update != self.account_creation:
            user_elt.set(
                'updated', self.account_update.isoformat().partition('.')[0])
        if self.last_login:
            user_elt.set(
                'last-login', self.last_login.isoformat().partition('.')[0])

        etree.SubElement(user_elt, 'login').text = self.login

        elt = etree.SubElement(user_elt, 'password')
        elt.text = self.password
        if self.password_update:
            elt.set(
                'updated', self.password_update.isoformat().partition('.')[0])
        if self.password_mustchange:
            elt.set('must-change', 'true')

        if self.first_name:
            etree.SubElement(user_elt, 'firstname').text = self.first_name
        etree.SubElement(user_elt, 'lastname').text = self.last_name
        if self.honorific:
            etree.SubElement(user_elt, 'honorific').text = self.honorific

        elt = etree.SubElement(user_elt, 'email')
        elt.text = self.email
        if self.email_hidden:
            elt.set('hidden', 'true')

        if self.language:
            etree.SubElement(user_elt, 'language').text = self.language
        if self.time_zone:
            etree.SubElement(user_elt, 'timezone').text = self.time_zone
        if self.theme:
            etree.SubElement(user_elt, 'theme').text = self.theme
        if self.attachments_key:
            elt = etree.SubElement(
                user_elt, 'attachments', key=self.attachments_key)
            if self.picture:
                etree.SubElement(elt, 'picture').text = self.picture
        if self.page_size:
            etree.SubElement(user_elt, 'page-size').text = str(self.page_size)
        if self.expiration:
            etree.SubElement(user_elt, 'expiration').text = \
                self.expiration.isoformat()

        if self.authority:
            elt = etree.SubElement(user_elt, 'authority')
            elt.text = self.authority
            if self.authority_check:
                elt.set(
                    'checked',
                    self.authority_check.isoformat().partition('.')[0])

        self.db2xml_extra(user_elt)

        return user_elt

    # -------------------------------------------------------------------------
    def db2xml_extra(self, user_elt):
        """Serialize depedencies of a user to a XML representation.

        :type  user_elt: lxml.etree.Element
        :param user_elt:
            User XML element.
        """
        # Profiles
        if self.profiles:
            elt = etree.SubElement(user_elt, 'profiles')
            for item in self.profiles:
                etree.SubElement(elt, 'profile').text = item.profile_id

    # -------------------------------------------------------------------------
    @classmethod
    def paging_filter(cls, request, form, user_filter, user_paging):
        """Filter for users.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :type  user_filter: .lib.filter.Filter
        :param user_filter:
            Filter for users.
        :type  user_paging: .lib.paging.Paging
        :param user_paging:
            Paging for users.
        :rtype: str
        """
        translate = request.localizer.translate
        html = '<div class="cioPagingPagerFilter cioFlexRowContainer">\n'

        html += '<div class="cioPagingPager cioFlexItem">'\
            '{page_size} {pager}</div>\n'.format(
                page_size=form.select(
                    'page_size', '', PAGE_SIZES, True,
                    title=translate(_('Lines per page'))),
                pager=user_paging.pager_top())

        html += '<div class="cioPagingFilter">'
        if not user_filter.is_empty():
            html += '<span class="cioFilterConditions">{0}</span>'.format(
                user_filter.html_conditions())
        html += '{inputs} <span class="cioFilterSubmit">{submit}</span>'\
            '</div>\n'.format(
                inputs=user_filter.html_inputs(form),
                submit=form.submit(
                    'filter', translate(_('Filter')),
                    class_='cioFilterButton'))

        html += '</div>\n'
        return html

    # -------------------------------------------------------------------------
    def tab4view(self, request, tab_index, form):
        """Generate the tab content of user account.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param int index:
            Index of the tab.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :rtype: webhelpers2.html.literal
        """
        if tab_index == 0:
            return self._tab4view_information(request, form)
        if tab_index == 1:
            return self._tab4view_preferences(request, form)
        if tab_index == 2:
            return self._tab4view_profiles(request)
        if tab_index == 3:
            return self._tab4view_groups(request)
        return ''

    # -------------------------------------------------------------------------
    def _tab4view_information(self, request, form):
        """Generate the information tab.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :rtype: webhelpers2.html.literal
        """
        # Identify
        i_editor = request.has_permission('user-edit') or \
            self.user_id == request.session['user']['user_id']
        translate = request.localizer.translate
        html = HTML.h3(translate(_('Identity')))
        html += form.grid_item(translate(_('Login:')), self.login, clear=True)
        html += form.grid_item(
            translate(_('Title:')),
            translate(USER_HONORIFIC_LABELS.get(self.honorific))
            if self.honorific else None, clear=True)
        html += form.grid_item(
            translate(_('First Name:')), self.first_name, clear=True)
        html += form.grid_item(
            translate(_('Last Name:')), self.last_name, clear=True)
        if not self.email_hidden or i_editor:
            html += form.grid_item(
                translate(_('Email:')), self.email, clear=True)
        html += form.grid_item(
            translate(_('Language:')), self.language, clear=True)
        html += form.grid_item(
            translate(_('Time Zone:')), self.time_zone, clear=True)

        # Security
        html += HTML.h3(translate(_('Security')))
        html += form.grid_item(
            translate(_('Authority:')), self.authority, clear=True)
        html += form.grid_item(
            translate(_('Status:')),
            translate(self.status_labels[self.status]), clear=True)
        html += form.grid_item(
            translate(_('Creation:')), translate(age(self.account_creation)),
            title=self.account_creation.isoformat(' ').partition('.')[0],
            clear=True)
        html += form.grid_item(
            translate(_('Password:')),
            self.password_mustchange and translate(
                _('changed during next connexion')), clear=True)
        if self.account_update:
            html += form.grid_item(
                translate(_('Update:')), translate(age(self.account_update)),
                title=self.account_update.isoformat(' ').partition('.')[0],
                clear=True)
        if self.expiration:
            html += form.grid_item(
                translate(_('Expiration:')), self.expiration.isoformat(),
                clear=True)
        if self.last_login:
            html += form.grid_item(
                translate(_('Last connection:')),
                translate(age(self.last_login)),
                title=self.last_login.isoformat(' ').partition('.')[0],
                clear=True)

        return html

    # -------------------------------------------------------------------------
    def _tab4view_preferences(self, request, form):
        """Generate the preferences tab.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        html = ''
        html += form.grid_item(
            translate(_('Hide e-mail:')),
            self.email_hidden and translate(_('yes')), clear=True)
        lang = request.session.get('lang', 'en')
        theme = request.registry['themes'].get(self.theme)
        theme = theme['name'].get(lang, self.theme) if theme else ''
        html += form.grid_item(translate(_('Theme:')), theme, clear=True)
        if self.page_size:
            html += form.grid_item(
                translate(_('Lines per page:')), str(self.page_size),
                clear=True)

        return html or _('No preferences.')

    # -------------------------------------------------------------------------
    def _tab4view_profiles(self, request):
        """Generate the profiles tab.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        if not self.profiles:
            return translate(_('No attributed profile.'))

        html = '<table>\n<thead>\n'\
            '<tr><th>{label}</th><th>{description}</th></tr>\n'\
            '</thead>\n<tbody>\n'.format(
                label=translate(_('Label')),
                description=translate(_('Description')))
        for dbprofile in sorted(self.profiles, key=lambda k: k.profile_id):
            html += \
                '<tr><th><a href="{profile_view}">{label}</a></th>'\
                '<td>{description}</td></tr>\n'.format(
                    profile_view=request.route_path(
                        'profile_view', profile_id=dbprofile.profile_id),
                    label=dbprofile.label(request),
                    description=dbprofile.description(request))
        html += '</tbody>\n</table>\n'

        return literal(html)

    # -------------------------------------------------------------------------
    def _tab4view_groups(self, request):
        """Generate the groups tab.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        if not self.groups:
            return translate(_('This user is in any group.'))

        html = '<table>\n<thead>\n'\
            '<tr><th>{label}</th><th>{description}</th></tr>\n'\
            '</thead>\n<tbody>\n'.format(
                label=translate(_('Label')),
                description=translate(_('Description')))
        for dbgroup in sorted(self.groups, key=lambda k: k.group_id):
            html += \
                '<tr><th><a href="{group_view}">{label}</a></th>'\
                '<td>{description}</td></tr>\n'.format(
                    group_view=request.route_path(
                        'group_view', group_id=dbgroup.group_id),
                    label=dbgroup.label(request),
                    description=dbgroup.description(request))
        html += '</tbody>\n</table>\n'
        return literal(html)

    # -------------------------------------------------------------------------
    @classmethod
    def settings_schema(cls, request, profiles, groups, dbuser=None):
        """Return a Colander schema to edit user account.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param dict profiles:
            A dictionary such as ``{profile_id: (label, description),...}``.
        :param dict groups:
            A dictionary such as ``{group_id: (label, description),...}``.
        :type  dbuser: DBUser
        :param dbuser: (optional)
            Current user SqlAlchemy object.
        :rtype: tuple
        :return:
            A tuple such as ``(schema, defaults)``.
        """
        # Identity
        schema = colander.SchemaNode(colander.Mapping())

        schema.add(colander.SchemaNode(
            colander.String(), name='login',
            validator=colander.All(
                colander.Regex(r'^[\w@_.-]+$'),
                colander.Length(min=2, max=EMAIL_LEN))))

        schema.add(colander.SchemaNode(
            colander.String(), name='honorific',
            validator=colander.OneOf(
                cls.honorific.property.columns[0].type.enums), missing=None))
        schema.add(colander.SchemaNode(
            colander.String(), name='first_name',
            validator=colander.Length(max=NAME_LEN), missing=None))
        schema.add(colander.SchemaNode(
            colander.String(), name='last_name',
            validator=colander.Length(max=NAME_LEN)))
        schema.add(colander.SchemaNode(
            colander.String(), name='email',
            validator=colander.All(
                colander.Email(), colander.Length(max=LABEL_LEN))))
        schema.add(colander.SchemaNode(
            colander.String(), name='language',
            validator=colander.OneOf(settings_get_list(
                request.registry.settings, 'languages', ['en'])),
            missing=None))
        schema.add(colander.SchemaNode(
            colander.String(), name='time_zone',
            validator=colander.OneOf(common_timezones),
            missing=None))

        # Security
        i_admin = request.has_permission('system.administrator')
        if 'authorities' in request.registry and i_admin:
            schema.add(colander.SchemaNode(
                colander.String(), name='authority',
                validator=colander.All(
                    colander.Regex(r'^[0-9a-z-]+$'),
                    colander.Length(max=ID_LEN)),
                missing=None))
        if dbuser is None or (
                dbuser.user_id != request.session['user']['user_id'] and
                (dbuser.status != 'administrator' or i_admin) and
                request.has_permission('user-edit')):
            status = list(USER_STATUS_LABELS.keys())
            if not i_admin:
                del status[status.index('administrator')]
            schema.add(colander.SchemaNode(
                colander.String(), name='status',
                validator=colander.OneOf(status)))
        password_min_length = request.registry['settings'][
            'password-min-length']
        if dbuser is None:
            schema.add(colander.SchemaNode(
                colander.String(), name='password1',
                validator=colander.Length(min=password_min_length)))
            schema.add(colander.SchemaNode(
                colander.String(), name='password2',
                validator=SameAs(request, 'password1', _(
                    'The two passwords are not identical.'))))
        else:
            schema.add(colander.SchemaNode(
                colander.String(), name='password1', missing=None,
                validator=colander.Length(min=password_min_length)))
            schema.add(colander.SchemaNode(
                colander.String(), name='password2', missing=None,
                validator=SameAs(request, 'password1', _(
                    'The two passwords are not identical.'))))
        schema.add(colander.SchemaNode(
            colander.Boolean(), name='password_mustchange', missing=False))

        # Preferences
        schema.add(colander.SchemaNode(
            colander.Boolean(), name='email_hidden', missing=False))
        if len(request.registry['themes']) > 1:
            schema.add(colander.SchemaNode(
                colander.String(), name='theme',
                validator=colander.OneOf(request.registry['themes']),
                missing=None))
        schema.add(colander.SchemaNode(
            colander.Integer(), name='page_size',
            validator=colander.OneOf(PAGE_SIZES[1:-1]), missing=None))

        if request.has_permission('user-create'):
            cls._settings_schema_creator(profiles, groups, schema)

        # Defaults
        if dbuser is None:
            defaults = {'status': 'active'}
        else:
            defaults = {}
            for dbprofile in dbuser.profiles:
                defaults['pfl:{0}'.format(dbprofile.profile_id)] = True
            for dbgroup in dbuser.groups:
                defaults['grp:{0}'.format(dbgroup.group_id)] = True

        return schema, defaults

    # -------------------------------------------------------------------------
    @classmethod
    def _settings_schema_creator(cls, profiles, groups, schema):
        """Complete the Colander schema if I am a creator.

        :param dict profiles:
            A dictionary such as ``{profile_id: (label, description),...}``.
        :param dict groups:
            A dictionary such as ``{group_id: (label, description),...}``.
        :type  schema: colander.SchemaNode
        :param schema:
            Current schema to complete.
        """
        # Expiration
        schema.add(colander.SchemaNode(
            colander.Date(), name='expiration', missing=None))

        # Profiles
        for profile_id in profiles:
            schema.add(colander.SchemaNode(
                colander.Boolean(), name='pfl:{0}'.format(profile_id),
                missing=False))

        # Groups
        for group_id in groups:
            schema.add(colander.SchemaNode(
                colander.Boolean(), name='grp:{0}'.format(group_id),
                missing=False))

    # -------------------------------------------------------------------------
    @classmethod
    def tab4edit(cls, request, tab_index, form, profiles, groups, dbuser=None):
        """Generate the tab content of user account for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param int tab_index:
            Index of the tab.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :param dict profiles:
            A dictionary such as ``{profile_id: (label, description),...}``.
        :param dict groups:
            A dictionary such as ``{group_id: (label, description),...}``.
        :type  dbuser: DBUser
        :param dbuser: (optional)
            Current user SqlAlchemy object.
        :rtype: webhelpers2.html.literal
        """
        # pylint: disable = too-many-arguments
        if tab_index == 0:
            return cls._tab4edit_information(request, form, dbuser)
        if tab_index == 1:
            return cls._tab4edit_preferences(request, form)
        if tab_index == 2:
            return cls._tab4edit_profiles(request, form, profiles)
        if tab_index == 3:
            return cls._tab4edit_groups(request, form, groups)
        return ''

    # -------------------------------------------------------------------------
    @classmethod
    def _tab4edit_information(cls, request, form, dbuser):
        """Generate the information tab for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :type  dbuser: DBUser
        :param dbuser:
            Current user SqlAlchemy object.
        :rtype: webhelpers2.html.literal
        """
        # Identify
        i_admin = request.has_permission('system.administrator')
        has_authority = dbuser is not None and dbuser.authority is not None
        translate = request.localizer.translate
        html = HTML.h3(translate(_('Identity')))
        if has_authority and not i_admin:
            html += form.grid_item(
                translate(_('Login:')), dbuser.login, clear=True)
            html += form.hidden('login', dbuser.login)
        else:
            html += form.grid_text(
                'login', translate(_('Login:')), maxlength=EMAIL_LEN,
                required=True, clear=True)
        html += form.grid_select(
            'honorific', translate(_('Title:')),
            [('', ' ')] + list(cls.honorific_labels.items()), clear=True)
        html += form.grid_text(
            'first_name', translate(_('First Name:')), maxlength=NAME_LEN,
            clear=True)
        html += form.grid_text(
            'last_name', translate(_('Last Name:')), maxlength=NAME_LEN,
            required=True, clear=True)
        html += form.grid_text(
            'email', translate(_('Email:')), maxlength=EMAIL_LEN,
            required=True, clear=True)
        html += form.grid_select(
            'language', translate(_('Language:')),
            [('', ' ')] + sorted(settings_get_list(
                request.registry.settings, 'languages', ['en'])), clear=True)
        html += form.grid_select(
            'time_zone', translate(_('Time Zone:')),
            [('', ' ')] + list(common_timezones), clear=True)

        # Security
        html += HTML.h3(translate(_('Security')))
        if 'authorities' in request.registry and \
           request.registry['authorities']:
            if i_admin:
                html += form.grid_select(
                    'authority', translate(_('Authority:')),
                    [('', ' ')] + sorted(request.registry['authorities']),
                    clear=True)
            elif has_authority:
                html += form.grid_item(
                    translate(_('Authority:')), dbuser.authority, clear=True)
        if dbuser is None or (
                dbuser.user_id != request.session['user']['user_id'] and
                (dbuser.status != 'administrator' or i_admin) and
                request.has_permission('user-edit')):
            status = cls.status_labels.items() if i_admin else \
                [k for k in cls.status_labels.items()
                 if k[0] != 'administrator']
            html += form.grid_select(
                'status', translate(_('Status:')), status, clear=True)
        else:
            html += form.grid_item(
                translate(_('Status:')),
                translate(dbuser.status_labels[dbuser.status]), clear=True)
        if not has_authority or i_admin:
            html += form.grid_password(
                'password1', translate(_('Password:')), maxlength=64,
                required=dbuser is None, clear=True)
            html += form.grid_password(
                'password2', translate(_('Confirmation:')), maxlength=64,
                required=dbuser is None, clear=True)
            html += form.grid_custom_checkbox(
                'password_mustchange', translate(_('Force change:')),
                clear=True)
        if request.has_permission('user-create'):
            html += form.grid_text(
                'expiration', translate(_('Expiration:')), maxlength=10,
                hint=translate(_('Format: YYYY-MM-DD')),
                class_='cioFormItem cioDate', clear=True)

        return html

    # -------------------------------------------------------------------------
    @classmethod
    def _tab4edit_preferences(cls, request, form):
        """Generate the preferences tab for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        html = form.grid_custom_checkbox(
            'email_hidden', translate(_('Hide e-mail:')), clear=True)
        if len(request.registry['themes']) > 1:
            lang = request.session.get('lang', 'en')
            themes = [(i, k['name'].get(lang, i))
                      for i, k in request.registry['themes'].items()]
            html += form.grid_select(
                'theme', translate(_('Theme:')),
                [('', ' ')] + sorted(themes, key=lambda k: k[1]), clear=True)
        html += form.grid_select(
            'page_size', translate(_('Lines per page:')), PAGE_SIZES[:-1],
            clear=True)

        return html

    # -------------------------------------------------------------------------
    @classmethod
    def _tab4edit_profiles(cls, request, form, profiles):
        """Generate the profiles tab for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :param dict profiles:
            A dictionary such as ``{profile_id: (label, description),...}``.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        if not profiles:
            return translate(_('No available profile.'))

        if not request.has_permission('user-create'):
            return translate(
                _('You do not have the rigths to edit profiles.'))

        html = '<table>\n<thead>\n'\
            '<tr><th></th><th>{label}</th>'\
            '<th>{description}</th></tr>\n</thead>\n<tbody>\n'.format(
                label=translate(_('Label')),
                description=translate(_('Description')))
        for profile_id in sorted(profiles):
            html += \
                '<tr><td>{selected}</td>'\
                '<th><label for="{id}">{label}</label></th>'\
                '<td>{description}</td></tr>\n'.format(
                    selected=form.custom_checkbox(
                        'pfl:{0}'.format(profile_id)),
                    id='pfl{0}'.format(profile_id),
                    label=profiles[profile_id][0],
                    description=profiles[profile_id][1])
        html += '</tbody>\n</table>\n'

        return literal(html)

    # -------------------------------------------------------------------------
    @classmethod
    def _tab4edit_groups(cls, request, form, groups):
        """Generate the groups tab for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :param dict groups:
            A dictionary such as ``{group_id: (label, description),...}``.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        if not groups:
            return translate(_('No available group.'))
        if not request.has_permission('user-create'):
            return translate(
                _('You do not have the rigths to edit groups.'))

        html = '<table>\n<thead>\n'\
            '<tr><th></th><th>{label}</th>'\
            '<th>{description}</th></tr>\n</thead>\n<tbody>\n'.format(
                label=translate(_('Label')),
                description=translate(_('Description')))
        for group_id in sorted(groups):
            html += \
                '<tr><td>{selected}</td>'\
                '<th><label for="{id}">{label}</label></th>'\
                '<td>{description}</td></tr>\n'.format(
                    selected=form.custom_checkbox('grp:{0}'.format(group_id)),
                    id='grp{0}'.format(group_id),
                    label=groups[group_id][0],
                    description=groups[group_id][1])
        html += '</tbody>\n</table>\n'

        return literal(html)


# =============================================================================
class DBUserProfile(DBDeclarativeClass):
    """Class to link users with their profiles (many-to-many)."""
    # pylint: disable = too-few-public-methods

    __tablename__ = 'users_profiles'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    user_id = Column(
        Integer, ForeignKey('users.user_id', ondelete='CASCADE'),
        primary_key=True)
    profile_id = Column(
        String(ID_LEN), ForeignKey('profiles.profile_id', ondelete='CASCADE'),
        primary_key=True)
