"""Configuration view callables."""

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import FlushError
from lxml import etree

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

from ....lib.i18n import _
from ....lib.log import log_info
from ....lib.utils import make_id
from ....lib.form import get_action, Form
from ....lib.xml import validate_xml, relaxng4validation
from ....views import BaseView
from ....models.populate import web2db
from ....models.dbprofile import DBProfile
from ..models.populate import xml2db
from ..models.dbldap import DBLdap, DBLdapProfile
from ..relaxng import RELAXNG_CIOLDAP


# =============================================================================
class CioLDAPView(BaseView):
    """Class to configure CioLDAP module.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """

    # -------------------------------------------------------------------------
    @view_config(
        route_name='cioldap_view',
        renderer='chrysalio:modules/cioldap/Templates/cioldap_view.pt',
        permission='modules-view')
    @view_config(route_name='cioldap_view', renderer='json', xhr=True)
    def view(self):
        """Display CioLDAP configuration."""
        i_editor = self._request.has_permission('cioldap-edit')
        if self._request.is_xhr:
            if i_editor:
                self._web2db()
            return {}

        # Edition mode
        dbldap = self._request.dbsession.query(DBLdap).first()
        if dbldap is None and self._request.has_permission('modules-edit'):
            return HTTPFound(self._request.route_path('cioldap_edit'))

        # Initialization
        profile_labels = {
            k.profile_id: k.label(self._request)
            for k in self._request.dbsession.query(DBProfile)}

        # Action
        action = get_action(self._request)[0]
        if action == 'exp!' and dbldap is not None:
            action = self._db2web(dbldap)
            if action:
                return action
        elif action == 'imp!' and i_editor:
            self._web2db()
            dbldap = self._request.dbsession.query(DBLdap).first()

        self._request.breadcrumbs(
            _('CioLDAP Module Configuration'),
            replace=self._request.route_path('cioldap_edit'))

        return {
            'form': Form(self._request), 'dbldap': dbldap,
            'i_editor': i_editor, 'profile_labels': profile_labels,
            'action': action,
            'download_max_size': self._request.registry['settings'][
                'download-max-size']}

    # -------------------------------------------------------------------------
    @view_config(
        route_name='cioldap_edit',
        renderer='chrysalio:modules/cioldap/Templates/cioldap_edit.pt',
        permission='cioldap-edit')
    def edit(self):
        """Create or edit CioLDAP configuration."""
        dbldap = self._request.dbsession.query(DBLdap).first()
        creation = dbldap is None
        profile_labels = {
            k.profile_id: k.label(self._request)
            for k in self._request.dbsession.query(DBProfile)}

        # Form and action
        form = Form(
            self._request, *DBLdap.settings_schema(profile_labels, dbldap),
            obj=dbldap)
        action = get_action(self._request)[0]
        if action == 'imp!':
            web2db(
                self._request, xml2db, 'ldap',
                relaxngs={
                    '{{{0}}}{1}'.format(
                        RELAXNG_CIOLDAP['namespace'],
                        RELAXNG_CIOLDAP['root']): RELAXNG_CIOLDAP['file']})
            if not self._request.session.peek_flash('alert'):
                log_info(self._request, 'ldap_import')
                return HTTPFound(self._request.route_path('cioldap_view'))
        elif action == 'sav!' and form.validate():
            dbldap = self._save(dbldap, profile_labels, form.values)
            if dbldap is not None:
                self._request.registry['authorities'][
                    'ldap'].reset_configuration()
                log_info(
                    self._request, creation and 'ldap_edit' or 'ldap_create')
                return HTTPFound(self._request.route_path('cioldap_view'))
        if form.has_error():
            self._request.session.flash(_('Correct errors.'), 'alert')

        self._request.breadcrumbs(
            _('CioLDAP Module Edition'), replace=self._request.route_path(
                'cioldap_view'))

        return {
            'form': form, 'dbldap': dbldap or DBLdap,
            'profile_labels': profile_labels,
            'creation': dbldap is None, 'action': action}

    # -------------------------------------------------------------------------
    def _save(self, dbldap, profiles, values):
        """Save a CioLDAP configuration.

        :type  dbldap: .models.dbldap.DBLdap
        :param dbldap:
            Ldap to save.
        :param dict profiles:
            A dictionary such as ``{profile_id: label,...}``.
        :param dict values:
            Form values.
        :rtype: :class:`~.models.dbldap.Ldap` instance or ``None``
        """
        creation = dbldap is None
        dbldap = dbldap or DBLdap()

        # Update ldap
        record = {k: values[k] for k in values if hasattr(DBLdap, k)}
        record['root_password'] = \
            values['root_password1'] or \
            (not creation and dbldap.root_password) or None
        error = dbldap.record_format(record)
        if error:  # pragma: nocover
            self._request.session.flash(error, 'alert')
            return None
        for field in record:
            setattr(dbldap, field, record[field])

        # Save
        if creation:
            try:
                self._request.dbsession.add(dbldap)
                self._request.dbsession.flush()
            except (IntegrityError, FlushError):  # pragma: nocover
                self._request.session.flash(
                    _('This CioLDAP configuration already exists.'), 'alert')
                return None

        # Update profiles
        ldap_profiles = {k.profile_id: k for k in dbldap.user_profiles}
        for profile_id in profiles:
            value = values['pfl:{0}'.format(profile_id)]
            if value and profile_id not in ldap_profiles:
                self._request.dbsession.add(DBLdapProfile(
                    ldap_id=dbldap.ldap_id, profile_id=profile_id))
            elif not value and profile_id in ldap_profiles:
                self._request.dbsession.query(DBLdapProfile).filter_by(
                    ldap_id=dbldap.ldap_id, profile_id=profile_id).delete()

        return dbldap

    # -------------------------------------------------------------------------
    def _db2web(self, dbldap):
        """Export CioLDAP configuration as an XML file embedded in a Pyramid
        response.

        :type  dbldap: :class:`.modules.cioldap.models.dbldap.DBLdap`
        :param dbldap:
            Current SqlAlchemy LDPA object.
        :rtype: :class:`pyramid.response.Response` or ``''``
        """
        # Create the XML file
        root = '{{{0}}}{1}'.format(
            RELAXNG_CIOLDAP['namespace'], RELAXNG_CIOLDAP['root'])
        root_elt = etree.Element(
            root, version=RELAXNG_CIOLDAP['version'],
            nsmap={None: RELAXNG_CIOLDAP['namespace']})
        root_elt.append(dbldap.db2xml())
        root_elt = etree.XML(etree.tostring(root_elt, encoding='utf-8'))
        error = validate_xml(
            etree.ElementTree(root_elt), relaxng4validation(RELAXNG_CIOLDAP),
            True)
        if error:  # pragma: nocover
            return self._request.localizer.translate(error)

        # Convert it into a response
        filename = '{0}.{1}.xml'.format(
            make_id(self._request.registry['settings']['title'], 'token'),
            DBLdap.suffix)
        response = Response(
            body=etree.tostring(
                root_elt, pretty_print=True, encoding='utf-8',
                xml_declaration=True), content_type='application/xml')
        response.headerlist.append((
            'Content-Disposition', 'attachment; filename="{0}"'.format(
                filename)))
        log_info(self._request, 'cioldap_export')
        return response

    # -------------------------------------------------------------------------
    def _web2db(self):
        """Import a CioLDAP configuration."""
        web2db(
            self._request, xml2db, 'ldap', relaxngs={
                '{{{0}}}{1}'.format(
                    RELAXNG_CIOLDAP['namespace'],
                    RELAXNG_CIOLDAP['root']): RELAXNG_CIOLDAP['file']})
        log_info(self._request, 'cioldap_import')
