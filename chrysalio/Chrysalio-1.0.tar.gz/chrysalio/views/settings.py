"""Settings management view callables."""

from lxml import etree

from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound

from ..lib.i18n import _
from ..lib.log import log_info
from ..lib.utils import make_id
from ..lib.xml import create_entire_xml
from ..lib.form import get_action, Form
from ..lib.tabset import Tabset
from ..models.populate import xml2db, web2db
from ..models.dbsettings import DBSettings
from . import BaseView


# =============================================================================
class SettingsView(BaseView):
    """Class to manage settings views.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """

    # -------------------------------------------------------------------------
    @view_config(
        route_name='settings_view',
        renderer='chrysalio:Templates/settings_view.pt',
        permission='settings-view')
    @view_config(route_name='settings_view', renderer='json', xhr=True)
    def view(self):
        """Show general settings."""
        # Ajax
        i_editor = self._request.has_permission('settings-edit')
        if self._request.is_xhr:
            if i_editor:
                web2db(self._request, xml2db, 'settings')
                self._request.registry['settings'] = DBSettings.db2dict(
                    self._request.registry.settings, self._request.dbsession,
                    self._request.registry['settings']['email'])
                log_info(self._request, 'settings_import')
            return {}

        # Action
        action = get_action(self._request)[0]
        if action == 'exp!':
            action = self._settings2response()
            if action:
                return action
        elif action == 'imp!' and i_editor:
            web2db(self._request, xml2db, 'settings')
            self._request.registry['settings'] = DBSettings.db2dict(
                self._request.registry.settings, self._request.dbsession,
                self._request.registry['settings']['email'])
            log_info(self._request, 'settings_import')

        # Breadcrumbs
        self._request.breadcrumbs(
            _('General Settings'), 2,
            replace=self._request.route_path('settings_edit'))

        return {
            'form': Form(self._request), 'dbsettings': DBSettings,
            'i_editor': i_editor, 'action': action,
            'download_max_size': self._request.registry['settings'][
                'download-max-size'],
            'tabset': Tabset(
                self._request, 'tabSettings',
                DBSettings.settings_tabs(self._request))}

    # -------------------------------------------------------------------------
    @view_config(
        route_name='settings_edit',
        renderer='chrysalio:Templates/settings_edit.pt',
        permission='settings-edit')
    def edit(self):
        """Edit general settings."""
        # Form and action
        form = Form(self._request, *DBSettings.settings_schema(self._request))
        action = get_action(self._request)[0]
        if action == 'sav!' and form.validate():
            self._save(form.values)
            log_info(self._request, 'settings_edit')
            return HTTPFound(self._request.route_path('settings_view'))
        if form.has_error():
            self._request.session.flash(_('Correct errors.'), 'alert')

        # Breadcrumbs
        self._request.breadcrumbs(
            _('General Settings Edition'), 2,
            replace=self._request.route_path('settings_view'))

        return {
            'form': form, 'dbsettings': DBSettings,
            'tabset': Tabset(
                self._request, 'tabSettings',
                DBSettings.settings_tabs(self._request))}

    # -------------------------------------------------------------------------
    def _settings2response(self):
        """Export settings as an XML file embedded in a Pyramid response.

        :rtype: :class:`pyramid.response.Response` or ``''``
        """
        # Create the XML file
        root = create_entire_xml(
            self._request.registry['relaxng'],
            [DBSettings.db2xml(self._request.dbsession)])
        # pylint: disable = protected-access
        if not isinstance(root, etree._Element):  # pragma: nocover
            return Response(body=root)
        # pylint: enable = protected-access

        filename = '{0}_settings.{1}.xml'.format(
            make_id(self._request.registry['settings']['title'], 'token'),
            DBSettings.suffix)
        response = Response(
            body=etree.tostring(
                root, pretty_print=True, xml_declaration=True,
                encoding='utf-8'),
            content_type='application/xml')
        response.headerlist.append((
            'Content-Disposition', 'attachment; filename="{0}"'.format(
                filename)))

        log_info(self._request, 'settings_export')
        return response

    # -------------------------------------------------------------------------
    def _save(self, values):
        """Save settings."""
        # Update settings table
        for key, value in values.items():
            dbsetting = self._request.dbsession.query(DBSettings).filter_by(
                key=key).first()
            if dbsetting is None:  # pragma: nocover
                self._request.dbsession.add(DBSettings(key=key, value=value))
            else:
                dbsetting.value = value

        # Update registry
        self._request.registry['settings'] = DBSettings.db2dict(
            self._request.registry.settings, self._request.dbsession,
            values['email'])
