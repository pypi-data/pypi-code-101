"""Profile management view callables."""

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
from ..models.populate import xml2db, db2web, web2db
from ..models.dbprofile import DBProfile, DBProfilePrincipal
from . import BaseView


# =============================================================================
class ProfileView(BaseView):
    """Class to manage profile views.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    _DBProfile = DBProfile
    _xml2db = (xml2db,)

    # -------------------------------------------------------------------------
    @view_config(
        route_name='profile_index',
        renderer='chrysalio:Templates/profile_index.pt',
        permission='profile-view')
    @view_config(route_name='profile_index', renderer='json', xhr=True)
    def index(self):
        """List all profiles."""
        # Ajax
        i_creator = self._request.has_permission('profile-create')
        if self._request.is_xhr:
            if i_creator:
                self._import_profiles()
            return {}

        # Action
        action, items = get_action(self._request)
        if action[:4] == 'del!' and i_creator:
            self._delete_profiles(items)
        elif action == 'imp!' and i_creator:
            self._import_profiles()
        elif action[:4] == 'exp!':
            action = self._profiles2response(items)
            if action:
                return action

        # Filter
        paging_id = 'profiles'
        pfilter = Filter(
            self._request, paging_id, (
                ('profile_id', _('Identifier'), False, ''),
                ('i18n_label', _('Label'), False, '')),
            remove=action[:4] == 'crm!' and action[4:] or None)

        # Paging
        defaults = Paging.params(self._request, paging_id, '+profile_id')
        dbquery = pfilter.sql(
            self._request.dbsession.query(self._DBProfile), 'profiles')
        oby = getattr(self._DBProfile, defaults['sort'][1:])
        dbquery = dbquery.order_by(
            desc(oby) if defaults['sort'][0] == '-' else oby)
        profile_paging = Paging(self._request, paging_id, dbquery, defaults)
        profile_paging.set_current_ids('profile_id')

        # Form & completed action
        form = Form(self._request, defaults=defaults)
        form.forget('filter_value')
        if action and action[3] == '!':
            action = ''

        # Breadcrumbs
        self._request.breadcrumbs(_('Profiles'), 2)

        return {
            'action': action, 'items': items, 'form': form, 'pfilter': pfilter,
            'paging': profile_paging, 'PAGE_SIZES': PAGE_SIZES,
            'download_max_size': self._request.registry['settings'][
                'download-max-size'],
            'i_creator': i_creator,
            'i_editor': self._request.has_permission('profile-edit')}

    # -------------------------------------------------------------------------
    @view_config(route_name='profile_index_filter', renderer='json', xhr=True)
    def index_filter(self):
        """Return a list to autocomplete a filter field."""
        return Filter.sql_autocomplete(self._request, self._DBProfile)

    # -------------------------------------------------------------------------
    @view_config(
        route_name='profile_view',
        renderer='chrysalio:Templates/profile_view.pt',
        permission='profile-view')
    def view(self):
        """Show profile."""
        dbprofile = self._get_profile()

        action = get_action(self._request)[0]
        if action == 'exp!':
            action = self._profiles2response((dbprofile.profile_id,))
            if action:
                return action

        # Breadcrumbs
        label = dbprofile.label(self._request)
        self._request.breadcrumbs(
            _('Profile "${l}"', {'l': label}),
            replace=self._request.route_path(
                'profile_edit', profile_id=dbprofile.profile_id))

        return {
            'form': Form(self._request), 'label': label,
            'tabset': Tabset(
                self._request, 'tabProfile',
                dbprofile.settings_tabs(self._request)),
            'dbprofile': dbprofile,
            'navigator': Paging.navigator(
                self._request, 'profiles', dbprofile.profile_id,
                self._request.route_path('profile_view', profile_id='_ID_')),
            'i_editor': self._request.has_permission('profile-edit')}

    # -------------------------------------------------------------------------
    @view_config(
        route_name='profile_create',
        renderer='chrysalio:Templates/profile_edit.pt',
        permission='profile-create')
    @view_config(
        route_name='profile_edit',
        renderer='chrysalio:Templates/profile_edit.pt',
        permission='profile-edit')
    def edit(self):
        """Create or edit a profile."""
        dbprofile = self._get_profile() \
            if 'profile_id' in self._request.matchdict else None
        form = Form(
            self._request,
            *self._DBProfile.settings_schema(self._request, dbprofile),
            obj=dbprofile)

        action = get_action(self._request)[0]
        if action == 'sav!' and form.validate():
            dbprofile = self._save(dbprofile, form.values)
            if dbprofile is not None:
                if 'profile_id' not in self._request.matchdict:
                    self._request.breadcrumbs.pop()
                log_info(
                    self._request,
                    'profile_id' in self._request.matchdict and
                    'profile_edit' or 'profile_create', dbprofile.profile_id)
                return HTTPFound(self._request.route_path(
                    'profile_view', profile_id=dbprofile.profile_id))
        if form.has_error():
            self._request.session.flash(_('Correct errors.'), 'alert')

        # Breadcrumbs
        label = dbprofile and dbprofile.label(self._request)
        if not dbprofile:
            self._request.breadcrumbs(_('Profile Creation'))
        else:
            self._request.breadcrumbs(
                _('Profile "${l}" Edition', {'l': label}),
                replace=self._request.route_path(
                    'profile_view', profile_id=dbprofile.profile_id))
        return {
            'form': form, 'dbprofile': dbprofile or self._DBProfile,
            'label': label, 'tabset': Tabset(
                self._request, 'tabProfile',
                self._DBProfile.settings_tabs(self._request))}

    # -------------------------------------------------------------------------
    def _get_profile(self):
        """Return the SqlAlchemy object of the selected profile or raise
        an HTTPNotFound exception.

        :rtype: .models.dbprofile.DBProfile
        """
        profile_id = self._request.matchdict['profile_id']
        dbprofile = self._request.dbsession.query(self._DBProfile).filter_by(
            profile_id=profile_id).first()
        if dbprofile is None:
            raise HTTPNotFound()
        return dbprofile

    # -------------------------------------------------------------------------
    def _delete_profiles(self, profile_ids):
        """Delete profiles.

        :param list profile_ids:
            List of profile IDs to delete.
        """
        deleted = []
        for dbprofile in self._request.dbsession.query(self._DBProfile).filter(
                self._DBProfile.profile_id.in_(profile_ids)):
            deleted.append(dbprofile.profile_id)
            self._request.dbsession.delete(dbprofile)
        if deleted:
            log_info(self._request, 'profile_delete', ' '.join(deleted))

    # -------------------------------------------------------------------------
    def _import_profiles(self):
        """Import profiles."""
        # Get current IDs
        profile_ids = {k[0] for k in self._request.dbsession.query(
            DBProfile.profile_id)}

        # Update database
        web2db(self._request, self._xml2db[0], 'profile')

        # Get new IDs
        profile_ids = {k[0] for k in self._request.dbsession.query(
            DBProfile.profile_id)} - profile_ids
        if profile_ids:
            log_info(self._request, 'profile_import', ' '.join(profile_ids))

    # -------------------------------------------------------------------------
    def _profiles2response(self, profile_ids):
        """Export profiles as an XML file embedded in a Pyramid response.

        :param list profile_ids:
            List of profile IDs to export.
        :rtype: :class:`pyramid.response.Response` or ``''``
        """
        dbitems = tuple(self._request.dbsession.query(self._DBProfile).filter(
            self._DBProfile.profile_id.in_(profile_ids)).order_by(
                'profile_id'))
        if not dbitems:
            return ''
        filename = '{0}.{1}.xml'.format(
            len(dbitems) == 1 and dbitems[0].profile_id or
            make_id(self._request.registry['settings']['title'], 'token'),
            self._DBProfile.suffix)

        log_info(
            self._request, 'profile_export',
            ' '.join([k.profile_id for k in dbitems]))
        return db2web(self._request, dbitems, filename)

    # -------------------------------------------------------------------------
    def _save(self, dbprofile, values):
        """Save a profile.

        :type  dbprofile: .models.dbprofile.DBProfile
        :param dbprofile:
            Profile to save.
        :param dict values:
            Form values.
        :rtype: :class:`~.models.dbprofile.DBProfile` instance or ``None``
        """
        creation = dbprofile is None
        dbprofile = dbprofile or self._DBProfile()

        # Update profile
        record = {k: values[k] for k in values if not k.startswith('pcpl:')}
        if not creation:
            record['profile_id'] = dbprofile.profile_id
        error = dbprofile.record_format(record)
        if error:  # pragma: nocover
            self._request.session.flash(error, 'alert')
            return None
        for field in record:
            if getattr(dbprofile, field) != record[field]:
                setattr(dbprofile, field, record[field])

        # Save
        if creation:
            try:
                self._request.dbsession.add(dbprofile)
                self._request.dbsession.flush()
            except (IntegrityError, FlushError):
                self._request.session.flash(
                    _('This profile already exists.'), 'alert')
                return None

        # Update principals
        profile_principals = [k.principal for k in dbprofile.principals]
        for group in self._request.registry['principals']:
            for principal in group[2]:
                principal = '{0}.{1}'.format(group[0], principal[0])
                value = values.get('pcpl:{0}'.format(principal))
                if value and principal not in profile_principals:
                    dbprofile.principals.append(
                        DBProfilePrincipal(principal=principal))
                elif not value and principal in profile_principals:
                    self._request.dbsession.delete(
                        self._request.dbsession.query(DBProfilePrincipal)
                        .filter_by(
                            profile_id=dbprofile.profile_id,
                            principal=principal).first())

        return dbprofile
