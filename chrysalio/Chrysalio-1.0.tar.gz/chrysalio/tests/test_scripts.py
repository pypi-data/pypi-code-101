# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``scripts`` classes."""

from collections import namedtuple

from . import DBUnitTestCase


# =============================================================================
class UScriptsScript(DBUnitTestCase):
    """Unit test class for :class:`scripts.Script`."""

    # -------------------------------------------------------------------------
    def test_init(self):
        """[u:scripts.Script]"""
        from . import TEST_INI, TEST1_INI
        from ..scripts import Script

        args = namedtuple('ArgumentParser', 'conf_uri options lang')(
            conf_uri='foo.ini', options=None, lang=None)
        script = Script(args, False)
        self.assertIsNone(script.registry)

        args = namedtuple('ArgumentParser', 'conf_uri options lang')(
            conf_uri=TEST1_INI, options=None, lang=None)
        script = Script(args, False)
        self.assertIsNone(script.registry)

        args = namedtuple(
            'ArgumentParser', 'conf_uri options lang drop_tables')(
                conf_uri=TEST_INI, options=None, lang=None, drop_tables=True)
        script = Script(args, False)
        self.assertIsNotNone(script.registry)

        script = Script(args, True)
        self.assertIsNotNone(script.registry)

    # -------------------------------------------------------------------------
    def test_init_bad_include(self):
        """[u:scripts.Script] bad included module"""
        from . import TEST5_INI
        from ..scripts import Script

        args = namedtuple(
            'ArgumentParser', 'conf_uri options lang drop_tables')(
                conf_uri=TEST5_INI, options=None, lang=None, drop_tables=False)
        self.assertRaises(SystemExit, Script, args, False)

    # -------------------------------------------------------------------------
    def test_init_no_includeme(self):
        """[u:scripts.Script] included module without includeme()"""
        from . import TEST6_INI
        from ..scripts import Script

        args = namedtuple(
            'ArgumentParser', 'conf_uri options lang drop_tables')(
                conf_uri=TEST6_INI, options=None, lang=None, drop_tables=False)
        self.assertRaises(SystemExit, Script, args, True)

    # -------------------------------------------------------------------------
    def test_init_bad_dependency(self):
        """[u:scripts.Script] included module with unsatisfied dependency"""
        from . import TEST7_INI
        from ..scripts import Script

        args = namedtuple(
            'ArgumentParser', 'conf_uri options lang drop_tables')(
                conf_uri=TEST7_INI, options=None, lang=None, drop_tables=False)
        self.assertRaises(SystemExit, Script, args, True)

    # -------------------------------------------------------------------------
    def test_init_conflict(self):
        """[u:scripts.Script] included conflicting modules"""
        from . import TEST8_INI
        from ..scripts import Script

        args = namedtuple(
            'ArgumentParser', 'conf_uri options lang drop_tables')(
                conf_uri=TEST8_INI, options=None, lang=None, drop_tables=False)
        self.assertRaises(SystemExit, Script, args, True)

    # -------------------------------------------------------------------------
    def test_argument_parser(self):
        """[u:scripts.Script.argument_parser]"""
        from argparse import ArgumentParser
        from ..scripts import Script

        parser = Script.argument_parser('éÔ')
        self.assertIsInstance(parser, ArgumentParser)
        self.assertEqual(parser.description, 'éÔ')

    # -------------------------------------------------------------------------
    def test_arguments(self):
        """[u:scripts.Script.argument]"""
        from . import TEST_INI
        from ..scripts import Script

        parser = Script.argument_parser('My description')
        self.assertRaises(SystemExit, Script.arguments, parser)

        args = namedtuple('ArgumentParser', 'conf_uri')(conf_uri='foo.ini')
        self.assertIsNone(Script.arguments(parser, args))

        args = namedtuple('ArgumentParser', 'conf_uri')(conf_uri=TEST_INI)
        args = Script.arguments(parser, args)
        self.assertIn('conf_uri', args)
        self.assertEqual(args.conf_uri, TEST_INI)
        self.assertIn('log_level', args)
        self.assertEqual(args.log_level, 'INFO')
