# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``lib.ftp`` classes."""

from os.path import join, exists, basename
from ftplib import FTP, all_errors

from . import TmpDirTestCase


# =============================================================================
class ULibFtpFtp(TmpDirTestCase):
    """Unit test class for :class:`lib.ftp.Ftp`."""

    # -------------------------------------------------------------------------
    def _make_one(self):
        """Return a connected Ftp object.

        :rtype: :class:`.lib.ftp.Ftp` or ``None``
        """
        from chrysalio.lib.utils import decrypt
        from . import FTP_HOST, FTP_USER, FTP_PASSWORD
        from ..lib.ftp import Ftp

        values = {
            'ftp_host': FTP_HOST, 'ftp_user': FTP_USER,
            'ftp_password': decrypt(FTP_PASSWORD, 'test'), 'ftp_pasv': True}
        ftp = Ftp(self.log_error)
        return ftp if ftp.connect(values) else None

    # -------------------------------------------------------------------------
    def log_error(self, text):
        """Dummy method for ``log_error``.

        :param str text:
            Error.
        """

    # -------------------------------------------------------------------------
    def test_connect(self):
        """[u:lib.ftp.Ftp.connect]"""
        from chrysalio.lib.utils import decrypt
        from . import FTP_HOST, FTP_USER, FTP_PASSWORD
        from ..lib.ftp import Ftp

        ftp = Ftp(self.log_error)

        # Missing values
        self.assertFalse(ftp.connect({}))

        # Invalid host
        values = {
            'ftp_host': 'ftp.chrysal2.io', 'ftp_user': FTP_USER,
            'ftp_password': 'foo', 'ftp_pasv': True, 'ftp_path': 'Foo'}
        self.assertFalse(ftp.connect(values))

        # Invalid password
        values['ftp_host'] = FTP_HOST
        self.assertFalse(ftp.connect(values))

        # Not existing directory
        values['ftp_password'] = decrypt(FTP_PASSWORD, 'test')
        self.assertFalse(ftp.connect(values))

        # Connection
        del values['ftp_path']
        ftp.connection = FTP()
        try:
            ftp.connection.connect(
                values.get('ftp_host'), values.get('ftp_port', 21))
        except all_errors:
            return
        self.assertTrue(
            ftp.connect(values), msg='Put somes files in {0}@{1}'.format(
                FTP_USER, FTP_HOST))
        ftp.quit()

    # -------------------------------------------------------------------------
    def test_cwd(self):
        """[u:lib.ftp.Ftp.cwd]"""
        ftp = self._make_one()
        if not ftp:
            return

        # Not existing directory
        self.assertFalse(ftp.cwd('Foo'))

        # Existing directoy
        ftp.mkdir('Bar')
        self.assertTrue(ftp.cwd('Bar'))
        ftp.rmtree('Bar')
        ftp.quit()

    # -------------------------------------------------------------------------
    def test_mkdir(self):
        """[u:lib.ftp.Ftp.mkdir]"""
        ftp = self._make_one()
        if not ftp:
            return

        self.assertTrue(ftp.mkdir('Foo'))
        ftp.rmtree('Foo')
        ftp.quit()

    # -------------------------------------------------------------------------
    def test_list_directory(self):
        """[u:lib.ftp.Ftp.list_directory]"""

        ftp = self._make_one()
        if not ftp:
            return
        ftp.mkdir('Bar')

        dirs, files = ftp.list_directory()
        self.assertIsInstance(dirs, dict)
        self.assertIsInstance(files, dict)
        self.assertTrue(dirs)
        ftp.rmtree('Bar')
        ftp.quit()

    # -------------------------------------------------------------------------
    def test_rmtree(self):
        """[u:lib.ftp.Ftp.rmtree]"""
        from . import TEST_INI

        ftp = self._make_one()
        if not ftp:
            return

        # Not existing directory
        self.assertFalse(ftp.rmtree('Foo'))

        # Existing directory
        ftp.mkdir('Bar')
        ftp.cwd('Bar')
        ftp.mkdir('Baz')
        with open(TEST_INI, 'rb') as hdl:
            ftp.connection.storbinary('STOR test.ini', hdl)
        ftp.cwd('..')
        self.assertTrue(ftp.rmtree('Bar'))
        ftp.quit()

    # -------------------------------------------------------------------------
    def test_download(self):
        """[u:lib.ftp.Ftp.download]"""
        from ..lib.utils import tostr
        from . import TEST_INI, TEST_DIR

        ftp = self._make_one()
        if not ftp:
            return
        ftp.rmtree('Baz')
        ftp.mkdir('Baz')
        ftp.connection.cwd('Baz')
        destination = join(TEST_DIR, 'Download')

        # Empty
        self.assertTrue(ftp.download(destination))
        self.assertFalse(exists(destination))

        # Not empty
        ftp.mkdir('Foo')
        ftp.mkdir('.svn')
        ftp.upload(TEST_INI)
        with open(TEST_INI, 'rb') as hdl:
            ftp.connection.storbinary(tostr('STOR écrit.ini.part'), hdl)
        with open(TEST_INI, 'rb') as hdl:
            ftp.connection.storbinary('STOR Thumbs.db', hdl)

        self.assertFalse(ftp.download(destination))
        self.assertTrue(exists(destination))
        ftp.delete(tostr('écrit.ini.part'))
        self.assertTrue(ftp.download(destination))
        self.assertTrue(exists(join(destination, basename(TEST_INI))))
        self.assertFalse(exists(join(destination, 'Thumbs.db')))
        self.assertFalse(exists(join(destination, '.svn')))

        ftp.connection.cwd('..')
        ftp.rmtree('Baz')
        ftp.quit()

        self.assertTrue(exists(join(destination, 'test.ini')))
        self.assertTrue(exists(join(destination, 'Foo')))

    # -------------------------------------------------------------------------
    def test_upload(self):
        """[u:lib.ftp.Ftp.uplaod]"""
        from . import TEST_INI

        ftp = self._make_one()
        if not ftp:
            return
        ftp.upload(TEST_INI)
        files = ftp.list_directory()[1]
        self.assertIn('test.ini', files)
        ftp.delete('test.ini')
        ftp.quit()

    # -------------------------------------------------------------------------
    def test_quit(self):
        """[u:lib.ftp.Ftp.quit]"""
        ftp = self._make_one()
        if not ftp:
            return

        self.assertIsNotNone(ftp.connection)
        ftp.quit()
        self.assertIsNone(ftp.connection)
