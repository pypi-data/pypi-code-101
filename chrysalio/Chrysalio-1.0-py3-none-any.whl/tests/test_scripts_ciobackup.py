# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``scripts.ciobackup`` function and class."""

from os import makedirs
from os.path import exists, join
from collections import namedtuple
from datetime import datetime
from shutil import rmtree
from unittest import TestCase

from transaction import manager

from . import DBUnitTestCase
# pylint: disable = unused-import
from ..includes.modules.models import DBModule  # noqa
from ..modules.cioskeleton.models.dbbone import DBBone  # noqa
# pylint: enable = unused-import


# =============================================================================
class UScriptsCIOBackupMain(TestCase):
    """Unit test class for :func:`scripts.ciobackup.main`."""

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Clear up temporary files."""
        from . import BACKUP_DIR

        if exists(BACKUP_DIR):
            rmtree(BACKUP_DIR)

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:scripts.ciobackup.main]"""
        from ..scripts.ciobackup import main
        from . import TEST_INI, BACKUP_DIR

        self.assertRaises(SystemExit, main)
        try:
            main([TEST_INI, BACKUP_DIR])
        except SystemExit:
            pass


# =============================================================================
class UScriptsBackup(DBUnitTestCase):
    """Unit test class for :class:`scripts.Backup`."""

    # -------------------------------------------------------------------------
    def test_argument_parser(self):
        """[u:scripts.Backup.argument_parser]"""
        from argparse import ArgumentParser
        from ..scripts.ciobackup import Backup

        parser = Backup.argument_parser()
        self.assertIsInstance(parser, ArgumentParser)
        self.assertEqual(parser.description, 'Backup database.')

    # -------------------------------------------------------------------------
    def test_run(self):
        """[u:scripts.Backup.run]"""
        # pylint: disable = too-many-locals
        from . import TEST_INI, TEST1_INI, TEST_DIR, BACKUP_DIR
        from ..relaxng import RELAXNG
        from ..scripts.ciobackup import Backup
        from ..models import get_dbsession_factory
        from ..models.populate import db2xml
        from ..models.dbsettings import DBSettings
        from ..models.dbuser import DBUser

        args = namedtuple('ArgumentParser', 'conf_uri options lang')(
            conf_uri=TEST1_INI, options=None, lang=None)
        self.assertEqual(Backup(args, db2xml, RELAXNG).run(BACKUP_DIR), 1)

        dbsession = self.request.dbsession
        args = namedtuple('ArgumentParser', 'conf_uri options lang')(
            conf_uri=TEST_INI, options=None, lang=None)
        self.assertEqual(Backup(
            args, db2xml, RELAXNG, dbsession_factory=get_dbsession_factory(
                dbsession.get_bind())).run(TEST_INI), 0)

        dbsession.add(DBSettings(
            key='populate', value=datetime.now().isoformat(' ').split('.')[0]))
        dbuser = DBUser(
            login='test1', first_name='Édith', last_name='AVULEUR',
            email='test1@chrysal.io')
        dbuser.set_password('test1pwd')
        dbsession.add(dbuser)
        manager.commit()
        makedirs(join(TEST_DIR, 'Attachments', 'Users'))

        args = namedtuple('ArgumentParser', 'conf_uri options lang')(
            conf_uri=TEST_INI, options=None, lang=None)
        self.assertEqual(Backup(
            args, db2xml, RELAXNG, dbsession_factory=get_dbsession_factory(
                dbsession.get_bind())).run(TEST_INI), 1)

        args = namedtuple(
            'ArgumentParser', 'conf_uri options lang no_validation')(
                conf_uri=TEST_INI, options=None, lang=None,
                no_validation=False)
        self.assertEqual(Backup(
            args, db2xml, RELAXNG, dbsession_factory=get_dbsession_factory(
                dbsession.get_bind())).run(BACKUP_DIR), 0)
        self.assertTrue(exists(BACKUP_DIR))
        self.assertTrue(exists(join(BACKUP_DIR, 'testchrysalio.xml')))
        self.assertTrue(exists(join(BACKUP_DIR, 'Users')))

        if not exists(join(BACKUP_DIR, 'Foo')):
            makedirs(join(BACKUP_DIR, 'Foo'))
        if not exists(join(BACKUP_DIR, 'foo.xml')):
            with open(join(BACKUP_DIR, 'foo.xml'), 'w') as hdl:
                hdl.write('<chrysalio/>')
        self.assertEqual(Backup(
            args, db2xml, RELAXNG, dbsession_factory=get_dbsession_factory(
                dbsession.get_bind())).run(BACKUP_DIR), 0)
        self.assertFalse(exists(join(BACKUP_DIR, 'Foo')))
        self.assertTrue(exists(join(BACKUP_DIR, 'foo.xml')))
