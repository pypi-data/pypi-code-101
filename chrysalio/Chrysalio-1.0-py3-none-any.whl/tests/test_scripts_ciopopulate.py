# pylint: disable = import-outside-toplevel
"""Tests of ``scripts.ciopopulate`` function and class."""

from os import makedirs, sep
from os.path import exists, join, dirname
from collections import namedtuple
from unittest import TestCase

from . import DBUnitTestCase


# =============================================================================
class UScriptsCIOPopulateMain(TestCase):
    """Unit test class for :func:`scripts.ciopopulate.main`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:scripts.ciopopulate.main]"""
        from ..scripts.ciopopulate import main
        from . import TEST_INI

        self.assertRaises(SystemExit, main)
        try:
            main([TEST_INI])
        except SystemExit:
            pass


# =============================================================================
class UScriptsCIOPopulatePopulate(DBUnitTestCase):
    """Unit test class for :class:`scripts.ciopopulate.Populate`."""

    # -------------------------------------------------------------------------
    def test_argument_parser(self):
        """[u:scripts.ciopopulate.Populate.argument_parser]"""
        from argparse import ArgumentParser
        from ..scripts.ciopopulate import Populate

        parser = Populate.argument_parser()
        self.assertIsInstance(parser, ArgumentParser)
        self.assertEqual(parser.description, 'Populate database.')

    # -------------------------------------------------------------------------
    def test_run(self):
        """[u:scripts.ciopopulate.Populate.run]"""
        from . import TEST_INI, TEST_DIR, TEST1_INI, TEST2_INI, TEST4_INI
        from . import TEST1_USR_XML, TEST3_USR_XML
        from ..scripts.ciopopulate import Populate
        from ..models.dbuser import DBUser
        from ..models.populate import xml2db
        from ..relaxng import RELAXNG

        # No database
        args = namedtuple(
            'ArgumentParser', 'conf_uri options lang attachments')(
                conf_uri=TEST1_INI, options=None, lang=None, attachments=None)
        self.assertEqual(Populate(args, DBUser, xml2db, RELAXNG).run(), 1)

        # No data
        args = namedtuple(
            'ArgumentParser', 'conf_uri options lang attachments')(
                conf_uri=TEST2_INI, options=None, lang=None, attachments=None)
        self.assertEqual(Populate(args, DBUser, xml2db, RELAXNG).run(), 1)

        # No attachments
        args = namedtuple(
            'ArgumentParser', 'conf_uri options lang attachments')(
                conf_uri=TEST4_INI, options=None, lang=None, attachments=None)
        self.assertEqual(Populate(args, DBUser, xml2db, RELAXNG).run(), 0)

        # Correct test.ini
        makedirs(join(TEST_DIR, 'Attachments'))
        args = namedtuple(
            'ArgumentParser', 'conf_uri options lang attachments')(
                conf_uri=TEST_INI, options=None, lang=None,
                attachments=join(
                    dirname(__file__), 'Attachments{0}'.format(sep)))
        self.assertEqual(Populate(args, DBUser, xml2db, RELAXNG).run(
            [TEST1_USR_XML, TEST3_USR_XML, TEST3_USR_XML]), 0)
        self.assertTrue(exists(
            join(TEST_DIR, 'Attachments', 'Users', 'Test1')))
        self.assertTrue(exists(
            join(TEST_DIR, 'Attachments', 'Users', 'Test5')))
