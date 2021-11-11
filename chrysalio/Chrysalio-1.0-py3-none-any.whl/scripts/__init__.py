"""Console scripts."""

from sys import exit as sys_exit
from logging import getLogger
from os.path import exists, abspath, dirname
from argparse import ArgumentParser
from collections import OrderedDict
from configparser import ConfigParser
from importlib import import_module

from sqlalchemy.exc import OperationalError
from plaster.exceptions import InvalidURI

from pyramid.paster import get_appsettings

from ..security import PRINCIPALS
from ..lib.i18n import _, translate
from ..lib.config import config_get, settings_get_list
from ..lib.log import setup_logging
from ..lib.utils import tounicode
from ..modules import Module
from ..models import DB_METADATA
from ..models import get_dbengine, get_dbsession_factory


LOG = getLogger(__name__)


# =============================================================================
class ScriptRegistry(dict):
    """Class to simulate Application Registry."""

    def __init__(self, settings):
        """Constructor method."""
        super(ScriptRegistry, self).__init__()
        self.settings = settings


# =============================================================================
class Script(object):
    """Base class for a script which reads the INI file and interacts with the
    database.

    :type  args: argparse.Namespace
    :param args:
        Command line arguments.
    :param bool create_all:
        If ``True``, it creates all the tables, otherwise, it checks if the
        table ``users`` exists with at least one user.
    :param list includes: (optional)
        List of hard coding `includes`.
    :type  dbsession_factory: sqlalchemy.orm.session.sessionmaker
    :param dbsession_factory: (optional)
        Function to create session.
    """

    # -------------------------------------------------------------------------
    def __init__(
            self, args, create_all, includes=None, dbsession_factory=None):
        """Constructor method."""
        self._args = args
        self.registry = None

        try:
            settings = get_appsettings(args.conf_uri, options=args.options)
        except (LookupError, IOError, InvalidURI) as error:
            LOG.critical(error)
            return

        config_file = abspath(args.conf_uri.partition('#')[0])
        self._config = ConfigParser({'here': dirname(config_file)})
        self._config.read(tounicode(config_file), encoding='utf8')

        self.registry = ScriptRegistry(settings)
        self.registry.settings['__file__'] = config_file
        self.registry['principals'] = list(PRINCIPALS)
        self.registry['modules'] = OrderedDict()
        self._load_includes(includes)

        if not self._initialize_database(create_all, dbsession_factory):
            self.registry = None
            return

    # -------------------------------------------------------------------------
    @classmethod
    def argument_parser(cls, description):
        """Create an argument parser object to parse command line arguments.

        :param str description:
            Description of the script.
        :rtype: argparse.ArgumentParser
        """
        parser = ArgumentParser(description=description)
        parser.add_argument(
            'conf_uri', help='URI of configuration (e.g. production.ini#foo)')
        parser.add_argument(
            '--options', dest='options', help='optional configuration options')
        parser.add_argument('--lang', dest='lang', help='user language')
        parser.add_argument(
            '--log-level', dest='log_level', help='log level', default='INFO',
            choices=('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'))
        parser.add_argument('--log-file', dest='log_file', help='log file')
        return parser

    # -------------------------------------------------------------------------
    @classmethod
    def arguments(cls, parser, args=None, filemode='w'):
        """Retrieve arguments from parser, check them and setup logging.

        :type parser: argparse.ArgumentParser
        :param parser:
             Configuration parser object.
        :param list args: (optional)
             Command line arguments (for testing).
        :param str filemode:
             File mode for logging (``'w'`` or ``'a'``).
        :rtype: argparse.Namespace
        """
        args = parser.parse_args(args)
        if not exists(args.conf_uri.partition('#')[0]):
            parser.print_usage()
            return None
        setup_logging(args.log_level, args.log_file, filemode=filemode)
        return args

    # -------------------------------------------------------------------------
    def _load_includes(self, includes=None):
        """Load needed modules with an `includeme()` function and fill
        ``self.registry`` dictionary.

        :param list includes: (optional)
            List of hard coding `includes`.
        """
        # Read include list
        if includes is None:
            includes = []
        includes += [k for k in settings_get_list(
            self.registry.settings, 'chrysalio.includes') if k]

        # Load modules
        for include in includes:
            try:
                module = import_module(include)
            except ImportError as error:
                sys_exit(self._translate(
                    _('*** Unable to load module "${m}" [${e}]', {
                        'm': include, 'e': error})))
            try:
                module.includeme(self.registry)
            except AttributeError as error:
                sys_exit(self._translate(_(
                    '*** Module "${m}" error: ${e}',
                    {'m': include, 'e': error})))

        # Check conflicts
        implementations, error = Module.check_conflicts(
            includes, self.registry['modules'])
        if error is not None:
            sys_exit(self._translate(error))

        # Check dependencies
        for module_id in self.registry['modules']:
            error = self.registry['modules'][module_id].check_dependencies(
                implementations)
            if error is not None:
                sys_exit(self._translate(error))

    # -------------------------------------------------------------------------
    def _initialize_database(self, create_all, dbsession_factory=None):
        """Database initialization.

        :param bool create_all:
            If ``True``, it creates all the tables, otherwise, it checks if the
            table ``users`` exists with at least one user.
        :type  dbsession_factory: sqlalchemy.orm.session.sessionmaker
        :param dbsession_factory: (optional)
            Function to create session.
        :rtype: bool
        """
        # Get database session factory
        self.registry['dbsession_factory'] = dbsession_factory
        if self.registry['dbsession_factory'] is None:
            try:
                dbengine = get_dbengine(self.registry.settings)
            except KeyError:
                LOG.critical(self._translate(_('Database is not defined.')))
                return False
            DB_METADATA.bind = dbengine
            self.registry['dbsession_factory'] = get_dbsession_factory(
                dbengine)

        # Possibly, drop any existing tables
        if hasattr(self._args, 'drop_tables') and (
                self._args.drop_tables or
                config_get(self._config, 'Populate', 'drop_tables') == 'true'):
            LOG.info(self._translate(_('====== Dropping existing tables')))
            tables = set(DB_METADATA.tables)
            try:
                DB_METADATA.reflect()
                DB_METADATA.drop_all()
            except UnicodeEncodeError:  # pragma: nocover
                LOG.error(self._translate(_('Unknown database!')))
                return False
            except OperationalError as error:  # pragma: nocover
                LOG.error(error.args[0])
                return False
            for table in set(DB_METADATA.tables) - tables:  # pragma: nocover
                DB_METADATA.remove(DB_METADATA.tables[table])

        if create_all:
            # Create the tables if they don't already exist
            try:
                DB_METADATA.create_all()
            except OperationalError as error:  # pragma: nocover
                LOG.error(error.args[0])
                return False

        return True

    # -------------------------------------------------------------------------
    def _translate(self, text):
        """Return ``text`` translated.

        :param str text:
            Text to translate.
        :rtype: str
        """
        return translate(text, self._args.lang)
