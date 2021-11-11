# -*- coding: utf-8 -*-
"""SQLAlchemy-powered model definitions for LDAP."""

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from lxml import etree
from webhelpers2.html import HTML, literal
import colander

from ....lib.i18n import _
from ....lib.utils import encrypt, make_id, deltatime_label
from ....models import DBDeclarativeClass, ID_LEN
from ..relaxng import RELAXNG_CIOLDAP

LDAP_SUFFIX = 'cioldap'
LDAP_USER_FILTER = '(&(objectclass=inetOrgPerson)(uid=_UID_))'
LDAP_FIELD_FIRSTNAME = 'givenName'
LDAP_FIELD_LASTNAME = 'sn'
LDAP_FIELD_EMAIL = 'mail'
LDAP_CHECK_INTERVAL = 3600


# =============================================================================
class DBLdap(DBDeclarativeClass):
    """SQLAlchemy-powered LDAP class."""

    __tablename__ = 'ldap'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    ldap_id = Column(Integer, primary_key=True)
    host = Column(String(128), default='localhost')
    port = Column(Integer, default=389)
    ssl = Column(Boolean(name='ssl'), default=False)
    check_interval = Column(Integer, default=LDAP_CHECK_INTERVAL)
    root_dn = Column(String(128))
    root_password = Column(String(128))
    base = Column(String(128), nullable=False)
    user_dn = Column(String(128), nullable=False)
    user_filter = Column(String(128), nullable=False)
    field_first_name = Column(String(32))
    field_last_name = Column(String(32), default='sn')
    field_email = Column(String(32), default='mail')

    user_profiles = relationship('DBLdapProfile', cascade='all, delete')

    suffix = LDAP_SUFFIX

    # -------------------------------------------------------------------------
    @classmethod
    def xml2db(cls, dbsession, ldap_elt):
        """Load LDAP settings from a XML element.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :type  ldap_elt: lxml.etree.Element
        :param ldap_elt:
            Ldap XML element.
        :rtype: :class:`pyramid.i18n.TranslationString` or ``None``
        :return:
            Error message or ``None``.
        """
        if ldap_elt is None:
            return None

        # Clean up old settings
        for dbldap in dbsession.query(cls):
            dbsession.delete(dbldap)

        # Create LDAP settings
        ldap_record = cls.record_from_xml(ldap_elt)
        error = cls.record_format(ldap_record)
        if error:
            return error
        dbldap = cls(**ldap_record)
        dbsession.add(dbldap)

        # Add profiles
        dbsession.flush()
        namespace = '{{{0}}}'.format(RELAXNG_CIOLDAP['namespace'])
        user_elt = ldap_elt.find('{0}user'.format(namespace))
        for elt in user_elt.xpath('ns0:profiles/ns0:profile', namespaces={
                'ns0': RELAXNG_CIOLDAP['namespace']}):
            dbldap.user_profiles.append(
                DBLdapProfile(profile_id=make_id(elt.text, 'token', ID_LEN)))
        return None

    # -------------------------------------------------------------------------
    @classmethod
    def record_from_xml(cls, ldap_elt):
        """Convert a LDAP XML element into a dictionary.

        :type  ldap_elt: lxml.etree.Element
        :param ldap_elt:
            LDAP XML element.
        :rtype: dict
        """
        namespace = '{{{0}}}'.format(RELAXNG_CIOLDAP['namespace'])
        user_elt = ldap_elt.find('{0}user'.format(namespace))

        return {
            'host': ldap_elt.findtext(
                '{0}host'.format(namespace)) or 'localhost',
            'port': int(
                ldap_elt.findtext('{0}port'.format(namespace)) or '389'),
            'ssl': ldap_elt.findtext('{0}ssl'.format(namespace)) == 'true',
            'check_interval': int(
                ldap_elt.findtext('{0}check-interval'.format(namespace)) or
                LDAP_CHECK_INTERVAL),
            'root_dn': ldap_elt.findtext('{0}dn'.format(namespace)),
            'root_password': ldap_elt.findtext(
                '{0}password'.format(namespace)),
            'base': ldap_elt.findtext('{0}base'.format(namespace)),
            'user_dn': user_elt.findtext('{0}dn'.format(namespace)),
            'user_filter': (
                user_elt.findtext('{0}filter'.format(namespace)) or
                '(&(objectclass=inetOrgPerson)(uid=_UID_))'),
            'field_first_name': user_elt.findtext(
                '{0}first-name'.format(namespace)),
            'field_last_name': user_elt.findtext(
                '{0}last-name'.format(namespace)) or 'sn',
            'field_email': user_elt.findtext(
                '{0}email'.format(namespace)) or 'mail'}

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
        for k in [i for i in record if record[i] is None]:
            del record[k]

        password = record.get('root_password')
        if password and not record.get('root_dn'):
            del record['root_password']
        elif password and len(password) < 44:
            record['root_password'] = encrypt(password, 'ldap')

        if not record.get('base'):
            return _('No base for search.')

        if not record.get('user_dn'):
            return _('No DN for user.')
        if '_UID_' not in record['user_dn']:
            return _('_UID_ not found in user DN.')
        return None

    # -------------------------------------------------------------------------
    def db2xml(self):
        """Serialize LDAP settings to a XML representation.

        :rtype: lxml.etree.Element
        """
        ldap_elt = etree.Element('{{{0}}}ldap'.format(
            RELAXNG_CIOLDAP['namespace']))
        etree.SubElement(ldap_elt, 'host').text = self.host
        etree.SubElement(ldap_elt, 'port').text = str(self.port)
        if self.ssl:
            etree.SubElement(ldap_elt, 'ssl').text = 'true'
        etree.SubElement(ldap_elt, 'check-interval').text = \
            str(self.check_interval)
        if self.root_dn:
            etree.SubElement(ldap_elt, 'dn').text = self.root_dn
            etree.SubElement(ldap_elt, 'password').text = self.root_password
        etree.SubElement(ldap_elt, 'base').text = self.base

        user_elt = etree.SubElement(ldap_elt, 'user')
        etree.SubElement(user_elt, 'dn').text = self.user_dn
        etree.SubElement(user_elt, 'filter').text = self.user_filter
        if self.field_first_name:
            etree.SubElement(user_elt, 'first-name').text = \
                self.field_first_name
        etree.SubElement(user_elt, 'last-name').text = self.field_last_name
        etree.SubElement(user_elt, 'email').text = self.field_email
        if self.user_profiles:
            elt = etree.SubElement(user_elt, 'profiles')
            for dbprofile in self.user_profiles:
                etree.SubElement(elt, 'profile').text = dbprofile.profile_id

        return ldap_elt

    # -------------------------------------------------------------------------
    @classmethod
    def attachments2directory(cls, attachments, directory):
        """Copy from attachments directory the file corresponding to the
        ldap.

        :param str attachments:
            Absolute path to the attachements directory.
        :param str directory:
            The backup directory.
        """

    # -------------------------------------------------------------------------
    def sheet4view(self, request, form, profile_labels):
        """Generate the sheet content.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :parem dict profile_labels:
            Label in user language of all profile.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        html = form.grid_item(translate(_('Host:')), self.host, clear=True)
        html += form.grid_item(translate(_('Port:')), self.port, clear=True)
        html += form.grid_item(
            translate(_('SSL:')), self.ssl and translate(_('yes')), clear=True)
        html += form.grid_item(
            translate(_('Check interval:')),
            deltatime_label(
                seconds=self.check_interval or 0, lang=request.locale_name),
            clear=True)
        html += form.grid_item(
            translate(_('Root DN:')), self.root_dn, clear=True)
        html += form.grid_item(translate(_('Base:')), self.base, clear=True)

        html += HTML.h3(translate(_('User')))
        html += form.grid_item(
            translate(_('User DN:')), self.user_dn, clear=True)
        html += form.grid_item(
            translate(_('User filter:')), self.user_filter, clear=True)
        html += form.grid_item(
            translate(_('First name field:')), self.field_first_name,
            clear=True)
        html += form.grid_item(
            translate(_('Last name field:')), self.field_last_name, clear=True)
        html += form.grid_item(
            translate(_('Email field:')), self.field_email, clear=True)
        if self.user_profiles:
            labels = [
                profile_labels[k.profile_id]
                for k in self.user_profiles if k.profile_id in profile_labels]
            html += form.grid_item(
                translate(_('Attributed Profiles:')), '<br/>'.join(labels),
                clear=True)

        return html

    # -------------------------------------------------------------------------
    @classmethod
    def settings_schema(cls, profiles, dbldap=None):
        """Return a Colander schema to edit LDAP.

        :param dict profiles:
            A dictionary such as ``{profile_id: label,...}``.
        :type  dbldap: DBLdap
        :param dbldap: (optional)
            Current CIOLdap SqlAlchemy object.
        :rtype: tuple
        :return:
            A tuple such as ``(schema, defaults)``.
        """
        # Schema
        schema = colander.SchemaNode(colander.Mapping())
        schema.add(colander.SchemaNode(
            colander.String(), name='host',
            validator=colander.Length(max=128), missing='localhost'))
        schema.add(colander.SchemaNode(
            colander.Integer(), name='port', missing=389))
        schema.add(colander.SchemaNode(
            colander.Boolean(), name='ssl', missing=False))
        schema.add(colander.SchemaNode(
            colander.Integer(), name='check_interval',
            missing=LDAP_CHECK_INTERVAL))
        schema.add(colander.SchemaNode(
            colander.String(), name='root_dn',
            validator=colander.Length(max=128), missing=''))
        schema.add(colander.SchemaNode(
            colander.String(), name='root_password1',
            validator=colander.Length(max=43), missing=None))
        schema.add(colander.SchemaNode(
            colander.String(), name='base',
            validator=colander.Length(max=128)))

        schema.add(colander.SchemaNode(
            colander.String(), name='user_dn',
            validator=colander.Length(max=128)))
        schema.add(colander.SchemaNode(
            colander.String(), name='user_filter',
            validator=colander.Length(max=128), missing=LDAP_USER_FILTER))
        schema.add(colander.SchemaNode(
            colander.String(), name='field_first_name',
            validator=colander.Length(max=32), missing=LDAP_FIELD_FIRSTNAME))
        schema.add(colander.SchemaNode(
            colander.String(), name='field_last_name',
            validator=colander.Length(max=32), missing=LDAP_FIELD_LASTNAME))
        schema.add(colander.SchemaNode(
            colander.String(), name='field_email',
            validator=colander.Length(max=32), missing=LDAP_FIELD_EMAIL))

        # Profiles
        for profile_id in profiles:
            schema.add(colander.SchemaNode(
                colander.Boolean(), name='pfl:{0}'.format(profile_id),
                missing=False))

        # Defaults
        defaults = {}
        if dbldap is None:
            defaults = {
                'host': 'localhost', 'port': 389,
                'check_interval': LDAP_CHECK_INTERVAL,
                'user_filter': LDAP_USER_FILTER,
                'field_first_name': LDAP_FIELD_FIRSTNAME,
                'field_last_name': LDAP_FIELD_LASTNAME,
                'field_email': LDAP_FIELD_EMAIL}
        else:
            defaults = {}
            for dbprofile in dbldap.user_profiles:
                defaults['pfl:{0}'.format(dbprofile.profile_id)] = True

        return schema, defaults

    # -------------------------------------------------------------------------
    @classmethod
    def sheet4edit(cls, request, form, profiles):
        """Generate the tab content for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :param dict profiles:
            A dictionary such as ``{profile_id: label,...}``.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        html = form.grid_text(
            'host', translate(_('Host:')), maxlength=128, required=True,
            clear=True)
        html += form.grid_text(
            'port', translate(_('Port:')), maxlength=8, required=True,
            clear=True)
        html += form.grid_custom_checkbox(
            'ssl', translate(_('SSL:')), clear=True)
        html += form.grid_text(
            'check_interval', translate(_('Check interval:')), maxlength=8,
            required=True, hint=translate(_('In seconds.')), clear=True)
        html += form.grid_text(
            'root_dn', translate(_('Root DN:')), maxlength=128, clear=True)
        html += form.grid_password(
            'root_password1', translate(_('Root password:')), maxlength=64,
            clear=True)
        html += form.grid_text(
            'base', translate(_('Base:')), maxlength=128, required=True,
            clear=True)

        html += HTML.h3(translate(_('User')))
        html += form.grid_text(
            'user_dn', translate(_('User DN:')), maxlength=128, required=True,
            clear=True)
        html += form.grid_text(
            'user_filter', translate(_('User filter:')), maxlength=128,
            required=True, hint=translate(_('Use _UID_ in place of user ID.')),
            clear=True)
        html += form.grid_text(
            'field_first_name', translate(_('First name field:')),
            maxlength=32, clear=True)
        html += form.grid_text(
            'field_last_name', translate(_('Last name field:')),
            maxlength=32, required=True, clear=True)
        html += form.grid_text(
            'field_email', translate(_('Email field:')), maxlength=32,
            clear=True)
        if profiles:
            html += literal(
                '<div class="cioFormItem">'
                '<label><strong>{0}</strong></label><div><ul>'.format(
                    translate(_('Attributed Profiles:'))))
            for profile_id in sorted(profiles):
                html += literal('<li>{0} {1}</li>'.format(
                    form.custom_checkbox(
                        'pfl:{0}'.format(profile_id)),
                    profiles[profile_id]))
            html += literal('</ul></div><div class="cioClear"></div></div>')

        return html


# =============================================================================
class DBLdapProfile(DBDeclarativeClass):
    """Class to link LDAP with its profiles (one-to-many)."""
    # pylint: disable = too-few-public-methods

    __tablename__ = 'ldap_profiles'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    ldap_id = Column(
        Integer, ForeignKey('ldap.ldap_id', ondelete='CASCADE'),
        primary_key=True)
    profile_id = Column(
        String(ID_LEN), ForeignKey('profiles.profile_id', ondelete='CASCADE'),
        primary_key=True)
