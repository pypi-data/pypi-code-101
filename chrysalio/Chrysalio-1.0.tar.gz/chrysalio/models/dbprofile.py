# -*- coding: utf-8 -*-
"""SQLAlchemy-powered model definitions for profiles."""

from json import dumps

import colander
from sqlalchemy import Column, ForeignKey, String, Text, PickleType
from sqlalchemy.orm import relationship
from lxml import etree
from webhelpers2.html import HTML, literal

from ..lib.i18n import _, record_format_i18n
from ..lib.i18n import schema_i18n_labels, defaults_i18n_labels
from ..lib.i18n import view_i18n_labels, edit_i18n_labels
from ..lib.utils import make_id
from ..lib.xml import i18n_xml_text, db2xml_i18n_labels
from . import DBDeclarativeClass, ID_LEN, LABEL_LEN, DESCRIPTION_LEN
from .dbbase import DBBaseClass


# =============================================================================
class DBProfile(DBDeclarativeClass, DBBaseClass):
    """SQLAlchemy-powered profile class."""

    suffix = 'ciopfl'
    _settings_tabs = (_('Information'), _('Permissions'))

    __tablename__ = 'profiles'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    profile_id = Column(String(ID_LEN), primary_key=True)
    i18n_label = Column(Text(), nullable=False)
    i18n_description = Column(PickleType(1))

    principals = relationship('DBProfilePrincipal', cascade='all, delete')

    # -------------------------------------------------------------------------
    @classmethod
    def xml2db(cls, dbsession, profile_elt, error_if_exists=True, kwargs=None):
        """Load a profile from a XML element.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :type  profile_elt: lxml.etree.Element
        :param profile_elt:
            Profile XML element.
        :param bool error_if_exists: (default=True)
            It returns an error if profile already exists.
        :param dict kwargs: (optional)
            Dictionary of keyword arguments.
        :rtype: :class:`pyramid.i18n.TranslationString` or ``None``
        :return:
            Error message or ``None``.
        """
        # pylint: disable = unused-argument
        # Check if already exists
        profile_id = make_id(profile_elt.get('id'), 'token', ID_LEN)
        dbprofile = dbsession.query(cls).filter_by(
            profile_id=profile_id).first()
        if dbprofile is not None:
            if error_if_exists:
                return _('Profile "${p}" already exists.', {'p': profile_id})
            return None

        # Create profile
        record = cls.record_from_xml(profile_id, profile_elt)
        error = cls.record_format(record)
        if error:
            return error
        dbprofile = cls(**record)
        dbsession.add(dbprofile)

        # Add principals
        dbsession.flush()
        for elt in profile_elt.findall('principals/principal'):
            dbprofile.principals.append(
                DBProfilePrincipal(principal=elt.text))

        return None

    # -------------------------------------------------------------------------
    @classmethod
    def record_from_xml(cls, profile_id, profile_elt):
        """Convert an profile XML element into a dictionary.

        :param str profile_id:
            Profile ID.
        :type  profile_elt: lxml.etree.Element
        :param profile_elt:
            Profile XML element.
        :rtype: dict
        """
        return {
            'profile_id': profile_id,
            'i18n_label': dumps(
                i18n_xml_text(profile_elt, 'label'), ensure_ascii=False),
            'i18n_description': i18n_xml_text(profile_elt, 'description')}

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

        # Profile ID
        if not record.get('profile_id'):
            return _('Profile without ID.')
        record['profile_id'] = make_id(record['profile_id'], 'xmlid', ID_LEN)

        # Labels and descriptions
        if not record_format_i18n(record):
            return _('Profile without label.')
        if not record.get('i18n_description'):
            record['i18n_description'] = {}
        return None

    # -------------------------------------------------------------------------
    def db2xml(self, dbsession=None):
        """Serialize an profile to a XML representation.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession: (optional)
            SQLAlchemy session.
        :rtype: lxml.etree.Element
        """
        # pylint: disable = unused-argument
        profile_elt = etree.Element('profile')
        profile_elt.set('id', self.profile_id)

        # Labels and descriptions
        db2xml_i18n_labels(self, profile_elt, 3)

        # Principals
        if self.principals:
            elt = etree.SubElement(profile_elt, 'principals')
            for dbprincipal in self.principals:
                etree.SubElement(elt, 'principal').text = dbprincipal.principal

        return profile_elt

    # -------------------------------------------------------------------------
    def tab4view(self, request, tab_index, form):
        """Generate the tab content of a profile.

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
            return self._tab4view_permissions(request)
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
        translate = request.localizer.translate
        html = form.grid_item(
            translate(_('Identifier:')), self.profile_id, clear=True)
        html += view_i18n_labels(request, form, self)
        return html

    # -------------------------------------------------------------------------
    def _tab4view_permissions(self, request):
        """Generate the permission tab.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: webhelpers2.html.literal
        """
        active_mode = 'modes' in request.registry
        translate = request.localizer.translate
        html = ''
        active = [k.principal for k in self.principals]
        for group in request.registry['principals']:
            if not active_mode and group[0] == 'mode':
                continue
            html += HTML.h3(translate(group[1]))
            for principal in group[2]:
                if '{0}.{1}'.format(group[0], principal[0]) in active:
                    html += HTML.div('✔ {0}'.format(translate(principal[1])))
                else:
                    html += HTML.div('☐ {0}'.format(translate(principal[1])))
        return html

    # -------------------------------------------------------------------------
    @classmethod
    def settings_schema(cls, request, dbprofile=None):
        """Return a Colander schema to edit profile.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  dbprofile: DBProfile
        :param dbprofile: (optional)
            Current profile SqlAlchemy object.
        :rtype: tuple
        :return:
            A tuple such as ``(schema, defaults)``.
        """
        # Schema
        schema = colander.SchemaNode(colander.Mapping())
        if dbprofile is None:
            schema.add(colander.SchemaNode(
                colander.String(), name='profile_id',
                validator=colander.All(
                    colander.Regex(r'^[a-z][a-z0-9_]+$'),
                    colander.Length(min=2, max=ID_LEN))))

        schema_i18n_labels(request, schema, LABEL_LEN, DESCRIPTION_LEN)

        for group in request.registry['principals']:
            for principal in group[2]:
                schema.add(colander.SchemaNode(
                    colander.Boolean(), name='pcpl:{0}.{1}'.format(
                        group[0], principal[0]), missing=False))

        # Defaults
        if dbprofile is None:
            defaults = {}
        else:
            defaults = defaults_i18n_labels(dbprofile)
            for dbprincipal in dbprofile.principals:
                defaults['pcpl:{0}'.format(dbprincipal.principal)] = True

        return schema, defaults

    # -------------------------------------------------------------------------
    @classmethod
    def tab4edit(cls, request, tab_index, form, dbprofile=None):
        """Generate the tab content of profile for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param int tab_index:
            Index of the tab.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :type  dbprofile: DBProfile
        :param dbprofile: (optional)
            Current profile SqlAlchemy object.
        :rtype: webhelpers2.html.literal
        """
        if tab_index == 0:
            return cls._tab4edit_information(request, form, dbprofile)
        if tab_index == 1:
            return cls._tab4edit_permissions(request, form)
        return ''

    # -------------------------------------------------------------------------
    @classmethod
    def _tab4edit_information(cls, request, form, dbprofile):
        """Generate the information tab for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :type  dbprofile: DBProfile
        :param dbprofile:
            Current profile SqlAlchemy object.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        if dbprofile is None:
            html = form.grid_text(
                'profile_id', translate(_('Identifier:')), required=True,
                maxlength=ID_LEN, clear=True)
        else:
            html = form.grid_item(
                translate(_('Identifier:')), dbprofile.profile_id, clear=True)
        html += edit_i18n_labels(request, form, LABEL_LEN, DESCRIPTION_LEN)
        return html

    # -------------------------------------------------------------------------
    @classmethod
    def _tab4edit_permissions(cls, request, form):
        """Generate the permission tab for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :rtype: webhelpers2.html.literal
        """
        active_mode = 'modes' in request.registry
        translate = request.localizer.translate
        html = ''
        for group in request.registry['principals']:
            if not active_mode and group[0] == 'mode':
                continue
            html += HTML.h3(translate(group[1]))
            for principal in group[2]:
                html += HTML.div(
                    form.custom_checkbox('pcpl:{0}.{1}'.format(
                        group[0], principal[0])) +
                    literal(' <label for="pcpl{0}{1}">{2}</label>'.format(
                        group[0], principal[0], translate(principal[1]))))
        return html


# =============================================================================
class DBProfilePrincipal(DBDeclarativeClass):
    """SQLAlchemy-powered profile permission class (one-to-many)."""
    # pylint: disable = too-few-public-methods

    __tablename__ = 'profiles_principals'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    profile_id = Column(
        String(ID_LEN), ForeignKey('profiles.profile_id', ondelete='CASCADE'),
        primary_key=True)
    principal = Column(String(ID_LEN), primary_key=True)
