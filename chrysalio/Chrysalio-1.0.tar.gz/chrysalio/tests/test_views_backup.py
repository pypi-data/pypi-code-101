# pylint: disable = import-outside-toplevel
"""Tests of ``views.backup`` class."""

from os import listdir, makedirs
from os.path import exists, join
from collections import OrderedDict, namedtuple
from cgi import FieldStorage

from pyramid.response import Response, FileResponse

from . import DBUnitTestCase


# =============================================================================
class UViewsBackupBackupView(DBUnitTestCase):
    """Unit test class for testing :class:`views.backup.BackupView`."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""

        super(UViewsBackupBackupView, self).setUp()

        self.request.matched_route = namedtuple('Route', 'name')(name='backup')
        self.configurator.registry['modules'] = OrderedDict()
        self.configurator.registry['modules_off'] = set()
        self.configurator.registry.settings['site.uid'] = 'test'

    # -------------------------------------------------------------------------
    def test_index(self):
        """[u:views.backup.BackupView.index]"""
        from ..views.backup import BackupView

        # Page display
        response = BackupView(self.request).index()
        self.assertIn('form', response)
        self.assertIn('action', response)
        self.assertIn('download_max_size', response)
        self.assertEqual(
            self.request.breadcrumbs.current_title(), 'Configuration Backup')

    # -------------------------------------------------------------------------
    def test_index_backup(self):
        """[u:views.backup.BackupView.index] Backup"""
        from ..views.backup import BackupView
        from . import ATTACHMENTS_DIR

        # Backup without attachments
        self.request.POST = {'bck!.x': True}
        response = BackupView(self.request).index()
        self.assertIsInstance(response, Response)

        # Backup with attachments
        self.configurator.registry.settings['attachments'] = ATTACHMENTS_DIR
        response = BackupView(self.request).index()
        self.assertIsInstance(response, FileResponse)

    # -------------------------------------------------------------------------
    def test_index_restore(self):
        """[u:views.backup.BackupView.index] Restore"""
        from . import TEST_INI, TEST1_INI, TEST1_USR_ZIP, TEST2_USR_ZIP
        from . import BACKUP_DIR, DummyPOST
        from ..models.dbuser import DBUser

        dbsession = self.request.dbsession
        self.configurator.add_route('logout', '/logout')
        self.request.POST = DummyPOST()
        self.request.POST['rst!.x'] = True

        # Without a main administrator
        self.request.params['reset'] = True
        self.request.registry.settings['__file__'] = TEST1_INI
        response = self._call_index_with_file(TEST1_USR_ZIP)
        self.assertIsInstance(response, dict)
        self.assertTrue(self.request.session.pop_flash('alert'))

        # With an incorrect backup
        self.request.registry.settings['__file__'] = TEST_INI
        response = self._call_index_with_file(TEST2_USR_ZIP)
        self.assertIsInstance(response, dict)
        self.assertTrue(self.request.session.pop_flash('alert'))

        # A correct backup with reset
        makedirs(BACKUP_DIR)
        self.request.registry.settings['attachments'] = BACKUP_DIR
        response = self._call_index_with_file(TEST1_USR_ZIP)
        self.assertNotIn('user', self.request.session)
        self.assertFalse(self.request.session.pop_flash('alert'))
        self.assertFalse(self.request.session.pop_flash())
        self.assertEqual(len(dbsession.query(DBUser).all()), 2)
        self.assertIsNotNone(
            dbsession.query(DBUser).filter_by(login='admin').first())
        self.assertIsNotNone(
            dbsession.query(DBUser).filter_by(login='user3').first())
        self.assertTrue(listdir(BACKUP_DIR))
        self.assertTrue(exists(join(
            BACKUP_DIR, DBUser.attachments_dir, 'User3', 'user3.svg')))

        # A correct backup without reset
        self.request.params['reset'] = False
        response = self._call_index_with_file(TEST1_USR_ZIP)
        self.assertFalse(self.request.session.pop_flash('alert'))
        self.assertTrue(self.request.session.pop_flash())

        # Ajax
        self.request.is_xhr = True
        response = self._call_index_with_file(TEST1_USR_ZIP)
        self.assertIsInstance(response, dict)
        self.assertTrue(self.request.session.pop_flash())

    # -------------------------------------------------------------------------
    def _call_index_with_file(self, filename):
        """Call index with a file.

        :param str filename:
            Absolute path to the file to use.
        :rtype: dict
        """
        from ..views.backup import BackupView

        with open(filename, 'rb') as hdl:
            input_file = FieldStorage()
            input_file.filename = filename
            input_file.file = hdl
            self.request.POST.multikeys = {'file': (input_file,)}
            response = BackupView(self.request).index()
        return response
