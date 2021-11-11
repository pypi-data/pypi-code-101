# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``models`` functions and class."""

from os import makedirs, listdir
from os.path import exists
from json import dumps

from sqlalchemy import Column, String, Integer, Text, PickleType

from . import DBUnitTestCase


# =============================================================================
class UModelsDBBaseClass(DBUnitTestCase):
    """Unit test class for :class:`models.DBBaseClass`."""

    # -------------------------------------------------------------------------
    def test_label(self):
        """[u:models.DBBaseClass.label]"""
        from ..models import DBDeclarativeClass
        from ..models.dbbase import DBBaseClass

        class DBDummy1(DBDeclarativeClass, DBBaseClass):
            """SQLAlchemy-powered dummy model."""
            # pylint: disable = too-few-public-methods
            __tablename__ = 'dummy1'
            uid = Column(Integer, primary_key=True)
            i18n_label = Column(Text(), nullable=False)

        dbitem = DBBaseClass()
        self.assertEqual(dbitem.label(self.request), '')

        dbitem = DBDummy1(
            i18n_label=dumps({
                'en': 'FTP Monitoring', 'fr': 'Surveillance FTP'}))
        self.assertEqual(dbitem.label(self.request), 'FTP Monitoring')

        self.request.session['lang'] = 'fr'
        self.assertEqual(dbitem.label(self.request), 'Surveillance FTP')

    # -------------------------------------------------------------------------
    def test_description(self):
        """[u:models.DBBaseClass.description]"""
        from ..models import DBDeclarativeClass
        from ..models.dbbase import DBBaseClass

        class DBDummy2(DBDeclarativeClass, DBBaseClass):
            """SQLAlchemy-powered dummy model."""
            # pylint: disable = too-few-public-methods
            __tablename__ = 'dummy2'
            uid = Column(Integer, primary_key=True)
            i18n_description = Column(PickleType(1))

        dbitem = DBBaseClass()
        self.assertEqual(dbitem.description(self.request), '')

        dbitem = DBDummy2(
            i18n_description={
                'en': 'Periodically scan a FTP server.',
                'fr': 'Scrute périodiquement un serveur FTP.'})
        self.assertEqual(
            dbitem.description(self.request),
            'Periodically scan a FTP server.')

        self.request.session['lang'] = 'fr'
        self.assertEqual(
            dbitem.description(self.request),
            'Scrute périodiquement un serveur FTP.')

    # -------------------------------------------------------------------------
    def test_attachments2directory(self):
        """[u:models.DBBaseClass.attachments2directory]"""
        from ..models import DBDeclarativeClass, ID_LEN
        from ..models.dbbase import DBBaseClass
        from . import ATTACHMENTS_DIR, TEST_DIR

        class DBDummy3(DBDeclarativeClass, DBBaseClass):
            """SQLAlchemy-powered dummy model."""
            # pylint: disable = too-few-public-methods
            attachments_dir = 'Dummy'
            __tablename__ = 'dummy3'
            uid = Column(Integer, primary_key=True)
            attachments_key = Column(String(ID_LEN + 20))
            picture = Column(String(ID_LEN + 4))

        if not exists(TEST_DIR):
            makedirs(TEST_DIR)

        # No attachment
        dbitem = DBBaseClass()
        dbitem.attachments2directory(ATTACHMENTS_DIR, TEST_DIR)
        self.assertFalse(listdir(TEST_DIR))

        # Incorrect attachment
        dbitem = DBDummy3(
            attachments_key='Test1', picture='testX.svg')
        dbitem.attachments2directory(ATTACHMENTS_DIR, TEST_DIR)
        self.assertFalse(listdir(TEST_DIR))

        # Correct attachment
        dbitem = DBDummy3(
            attachments_key='Test1', picture='test1.svg')
        dbitem.attachments2directory(ATTACHMENTS_DIR, TEST_DIR)
        self.assertTrue(listdir(TEST_DIR))
