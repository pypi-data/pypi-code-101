# pylint: disable = import-outside-toplevel
"""Tests of ``lib.log`` functions."""

from logging import getLogger
from os.path import join, dirname, exists
from tempfile import mkdtemp
from shutil import rmtree
from configparser import ConfigParser
from unittest import TestCase

from testfixtures import LogCapture

from pyramid.testing import DummyRequest

from . import TmpDirTestCase


# =============================================================================
class ULibLogSetupLogging(TestCase):
    """Unit test class for :func:`lib.log.setup_logging`."""

    # -------------------------------------------------------------------------
    def test_console(self):
        """[u:lib.log.setup_logging] console"""
        from ..lib.log import setup_logging

        setup_logging()
        log = getLogger()
        self.assertGreater(len(log.handlers), 0)
        # self.assertIsInstance(log.handlers[0], StreamHandler)

    # -------------------------------------------------------------------------
    def test_file(self):
        """[u:lib.log.setup_logging] file"""
        from ..lib.log import setup_logging

        log_dir = mkdtemp()
        try:
            setup_logging(log_file=join(log_dir, 'test.log'))
            log = getLogger()
            self.assertGreater(len(log.handlers), 0)
        finally:
            rmtree(log_dir)


# =============================================================================
class ULibLogLogActivitySetup(TmpDirTestCase):
    """Unit test class for :func:`lib.log.log_activity_setup`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.log.log_activity_setup]"""
        from . import TEST_DIR, TEST2_INI, TEST3_INI
        from ..lib.utils import tounicode
        from ..lib.log import log_activity_setup

        config = ConfigParser({'here': dirname(TEST2_INI)})
        config.read(tounicode(TEST2_INI), encoding='utf8')
        self.assertFalse(log_activity_setup(config))

        config = ConfigParser({'here': dirname(TEST3_INI)})
        config.read(tounicode(TEST3_INI), encoding='utf8')
        self.assertTrue(log_activity_setup(config))
        self.assertTrue(exists(TEST_DIR))


# =============================================================================
class ULibLogLogActivity(TestCase):
    """Unit test class for :func:`lib.log.log_info`."""

    # -------------------------------------------------------------------------
    @classmethod
    def test_it(cls):
        """[u:lib.log.log_info]"""
        from ..lib.log import LOG_ACTIVITY, log_info

        with LogCapture() as log_capture:
            request = DummyRequest()
            request.session['user'] = {'user_id': 1, 'login': 'test1'}
            request.registry['log_activity'] = LOG_ACTIVITY
            log_info(request, 'action', 'foo', 'bar')
            log_capture.check(('activity', 'INFO', '[test1] action foo bar'))


# =============================================================================
class ULibLogLogError(TestCase):
    """Unit test class for :func:`lib.log.log_error`."""

    # -------------------------------------------------------------------------
    @classmethod
    def test_it(cls):
        """[u:lib.log.log_error]"""
        from ..lib.log import LOG_ACTIVITY, log_error

        with LogCapture() as log_capture:
            request = DummyRequest()
            request.session['user'] = {'user_id': 1, 'login': 'test1'}
            request.registry['log_activity'] = LOG_ACTIVITY
            log_error(request, 'An error occured!')
            log_capture.check(
                ('activity', 'ERROR', '[test1] An error occured!'))


# =============================================================================
class ULibLogLogWarning(TestCase):
    """Unit test class for :func:`lib.log.log_warning`."""

    # -------------------------------------------------------------------------
    @classmethod
    def test_it(cls):
        """[u:lib.log.log_warning]"""
        from ..lib.log import LOG_ACTIVITY, log_warning

        with LogCapture() as log_capture:
            request = DummyRequest()
            request.session['user'] = {'user_id': 2, 'login': 'test2'}
            request.registry['log_activity'] = LOG_ACTIVITY
            log_warning(request, 'Warning!')
            log_capture.check(('activity', 'WARNING', '[test2] Warning!'))


# =============================================================================
class ULibLogLogDebug(TestCase):
    """Unit test class for :func:`lib.log.log_debug`."""

    # -------------------------------------------------------------------------
    @classmethod
    def test_it(cls):
        """[u:lib.log.log_warning]"""
        from ..lib.log import LOG_ACTIVITY, log_debug

        with LogCapture() as log_capture:
            request = DummyRequest()
            request.session['user'] = {'user_id': 3, 'login': 'test3'}
            request.registry['log_activity'] = LOG_ACTIVITY
            log_debug(request, 'Debug message')
            log_capture.check(('activity', 'DEBUG', '[test3] Debug message'))
