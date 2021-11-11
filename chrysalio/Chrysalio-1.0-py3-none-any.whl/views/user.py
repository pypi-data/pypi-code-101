# -*- coding: utf-8 -*-
"""User management view callables."""

from os.path import join, exists
from datetime import date, datetime
from hashlib import sha1
from shutil import rmtree

from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import FlushError
from colander import Mapping, SchemaNode, String, All, Length, Email

from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPForbidden
from pyramid.view import view_config
from pyramid.security import NO_PERMISSION_REQUIRED

from ..lib.i18n import _
from ..lib.log import log_info
from ..lib.utils import make_id, age
from ..lib.form import get_action, SameAs, Form
from ..lib.paging import PAGE_SIZES, Paging
from ..lib.filter import Filter
from ..lib.tabset import Tabset
from ..lib.mailing import Mailing
from ..lib.attachment import attachment_url, attachment_update
from ..includes.themes import theme_static_prefix
from ..models import LABEL_LEN
from ..models.populate import xml2db, db2web, web2db
from ..models.dbprofile import DBProfile
from ..models.dbuser import DBUser, DBUserProfile
from ..models.dbgroup import DBGroup, DBGroupUser
from . import BaseView


# =============================================================================
class UserView(BaseView):
    """Class to manage user views.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    _DBUser = DBUser
    _xml2db = (xml2db,)
    _invitation_html = 'chrysalio:Templates/email_invitation.pt'
    _invitation_text = 'chrysalio:Templates/email_invitation.txt'
    _reset_password_html = 'chrysalio:Templates/email_reset_password.pt'
    _reset_password_text = 'chrysalio:Templates/email_reset_password.txt'

    # -------------------------------------------------------------------------
    @view_config(
        route_name='user_index', renderer='chrysalio:Templates/user_index.pt',
        permission='user-view')
    @view_config(route_name='user_index', renderer='json', xhr=True)
    def index(self):
        """List all users."""
        # Ajax
        i_creator = self._request.has_permission('user-create')
        if self._request.is_xhr:
            if i_creator:
                self._import_users()
            return {}

        # Action
        action, items = get_action(self._request)
        i_editor = self._request.has_permission('user-edit')
        if action[:4] == 'mel!' and i_editor:
            errors = self._send_invitation(items)
            if not errors:  # pragma: nocover
                self._request.session.flash(_('The invitation has been sent.'))
            else:
                for error in errors:
                    self._request.session.flash(error, 'alert')
        elif action[:4] == 'del!' and i_creator:
            self._delete_users(items)
        elif action == 'imp!' and i_creator:
            self._import_users()
        elif action[:4] == 'exp!' and i_editor:
            action = self._users2response(items)
            if action:
                return action

        # Filter
        paging_id = 'users'
        pfilter = Filter(
            self._request, paging_id, (
                ('login', _('Login'), False, ''),
                ('last_name', _('Last name'), False, ''),
                ('email', _('Email'), False, ''),
                # ('email_hidden', _('Hidden Email'), False, True),
                ('status', _('Status'), False,
                 [('', ' ')] + list(self._DBUser.status_labels.items()))),
            (('status', '=', 'active'),),
            remove=action[:4] == 'crm!' and action[4:] or None)

        # Paging
        defaults = Paging.params(self._request, paging_id, '+last_name')
        dbquery = pfilter.sql(
            self._request.dbsession.query(self._DBUser), 'users')
        oby = getattr(self._DBUser, defaults['sort'][1:])
        dbquery = dbquery.order_by(
            desc(oby) if defaults['sort'][0] == '-' else oby)
        user_paging = Paging(self._request, paging_id, dbquery, defaults)
        user_paging.set_current_ids('user_id')

        # Form & completed action
        form = Form(self._request, defaults=defaults)
        form.forget('filter_value')
        if action and action[3] == '!':
            action = ''

        # Breadcrumbs
        self._request.breadcrumbs(_('Users'), 2)

        return {
            'age': age, 'action': action, 'items': items, 'form': form,
            'pfilter': pfilter, 'paging': user_paging,
            'status_labels': self._DBUser.status_labels,
            'PAGE_SIZES': PAGE_SIZES, 'i_creator': i_creator,
            'i_editor': i_editor, 'has_attachments': bool(
                self._request.registry.settings.get('attachments')),
            'download_max_size': self._request.registry['settings'][
                'download-max-size'],
            'attachment_url': attachment_url}

    # -------------------------------------------------------------------------
    @view_config(route_name='user_index_filter', renderer='json', xhr=True)
    def index_filter(self):
        """Return a list to autocomplete a filter field."""
        return Filter.sql_autocomplete(self._request, self._DBUser)

    # -------------------------------------------------------------------------
    @view_config(
        route_name='user_view', renderer='chrysalio:Templates/user_view.pt')
    @view_config(
        route_name='user_account', renderer='chrysalio:Templates/user_view.pt')
    def view(self):
        """Show user settings."""
        if not self.can_view():
            raise HTTPForbidden()

        dbuser = self._get_user(str(self._request.session['user']['user_id']))
        is_me = dbuser.user_id == self._request.session['user']['user_id']
        picture = self._request.registry.settings.get('attachments') and (
            attachment_url(
                self._request, dbuser.attachments_dir, dbuser.attachments_key,
                dbuser.picture) or
            (dbuser.honorific == 'Mrs' and
             '{0}/images/user_picture_girl.svg'.format(
                 theme_static_prefix(self._request))) or
            '{0}/images/user_picture_boy.svg'.format(
                theme_static_prefix(self._request)))
        navigator = Paging.navigator(
            self._request, 'users', dbuser.user_id,
            self._request.route_path('user_view', user_id='_ID_')) \
            if self._request.matched_route.name == 'user_view' else ''

        action = get_action(self._request)[0]
        if action == 'exp!':
            action = self._users2response((dbuser.user_id,))
            if action:
                return action
        elif action == 'mel!':
            errors = self._send_invitation((dbuser.user_id,))
            if not errors:  # pragma: nocover
                self._request.session.flash(_('The invitation has been sent.'))
            else:
                self._request.session.flash(errors[0], 'alert')
            action = ''

        # Breadcrumbs
        user_name = '{0} {1}'.format(
            dbuser.first_name or '', dbuser.last_name).strip()
        if self._request.referrer and  \
           '/user/view/' in self._request.referrer:
            self._request.breadcrumbs.pop()
        self._request.breadcrumbs(
            _('My Account') if is_me else _('${n} Account', {'n': user_name}),
            replace=self._request.route_path(
                'user_edit', user_id=dbuser.user_id))
        return {
            'form': Form(self._request),
            'tabset': Tabset(
                self._request, 'tabUser', dbuser.settings_tabs(self._request)),
            'dbuser': dbuser, 'is_me': is_me, 'user_name': user_name,
            'navigator': navigator, 'picture': picture,
            'i_editor': self._request.has_permission('user-edit')}

    # -------------------------------------------------------------------------
    @view_config(
        route_name='user_create', renderer='chrysalio:Templates/user_edit.pt')
    @view_config(
        route_name='user_edit', renderer='chrysalio:Templates/user_edit.pt')
    @view_config(route_name='user_edit', renderer='json', xhr=True)
    def edit(self):
        """Create or edit user settings."""
        # Authorization
        dbuser = self._get_user() if 'user_id' in self._request.matchdict \
            else None
        if (not dbuser and not self.can_create()) or \
           (dbuser and not self.can_edit()):
            raise HTTPForbidden()

        # Ajax
        if self._request.is_xhr:
            if dbuser is not None:
                dbuser.attachments_key, dbuser.picture = attachment_update(
                    self._request, dbuser.attachments_dir,
                    dbuser.attachments_key, self._request.POST['picture'],
                    replace=dbuser.picture,
                    prefix=dbuser.login.replace('@', '_')[:12])
                dbuser.account_update = datetime.now()
                log_info(self._request, 'user_update_picture', dbuser.login)
            return {}

        # Initialization
        is_me = dbuser and \
            dbuser.user_id == self._request.session['user']['user_id']
        profiles = {
            k.profile_id: (
                k.label(self._request), k.description(self._request))
            for k in self._request.dbsession.query(DBProfile)}
        groups = {
            k.group_id: (
                k.label(self._request), k.description(self._request))
            for k in self._request.dbsession.query(DBGroup)}

        # Form and action
        form = Form(
            self._request,
            *self._DBUser.settings_schema(
                self._request, profiles, groups, dbuser),
            obj=dbuser)
        action = get_action(self._request)[0]
        if action == 'pct!' and dbuser is not None:
            dbuser.attachments_key, dbuser.picture = attachment_update(
                self._request, dbuser.attachments_dir, dbuser.attachments_key,
                self._request.POST['picture'], replace=dbuser.picture,
                prefix=dbuser.login.replace('@', '_')[:12])
            dbuser.account_update = datetime.now()
            log_info(self._request, 'user_update_picture', dbuser.login)
        elif action == 'sav!' and form.validate():
            dbuser = self._save(dbuser, profiles, groups, form.values)
            if dbuser is not None:
                if is_me:
                    dbuser.set_session(self._request)
                if 'user_id' not in self._request.matchdict:
                    self._request.breadcrumbs.pop()
                log_info(
                    self._request, 'user_id' in self._request.matchdict and
                    'user_edit' or 'user_create', dbuser.login)
                return HTTPFound(self._request.route_path(
                    'user_view', user_id=dbuser.user_id))
        if form.has_error():
            self._request.session.flash(_('Correct errors.'), 'alert')

        # Picture
        picture = \
            dbuser and self._request.registry.settings.get('attachments') and (
                attachment_url(
                    self._request, DBUser.attachments_dir,
                    dbuser.attachments_key, dbuser.picture) or
                (dbuser.honorific == 'Mrs' and
                 '{0}/images/user_picture_girl.svg'.format(
                     theme_static_prefix(self._request))) or
                '{0}/images/user_picture_boy.svg'.format(
                    theme_static_prefix(self._request)))

        # Breadcrumbs
        user_name = dbuser and '{0} {1}'.format(
            dbuser.first_name or '', dbuser.last_name).strip()
        if self._request.referrer and  \
           '/user/account' in self._request.referrer:
            self._request.breadcrumbs.pop()
        if not dbuser:
            self._request.breadcrumbs(_('User Creation'))
        else:
            self._request.breadcrumbs(
                _('My Account Edition') if is_me else _(
                    '${n} Edition', {'n': user_name}),
                replace=self._request.route_path(
                    'user_view', user_id=dbuser.user_id))
        return {
            'form': form, 'dbuser': dbuser or self._DBUser,
            'user_name': user_name, 'action': action, 'profiles': profiles,
            'groups': groups, 'is_me': is_me, 'picture': picture,
            'tabset': Tabset(
                self._request, 'tabUser',
                self._DBUser.settings_tabs(self._request))}

    # -------------------------------------------------------------------------
    @view_config(
        route_name='user_password_forgot',
        renderer='chrysalio:Templates/user_password_forgot.pt',
        permission=NO_PERMISSION_REQUIRED)
    def password_forgot(self):
        """Get email address to send a token to reset the password."""
        schema = SchemaNode(Mapping())
        schema.add(SchemaNode(
            String(), name='email',
            validator=All(Email(), Length(max=LABEL_LEN))))
        form = Form(self._request, schema)
        if form.validate():
            dbuser = self._request.dbsession.query(self._DBUser).filter(
                self._DBUser.email.ilike(form.values['email'])).first()
            if dbuser is None:
                self._request.session.flash(
                    _('Please use the email associated with your account.'),
                    'alert')
            elif self._send_reset_password_link(dbuser):  # pragma: nocover
                self._request.session.flash(
                    _('A link to reset your password has been sent by mail.'))
                log_info(
                    self._request, 'user_password_forgot', dbuser.login)
                return HTTPFound(self._request.route_path('home'))

        self._request.breadcrumbs(_('Forgot Password'), 1)
        return {'form': form}

    # -------------------------------------------------------------------------
    @view_config(
        route_name='user_password_reset',
        renderer='chrysalio:Templates/user_password_reset.pt',
        permission=NO_PERMISSION_REQUIRED)
    def password_reset(self):
        """Reset the user password."""
        dbuser = self._get_user()
        token = '{0}{1}'.format(dbuser.login, date.today().isoformat())
        token = sha1(token.encode('utf8')).hexdigest()
        if token != self._request.matchdict['token']:
            raise HTTPNotFound(comment=_('This page does not exist anymore.'))

        password_min_length = self._request.registry['settings'][
            'password-min-length']
        schema = SchemaNode(Mapping())
        schema.add(SchemaNode(
            String(), name='password1',
            validator=All(
                Length(min=password_min_length),
                SameAs(self._request, 'password2'))))
        schema.add(SchemaNode(String(), name='password2'))
        form = Form(self._request, schema)
        if form.validate():
            dbuser.set_password(form.values['password1'])
            dbuser.password_mustchange = False
            self._request.session.flash(
                _('Your password has been changed. You can use it.'))
            log_info(self._request, 'user_password_reset')
            return HTTPFound(self._request.route_path('home'))

        self._request.breadcrumbs(_('Password Reset'), 1)
        return {'form': form}

    # -------------------------------------------------------------------------
    def can_view(self):
        """Check if the current user can view the user account.

        :rtype: bool
        """
        if self._request.has_permission('user-view'):
            return True
        user_id = self._request.matchdict.get('user_id')
        if user_id is None or (
                user_id.isdigit() and
                int(user_id) == self._request.session['user']['user_id']):
            return True
        return False

    # -------------------------------------------------------------------------
    def can_create(self):
        """Check if the current user can create a new user.

        :rtype: bool
        """
        if not self._request.has_permission('user-create'):
            return False
        return True

    # -------------------------------------------------------------------------
    def can_edit(self):
        """Check if the current user can edit an user account.

        :rtype: bool
        """
        if self._request.has_permission('user-edit'):
            return True
        user_id = self._request.matchdict['user_id']
        if user_id.isdigit() and \
           int(user_id) == self._request.session['user']['user_id']:
            return True
        return False

    # -------------------------------------------------------------------------
    def _get_user(self, my_user_id=''):
        """Return the SqlAlchemy object of the selected user or raise an
        HTTPNotFound exception.

        :param str my_user_id: (optional)
            User ID of current user.
        :rtype: .models.dbuser.DBUser
        """
        user_id = self._request.matchdict.get('user_id', my_user_id)
        if not user_id.isdigit():
            raise HTTPNotFound()
        dbuser = self._request.dbsession.query(self._DBUser).filter_by(
            user_id=int(user_id)).first()
        if dbuser is None:
            raise HTTPNotFound()
        return dbuser

    # -------------------------------------------------------------------------
    def _delete_users(self, user_ids):
        """Delete users.

        :param list user_ids:
            List of user IDs to delete.
        """
        user_ids = {int(k) for k in user_ids}

        # Do not delete myself
        if self._request.session['user']['user_id'] in user_ids:
            self._request.session.flash(
                _("You can't delete your own user."), 'alert')
            return

        # Do not delete an administrator
        if 1 in user_ids or \
           (not self._request.has_permission('system.administrator') and
            self._request.dbsession.query(self._DBUser.user_id).filter(
                self._DBUser.user_id.in_(user_ids)).filter_by(
                    status='administrator').first() is not None):
            self._request.session.flash(
                _("You can't delete an administrator."), 'alert')
            return

        # Delete
        deleted = []
        attachments = self._request.registry.settings.get('attachments')
        for dbuser in self._request.dbsession.query(self._DBUser).filter(
                self._DBUser.user_id.in_(user_ids)):
            if attachments and dbuser.attachments_key:
                attachment = join(
                    attachments, DBUser.attachments_dir,
                    dbuser.attachments_key)
                if exists(attachment):
                    rmtree(attachment)
            deleted.append(dbuser.login)
            self._request.dbsession.delete(dbuser)
        if deleted:
            log_info(self._request, 'user_delete', ' '.join(deleted))

    # -------------------------------------------------------------------------
    def _import_users(self):
        """Import users."""
        # Get current IDs
        user_logins = {
            k[0] for k in self._request.dbsession.query(DBUser.login)}

        # Update database
        web2db(self._request, self._xml2db[0], 'user')

        # Get new IDs
        user_logins = {k[0] for k in self._request.dbsession.query(
            DBUser.login)} - user_logins
        if user_logins:
            log_info(self._request, 'user_import', ' '.join(user_logins))

    # -------------------------------------------------------------------------
    def _users2response(self, user_ids):
        """Export users as an XML file embedded in a Pyramid response.

        :param list user_ids:
            List of user IDs to export.
        :rtype: :class:`pyramid.response.Response` or ``''``
        """
        dbitems = [
            k for k in self._request.dbsession.query(self._DBUser).filter(
                self._DBUser.user_id.in_(user_ids))
            if k.user_id != 1 or k.status != 'administrator']
        if not dbitems:
            self._request.session.flash(
                _('You cannot export the main administrator.'), 'alert')
            return ''
        filename = '{0}.{1}.xml'.format(
            len(dbitems) == 1 and dbitems[0].login or
            make_id(self._request.registry['settings']['title'], 'token'),
            self._DBUser.suffix)
        log_info(
            self._request, 'user_export',
            ' '.join([k.login for k in dbitems]))

        return db2web(self._request, dbitems, filename)

    # -------------------------------------------------------------------------
    def _send_invitation(self, user_ids):
        """Send an e-mail invitation to each user.

        :param list user_ids:
            List of user IDs to invite.
        :rtype: list
        :return:
            A list of errors.
        """
        site_title = self._request.registry['settings']['title']
        email_template = {
            'subject': _('Invitation to join ${n}', {'n': site_title}),
            'from': self._request.session['user']['email'],
            'html_template': self._invitation_html,
            'text_template': self._invitation_text}
        recipients = []
        for dbuser in self._request.dbsession.query(self._DBUser).filter(
                self._DBUser.user_id.in_(user_ids)):
            recipients.append({
                'to': dbuser.email,
                'site_title': site_title,
                'login': dbuser.login,
                'honorific': dbuser.honorific,
                'first_name': dbuser.first_name or '',
                'last_name': dbuser.last_name,
                'url': self._request.route_url('home')})
        log_info(
            self._request, 'user_send_invitation',
            ' '.join([k['login'] for k in recipients]))

        return Mailing(self._request).mailing(email_template, recipients)

    # -------------------------------------------------------------------------
    def _send_reset_password_link(self, dbuser):
        """Send an e-mail with a link to the page to reset the password.

        :type  dbuser: .models.dbuser.DBUser
        :param dbuser:
            The concerned user.
        :rtype: bool
        """
        site_title = self._request.registry['settings']['title']
        from_field = self._request.registry['settings']['email']
        email_template = {
            'subject': _('Password Reset on ${n}', {'n': site_title}),
            'from': from_field,
            'html_template': self._reset_password_html,
            'text_template': self._reset_password_text}

        token = '{0}{1}'.format(dbuser.login, date.today().isoformat())
        token = sha1(token.encode('utf8')).hexdigest()
        recipient = {
            'to': dbuser.email,
            'site_title': site_title,
            'login': dbuser.login,
            'honorific': dbuser.honorific,
            'first_name': dbuser.first_name or '',
            'last_name': dbuser.last_name,
            'url': self._request.route_url(
                'user_password_reset', user_id=dbuser.user_id, token=token)}

        error = Mailing(self._request).mailing(email_template, [recipient])
        if error:
            self._request.session.flash(error[0], 'alert')
            return False
        return True  # pragma: nocover

    # -------------------------------------------------------------------------
    def _save(self, dbuser, profiles, groups, values):
        """Save a user settings.

        :type  dbuser: :class:`.models.dbuser.DBUser` or ``None``
        :param dbuser:
            User to save.
        :param dict profiles:
            A dictionary such as ``{profile_id: (label, description),...}``.
        :param dict groups:
            A dictionary such as ``{group_id: (label, description),...}``.
        :param dict values:
            Form values.
        :rtype: :class:`~.models.dbuser.DBUser` instance or ``None``
        """
        creation = dbuser is None
        dbuser = dbuser or self._DBUser()

        # Update user
        record = {k: values[k] for k in values if hasattr(self._DBUser, k)}
        record['password'] = values['password1'] or dbuser.password
        error = dbuser.record_format(record)
        if error:  # pragma: nocover
            self._request.session.flash(error, 'alert')
            return None
        modified = creation
        record.update({
            k:  None for k in values
            if not values[k] and hasattr(self._DBUser, k)})
        for field in record:
            if getattr(dbuser, field) != record[field]:
                modified = True
                setattr(dbuser, field, record[field])
        if not creation and values['password1']:
            modified = True
            dbuser.password_update = datetime.now()

        # Save
        if creation:
            try:
                self._request.dbsession.add(dbuser)
                self._request.dbsession.flush()
            except (IntegrityError, FlushError):
                self._request.session.flash(
                    _('This user already exists.'), 'alert')
                return None

        # Update extra informations
        modified |= self._save_extra(dbuser, profiles, groups, values)

        if modified:
            dbuser.account_update = datetime.now()

        return dbuser

    # -------------------------------------------------------------------------
    def _save_extra(self, dbuser, profiles, groups, values):
        """Save extra information on a user .

        :type  dbuser: :class:`.models.dbuser.DBUser` or ``None``
        :param dbuser:
            User to save.
        :param dict profiles:
            A dictionary such as ``{profile_id: (label, description),...}``.
        :param dict groups:
            A dictionary such as ``{group_id: (label, description),...}``.
        :param dict values:
            Form values.
        :rtype: bool
        """
        modified = False
        if not self._request.has_permission('user-create'):
            return False

        # Update profiles
        user_profiles = {k.profile_id: k for k in dbuser.profiles}
        for profile_id in profiles:
            value = values['pfl:{0}'.format(profile_id)]
            if value and profile_id not in user_profiles:
                modified = True
                self._request.dbsession.add(DBUserProfile(
                    user_id=dbuser.user_id, profile_id=profile_id))
            elif not value and profile_id in user_profiles:
                modified = True
                self._request.dbsession.delete(
                    self._request.dbsession.query(DBUserProfile).filter_by(
                        user_id=dbuser.user_id, profile_id=profile_id)
                    .first())

        # Update groups
        user_groups = {k.group_id: k for k in dbuser.groups}
        for group_id in groups:
            value = values['grp:{0}'.format(group_id)]
            if value and group_id not in user_groups:
                modified = True
                self._request.dbsession.add(DBGroupUser(
                    group_id=group_id, user_id=dbuser.user_id))
            elif not value and group_id in user_groups:
                modified = True
                self._request.dbsession.delete(
                    self._request.dbsession.query(DBGroupUser).filter_by(
                        group_id=group_id, user_id=dbuser.user_id)
                    .first())

        return modified
