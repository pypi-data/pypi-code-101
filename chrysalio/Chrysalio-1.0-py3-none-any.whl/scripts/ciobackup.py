"""Backup database into an XML file."""

from sys import exit as sys_exit
from os import makedirs
from os.path import exists, join, isdir
from shutil import rmtree
from logging import getLogger
from argparse import REMAINDER

from lxml import etree
from transaction import manager as transaction_manager

from ..lib.i18n import _
from ..lib.utils import scandir, copy_content
from ..lib.xml import create_entire_xml
from ..relaxng import RELAXNG
from ..models import get_tm_dbsession
from ..models.dbsettings import DBSettings
from ..models.populate import db2xml
from . import Script


LOG = getLogger(__name__)


# =============================================================================
def main(args=None):
    """Main function."""
    args = Backup.arguments(Backup.argument_parser(), args)
    if args is not None:
        sys_exit(Backup(args, db2xml, RELAXNG).run(args.directory))


# =============================================================================
class Backup(Script):
    """Class to backup database.

    :type  args: argparse.Namespace
    :param args:
        Command line arguments.
    :param function _db2xml:
        Function to save database fields into XML elements. See
        :meth:`~chrysalio.models.populate.db2xml`.
    :param dict relaxng:
        A dictionary describing the main Relax NG with the following keys:
        ``'root'``, ``'version'`` and ``'file'``.
    :param list includes: (optional)
        List of hard coding `includes`.
    :type  dbsession_factory: sqlalchemy.orm.session.sessionmaker
    :param dbsession_factory: (optional)
        Function to create session.
    """

    # -------------------------------------------------------------------------
    def __init__(self, args, _db2xml, relaxng, includes=None,
                 dbsession_factory=None):
        """Constructor method."""
        super(Backup, self).__init__(args, False, includes, dbsession_factory)
        self._db2xml = _db2xml
        self._relaxng = relaxng

    # -------------------------------------------------------------------------
    @classmethod
    def argument_parser(cls, description='Backup database.'):
        """Create an argument parser object to parse command line arguments.

        :param str description: (optional)
            Description of the script saving the database.
        :rtype: argparse.ArgumentParser
        """
        parser = super(Backup, cls).argument_parser(description=description)
        parser.add_argument('directory', help='path to backup directory')
        parser.add_argument(
            '--no-validation', dest='no_validation',
            help='do not validate the result', action='store_true')
        parser.add_argument('extra', nargs=REMAINDER, help='extra options')
        return parser

    # -------------------------------------------------------------------------
    def run(self, directory):
        """Save asked elements.

        :param str directory:
            Path to the backup directory.
        :rtype: int
        :return:
            Exit code.
        """
        # pylint: disable = too-many-return-statements
        if self.registry is None:
            return 1

        with transaction_manager:
            dbsession = get_tm_dbsession(
                self.registry['dbsession_factory'], transaction_manager)
            if not DBSettings.exists(dbsession):
                LOG.warning(self._translate(_('Database is empty!')))
                return 0

            # Browse elements
            elements = self._db2xml(
                dbsession, modules=self.registry['modules'])

            # Prepare output directory
            if not self._prepare_directory(directory):
                return 1

            # Save XML file
            root = create_entire_xml(
                self._relaxng, elements, not self._args.no_validation)
            # pylint: disable = protected-access
            if not isinstance(root, etree._Element):  # pragma: nocover
                LOG.error(root)
                return 1
            # pylint: enable = protected-access
            try:
                filename = join(directory, '{0}.xml'.format(
                    self.registry.settings['site.uid']))
                etree.ElementTree(root).write(
                    filename, pretty_print=True, encoding='utf-8',
                    xml_declaration=True)
            except (OSError, IOError):  # pragma: nocover
                LOG.error(self._translate(
                    _('${f} is write protected.', {'f': filename})))
                return 1

            # Complete operation
            for module_id in self.registry['modules']:
                self.registry['modules'][module_id].activate(
                    self.registry, dbsession)
            for module_id in self.registry['modules']:
                error = self.registry['modules'][module_id].backup(
                    self._args, self.registry, dbsession, directory)
                if error:  # pragma: nocover
                    LOG.error(self._translate(error))
                    return 1

        # Save attachments
        self._copy_attachments(directory)

        return 0

    # -------------------------------------------------------------------------
    def _prepare_directory(self, directory):
        """Create or clean up output directory.

        :param str directory:
            Path to the backup directory.
        :rtype: bool
        """
        if exists(directory) and not isdir(directory):
            LOG.error(self._translate(
                _('${d} must be a directory.', {'d': directory})))
            return False

        if not exists(directory):
            try:
                makedirs(directory)
            except (OSError, IOError):  # pragma: nocover
                LOG.error(self._translate(
                    _('${d} is write protected.', {'d': directory})))
                return False

        for entry in scandir(directory):
            if entry.is_dir():
                rmtree(entry.path)

        return True

    # -------------------------------------------------------------------------
    def _copy_attachments(self, directory):
        """Possibly copy attachment files.

        :param str directory:
            Path to the backup directory.
        """
        attachments = self.registry.settings.get('attachments')
        if attachments and exists(attachments):
            for entry in scandir(attachments):
                if entry.is_dir():
                    copy_content(entry.path, join(directory, entry.name))
