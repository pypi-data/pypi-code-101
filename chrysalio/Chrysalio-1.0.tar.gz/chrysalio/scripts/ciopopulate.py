"""Populate the database and the attachment directory."""

from sys import exit as sys_exit
from os import makedirs, sep
from os.path import exists, join, abspath, basename
from shutil import rmtree
from logging import getLogger
from argparse import REMAINDER
from datetime import datetime

from lxml import etree
from transaction import manager

from ..lib.i18n import _
from ..lib.utils import scandir, copy_content
from ..lib.xml import load_xml, relaxng4validation
from ..lib.config import config_get, config_get_namespace
from ..relaxng import RELAXNG
from ..models import get_tm_dbsession
from ..models.dbsettings import DBSettings
from ..models.dbuser import DBUser
from ..models.populate import xml2db
from . import Script


LOG = getLogger(__name__)


# =============================================================================
def main(args=None):
    """Main function."""
    args = Populate.arguments(Populate.argument_parser(), args)
    if args is not None:
        sys_exit(Populate(args, DBUser, xml2db, RELAXNG).run(args.files))


# =============================================================================
class Populate(Script):
    """Class to populate database.

    :type  args: argparse.Namespace
    :param args:
        Command line arguments.
    :param dbuser_class:
        Class to manage user SQL table.
    :param function _xml2db:
        Function to load XML configuration files. See
        :meth:`~chrysalio.models.populate.xml2db`.
    :param dict relaxng:
        A dictionary describing the main Relax NG with the following keys:
        ``'root'``, ``'version'`` and ``'file'``.
    :param list includes: (optional)
        List of hard coding `includes`.
    :type  dbsession_factory: sqlalchemy.orm.session.sessionmaker
    :param dbsession_factory: (optional)
        Function to create session.
    """
    # pylint: disable = too-many-arguments

    # -------------------------------------------------------------------------
    def __init__(self, args, dbuser_class, _xml2db, relaxng, includes=None,
                 dbsession_factory=None):
        """Constructor method."""
        super(Populate, self).__init__(args, True, includes, dbsession_factory)
        self._dbuser_class = dbuser_class
        self._xml2db = _xml2db
        self._relaxng = relaxng

    # -------------------------------------------------------------------------
    @classmethod
    def argument_parser(cls, description='Populate database.'):
        """Create an argument parser object to parse command line arguments.

        :param str description: (optional)
            Description of the script populating the database.
        :rtype: argparse.ArgumentParser
        """
        parser = super(Populate, cls).argument_parser(description=description)
        parser.add_argument(
            'files', nargs='*', help='optional XML configuration files to use')
        parser.add_argument(
            '--attachments', help='optional attachment directory  to use')
        parser.add_argument(
            '--drop-tables', dest='drop_tables', help='drop existing tables',
            action='store_true')
        parser.add_argument(
            '--remove-locks', dest='remove_locks', action='store_true',
            help='remove locks directory')
        parser.add_argument(
            '--remove-builds', dest='remove_builds', action='store_true',
            help='remove builds directory')
        parser.add_argument(
            '--skip-refresh', dest='skip_refresh', action='store_true',
            help='skip refreshment step')
        parser.add_argument(
            '--recreate-thumbnails', dest='recreate_thumbnails',
            action='store_true', help='recreate thumbnails')
        parser.add_argument(
            '--reindex', dest='reindex', action='store_true',
            help='recreate indexes')
        parser.add_argument('extra', nargs=REMAINDER, help='extra options')
        return parser

    # -------------------------------------------------------------------------
    def run(self, files=None):
        """Check settings and initialize database.

        :param list files: (optional)
            List of files on command-line.
        :rtype: int
        :return:
            Exit code.
        """
        if self.registry is None:
            return 1

        with manager:
            dbsession = get_tm_dbsession(
                self.registry['dbsession_factory'], manager)

            # Load administrator
            LOG.info(self._translate(_('====== Adding administrator')))
            error = self._dbuser_class.load_administrator(
                dbsession, config_get_namespace(
                    self._config, 'Populate', 'admin'))
            if error:
                LOG.error(self._translate(error))
                LOG.critical(self._translate(_('Incorrect administrator.')))
                return 1

            # Load XML configuration files
            self._populate_from_xml(dbsession, files or [])

            # Copy attachments
            self._copy_attachments(self._args.attachments)

            # Update settings
            dbsetting = dbsession.query(DBSettings).filter_by(
                key='populate').first()
            if dbsetting is None:
                dbsetting = DBSettings(key='populate')
                dbsession.add(dbsetting)
            dbsetting.value = datetime.now().isoformat(' ').split('.')[0]

            # Complete operation
            for module_id in self.registry['modules']:
                self.registry['modules'][module_id].activate(
                    self.registry, dbsession)
            for module_id in self.registry['modules']:
                error = self.registry['modules'][module_id].populate(
                    self._args, self.registry, dbsession)
                if error:  # pragma: nocover
                    LOG.error(self._translate(error))
                    return 1

        return 0

    # -------------------------------------------------------------------------
    def _populate_from_xml(self, dbsession, extra_files):
        """Populate database with XML content.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :param list extra_files:
             List of files on command-line.
        """
        # List of files to load
        files = config_get_namespace(self._config, 'Populate', 'data')
        files = [files[k] for k in sorted(files.keys())] + list(extra_files)
        if not files:  # pragma: nocover
            return

        # Load main Relax NG and Relax NG of each module
        relaxngs = relaxng4validation(self._relaxng)
        for module_id in self.registry['modules']:
            if self.registry['modules'][module_id].relaxng is not None:
                relaxngs.update(relaxng4validation(
                    self.registry['modules'][module_id].relaxng))

        # Load files
        LOG.info(self._translate(_('====== Loading configurations')))
        done = set()
        for filename in files:
            filename = abspath(filename)
            if filename in done:
                continue
            LOG.info(filename)
            tree = load_xml(filename, relaxngs)
            # pylint: disable = protected-access
            if not isinstance(tree, etree._ElementTree):
                LOG.error(self._translate(tree))
                continue
            # pylint: enable = protected-access
            errors = self._xml2db(
                dbsession, tree, error_if_exists=False,
                modules=self.registry['modules'])
            for error in errors:  # pragma: nocover
                LOG.error(self._translate(error))
            done.add(filename)

    # -------------------------------------------------------------------------
    def _copy_attachments(self, extra_attachments):
        """Possibly copy attachment files.

        :param list extra_attachments:
             Attachment directory on command-line.
        """
        destination = self.registry.settings.get('attachments')
        if not destination:
            return
        if config_get(self._config, 'Populate', 'drop_tables') == 'true' and \
           exists(destination):
            rmtree(destination)
        if not exists(destination):
            makedirs(destination)

        # List of attachments to copy
        attachments = config_get_namespace(
            self._config, 'Populate', 'attachment')
        attachments = [attachments[k] for k in sorted(attachments.keys())]
        if extra_attachments and exists(extra_attachments):
            if extra_attachments.endswith(sep):
                extra_attachments = extra_attachments[:-len(sep)]
            attachments += [
                join(extra_attachments, k.name)
                for k in scandir(extra_attachments)]
        for attachment in attachments:
            if exists(attachment):
                name = basename(attachment)
                for entry in scandir(attachment):
                    if entry.is_dir():
                        copy_content(
                            entry.path, join(destination, name, entry.name))
