# -*- coding: utf-8 -*-
"""SQLAlchemy-powered model definitions for user groups."""

from json import dumps

import colander
from sqlalchemy import Column, ForeignKey, Integer, String, Text, PickleType
from sqlalchemy.orm import relationship
from lxml import etree
from webhelpers2.html import literal

from ..lib.i18n import _, record_format_i18n
from ..lib.i18n import schema_i18n_labels, defaults_i18n_labels
from ..lib.i18n import view_i18n_labels, edit_i18n_labels
from ..lib.utils import make_id
from ..lib.xml import i18n_xml_text, db2xml_i18n_labels
from . import DBDeclarativeClass, ID_LEN, LABEL_LEN, DESCRIPTION_LEN
from .dbbase import DBBaseClass
from .dbuser import DBUser
from .dbprofile import DBProfile


# =============================================================================
class DBGroup(DBDeclarativeClass, DBBaseClass):
    """SQLAlchemy-powered user group class."""

    suffix = 'ciogrp'
    attachments_dir = 'Groups'
    _settings_tabs = (_('Information'), _('Users'), _('Profiles'))

    __tablename__ = 'groups'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    group_id = Column(String(ID_LEN), primary_key=True)
    i18n_label = Column(Text(), nullable=False)
    i18n_description = Column(PickleType(1))
    attachments_key = Column(String(ID_LEN + 20))
    picture = Column(String(ID_LEN + 4))

    users = relationship('DBGroupUser', cascade='all, delete')
    profiles = relationship(DBProfile, secondary='groups_profiles')

    # -------------------------------------------------------------------------
    @classmethod
    def xml2db(cls, dbsession, group_elt, error_if_exists=True, kwargs=None):
        """Load a user group from a XML element.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :type  group_elt: lxml.etree.Element
        :param group_elt:
            User group XML element.
        :param bool error_if_exists: (default=True)
            It returns an error if user group already exists.
        :param dict kwargs: (optional)
            Dictionary of keyword arguments.
        :rtype: :class:`pyramid.i18n.TranslationString` or ``None``
        :return:
            Error message or ``None``.
        """
        # pylint: disable = unused-argument
        # Check if already exists
        group_id = make_id(group_elt.get('id'), 'token', ID_LEN)
        dbgroup = dbsession.query(cls).filter_by(
            group_id=group_id).first()
        if dbgroup is not None:
            if error_if_exists:
                return _('Group "${g}" already exists.', {'g': group_id})
            return None

        # Create group
        record = cls.record_from_xml(group_id, group_elt)
        error = cls.record_format(record)
        if error:
            return error
        dbgroup = cls(**record)
        dbsession.add(dbgroup)

        return dbgroup.xml2db_extra(dbsession, group_elt, kwargs)

    # -------------------------------------------------------------------------
    def xml2db_extra(self, dbsession, group_elt, kwargs):
        """Load extra information on a group from a XML element.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :type  group_elt: lxml.etree.Element
        :param group_elt:
            Group XML element.
        :param dict kawrgs:
            Dictionary of keyword arguments with the key ``'profiles'``.
        :rtype: :class:`pyramid.i18n.TranslationString` or ``None``
        :return:
            Error message or ``None``.
        """
        dbsession.flush()

        # Add users
        refs = kwargs.get('users', {})
        done = set()
        for elt in group_elt.xpath('users/user'):
            user_id = refs.get(elt.text)
            if user_id is not None and user_id not in done:
                dbsession.add(DBGroupUser(
                    group_id=self.group_id, user_id=user_id))
                done.add(user_id)

        # Add profiles
        profile_ids = kwargs.get('profiles') if kwargs else None
        if profile_ids:
            done = set()
            for elt in group_elt.findall('profiles/profile'):
                profile_id = elt.text
                if profile_id not in done and profile_id in profile_ids:
                    dbsession.add(DBGroupProfile(
                        group_id=self.group_id, profile_id=profile_id))
                    done.add(profile_id)

    # -------------------------------------------------------------------------
    @classmethod
    def record_from_xml(cls, group_id, group_elt):
        """Convert an user group XML element into a dictionary.

        :param str group_id:
            User group ID.
        :type  group_elt: lxml.etree.Element
        :param group_elt:
            Group XML element.
        :rtype: dict
        """
        attachments_elt = group_elt.find('attachments')
        return {
            'group_id': group_id,
            'i18n_label': dumps(
                i18n_xml_text(group_elt, 'label'), ensure_ascii=False),
            'i18n_description': i18n_xml_text(group_elt, 'description'),
            'attachments_key':
            attachments_elt is not None and attachments_elt.get('key') or None,
            'picture':
            attachments_elt is not None and attachments_elt.findtext(
                'picture') or None}

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

        # Group ID
        if not record.get('group_id'):
            return _('User group without ID.')
        record['group_id'] = make_id(record['group_id'], 'xmlid', ID_LEN)

        # Labels and descriptions
        if not record_format_i18n(record):
            return _('User group without label.')
        if not record.get('i18n_description'):
            record['i18n_description'] = {}
        return None

    # -------------------------------------------------------------------------
    def db2xml(self, dbsession):
        """Serialize an user group to a XML representation.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :rtype: lxml.etree.Element
        """
        group_elt = etree.Element('group')
        group_elt.set('id', self.group_id)

        # Labels and descriptions
        db2xml_i18n_labels(self, group_elt, 3)

        # Attachments
        if self.attachments_key:
            elt = etree.SubElement(
                group_elt, 'attachments', key=self.attachments_key)
            if self.picture:
                etree.SubElement(elt, 'picture').text = self.picture

        # Users
        if self.users:
            users = {}
            users_elt = etree.SubElement(group_elt, 'users')
            for dbuser in self.users:
                if dbuser.user_id not in users:
                    users[dbuser.user_id] = dbsession.query(
                        DBUser.login).filter_by(
                            user_id=dbuser.user_id).first()[0]
                etree.SubElement(users_elt, 'user').text = \
                    users[dbuser.user_id]

        # Profiles
        if self.profiles:
            elt = etree.SubElement(group_elt, 'profiles')
            for item in self.profiles:
                etree.SubElement(elt, 'profile').text = item.profile_id

        return group_elt

    # -------------------------------------------------------------------------
    def tab4view(self, request, tab_index, form, user_filter, user_paging):
        """Generate the tab content of a user group.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param int index:
            Index of the tab.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :type  user_filter: chrysalio.lib.filter.Filter
        :param user_filter:
            Filter for users.
        :type  user_paging: chrysalio.lib.paging.Paging
        :param user_paging:
            Paging for warehouse users.
        :rtype: webhelpers2.html.literal
        """
        if tab_index == 0:
            return self._tab4view_information(request, form)
        if tab_index == 1:
            return self._tab4view_users(
                request, form, user_filter, user_paging)
        if tab_index == 2:
            return self._tab4view_profiles(request)
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
            translate(_('Identifier:')), self.group_id, clear=True)
        html += view_i18n_labels(request, form, self)
        return html

    # -------------------------------------------------------------------------
    def _tab4view_users(self, request, form, user_filter, user_paging):
        """Generate the users tab.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :type  user_filter: chrysalio.lib.filter.Filter
        :param user_filter:
            Filter for users.
        :type  user_paging: chrysalio.lib.paging.Paging
        :param user_paging:
            Paging for warehouse users.
        :rtype: webhelpers2.html.literal
        """
        html = DBUser.paging_filter(
            request, form, user_filter, user_paging)
        html += self._user_thead(request, user_paging)
        for dbuser in user_paging:
            html += '<tr>'\
                '<th><a href="{user_view}">{login}</a></th>'\
                '<td class="cioOptional">{fname}</td><td>{lname}</td>'\
                '</tr>\n'.format(
                    user_view=request.route_path(
                        'user_view', user_id=dbuser.user_id),
                    login=dbuser.login,
                    fname=dbuser.first_name or '', lname=dbuser.last_name)
        html += '</tbody>\n</table>\n'

        return literal(html)

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
    @classmethod
    def settings_schema(cls, request, defaults, profiles, dbgroup=None):
        """Return a Colander schema to edit user group.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param dict defaults:
            Default values for the form set by the user paging object.
        :param dict profiles:
            A dictionary such as ``{profile_id: (label, description),...}``.
        :type  dbgroup: DBGroup
        :param dbgroup: (optional)
            Current user group SqlAlchemy object.
        :rtype: tuple
        :return:
            A tuple such as ``(schema, defaults)``.
        """
        # Schema
        schema = colander.SchemaNode(colander.Mapping())
        if dbgroup is None:
            schema.add(colander.SchemaNode(
                colander.String(), name='group_id',
                validator=colander.All(
                    colander.Regex(r'^[a-z][a-z0-9_]+$'),
                    colander.Length(min=2, max=ID_LEN))))

        schema_i18n_labels(request, schema, LABEL_LEN, DESCRIPTION_LEN)

        # Profiles
        if request.has_permission('group-create'):
            for profile_id in profiles:
                schema.add(colander.SchemaNode(
                    colander.Boolean(), name='pfl:{0}'.format(profile_id),
                    missing=False))

        # Defaults
        if dbgroup is not None:
            defaults.update(defaults_i18n_labels(dbgroup))
            for dbitem in dbgroup.users:
                defaults['mbr:{0}'.format(dbitem.user_id)] = True
            for dbitem in dbgroup.profiles:
                defaults['pfl:{0}'.format(dbitem.profile_id)] = True

        return schema, defaults

    # -------------------------------------------------------------------------
    @classmethod
    def tab4edit(cls, request, tab_index, form, user_filter, user_paging,
                 profiles, dbgroup=None):
        """Generate the tab content of user group for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param int tab_index:
            Index of the tab.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :type  user_filter: chrysalio.lib.filter.Filter
        :param user_filter:
            Filter for users.
        :type  user_paging: chrysalio.lib.paging.Paging
        :param user_paging:
            Paging for all users.
        :param dict profiles:
            A dictionary such as ``{profile_id: (label, description),...}``.
        :type  dbgroup: DBGroup
        :param dbgroup: (optional)
            Current user group SqlAlchemy object.
        :rtype: webhelpers2.html.literal
        """
        # pylint: disable = too-many-arguments
        if tab_index == 0:
            return cls._tab4edit_information(request, form, dbgroup)
        if tab_index == 1:
            return cls._tab4edit_users(
                request, form, user_filter, user_paging)
        if tab_index == 2:
            return cls._tab4edit_profiles(request, form, profiles)
        return ''

    # -------------------------------------------------------------------------
    @classmethod
    def _tab4edit_information(cls, request, form, dbgroup):
        """Generate the information tab for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :type  dbgroup: DBGroup
        :param dbgroup:
            Current user group SqlAlchemy object.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        if dbgroup is None:
            html = form.grid_text(
                'group_id', translate(_('Identifier:')), required=True,
                maxlength=ID_LEN, clear=True)
        else:
            html = form.grid_item(
                translate(_('Identifier:')), dbgroup.group_id, clear=True)
        html += edit_i18n_labels(request, form, LABEL_LEN, DESCRIPTION_LEN)
        return html

    # -------------------------------------------------------------------------
    @classmethod
    def _tab4edit_users(cls, request, form, user_filter, user_paging):
        """Generate the users tab for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :type  user_filter: chrysalio.lib.filter.Filter
        :param user_filter:
            Filter for users.
        :type  user_paging: chrysalio.lib.paging.Paging
        :param user_paging:
            Paging for all users.
        :rtype: webhelpers2.html.literal
        """
        html = DBUser.paging_filter(
            request, form, user_filter, user_paging)
        html += cls._user_thead(request, user_paging).replace(
            '<tr>', '<tr><th class="cioCheckbox" id="check_all"></th>')
        for dbuser in user_paging:
            html += '<tr>'\
                '<td class="cioCheckbox cioSelect">{check}{shown}</td>'\
                '<th>{login}</th>'\
                '<td class="cioOptional">{fname}</td><td>{lname}</td>'\
                '</tr>\n'.format(
                    check=form.custom_checkbox(
                        'mbr:{0}'.format(dbuser.user_id)),
                    shown=form.hidden('shw:{0}'.format(dbuser.user_id)),
                    login=dbuser.login,
                    fname=dbuser.first_name or '', lname=dbuser.last_name)
        html += '</tbody>\n</table>\n'

        return literal(html)

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
    def _user_thead(cls, request, user_paging):
        """Table header for group users.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  user_paging: chrysalio.lib.paging.Paging
        :param user_paging:
            Paging for users.
        :rtype: str
        """
        translate = request.localizer.translate
        return \
            '<table class="cioPagingList">\n<thead><tr>'\
            '<th>{login}</th>'\
            '<th class="cioOptional">{fname}</th><th>{lname}</th>'\
            '</tr></thead>\n<tbody>\n'.format(
                login=user_paging.sortable_column(
                    translate(_('Login')), 'login'),
                fname=user_paging.sortable_column(
                    translate(_('First name')), 'first_name'),
                lname=user_paging.sortable_column(
                    translate(_('Last name')), 'last_name'))


# =============================================================================
class DBGroupUser(DBDeclarativeClass):
    """Class to link groups with their authorized users (many-to-many)."""
    # pylint: disable = too-few-public-methods

    __tablename__ = 'groups_users'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    group_id = Column(
        String(ID_LEN), ForeignKey('groups.group_id', ondelete='CASCADE'),
        primary_key=True)
    user_id = Column(
        Integer, ForeignKey('users.user_id', ondelete='CASCADE'),
        primary_key=True)


# =============================================================================
class DBGroupProfile(DBDeclarativeClass):
    """Class to link groups with their profiles (many-to-many)."""
    # pylint: disable = too-few-public-methods

    __tablename__ = 'groups_profiles'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    group_id = Column(
        String(ID_LEN), ForeignKey('groups.group_id', ondelete='CASCADE'),
        primary_key=True)
    profile_id = Column(
        String(ID_LEN), ForeignKey('profiles.profile_id', ondelete='CASCADE'),
        primary_key=True)
