"""Backup view callables."""

from os.path import exists, join, relpath
from time import time
from tempfile import mkdtemp
from shutil import rmtree
from zipfile import ZIP_DEFLATED, ZipFile, LargeZipFile
from configparser import ConfigParser

from lxml import etree
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm.session import close_all_sessions
from transaction import manager

from pyramid.view import view_config
from pyramid.response import Response, FileResponse

from ..lib.i18n import _
from ..lib.utils import scandir, walk, tounicode
from ..lib.form import get_action, Form
from ..lib.xml import create_entire_xml
from ..lib.config import config_get_namespace
from ..lib.log import log_info, log_error
from ..models import DB_METADATA, get_tm_dbsession
from ..models.dbuser import DBUser
from ..models.populate import db2xml, xml2db, web2db
from . import BaseView


# =============================================================================
class BackupView(BaseView):
    """Class to manage backup and restore operations.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """
    _DBUser = DBUser
    _db2xml = (db2xml,)
    _xml2db = (xml2db,)

    # -------------------------------------------------------------------------
    @view_config(
        route_name='backup', renderer='chrysalio:Templates/backup.pt',
        permission='backup-create')
    @view_config(
        route_name='backup', renderer='json', xhr=True,
        permission='backup-create')
    def index(self):
        """Choose between backup and restore."""
        # Ajax
        if self._request.is_xhr:
            self._restore()
            return {}

        # Action
        action = get_action(self._request)[0]
        if action == 'bck!':
            response = self._backup()
            if response is not None:
                return response
        if action == 'rst!':
            self._restore()

        # Breadcrumbs
        self._request.breadcrumbs(_('Configuration Backup'), 2)

        return {
            'form': Form(self._request), 'action': action,
            'download_max_size': self._request.registry['settings'][
                'download-max-size']}

    # -------------------------------------------------------------------------
    def _backup(self):
        """Backup the configuration into a ZIP or an XML file.

        :rtype: pyramid.response.Response
        """
        # Create the XML file
        elements = self._db2xml[0](
            self._request.dbsession,
            modules=self._request.registry.get('modules'))
        root_elt = create_entire_xml(
            self._request.registry['relaxng'], elements)
        # pylint: disable = protected-access
        if not isinstance(root_elt, etree._Element):  # pragma: nocover
            self._request.session.flash(root_elt, 'alert')
            return None
        # pylint: enable = protected-access

        # Return a XML file
        site_uid = self._request.registry.settings['site.uid']
        attachments = self._request.registry.settings.get('attachments')
        if not attachments or not exists(attachments) \
           or not tuple(scandir(attachments)):
            response = Response(
                body=etree.tostring(
                    root_elt, pretty_print=True, xml_declaration=True,
                    encoding='utf-8'),
                content_type='application/xml')
            response.headerlist.append((
                'Content-Disposition', 'attachment; filename="{0}.xml"'.format(
                    site_uid)))
            log_info(self._request, 'backup without attachments')
            return response

        # Return a Zip
        # pylint: disable = consider-using-with
        tmp_dir = mkdtemp(
            prefix=site_uid,
            dir=self._request.registry.settings.get('temporary'))
        zip_file = ZipFile(
            join(tmp_dir, '{0}.zip'.format(site_uid)), 'w', ZIP_DEFLATED)
        zip_file.writestr(
            '{0}.xml'.format(site_uid), etree.tostring(
                root_elt, encoding='utf-8', xml_declaration=True,
                pretty_print=True))
        for root, unused_, files in walk(attachments):
            for name in files:
                name = join(root, name)
                try:
                    zip_file.write(name, relpath(name, attachments))
                except LargeZipFile:  # pragma: nocover
                    zip_file.close()
                    rmtree(tmp_dir)
                    self._request.session.flash(
                        _('This configuration is too big!'), 'alert')
                    return None
                except IOError as error:  # pragma: nocover
                    zip_file.close()
                    rmtree(tmp_dir)
                    self._request.session.flash(error, 'alert')
                    return None
        zip_file.close()

        filename = zip_file.filename
        response = FileResponse(
            filename, request=self._request, content_type='application/zip')
        response.headers['Content-Disposition'] = \
            'attachment; filename="{0}.zip"'.format(site_uid)
        rmtree(tmp_dir)
        log_info(self._request, 'backup with attachments')
        return response

    # -------------------------------------------------------------------------
    def _restore(self):
        """Restore a configuration from a ZIP or an XML file.

        :rtype: bool
        """
        # Reset the old configuration
        reset = self._request.params.get('reset')
        admin = None
        if reset:
            admin = self._administrator_retrieve()
            if not self._drop_dbtables():  # pragma: nocover
                return False
            attachments = self._request.registry.settings.get('attachments')
            if attachments and exists(attachments):
                rmtree(attachments)

        # Restore the new configuration
        with manager:
            self._request.dbsession = get_tm_dbsession(
                self._request.registry['dbsession_factory'], manager)
            if not self._administrator_restore(admin):
                return False
            web2db(self._request, self._xml2db[0], error_if_exists=reset)
            if self._request.session.peek_flash('alert'):
                return False

        # To be continued
        self._request.session.flash(_('Backup restored.'))
        log_info(self._request, 'restore with reset' if reset else 'restore')
        if reset:
            self._request.session.clear()
            self._request.session['_creation_time'] = time()
            self._request.session['_accessed_time'] = time()
            self._request.response.delete_cookie(
                self._request.registry.settings.get('auth.cookie', 'CIO_AUTH'))
        return True

    # -------------------------------------------------------------------------
    def _administrator_retrieve(self):
        """Retrieve the administrator record.

        :rtype: dict
        """
        dbuser = self._request.dbsession.query(self._DBUser).filter_by(
            status='administrator').order_by('user_id').first()

        if dbuser is not None:
            return {
                k: dbuser.__dict__[k] for k in dbuser.__dict__
                if k[0] != '_' and k != 'user_id'}

        return None

    # -------------------------------------------------------------------------
    def _administrator_restore(self, record):
        """Restore the administrator record.

        :param dict record:
            Dictionary representing the administrator configuration.
        :rtype: bool
        """
        # Read administrator configuration from configuration file
        if record is None:
            config_file = self._request.registry.settings['__file__']
            config = ConfigParser({'here': config_file})
            config.read(tounicode(config_file), encoding='utf8')
            record = config_get_namespace(config, 'Populate', 'admin')

        error = self._DBUser.load_administrator(
            self._request.dbsession, record)
        if error:
            log_error(self._request, error)
            self._request.session.flash(error, 'alert')
            return False

        return True

    # -------------------------------------------------------------------------
    def _drop_dbtables(self):
        """Drop all tables of the database.

        :rtype: bool
        """
        # Drop
        try:
            close_all_sessions()
            DB_METADATA.drop_all()
        except OperationalError as error:  # pragma: nocover
            log_error(self._request, error.args[0])
            self._request.session.flash(error.args[0], 'alert')
            return False

        # Recreate
        try:
            DB_METADATA.create_all()
        except OperationalError as error:  # pragma: nocover
            log_error(self._request, error.args[0])
            self._request.session.flash(error.args[0], 'alert')
            return False

        return True
