# -*- coding: utf-8 -*-
"""User group management view callables."""

from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import FlushError

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from ..lib.i18n import _
from ..lib.log import log_info
from ..lib.form import get_action, Form
from ..lib.filter import Filter
from ..lib.paging import PAGE_SIZES, Paging
from ..lib.utils import make_id
from ..lib.tabset import Tabset
from ..lib.attachment import attachment_url, attachment_update
from ..includes.themes import theme_static_prefix
from ..models.populate import xml2db, db2web, web2db
from ..models.dbprofile import DBProfile
from ..models.dbuser import DBUser
from ..models.dbgroup import DBGroup, DBGroupUser, DBGroupProfile
from . import BaseView


# =============================================================================
class GroupView(BaseView):
    """Class to manage user group views.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    _DBGroup = DBGroup
    _xml2db = (xml2db,)

    # -------------------------------------------------------------------------
    @view_config(
        route_name='group_index',
        renderer='chrysalio:Templates/group_index.pt',
        permission='group-view')
    @view_config(route_name='group_index', renderer='json', xhr=True)
    def index(self):
        """List all user groups."""
        # Ajax
        i_creator = self._request.has_permission('group-create')
        if self._request.is_xhr:
            if i_creator:
                self._import_groups()
            return {}

        # Action
        action, items = get_action(self._request)
        if action[:4] == 'del!' and i_creator:
            self._delete_groups(items)
        elif action == 'imp!' and i_creator:
            self._import_groups()
        elif action[:4] == 'exp!':
            action = self._groups2response(items)
            if action:
                return action

        # Filter
        paging_id = 'groups'
        pfilter = Filter(
            self._request, paging_id, (
                ('group_id', _('Identifier'), False, ''),
                ('i18n_label', _('Label'), False, '')),
            remove=action[:4] == 'crm!' and action[4:] or None)

        # Paging
        defaults = Paging.params(self._request, paging_id, '+group_id')
        dbquery = pfilter.sql(
            self._request.dbsession.query(self._DBGroup), 'groups')
        oby = getattr(self._DBGroup, defaults['sort'][1:])
        dbquery = dbquery.order_by(
            desc(oby) if defaults['sort'][0] == '-' else oby)
        group_paging = Paging(self._request, paging_id, dbquery, defaults)
        group_paging.set_current_ids('group_id')

        # Form & completed action
        form = Form(self._request, defaults=defaults)
        form.forget('filter_value')
        if action and action[3] == '!':
            action = ''

        # Breadcrumbs
        self._request.breadcrumbs(_('Groups'), 2)

        return {
            'action': action, 'items': items, 'form': form, 'pfilter': pfilter,
            'paging': group_paging, 'PAGE_SIZES': PAGE_SIZES,
            'download_max_size': self._request.registry['settings'][
                'download-max-size'],
            'i_creator': i_creator,
            'i_editor': self._request.has_permission('group-edit'),
            'has_attachments': bool(
                self._request.registry.settings.get('attachments')),
            'attachment_url': attachment_url}

    # -------------------------------------------------------------------------
    @view_config(route_name='group_index_filter', renderer='json', xhr=True)
    def index_filter(self):
        """Return a list to autocomplete a filter field."""
        print(Filter.sql_autocomplete(self._request, self._DBGroup))
        return Filter.sql_autocomplete(self._request, self._DBGroup)

    # -------------------------------------------------------------------------
    @view_config(
        route_name='group_view',
        renderer='chrysalio:Templates/group_view.pt',
        permission='group-view')
    def view(self):
        """Show user group."""
        dbgroup = self._get_group()
        picture = self._request.registry.settings.get('attachments') and (
            attachment_url(
                self._request, dbgroup.attachments_dir,
                dbgroup.attachments_key, dbgroup.picture) or
            '{0}/images/group_picture.svg'.format(
                theme_static_prefix(self._request)))

        action = get_action(self._request)[0]
        if action == 'exp!':
            action = self._groups2response((dbgroup.group_id,))
            if action:
                return action

        # User paging
        user_paging, defaults, user_filter = self._user_paging(
            action, dbgroup)

        # Form
        form = Form(self._request, defaults=defaults)
        form.forget('filter_value')

        # Breadcrumbs
        label = dbgroup.label(self._request)
        self._request.breadcrumbs(
            _('Group "${l}"', {'l': label}),
            replace=self._request.route_path(
                'group_edit', group_id=dbgroup.group_id))

        return {
            'form': form, 'label': label, 'user_filter': user_filter,
            'user_paging': user_paging, 'tabset': Tabset(
                self._request, 'tabGroup',
                dbgroup.settings_tabs(self._request)),
            'picture': picture, 'dbgroup': dbgroup,
            'navigator': Paging.navigator(
                self._request, 'groups', dbgroup.group_id,
                self._request.route_path('group_view', group_id='_ID_')),
            'i_editor': self._request.has_permission('group-edit')}

    # -------------------------------------------------------------------------
    @view_config(
        route_name='group_create',
        renderer='chrysalio:Templates/group_edit.pt',
        permission='group-create')
    @view_config(
        route_name='group_edit',
        renderer='chrysalio:Templates/group_edit.pt',
        permission='group-edit')
    @view_config(
        route_name='group_edit', renderer='json', xhr=True,
        permission='group-edit')
    def edit(self):
        """Create or edit a user group."""
        # Initialization
        dbgroup = self._get_group() \
            if 'group_id' in self._request.matchdict else None
        # Ajax
        if self._request.is_xhr:
            if dbgroup is not None:
                dbgroup.attachments_key, dbgroup.picture = \
                    attachment_update(
                        self._request, dbgroup.attachments_dir,
                        dbgroup.attachments_key,
                        self._request.POST['picture'],
                        replace=dbgroup.picture,
                        prefix=dbgroup.group_id[:12])
                log_info(
                    self._request, 'group_update_picture',
                    dbgroup.group_id)
            return {}

        # User paging
        action = get_action(self._request)[0]
        user_paging, defaults, user_filter = self._user_paging(action)

        # Profiles
        profiles = {
            k.profile_id: (
                k.label(self._request), k.description(self._request))
            for k in self._request.dbsession.query(DBProfile)}

        # Form and action
        form = Form(
            self._request,
            *self._DBGroup.settings_schema(
                self._request, defaults, profiles, dbgroup),
            obj=dbgroup)
        if action == 'pct!' and dbgroup is not None:
            dbgroup.attachments_key, dbgroup.picture = \
                attachment_update(
                    self._request, dbgroup.attachments_dir,
                    dbgroup.attachments_key, self._request.POST['picture'],
                    replace=dbgroup.picture,
                    prefix=dbgroup.group_id[:12])
            log_info(
                self._request, 'group_update_picture',
                dbgroup.group_id)
        elif action == 'sav!' and form.validate():
            dbgroup = self._save(dbgroup, profiles, form.values)
            if dbgroup is not None:
                dbuser = self._request.dbsession.query(DBUser).filter_by(
                    user_id=self._request.session['user']['user_id']).first()
                dbuser.set_session(self._request)
                if 'group_id' not in self._request.matchdict:
                    self._request.breadcrumbs.pop()
                log_info(
                    self._request,
                    'group_id' in self._request.matchdict and
                    'group_edit' or 'group_create', dbgroup.group_id)
                return HTTPFound(self._request.route_path(
                    'group_view', group_id=dbgroup.group_id))
        if form.has_error():
            self._request.session.flash(_('Correct errors.'), 'alert')

        # Picture
        picture = \
            dbgroup \
            and self._request.registry.settings.get('attachments') \
            and (attachment_url(
                self._request, DBGroup.attachments_dir,
                dbgroup.attachments_key, dbgroup.picture) or
                 '{0}/images/group_picture.svg'.format(
                     theme_static_prefix(self._request)))

        # Breadcrumbs
        label = dbgroup and dbgroup.label(self._request)
        if not dbgroup:
            self._request.breadcrumbs(_('Group Creation'))
        else:
            self._request.breadcrumbs(
                _('Group "${l}" Edition', {'l': label}),
                replace=self._request.route_path(
                    'group_view', group_id=dbgroup.group_id))
        return {
            'form': form, 'dbgroup': dbgroup or self._DBGroup,
            'action': action, 'label': label, 'profiles': profiles,
            'user_filter': user_filter, 'user_paging': user_paging,
            'picture': picture, 'tabset': Tabset(
                self._request, 'tabGroup',
                self._DBGroup.settings_tabs(self._request))}

    # -------------------------------------------------------------------------
    def _get_group(self):
        """Return the SqlAlchemy object of the selected user group or raise
        an HTTPNotFound exception.

        :rtype: .models.dbgroup.DBGroup
        """
        group_id = self._request.matchdict['group_id']
        dbgroup = self._request.dbsession.query(self._DBGroup).filter_by(
            group_id=group_id).first()
        if dbgroup is None:
            raise HTTPNotFound()
        return dbgroup

    # -------------------------------------------------------------------------
    def _delete_groups(self, group_ids):
        """Delete groups.

        :param list group_ids:
            List of group IDs to delete.
        """
        deleted = []
        for dbgroup in self._request.dbsession.query(self._DBGroup).filter(
                self._DBGroup.group_id.in_(group_ids)):
            deleted.append(dbgroup.group_id)
            self._request.dbsession.delete(dbgroup)
        if deleted:
            log_info(self._request, 'group_delete', ' '.join(deleted))

    # -------------------------------------------------------------------------
    def _import_groups(self):
        """Import groups."""
        # Get current IDs
        group_ids = {k[0] for k in self._request.dbsession.query(
            DBGroup.group_id)}

        # Update database
        web2db(self._request, self._xml2db[0], 'group')

        # Get new IDs
        group_ids = {k[0] for k in self._request.dbsession.query(
            DBGroup.group_id)} - group_ids
        if group_ids:
            log_info(self._request, 'group_import', ' '.join(group_ids))

    # -------------------------------------------------------------------------
    def _groups2response(self, group_ids):
        """Export user groups as an XML file embedded in a Pyramid response.

        :param list group_ids:
            List of group IDs to export.
        :rtype: :class:`pyramid.response.Response` or ``''``
        """
        dbitems = tuple(self._request.dbsession.query(self._DBGroup).filter(
            self._DBGroup.group_id.in_(group_ids)).order_by('group_id'))
        if not dbitems:
            return ''
        filename = '{0}.{1}.xml'.format(
            len(dbitems) == 1 and dbitems[0].group_id or
            make_id(self._request.registry['settings']['title'], 'token'),
            self._DBGroup.suffix)

        log_info(
            self._request, 'group_export',
            ' '.join([k.group_id for k in dbitems]))
        return db2web(self._request, dbitems, filename)

    # -------------------------------------------------------------------------
    def _save(self, dbgroup, profiles, values):
        """Save a user group.

        :type  dbgroup: .models.dbgroup.DBGroup
        :param dbgroup:
            Group to save.
        :param dict profiles:
            A dictionary such as ``{profile_id: (label, description),...}``.
        :param dict values:
            Form values.
        :rtype: :class:`~.models.dbgroup.DBGroup` instance or ``None``
        """
        creation = dbgroup is None
        dbgroup = dbgroup or self._DBGroup()

        # Update group
        record = {k: values[k] for k in values if k[:4] not in (
            'mbr:', 'shw:', 'pfl:')}
        if not creation:
            record['group_id'] = dbgroup.group_id
        error = dbgroup.record_format(record)
        if error:  # pragma: nocover
            self._request.session.flash(error, 'alert')
            return None
        for field in record:
            if getattr(dbgroup, field) != record[field]:
                setattr(dbgroup, field, record[field])

        # Save
        if creation:
            try:
                self._request.dbsession.add(dbgroup)
                self._request.dbsession.flush()
            except (IntegrityError, FlushError):
                self._request.session.flash(
                    _('This group already exists.'), 'alert')
                return None

        # Update users
        self._users_update(dbgroup)

        # Update profiles
        self._profiles_update(dbgroup, profiles, values)

        return dbgroup

    # -------------------------------------------------------------------------
    def _users_update(self, dbgroup):
        """Update the list of group users.

        :type  dbgroup: .models.dbwarhouse.DBGroup
        :param dbgroup:
            SQLAlchemy object for the current group.
        """
        if not self._request.has_permission('user-create'):
            return

        is_set = {}
        for value in self._request.POST:
            if value[:4] == 'mbr:':
                is_set[value[4:]] = True
            elif value[:4] == 'shw:' and value[4:] not in is_set:
                is_set[value[4:]] = False

        for user_id, user_set in is_set.items():
            dbgroup_user = self._request.dbsession.query(
                DBGroupUser).filter_by(
                    group_id=dbgroup.group_id,
                    user_id=int(user_id)).first()
            if dbgroup_user is not None and not user_set:
                self._request.dbsession.delete(dbgroup_user)
            elif dbgroup_user is None and user_set:
                self._request.dbsession.add(DBGroupUser(
                    group_id=dbgroup.group_id, user_id=int(user_id)))

    # -------------------------------------------------------------------------
    def _user_paging(self, action, dbgroup=None):
        """Return a paging object for users.

        :param str action:
            Current action.
        :type  dbgroup: .models.dbwarhouse.DBGroup
        :param dbgroup: (optional)
            If not ``None``, users are only users of the group.
        :rtype: tuple
        :return:
            A tuple such as ``(user_paging, defaults, user_filter)``.
        """
        # Filter
        paging_id = 'group_users'
        ufilter = Filter(
            self._request, paging_id, (
                ('login', _('Login'), False, None),
                ('last_name', _('Last name'), False, None),
                ('email', _('Email'), False, None),
                ('status', _('Status'), False,
                 [('', ' ')] + list(DBUser.status_labels.items()))),
            (('status', '=', 'active'),),
            remove=action[:4] == 'crm!' and action[4:] or None)

        # Database query
        defaults = Paging.params(
            self._request, paging_id, '+last_name', default_display='list')
        dbquery = ufilter.sql(
            self._request.dbsession.query(
                DBUser.user_id, DBUser.login,
                DBUser.first_name, DBUser.last_name,
                DBUser.honorific, DBUser.email,
                DBUser.email_hidden, DBUser.status,
                DBUser.last_login, DBUser.attachments_key,
                DBUser.picture), 'users')
        if dbgroup is not None:
            dbquery = dbquery.filter(DBUser.user_id.in_(
                [k.user_id for k in dbgroup.users]))
        oby = getattr(DBUser, defaults['sort'][1:])
        dbquery = dbquery.order_by(
            desc(oby) if defaults['sort'][0] == '-' else oby)

        return Paging(self._request, paging_id, dbquery, defaults), \
            dict(defaults), ufilter

    # -------------------------------------------------------------------------
    def _profiles_update(self, dbgroup, profiles, values):
        """Update the list of profiles.

        :type  dbgroup: .models.dbwarhouse.DBGroup
        :param dbgroup:
            SQLAlchemy object for the current group.
        :param dict profiles:
            A dictionary such as ``{profile_id: (label, description),...}``.
        :param dict values:
            Form values.
        """
        if not self._request.has_permission('user-create'):
            return

        group_profiles = {k.profile_id: k for k in dbgroup.profiles}
        for profile_id in profiles:
            value = values['pfl:{0}'.format(profile_id)]
            if value and profile_id not in group_profiles:
                self._request.dbsession.add(DBGroupProfile(
                    group_id=dbgroup.group_id, profile_id=profile_id))
            elif not value and profile_id in group_profiles:
                self._request.dbsession.delete(
                    self._request.dbsession.query(DBGroupProfile)
                    .filter_by(
                        group_id=dbgroup.group_id, profile_id=profile_id)
                    .first())
