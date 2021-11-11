# pylint: disable = import-outside-toplevel
"""Tests of ``scripts.cioupdate`` function and class."""

from os.path import exists, basename, join
from collections import namedtuple
from warnings import catch_warnings, simplefilter
from getpass import getuser
from unittest import TestCase

from testfixtures import log_capture

from . import TmpDirTestCase


# =============================================================================
class UScriptsCioUpdateMain(TestCase):
    """Unit test class for :func:`scripts.cioupdate.main`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:scripts.cioupdate.main]"""
        from ..scripts.cioupdate import main
        from . import CIOUPDATE_INI

        self.assertRaises(SystemExit, main, [])
        main(['foo.ini'])
        main([CIOUPDATE_INI])


# =============================================================================
class UScriptsCioUpdateCioUpdate(TmpDirTestCase):
    """Unit test class for :class:`scripts.cioupdate.CioUpdate`."""

    _currentdir = None

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        super(UScriptsCioUpdateCioUpdate, self).setUp()

        self.args = namedtuple(
            'ArgumentParser',
            'lang password no_backup no_update log_level log_file'
            ' drop_tables remove_locks remove_builds skip_refresh'
            ' recreate_thumbnails reindex extra key')(
                lang='en', password=None, no_backup=False, no_update=False,
                log_level='INFO', log_file=None, drop_tables=False,
                remove_locks=False, remove_builds=False, skip_refresh=False,
                recreate_thumbnails=False, reindex=False, extra=(), key=None)

    # -------------------------------------------------------------------------
    def test_start_encrypt(self):
        """[u:scripts.cioupdate.CioUpdate.start] encrypt"""
        from . import CIOUPDATE_INI
        from ..scripts.cioupdate import CioUpdate

        @log_capture()
        def call_test(log):
            """Function to ignore DeprecationWarning."""
            args = namedtuple('ArgumentParser', 'conf_file password key')(
                conf_file=CIOUPDATE_INI, password='foo', key=None)
            cioupdate = CioUpdate(args, CIOUPDATE_INI)
            self.assertTrue(cioupdate.start())
            self.assertEqual(len(log.records), 1)
            self.assertIn('foo = ', log.records[-1].getMessage())

        with catch_warnings():
            simplefilter('ignore')
            # pylint: disable = no-value-for-parameter
            call_test()

    # -------------------------------------------------------------------------
    def test_start_ok(self):
        """[u:scripts.cioupdate.CioUpdate.start] Ok"""
        from . import TEST_DIR, CIOUPDATE_INI, BACKUP_DIR
        from ..scripts.cioupdate import CioUpdate

        self._make_database()
        with open(CIOUPDATE_INI, 'r') as hdl:
            content = hdl.read()
        content = content\
            .replace('%(here)s/../..', '%(here)s/..')\
            .replace('#user =', 'user = {0}'.format(getuser()))
        cioupdate_ini = join(TEST_DIR, basename(CIOUPDATE_INI))
        with open(cioupdate_ini, 'w') as hdl:
            hdl.write(content)

        @log_capture()
        def call_test(log):
            """Function to ignore DeprecationWarning."""
            cioupdate = CioUpdate(self.args, cioupdate_ini)
            cioupdate.start()
            messages = '\n'.join([k.getMessage() for k in log.records])
            self.assertIn('ciobackup TestChrysalio', messages)
            self.assertIn('/Chrysalio', messages)
            print(messages)
            self.assertTrue(
                ('ciopopulate TestChrysalio' in messages) or
                ('Temporary failure' in messages) or
                ('uthorization failed' in messages) or
                ('Connection timed out' in messages) or
                ('No route to host') in messages or
                ('Could not resolve host') in messages or
                ('cannot pull with rebase') in messages)
            self.assertTrue(exists(BACKUP_DIR))

        with catch_warnings():
            simplefilter('ignore')
            # pylint: disable = no-value-for-parameter
            call_test()

    # -------------------------------------------------------------------------
    def test_start_invalid_backup_user(self):
        """[u:scripts.cioupdate.CioUpdate.start] Invalid backup user"""
        from . import CIOUPDATE1_INI
        from ..scripts.cioupdate import CioUpdate

        self._make_database()

        @log_capture()
        def call_test(log):
            """Function to ignore DeprecationWarning."""
            cioupdate = CioUpdate(self.args, CIOUPDATE1_INI)
            cioupdate.start(['TestChrysalio1'])
            self.assertFalse([
                True for k in log.records if k.levelname == 'ERROR'])
            cioupdate.start(['TestChrysalio2'])
            self.assertTrue([
                True for k in log.records if k.levelname == 'ERROR'])

        with catch_warnings():
            simplefilter('ignore')
            # pylint: disable = no-value-for-parameter
            call_test()

    # -------------------------------------------------------------------------
    def test_start_invalid_update_user(self):
        """[u:scripts.cioupdate.CioUpdate.start] Invalid update user"""
        from . import CIOUPDATE2_INI
        from ..scripts.cioupdate import CioUpdate

        @log_capture()
        def call_test(log):
            """Function to ignore DeprecationWarning."""
            cioupdate = CioUpdate(self.args, CIOUPDATE2_INI)
            self.assertFalse(cioupdate.start())
            messages = '\n'.join([k.getMessage() for k in log.records])
            self.assertTrue(
                ('name not found' in messages) or
                ('Temporary failure' in messages) or
                ('uthorization failed' in messages) or
                ('Connection timed out' in messages) or
                ('No route to host') in messages or
                ('Could not resolve host') in messages or
                ('cannot pull with rebase') in messages)

        with catch_warnings():
            simplefilter('ignore')
            # pylint: disable = no-value-for-parameter
            call_test()

    # -------------------------------------------------------------------------
    def test_start_incorrect_repository(self):
        """[u:scripts.cioupdate.CioUpdate.start] Incorrect repository"""
        from . import CIOUPDATE3_INI
        from ..scripts.cioupdate import CioUpdate

        @log_capture()
        def call_test(log):
            """Function to ignore DeprecationWarning."""
            cioupdate = CioUpdate(self.args, CIOUPDATE3_INI)
            self.assertFalse(cioupdate.start())
            self.assertIn(
                'Git', '\n'.join([k.getMessage() for k in log.records]))

        with catch_warnings():
            simplefilter('ignore')
            # pylint: disable = no-value-for-parameter
            call_test()

    # -------------------------------------------------------------------------
    def test_start_invalid_populate(self):
        """[u:scripts.cioupdate.CioUpdate.start] Invalid populate command"""
        from . import CIOUPDATE4_INI
        from ..scripts.cioupdate import CioUpdate

        @log_capture()
        def call_test(log):
            """Function to ignore DeprecationWarning."""
            cioupdate = CioUpdate(self.args, CIOUPDATE4_INI)
            self.assertFalse(cioupdate.start())
            self.assertIn(
                'foopopulate', '\n'.join(
                    [k.getMessage() for k in log.records]))

        with catch_warnings():
            simplefilter('ignore')
            # pylint: disable = no-value-for-parameter
            call_test()

    # -------------------------------------------------------------------------
    def test_start_invalid_backup(self):
        """[u:scripts.cioupdate.CioUpdate.start] Invalid backup command"""
        from . import CIOUPDATE5_INI
        from ..scripts.cioupdate import CioUpdate

        @log_capture()
        def call_test(log):
            """Function to ignore DeprecationWarning."""
            cioupdate = CioUpdate(self.args, CIOUPDATE5_INI)
            self.assertFalse(cioupdate.start())
            self.assertIn(
                'foobackup', '\n'.join([k.getMessage() for k in log.records]))

        with catch_warnings():
            simplefilter('ignore')
            # pylint: disable = no-value-for-parameter
            call_test()

    # -------------------------------------------------------------------------
    def test_start_empty_command(self):
        """[u:scripts.cioupdate.CioUpdate.start] Empty command"""
        from . import CIOUPDATE6_INI
        from ..scripts.cioupdate import CioUpdate

        cioupdate = CioUpdate(self.args, CIOUPDATE6_INI)
        self.assertTrue(cioupdate.start())

    # -------------------------------------------------------------------------
    @classmethod
    def _make_database(cls):
        """Create a temporary database."""
        from . import CIOUPDATE_INI
        from ..relaxng import RELAXNG
        from ..scripts.ciopopulate import Populate
        from ..models.dbuser import DBUser
        from ..models.populate import xml2db

        args = namedtuple(
            'ArgumentParser', 'conf_uri options lang attachments')(
                conf_uri=CIOUPDATE_INI, options=None, lang=None,
                attachments=None)
        Populate(args, DBUser, xml2db, RELAXNG).run()
